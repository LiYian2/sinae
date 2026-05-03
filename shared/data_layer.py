import json
from typing import Optional, Any
from shared.types import Paper, GraphData, NodeScores, ReadingPath, ResearchProfile


class SharedDataLayer:
    def __init__(self):
        self._store: dict[str, Any] = {
            "research_profile": None,
            "papers": {},
            "graph_data": None,
            "node_scores": {},
            "reading_path": None,
            "corpus_quality": {},
            "metadata": {},
        }

    def set_research_profile(self, profile: ResearchProfile) -> None:
        self._store["research_profile"] = profile

    def get_research_profile(self) -> Optional[ResearchProfile]:
        return self._store["research_profile"]

    def add_papers(self, papers: list[Paper]) -> None:
        for p in papers:
            self._store["papers"][p.paper_id] = p

    def get_paper(self, paper_id: str) -> Optional[Paper]:
        return self._store["papers"].get(paper_id)

    def get_all_papers(self) -> list[Paper]:
        return list(self._store["papers"].values())

    def get_paper_count(self) -> int:
        return len(self._store["papers"])

    def set_graph_data(self, graph_data: GraphData) -> None:
        self._store["graph_data"] = graph_data

    def get_graph_data(self) -> Optional[GraphData]:
        return self._store["graph_data"]

    def set_node_scores(self, scores: dict[str, NodeScores]) -> None:
        self._store["node_scores"] = scores

    def get_node_scores(self, paper_id: str) -> Optional[NodeScores]:
        return self._store["node_scores"].get(paper_id)

    def get_all_scores(self) -> dict[str, NodeScores]:
        return self._store["node_scores"]

    def set_reading_path(self, path: ReadingPath) -> None:
        self._store["reading_path"] = path

    def get_reading_path(self) -> Optional[ReadingPath]:
        return self._store["reading_path"]

    def set_corpus_quality(self, quality: dict) -> None:
        self._store["corpus_quality"] = quality

    def get_corpus_quality(self) -> dict:
        return self._store["corpus_quality"]

    def set_metadata(self, key: str, value: Any) -> None:
        self._store["metadata"][key] = value

    def get_metadata(self, key: str) -> Optional[Any]:
        return self._store["metadata"].get(key)

    def to_dict(self) -> dict:
        return {
            "research_profile": (
                self._store["research_profile"].to_dict()
                if self._store["research_profile"]
                else None
            ),
            "paper_count": len(self._store["papers"]),
            "papers": {
                pid: p.to_dict() for pid, p in self._store["papers"].items()
            },
            "node_scores": {
                pid: s.to_dict() for pid, s in self._store["node_scores"].items()
            },
        }

    def save(self, filepath: str) -> None:
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    def clear_papers(self) -> None:
        self._store["papers"] = {}
        self._store["graph_data"] = None
        self._store["node_scores"] = {}
        self._store["reading_path"] = None
        self._store["corpus_quality"] = {}
