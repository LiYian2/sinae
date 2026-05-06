from shared.data_layer import SharedDataLayer


def collect_metrics(data: SharedDataLayer) -> dict:
    return {
        "retrieval": data.get_corpus_quality(),
        "graph": data.get_metadata("graph_metrics") or {},
        "reading_path": data.get_metadata("reading_path_metrics") or {},
        "planner_mode": data.get_metadata("planner_mode"),
        "query_plan": data.get_metadata("query_plan") or {},
        "community_labels": data.get_metadata("community_labels") or {},
    }


def markdown_table(results: dict[str, dict]) -> str:
    lines = [
        "| Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, metrics in results.items():
        retrieval = metrics.get("retrieval", {})
        graph = metrics.get("graph", {})
        path = metrics.get("reading_path", {})
        lines.append(
            "| {name} | {papers} | {edges} | {components} | {largest:.1%} | {communities} | {modularity:.4f} | {stages} | {path_papers} |".format(
                name=name,
                papers=retrieval.get("total_papers", 0),
                edges=graph.get("edge_count", 0),
                components=graph.get("connected_components", 0),
                largest=graph.get("largest_component_ratio", 0),
                communities=graph.get("community_count", 0),
                modularity=graph.get("modularity", 0),
                stages=path.get("stage_count", 0),
                path_papers=path.get("unique_paper_count", 0),
            )
        )
    return "\n".join(lines)

