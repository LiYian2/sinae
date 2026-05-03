import json
import re
import time
import hashlib
import random
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Optional

import requests

from shared.data_layer import SharedDataLayer
from shared.types import Paper, ResearchProfile, UserLevel


class LiteratureRetrievalSkill:
    def __init__(self, data_layer: SharedDataLayer):
        self.data = data_layer

    def run(
        self,
        profile: ResearchProfile,
        override_queries: Optional[list[str]] = None,
        demo: bool = False,
    ) -> list[Paper]:
        self.data.set_research_profile(profile)

        if demo:
            papers = self._generate_demo_papers(profile.topic, profile.max_papers)
            self.data.add_papers(papers)
            quality = self._assess_corpus_quality(papers)
            self.data.set_corpus_quality(quality)
            return papers

        queries = override_queries or self._generate_query_plan(profile.topic, profile.user_level)

        all_papers: dict[str, Paper] = {}

        for query in queries:
            papers_arxiv = self._search_arxiv(query, profile.max_papers // len(queries))
            for p in papers_arxiv:
                all_papers[p.paper_id] = p

            papers_s2 = self._search_semantic_scholar(query, min(profile.max_papers // len(queries), 20))
            for p in papers_s2:
                if p.paper_id not in all_papers:
                    all_papers[p.paper_id] = p

            time.sleep(0.3)

        papers = list(all_papers.values())

        if profile.time_range != "all":
            papers = self._filter_by_time(papers, profile.time_range)

        papers = self._deduplicate(papers)
        papers = self._enrich_citations(papers, profile.max_papers)

        self.data.add_papers(papers)
        quality = self._assess_corpus_quality(papers)
        self.data.set_corpus_quality(quality)

        return papers

    def _generate_query_plan(self, topic: str, level: UserLevel) -> list[str]:
        queries = [topic.strip()]

        topic_words = re.findall(r"[A-Za-z0-9\-]+", topic)
        if len(topic) > 3:
            queries.append(f'"{topic.strip()}"')

        expansion_terms: dict[UserLevel, list[str]] = {
            UserLevel.BEGINNER: ["survey", "tutorial", "overview", "foundations"],
            UserLevel.INTERMEDIATE: ["method", "algorithm"],
            UserLevel.ADVANCED: ["state-of-the-art", "recent advances", "open problems"],
        }

        for suffix in expansion_terms.get(level, []):
            queries.append(f"{topic} {suffix}")

        if len(topic_words) >= 4:
            mid = len(topic_words) // 2
            queries.append(" ".join(topic_words[:mid]))
            queries.append(" ".join(topic_words[mid:]))

        return queries[:4]

    def _search_arxiv(self, query: str, max_results: int) -> list[Paper]:
        papers = []
        max_results = min(max_results, 50)
        query_encoded = urllib.parse.quote(query)
        url = (
            f"http://export.arxiv.org/api/query?"
            f"search_query=all:{query_encoded}&start=0&max_results={max_results}"
            f"&sortBy=relevance&sortOrder=descending"
        )
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ResearchTrail/1.0"})
            resp = urllib.request.urlopen(req, timeout=30)
            data = resp.read().decode("utf-8")
            root = ET.fromstring(data)
            ns = {
                "atom": "http://www.w3.org/2005/Atom",
                "arxiv": "http://arxiv.org/schemas/atom",
            }
            for entry in root.findall("atom:entry", ns):
                entry_id = entry.find("atom:id", ns)
                paper_id = entry_id.text.strip() if entry_id is not None and entry_id.text else ""
                paper_id = paper_id.split("/abs/")[-1] if "/abs/" in paper_id else paper_id

                title_el = entry.find("atom:title", ns)
                title = title_el.text.strip() if title_el is not None and title_el.text else ""
                title = re.sub(r"\s+", " ", title)

                abstract_el = entry.find("atom:summary", ns)
                abstract = abstract_el.text.strip() if abstract_el is not None and abstract_el.text else ""
                abstract = re.sub(r"\s+", " ", abstract)

                authors = []
                for author_el in entry.findall("atom:author", ns):
                    name_el = author_el.find("atom:name", ns)
                    if name_el is not None and name_el.text:
                        authors.append(name_el.text.strip())

                published_el = entry.find("atom:published", ns)
                year = 0
                if published_el is not None and published_el.text:
                    try:
                        year = int(published_el.text[:4])
                    except ValueError:
                        pass

                journal_el = entry.find("arxiv:journal_ref", ns)
                venue = journal_el.text.strip() if journal_el is not None and journal_el.text else ""

                papers.append(Paper(
                    paper_id=paper_id,
                    title=title,
                    authors=authors,
                    year=year,
                    abstract=abstract,
                    url=f"https://arxiv.org/abs/{paper_id}",
                    citation_count=0,
                    source="arxiv",
                    venue=venue,
                ))
        except Exception as e:
            print(f"[arXiv] Query '{query}' failed: {e}")
        return papers

    def _search_semantic_scholar(self, query: str, max_results: int, retries: int = 1) -> list[Paper]:
        papers = []
        max_results = min(max_results, 20)
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": query,
            "limit": max_results,
            "fields": "title,authors,year,abstract,externalIds,citationCount,venue",
        }

        for attempt in range(retries + 1):
            try:
                resp = requests.get(url, params=params, timeout=10)
                if resp.status_code == 429:
                    if attempt < retries:
                        time.sleep(2)
                        continue
                    break
                resp.raise_for_status()
                data = resp.json()
                for item in data.get("data", []):
                    ext_ids = item.get("externalIds", {}) or {}
                    paper_id = ext_ids.get("DOI") or ext_ids.get("ArXiv") or item.get("paperId", "")
                    authors = [a.get("name", "") for a in (item.get("authors") or [])]
                    papers.append(Paper(
                        paper_id=paper_id,
                        title=item.get("title", ""),
                        authors=authors,
                        year=item.get("year") or 0,
                        abstract=item.get("abstract") or "",
                        url=f"https://api.semanticscholar.org/{item.get('paperId', '')}",
                        citation_count=item.get("citationCount", 0),
                        source="semantic_scholar",
                        venue=item.get("venue", ""),
                    ))
                break
            except Exception as e:
                if "429" in str(e) and attempt < retries:
                    time.sleep(2)
                    continue
                if attempt == 0:
                    print(f"[Semantic Scholar] Query '{query[:50]}' failed: {e}")
        return papers

    def _filter_by_time(self, papers: list[Paper], time_range: str) -> list[Paper]:
        import datetime
        current_year = datetime.datetime.now().year
        if time_range == "last_5_years":
            return [p for p in papers if p.year >= current_year - 5]
        elif time_range == "last_3_years":
            return [p for p in papers if p.year >= current_year - 3]
        elif time_range == "last_year":
            return [p for p in papers if p.year >= current_year - 1]
        return papers

    def _deduplicate(self, papers: list[Paper]) -> list[Paper]:
        seen_titles: set[str] = set()
        unique: list[Paper] = []
        for p in papers:
            title_key = p.title.lower().strip()[:100]
            title_hash = hashlib.md5(title_key.encode()).hexdigest()
            if title_hash not in seen_titles:
                seen_titles.add(title_hash)
                unique.append(p)
            else:
                for existing in unique:
                    if existing.title.lower().strip()[:100] == title_key:
                        if p.citation_count > existing.citation_count:
                            existing.citation_count = p.citation_count
                        if p.abstract and not existing.abstract:
                            existing.abstract = p.abstract
                        break
        return unique

    def _enrich_citations(self, papers: list[Paper], max_total: int) -> list[Paper]:
        paper_ids = [p.paper_id for p in papers if p.paper_id]
        if not paper_ids:
            return papers

        s2_ids = [p.paper_id for p in papers if p.source == "semantic_scholar" and len(p.paper_id) > 10]
        if not s2_ids:
            return papers

        try:
            url = "https://api.semanticscholar.org/graph/v1/paper/batch"
            payload = {"ids": s2_ids[:500]}
            params = {"fields": "references,citations"}
            resp = requests.post(url, json=payload, params=params, timeout=60)
            resp.raise_for_status()
            data = resp.json()

            id_to_paper = {p.paper_id: p for p in papers}
            for item in data:
                pid = item.get("doi") or item.get("arxivId") or ""
                paper = id_to_paper.get(pid)
                if not paper:
                    continue
                paper.references = [
                    (r.get("paperId") or "") for r in (item.get("references") or [])
                ]
                paper.citations = [
                    (c.get("paperId") or "") for c in (item.get("citations") or [])
                ]
        except Exception as e:
            print(f"[Semantic Scholar] Citation enrichment failed: {e}")

        return papers

    def _assess_corpus_quality(self, papers: list[Paper]) -> dict:
        n = len(papers)
        years = [p.year for p in papers if p.year > 0]
        has_abstract = sum(1 for p in papers if p.abstract)
        has_citations = sum(1 for p in papers if p.references or p.citations)

        n_citation_edges = sum(len(p.references) for p in papers)

        return {
            "total_papers": n,
            "has_abstract_ratio": has_abstract / max(n, 1),
            "has_citation_ratio": has_citations / max(n, 1),
            "year_range": f"{min(years)}-{max(years)}" if years else "N/A",
            "median_year": sorted(years)[len(years) // 2] if years else 0,
            "citation_edges_total": n_citation_edges,
        }

    def expand_retrieval(self, query_suffix: str, max_papers: int = 50) -> list[Paper]:
        profile = self.data.get_research_profile()
        if not profile:
            return []
        new_query = f"{profile.topic} {query_suffix}"
        papers = self._search_arxiv(new_query, max_papers) + self._search_semantic_scholar(new_query, max_papers)
        papers = self._deduplicate(papers)
        self.data.add_papers(papers)
        return papers

    def _generate_demo_papers(self, topic: str, count: int = 50) -> list[Paper]:
        random.seed(hash(topic) % (2**31))

        seed_count = max(20, min(count, 60))
        papers: list[Paper] = []
        used_titles: set[str] = set()

        years = list(range(2000, 2026))
        weights = [max(1, y - 1999) for y in years]

        subtopics = ["Theory", "Algorithms", "Applications", "Foundations", "Methods",
                     "Analysis", "Extensions", "Optimization", "Evaluation", "Perspectives"]

        for i in range(seed_count):
            year = random.choices(years, weights=weights, k=1)[0]

            if year < 2008:
                category = "foundation"
            elif year < 2016:
                category = "method"
            elif year < 2023:
                category = "neural"
            else:
                category = "frontier"

            title, abstract = self._generate_paper_content(topic, category, i)
            suffix_idx = 0
            base_title = title
            while title in used_titles:
                suffix_idx += 1
                if suffix_idx <= len(subtopics):
                    title = f"{base_title}: {subtopics[suffix_idx - 1]}"
                else:
                    title = f"{base_title} (Extended Edition {suffix_idx})"
            used_titles.add(title)

            author_count = random.randint(1, 5)
            first_names = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "J.", "K.",
                          "L.", "M.", "N.", "P.", "R.", "S.", "T.", "V.", "W.", "X."]
            authors = [
                random.choice(first_names) + " " + random.choice([
                    "Johnson", "Smith", "Williams", "Brown", "Jones", "Garcia",
                    "Miller", "Davis", "Rodriguez", "Martinez", "Anderson", "Taylor",
                    "Thomas", "Moore", "Jackson", "Martin", "Lee", "Perez",
                ]) for _ in range(author_count)
            ]

            cit_count = random.randint(0, 500 if category == "foundation" else 200 if category == "method" else 100)
            if year < 2010:
                cit_count = min(2000, cit_count * 3)

            papers.append(Paper(
                paper_id=f"demo_{i}",
                title=title,
                authors=authors,
                year=year,
                abstract=abstract,
                url=f"https://arxiv.org/abs/demo.{i}",
                citation_count=cit_count,
                source="demo",
                venue="",
            ))

        self._link_demo_citations(papers, topic)
        return papers

    def _generate_paper_content(self, topic: str, category: str, idx: int) -> tuple[str, str]:
        topic_words = re.findall(r"[A-Za-z0-9]+", topic.lower())
        key = topic_words[0] if topic_words else "method"
        random.seed(hash(topic + category + str(idx)) % (2**31))

        templates = {
            "foundation": [
                (f"A Theoretical Framework for {topic.title()}",
                 f"We present a foundational theoretical framework for {topic}. This work establishes the core mathematical principles and formal definitions that underpin subsequent research in this area. We prove fundamental properties including convergence bounds, optimality conditions, and structural characteristics of the problem space."),
                (f"On the Foundations of {topic.title()}",
                 f"This paper establishes the mathematical foundations of {topic}. We formalize the key concepts and provide rigorous proofs of the main theorems that form the basis of this research field. Our analysis covers the fundamental assumptions, limitations, and guarantees that later work builds upon."),
                (f"An Introduction to {topic.title()}: Theory and Principles",
                 f"A comprehensive introduction to the theoretical principles underlying {topic}. We survey the early literature, synthesize key results, and provide a unified framework for understanding the field. This tutorial serves as an essential reference for newcomers to this research area."),
                (f"Fundamental Concepts in {topic.title()}",
                 f"This tutorial introduces the fundamental concepts and notation used in {topic}. We cover the essential background material including mathematical preliminaries, problem formulation, and early algorithmic approaches. Suitable as a self-contained starting point for graduate students."),
                (f"Early Work on {topic.title()}: A Historical Perspective",
                 f"We trace the historical development of {topic} from its origins to the establishment of the core paradigm. This retrospective highlights key conceptual breakthroughs, their motivating contexts, and how early limitations shaped subsequent research directions."),
            ],
            "method": [
                (f"Efficient Algorithms for {topic.title()}",
                 f"We propose a novel algorithm for {topic} that achieves state-of-the-art performance while maintaining computational efficiency. Our method combines theoretical insights with practical optimizations, demonstrating significant improvements over existing approaches on standard benchmarks."),
                (f"Scalable Approaches to {topic.title()}",
                 f"This work addresses scalability challenges in {topic}. We develop a distributed framework that enables the application of {topic} methods to large-scale problems. Empirical evaluation demonstrates linear scaling properties and robust performance across diverse datasets."),
                (f"Robust {topic.title()}: A Practical Guide",
                 f"We present robust methods for applying {topic} in practical settings. Our approach handles noisy data, missing information, and adversarial perturbations while maintaining theoretical guarantees. Extensive experiments validate the practical utility of our contributions."),
                (f"Optimization Methods for {topic.title()}",
                 f"We develop optimization-based approaches for {topic} that provide stronger theoretical guarantees. Our method achieves faster convergence rates through novel variance reduction techniques. Experiments on challenging benchmarks confirm the advantages."),
                (f"A Unified Algorithmic Framework for {topic.title()}",
                 f"We propose a unified framework that encompasses many existing algorithms for {topic} as special cases. This abstraction enables principled comparisons and reveals new algorithmic variants with improved performance characteristics."),
            ],
            "neural": [
                (f"Deep Learning Approaches for {topic.title()}",
                 f"We introduce deep neural network architectures designed for {topic}. Our model learns effective representations from raw data, eliminating the need for hand-crafted features. We demonstrate substantial improvements on all standard benchmarks through extensive empirical evaluation."),
                (f"Neural {topic.title()}: End-to-End Learning",
                 f"This paper proposes an end-to-end neural framework for {topic}. By integrating representation learning with decision-making, our approach achieves superior performance compared to traditional pipeline methods. We provide theoretical analysis of the learned representations."),
                (f"Learning Representations for {topic.title()}",
                 f"We investigate representation learning techniques for {topic}. Our method learns compact, interpretable representations that capture the essential structure of the problem. Quantitative and qualitative analyses demonstrate the effectiveness of the learned embeddings."),
                (f"Attention Mechanisms for {topic.title()}",
                 f"We propose attention-based architectures that selectively focus on relevant parts of the input for {topic}. This inductive bias leads to improved generalization and enables the model to scale to larger problem instances while maintaining interpretability."),
                (f"Graph Neural Networks for {topic.title()}",
                 f"We adapt graph neural network architectures to the {topic} setting. By exploiting the inherent relational structure of the problem, our approach achieves strong inductive bias and data efficiency, outperforming previous methods on structured benchmarks."),
            ],
            "frontier": [
                (f"Recent Advances in {topic.title()}: A Survey",
                 f"This survey reviews the most recent advances in {topic}, covering developments from 2022 to the present. We identify key trends, highlight breakthrough results, and discuss open problems and promising research directions for the coming years."),
                (f"Open Problems and Future Directions in {topic.title()}",
                 f"We identify and discuss the major open problems in {topic}. For each problem, we review current approaches, their limitations, and propose concrete directions for future investigation. This paper serves as a research roadmap for the field."),
                (f"Towards {topic.title()}: Challenges and Opportunities",
                 f"An analysis of the current challenges and emerging opportunities in {topic}. We examine the gap between theoretical guarantees and practical performance, discuss the role of large-scale pretraining, and outline the path toward real-world deployment of these methods."),
                (f"Survey of {topic.title()}: Methods and Applications",
                 f"A comprehensive survey of {topic} covering both foundational methods and recent developments. We organize the literature into a coherent taxonomy, compare approaches on standardized benchmarks, and provide guidance for practitioners selecting methods for specific applications."),
                (f"Emerging Paradigms in {topic.title()}",
                 f"We examine emerging paradigms that are reshaping {topic}. Our analysis covers new theoretical frameworks, hardware-aware algorithms, and interdisciplinary connections that promise to advance the field beyond current limitations."),
            ],
        }

        cat_templates = templates.get(category, templates["method"])
        title, abstract = cat_templates[idx % len(cat_templates)]
        return title, abstract

    def _link_demo_citations(self, papers: list[Paper], topic: str) -> None:
        sorted_papers = sorted(papers, key=lambda p: p.year)

        for p in papers:
            older = [o for o in sorted_papers if o.year < p.year and o != p]
            if not older:
                continue

            n_refs = random.randint(1, min(5, len(older)))
            refs = random.sample(older, min(n_refs, len(older)))

            for ref in refs:
                if ref.paper_id not in p.references:
                    p.references.append(ref.paper_id)

        foundation = [p for p in papers if p.year < 2010]
        if foundation:
            top_foundation = max(foundation, key=lambda p: p.citation_count)
            for p in papers:
                if p.year >= 2010 and top_foundation.paper_id not in p.references and p != top_foundation:
                    if random.random() < 0.6:
                        p.references.append(top_foundation.paper_id)
