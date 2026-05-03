import numpy as np
import networkx as nx
from networkx.algorithms import community as nx_community

from shared.data_layer import SharedDataLayer
from shared.types import Paper, NodeScores, GraphData


class GraphAnalysisSkill:
    def __init__(self, data_layer: SharedDataLayer):
        self.data = data_layer
        self._graph: nx.Graph | None = None
        self._current_year: int = 2026

    def run(self) -> dict[str, NodeScores]:
        graph_data = self.data.get_graph_data()
        if not graph_data:
            raise ValueError("No graph data available. Run GraphBuilder.build() first.")

        G = self._build_networkx_graph(graph_data)
        self._graph = G

        scores: dict[str, NodeScores] = {}
        papers = self.data.get_all_papers()
        year_map = {p.paper_id: p.year for p in papers}

        pagerank = nx.pagerank(G, weight="weight") if G.number_of_edges() > 0 else {n: 1.0 / max(len(G.nodes()), 1) for n in G.nodes()}
        betweenness = nx.betweenness_centrality(G, weight="weight", normalized=True) if G.number_of_edges() > 0 else {n: 0.0 for n in G.nodes()}

        communities = self._detect_communities(G)

        for node in G.nodes():
            pr = pagerank.get(node, 0.0)
            bc = betweenness.get(node, 0.0)
            comm = communities.get(node, -1)
            year = year_map.get(node, self._current_year)

            foundation_score = self._compute_foundation_score(pr, year)
            bridge_score = self._compute_bridge_score(bc, G, node)
            frontier_score = self._compute_frontier_score(pr, year, comm, G, node)

            scores[node] = NodeScores(
                pagerank=round(pr, 4),
                betweenness=round(bc, 4),
                community=comm,
                foundation_score=round(foundation_score, 4),
                bridge_score=round(bridge_score, 4),
                frontier_score=round(frontier_score, 4),
            )

        self.data.set_node_scores(scores)
        return scores

    def _build_networkx_graph(self, graph_data: GraphData) -> nx.Graph:
        G = nx.Graph()
        for node in graph_data.nodes:
            G.add_node(node)
        for edge in graph_data.edges:
            G.add_edge(edge.source, edge.target, type=edge.type, weight=edge.weight)
        return G

    def _detect_communities(self, G: nx.Graph) -> dict[str, int]:
        if G.number_of_edges() < 2:
            return {n: 0 for n in G.nodes()}

        try:
            communities_gen = nx_community.louvain_communities(G, seed=42)
            community_map: dict[str, int] = {}
            for comm_id, comm_nodes in enumerate(communities_gen):
                for node in comm_nodes:
                    community_map[node] = comm_id
            for node in G.nodes():
                if node not in community_map:
                    community_map[node] = -1
            return community_map
        except Exception:
            components = list(nx.connected_components(G))
            community_map = {}
            for cid, comp in enumerate(components):
                for node in comp:
                    community_map[node] = cid
            return community_map

    def _compute_foundation_score(self, pagerank: float, year: int) -> float:
        AGE_WEIGHT = 0.4
        PR_WEIGHT = 0.6
        age_factor = max(0.0, min(1.0, (self._current_year - year) / 30.0))
        return AGE_WEIGHT * age_factor + PR_WEIGHT * pagerank

    def _compute_bridge_score(self, betweenness: float, G: nx.Graph, node: str) -> float:
        BC_WEIGHT = 0.5
        DEG_WEIGHT = 0.25
        CROSS_WEIGHT = 0.25

        betweenness_factor = min(1.0, betweenness * 5)
        degree_factor = min(1.0, G.degree(node) / max(1, max(dict(G.degree()).values())))

        communities = self._detect_communities(G)
        own_comm = communities.get(node, -1)
        neighbors = list(G.neighbors(node))
        cross_edges = sum(1 for nb in neighbors if communities.get(nb, -2) != own_comm)
        cross_factor = min(1.0, cross_edges / max(1, len(neighbors)))

        return BC_WEIGHT * betweenness_factor + DEG_WEIGHT * degree_factor + CROSS_WEIGHT * cross_factor

    def _compute_frontier_score(
        self, pagerank: float, year: int, community: int, G: nx.Graph, node: str
    ) -> float:
        RECENCY_WEIGHT = 0.5
        PR_WEIGHT = 0.3
        ACTIVITY_WEIGHT = 0.2

        recency_factor = max(0.0, min(1.0, (year - 2015) / max(1, self._current_year - 2015)))

        communities = self._detect_communities(G)
        comm_nodes = [n for n, c in communities.items() if c == community]
        comm_years = [
            self.data.get_paper(n).year for n in comm_nodes
            if self.data.get_paper(n) and self.data.get_paper(n).year > 0
        ]
        avg_year = np.mean(comm_years) if comm_years else self._current_year
        activity_factor = min(1.0, (avg_year - 2015) / max(1, self._current_year - 2015))

        return RECENCY_WEIGHT * recency_factor + PR_WEIGHT * pagerank + ACTIVITY_WEIGHT * activity_factor

    def get_community_info(self) -> dict:
        scores = self.data.get_all_scores()
        papers = self.data.get_all_papers()
        comms: dict[int, list[dict]] = {}
        for node, score in scores.items():
            cid = score.community
            if cid not in comms:
                comms[cid] = []
            paper = self.data.get_paper(node)
            if paper:
                comms[cid].append({
                    "paper_id": node,
                    "title": paper.title,
                    "pagerank": score.pagerank,
                    "year": paper.year,
                })

        info = {}
        for cid, members in comms.items():
            top_titles = sorted(members, key=lambda x: x["pagerank"], reverse=True)[:3]
            avg_year = int(np.mean([m["year"] for m in members if m["year"] > 0])) if members else 0
            info[cid] = {
                "size": len(members),
                "avg_year": avg_year,
                "top_papers": [t["title"] for t in top_titles],
            }
        return info

    def get_nx_graph(self) -> nx.Graph | None:
        return self._graph
