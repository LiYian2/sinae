from typing import Optional

from shared.data_layer import SharedDataLayer
from shared.types import Paper, NodeScores, ReadingPath, ReadingPathItem, ResearchProfile, UserLevel
from shared.types import IntentType


class ReadingPathSkill:
    def __init__(self, data_layer: SharedDataLayer):
        self.data = data_layer

    def run(self) -> ReadingPath:
        papers = self.data.get_all_papers()
        scores = self.data.get_all_scores()
        profile = self.data.get_research_profile()

        if not papers or not scores:
            raise ValueError("Papers or scores not available. Run retrieval and graph analysis first.")

        # Classify papers into stages
        foundation = self._select_by_score_type(scores, "foundation_score", 3)
        core = self._select_by_score_type(scores, "pagerank", 3)
        bridges = self._select_by_score_type(scores, "bridge_score", 2)
        frontier = self._select_by_score_type(scores, "frontier_score", 3)

        # Remove duplicates across stages via paper_id set
        used_ids: set[str] = set()
        stages = self._build_stages(foundation, core, bridges, frontier, papers, scores, used_ids, profile)

        followup = self._generate_followup_suggestions(profile)
        report = self._generate_report_markdown(stages, profile)

        all_items: list[ReadingPathItem] = []
        for stage in stages:
            for p in stage["papers"]:
                all_items.append(ReadingPathItem(
                    paper_id=p["paper_id"],
                    title=p["title"],
                    reason=p["reason"],
                    read_order=p["read_order"],
                    stage=stage["stage"],
                ))

        path = ReadingPath(
            stages=stages,
            items=all_items,
            report_markdown=report,
            followup_suggestions=followup,
        )
        self.data.set_reading_path(path)
        return path

    def _select_by_score_type(
        self, scores: dict[str, NodeScores], score_field: str, top_n: int
    ) -> list[str]:
        scored = [(pid, getattr(s, score_field, 0.0)) for pid, s in scores.items()]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [pid for pid, _ in scored[:top_n]]

    def _build_stages(
        self,
        foundation_ids: list[str],
        core_ids: list[str],
        bridge_ids: list[str],
        frontier_ids: list[str],
        papers: list[Paper],
        scores: dict[str, NodeScores],
        used_ids: set[str],
        profile: Optional[ResearchProfile],
    ) -> list[dict]:
        paper_map = {p.paper_id: p for p in papers}
        score_map = scores

        stage_defs = [
            ("Foundations", foundation_ids, "Introduces foundational concepts for this research area."),
            ("Core Algorithms", core_ids, "Presents key algorithmic contributions and methods."),
            ("Bridge Papers", bridge_ids, "Connects different research communities or subfields."),
            ("Recent Frontier", frontier_ids, "Represents the latest advances and open problems."),
        ]

        if profile and profile.user_level == UserLevel.BEGINNER:
            stage_defs = [
                ("Conceptual Foundations", foundation_ids, "Explains the fundamental ideas and terminology."),
                ("Core Algorithms", core_ids, "Introduces the primary methods and techniques."),
                ("Bridge Papers", bridge_ids, "Links different ideas together for a broader understanding."),
                ("Recent Advances", frontier_ids, "Shows where the field is heading."),
            ]
        elif profile and profile.user_level == UserLevel.ADVANCED:
            stage_defs = [
                ("Foundations", foundation_ids, "Key prior work that established the field."),
                ("Core Methods", core_ids, "Central algorithmic contributions."),
                ("Research Gaps", bridge_ids, "Papers highlighting open problems and cross-field connections."),
                ("State of the Art", frontier_ids, "Most recent and impactful work."),
            ]

        stages: list[dict] = []
        order = 0
        for stage_name, ids, default_reason in stage_defs:
            stage_papers: list[dict] = []
            for pid in ids:
                if pid in used_ids:
                    continue
                paper = paper_map.get(pid)
                if not paper:
                    continue
                used_ids.add(pid)
                order += 1
                sc = score_map.get(pid)
                reason = self._generate_paper_reason(paper, sc, stage_name)
                stage_papers.append({
                    "paper_id": pid,
                    "title": paper.title,
                    "reason": reason or default_reason,
                    "read_order": order,
                    "year": paper.year,
                    "citation_count": paper.citation_count,
                })

            if stage_papers:
                stages.append({"stage": stage_name, "papers": stage_papers})

        return stages

    def _generate_paper_reason(
        self, paper: Paper, scores: Optional[NodeScores], stage: str
    ) -> str:
        if not scores:
            return ""

        if "Found" in stage:
            if scores.pagerank > 0.05:
                return f"Highly cited foundation paper ({paper.citation_count} citations). Establishes core principles of the field."
            return "Introduces the foundational framework that later work builds upon."
        elif "Core" in stage:
            return f"Central methodological contribution with significant impact (PageRank: {scores.pagerank:.3f})."
        elif "Bridge" in stage:
            if scores.bridge_score > 0.5:
                return f"Key bridge paper connecting multiple research communities (betweenness: {scores.betweenness:.3f})."
            return "Connects different subfields and provides broader context."
        elif "Frontier" in stage or "Recent" in stage:
            return f"Recent paper ({paper.year}) at the research frontier (frontier score: {scores.frontier_score:.3f})."
        return ""

    def _generate_report_markdown(self, stages: list[dict], profile: Optional[ResearchProfile]) -> str:
        lines = []
        topic = profile.topic if profile else "your research topic"
        level = profile.user_level.value if profile else "beginner"

        lines.append(f"# ResearchTrail Reading Path\n")
        lines.append(f"**Topic:** {topic}\n")
        lines.append(f"**Level:** {level}\n")
        lines.append(f"**Generated:** {self._timestamp()}\n")
        lines.append("---\n")

        for stage in stages:
            lines.append(f"## {stage['stage']}\n")
            for p in stage["papers"]:
                lines.append(f"### {p['read_order']}. {p['title']} ({p.get('year', 'N/A')})")
                lines.append(f"*{p['reason']}*")
                if "citation_count" in p and p["citation_count"] > 0:
                    lines.append(f"Citations: {p['citation_count']}")
                lines.append("")

        lines.append("---\n")
        total = sum(len(s["papers"]) for s in stages)
        lines.append(f"*Total: {total} papers in {len(stages)} stages.*\n")

        return "\n".join(lines)

    def _generate_followup_suggestions(self, profile: Optional[ResearchProfile]) -> list[str]:
        suggestions = [
            "Show bridge papers between key communities",
            "Generate a 7-day reading plan",
            "Show only papers after 2020",
            "Which authors should I follow?",
            "Replace theoretical papers with more applied papers",
            "Explain why these papers are foundational",
            "Show me the citation network visualization",
        ]
        if profile and profile.user_level == UserLevel.BEGINNER:
            suggestions.insert(0, "Add more survey and tutorial papers")
        if profile and profile.user_level == UserLevel.ADVANCED:
            suggestions.insert(0, "Show open problems and research gaps")
        return suggestions

    def filter_by_year(self, min_year: int) -> ReadingPath:
        papers = self.data.get_all_papers()
        filtered = [p for p in papers if p.year >= min_year]
        old_papers = {p.paper_id for p in self.data.get_all_papers()}
        self.data.clear_papers()
        self.data.add_papers(filtered)
        path = self.run()
        return path

    def regenerate_path(self) -> ReadingPath:
        return self.run()

    @staticmethod
    def _timestamp() -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
