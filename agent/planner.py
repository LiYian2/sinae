import re
from typing import Optional
from enum import Enum

from shared.data_layer import SharedDataLayer
from shared.types import (
    Paper, ResearchProfile, UserLevel, IntentType, ReadingPath,
)
from skill_retrieval.retrieval import LiteratureRetrievalSkill
from skill_graph.graph_builder import GraphBuilder
from skill_graph.analysis import GraphAnalysisSkill
from skill_reading_path.path_generator import ReadingPathSkill
from skill_reading_path.report import ReportGenerator
from skill_reading_path.visualization import VisualizationEngine


class PlannerState(Enum):
    IDLE = "idle"
    CORPUS_READY = "corpus_ready"
    GRAPH_READY = "graph_ready"
    PATH_READY = "path_ready"


class AgentPlanner:
    def __init__(self):
        self.data = SharedDataLayer()
        self.state = PlannerState.IDLE
        self.demo = False

        self.retrieval = LiteratureRetrievalSkill(self.data)
        self.graph_builder = GraphBuilder(self.data)
        self.graph_analysis = GraphAnalysisSkill(self.data)
        self.path_gen = ReadingPathSkill(self.data)
        self.reporter = ReportGenerator(self.data)
        self.visualizer = VisualizationEngine(self.data)

    def process(self, user_input: str) -> str:
        intent = self._detect_intent(user_input)
        profile = self._extract_profile(user_input)

        if intent == IntentType.BUILD_READING_PATH:
            return self._workflow_build_reading_path(profile, user_input)
        elif intent == IntentType.EXPLAIN_PAPER:
            return self._workflow_explain_paper(user_input)
        elif intent == IntentType.FILTER_BY_YEAR:
            return self._workflow_filter_by_year(user_input)
        elif intent == IntentType.FIND_BRIDGE_PAPERS:
            return self._workflow_find_bridge_papers(user_input)
        elif intent == IntentType.VISUALIZE:
            return self._workflow_visualize()
        elif intent == IntentType.ASK_FOLLOWUP:
            return self._workflow_followup(user_input)
        else:
            return "I couldn't determine your intent. Try asking me to build a reading path, explain a paper, filter by year, find bridge papers, or visualize the network."

    def _detect_intent(self, text: str) -> IntentType:
        t = text.lower()

        if any(kw in t for kw in [
            "reading path", "reading plan", "build", "create", "generate",
            "enter the field", "i want to learn", "i want to enter",
            "i am new to", "introduce me", "get me started",
            "i want to study", "i want to understand",
        ]):
            return IntentType.BUILD_READING_PATH

        if any(kw in t for kw in ["explain", "why is", "what role", "tell me about this paper"]):
            return IntentType.EXPLAIN_PAPER

        if any(kw in t for kw in ["after", "since", "only", "filter by year", "show papers from"]):
            if re.search(r"(19|20)\d{2}", t):
                return IntentType.FILTER_BY_YEAR
            return IntentType.BUILD_READING_PATH

        if any(kw in t for kw in ["bridge", "betweenness", "connect"]):
            return IntentType.FIND_BRIDGE_PAPERS

        if any(kw in t for kw in ["visualize", "plot", "draw", "show me the network", "render"]):
            return IntentType.VISUALIZE

        if self.state != PlannerState.IDLE:
            return IntentType.ASK_FOLLOWUP

        return IntentType.BUILD_READING_PATH

    def _extract_profile(self, text: str) -> ResearchProfile:
        t = text.lower()

        if "beginner" in t or "new to" in t or "introduce" in t or "entry" in t:
            level = UserLevel.BEGINNER
        elif "advanced" in t or "expert" in t or "state of the art" in t:
            level = UserLevel.ADVANCED
        else:
            level = UserLevel.INTERMEDIATE

        # Try to find paper count preference
        count_match = re.search(r"(\d+)\s*(?:paper|reading)", t)
        preferred_length = int(count_match.group(1)) if count_match else 10

        # Detect time range
        time_range = "all"
        if "last year" in t or "past year" in t or re.search(r"since 202[4-5]", t):
            time_range = "last_year"
        elif "last 3" in t or "past 3" in t:
            time_range = "last_3_years"
        elif "last 5" in t or "past 5" in t:
            time_range = "last_5_years"

        max_papers = 100
        if "more" in t or "many" in t or "lots" in t or "comprehensive" in t:
            max_papers = 200

        return ResearchProfile(
            topic=text.strip(),
            time_range=time_range,
            max_papers=max_papers,
            user_level=level,
            preferred_length=preferred_length,
        )

    def _workflow_build_reading_path(self, profile: ResearchProfile, user_input: str) -> str:
        output: list[str] = []

        # Step 1: Clean topic
        topic = self._clean_topic(user_input)
        profile.topic = topic
        output.append(f"## Step 1: Understanding your goal\n")
        output.append(f"**Topic:** {topic}")
        output.append(f"**Level:** {profile.user_level.value}")
        output.append(f"**Target papers:** {profile.max_papers}\n")

        # Step 2: Retrieval
        output.append(f"## Step 2: Retrieving papers\n")
        papers = self.retrieval.run(profile, demo=self.demo)
        n_papers = len(papers)

        # Step 3: Corpus quality check and adaptive retrieval
        if n_papers < 30:
            output.append(f"Only {n_papers} papers found. Expanding search...")
            self.retrieval.expand_retrieval("related work", 30)
            self.retrieval.expand_retrieval("methods", 30)
            papers = self.data.get_all_papers()
            n_papers = len(papers)

        quality = self.data.get_corpus_quality()
        output.append(f"Retrieved **{n_papers}** papers")
        output.append(f"Abstract coverage: {quality.get('has_abstract_ratio', 0):.1%}")
        output.append(f"Year range: {quality.get('year_range', 'N/A')}")
        output.append(f"Citation data: {quality.get('has_citation_ratio', 0):.1%}\n")

        # Step 3: Build graph
        output.append(f"## Step 3: Building research graph\n")
        graph_data = self.graph_builder.build()
        output.append(f"Nodes: {len(graph_data.nodes)}")
        output.append(f"Edges: {len(graph_data.edges)}")
        n_citation = sum(1 for e in graph_data.edges if e.type == "citation")
        n_similarity = sum(1 for e in graph_data.edges if e.type == "similarity")
        output.append(f"Citation edges: {n_citation}, Similarity edges: {n_similarity}\n")

        # Step 4: Graph analysis
        output.append(f"## Step 4: Analyzing graph structure\n")
        scores = self.graph_analysis.run()
        comm_info = self.graph_analysis.get_community_info()
        output.append(f"**Communities found:** {len(comm_info)}")
        for cid, cinfo in comm_info.items():
            output.append(f"  - Community {cid}: {cinfo['size']} papers, avg year {cinfo['avg_year']}")
            output.append(f"    Top: {', '.join(cinfo['top_papers'][:2])}")
        output.append("")

        dense = n_papers
        if n_papers < 30:
            output.append("Warning: Corpus is small. Results may be limited. Try broader keywords.\n")

        # Step 5: Generate reading path
        output.append(f"## Step 5: Generating personalized reading path\n")
        path = self.path_gen.run()
        for stage in path.stages:
            output.append(f"### {stage['stage']}")
            for p in stage["papers"]:
                output.append(f"**{p['read_order']}. {p['title']}** ({p.get('year', 'N/A')})")
                output.append(f"   {p['reason']}")
            output.append("")

        self.state = PlannerState.PATH_READY

        # Step 6: Follow-up suggestions
        output.append(f"## Follow-up Questions")
        for i, q in enumerate(path.followup_suggestions[:5], 1):
            output.append(f"{i}. \"{q}\"")

        output.append(f"\n*Try asking: \"visualize the network\", \"show bridge papers\", or \"give me a 7-day plan\"*\n")

        return "\n".join(output)

    def _workflow_explain_paper(self, user_input: str) -> str:
        papers = self.data.get_all_papers()
        if not papers:
            return "No papers loaded yet. Please build a reading path first."

        t = user_input.lower()
        matched: Optional[Paper] = None
        for p in papers:
            title_lower = p.title.lower()
            words = re.findall(r"\w+", t)
            matches = sum(1 for w in words if len(w) > 3 and w in title_lower)
            if matches >= 3:
                matched = p
                break

        if not matched:
            paper_list = "\n".join(
                f"- [{p.year}] {p.title[:80]} (ID: {p.paper_id[:30]})"
                for p in papers[:10]
            )
            return f"Which paper would you like explained? Here are some loaded papers:\n{paper_list}\n\nOr say: 'explain the paper about [keywords]'"

        return self.reporter.explain_paper_role(matched.paper_id)

    def _workflow_filter_by_year(self, user_input: str) -> str:
        year_match = re.search(r"(19|20)\d{2}", user_input)
        if not year_match:
            return "Please specify a year (e.g., 'show papers after 2020')."

        min_year = int(year_match.group(0))

        old_papers = self.data.get_all_papers()
        filtered = [p for p in old_papers if p.year >= min_year]

        output = [f"Filtering papers to year >= {min_year}:"]
        output.append(f"  Before: {len(old_papers)} papers")
        output.append(f"  After: {len(filtered)} papers\n")

        self.data.clear_papers()
        self.data.add_papers(filtered)
        self.graph_builder.build()
        self.graph_analysis.run()
        path = self.path_gen.run()
        self.state = PlannerState.PATH_READY

        output.append("## Updated Reading Path\n")
        for stage in path.stages:
            output.append(f"### {stage['stage']}")
            for p in stage["papers"]:
                output.append(f"**{p['read_order']}. {p['title']}** ({p.get('year', 'N/A')})")
            output.append("")

        return "\n".join(output)

    def _workflow_find_bridge_papers(self, user_input: str) -> str:
        if self.state == PlannerState.IDLE:
            return "No graph data available. Please build a reading path first."

        return self.reporter.generate_bridge_report()

    def _workflow_visualize(self) -> str:
        if self.state == PlannerState.IDLE:
            return "No graph data available. Please build a reading path first."

        output: list[str] = ["## Generating Visualizations\n"]

        try:
            path = self.visualizer.render_network("research_graph.png")
            output.append(f"- Network graph saved to: `{path}`")
        except Exception as e:
            output.append(f"- Network graph failed: {e}")

        try:
            path = self.visualizer.render_score_distribution("scores_distribution.png")
            output.append(f"- Score distributions saved to: `{path}`")
        except Exception as e:
            output.append(f"- Score distributions failed: {e}")

        return "\n".join(output)

    def _workflow_followup(self, user_input: str) -> str:
        t = user_input.lower()

        if any(kw in t for kw in ["7-day", "7 day", "weekly", "schedule"]):
            return self.reporter.generate_seven_day_plan()

        if any(kw in t for kw in ["author", "who should i follow"]):
            papers = self.data.get_all_papers()
            author_counts: dict[str, int] = {}
            for p in papers:
                for a in p.authors:
                    author_counts[a] = author_counts.get(a, 0) + 1
            top = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            lines = ["# Top Authors to Follow\n"]
            for name, count in top:
                lines.append(f"- **{name}** — {count} papers in corpus")
            return "\n".join(lines)

        if any(kw in t for kw in ["summary", "report", "briefing"]):
            return self.reporter.generate()

        if any(kw in t for kw in ["open problem", "research gap", "gap"]):
            scores = self.data.get_all_scores()
            sorted_frontier = sorted(scores.items(), key=lambda x: x[1].frontier_score, reverse=True)[:10]
            lines = ["# Research Gaps & Open Problems\n"]
            lines.append("Based on frontier paper analysis:\n")
            for pid, sc in sorted_frontier:
                p = self.data.get_paper(pid)
                if p:
                    lines.append(f"- **{p.title}** ({p.year}) — frontier score: {sc.frontier_score:.3f}")
            return "\n".join(lines)

        if any(kw in t for kw in ["foundation", "foundational"]):
            scores = self.data.get_all_scores()
            sorted_found = sorted(scores.items(), key=lambda x: x[1].foundation_score, reverse=True)[:10]
            lines = ["# Foundation Papers\n"]
            for pid, sc in sorted_found:
                p = self.data.get_paper(pid)
                if p:
                    lines.append(f"- **{p.title}** ({p.year}) — foundation score: {sc.foundation_score:.3f}")
            return "\n".join(lines)

        return self._workflow_build_reading_path(
            self._extract_profile(user_input), user_input
        )

    def _clean_topic(self, text: str) -> str:
        prefixes = [
            r"i want to (learn|study|enter|understand|research|explore)\s+(the\s+)?(field\s+of\s+)?",
            r"i am (trying to\s+)?(learning|getting into|starting)\s+(the\s+)?(field\s+of\s+)?",
            r"(build|create|generate|make|give)\s+(me\s+)?(a\s+)?(reading\s+)?(path|plan)\s+(for|about|on|understanding)\s+",
            r"i am new to\s+",
            r"introduce me to\s+",
            r"get me started (with|on)\s+",
            r"help me (understand|learn|study|explore)\s+(the\s+)?(field\s+of\s+)?",
            r"i would like to (learn|study|understand|explore|enter)\s+(the\s+)?(field\s+of\s+)?",
        ]
        for prefix in prefixes:
            text = re.sub(prefix, "", text, flags=re.IGNORECASE)
        text = text.strip(".,;: ")
        if len(text) > 80:
            text = text[:80]
        return text if text else "machine learning"
