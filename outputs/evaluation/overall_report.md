# ResearchTrail Overall Evaluation Report

## Evaluation Setup

We evaluated ResearchTrail on two live topics:

- `Counterfactual regret minimization` with an intermediate user profile.
- `Vision Transformer` with a beginner user profile.

Each topic was evaluated with five runs: a rule-only Agent, an LLM-assisted Agent, and three graph ablations (`citation`, `similarity`, and `hybrid`). Citation enrichment used Semantic Scholar when `S2_API_KEY` was available, then OpenAlex or curated landmark metadata as fallback.

## Main Results

| Topic | Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CFR | rule_only_agent | 43 | 394 | 1 | 100.0% | 4 | 0.2029 | 4 | 11 |
| CFR | llm_assisted_agent | 46 | 441 | 1 | 100.0% | 5 | 0.2079 | 4 | 11 |
| CFR | citation_graph | 15 | 3 | 13 | 20.0% | 13 | 0.0000 | 2 | 9 |
| CFR | similarity_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 5 | 11 |
| CFR | hybrid_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 5 | 11 |
| ViT | rule_only_agent | 84 | 829 | 1 | 100.0% | 5 | 0.2554 | 5 | 14 |
| ViT | llm_assisted_agent | 84 | 829 | 1 | 100.0% | 5 | 0.2554 | 5 | 14 |
| ViT | citation_graph | 29 | 36 | 12 | 62.1% | 15 | 0.2465 | 5 | 13 |
| ViT | similarity_graph | 29 | 152 | 2 | 96.6% | 5 | 0.1692 | 5 | 15 |
| ViT | hybrid_graph | 29 | 164 | 1 | 100.0% | 5 | 0.2623 | 5 | 14 |

## Findings

The Agent satisfies the course requirement of combining multiple Skills into one coherent system. Retrieval produces structured corpora, graph analysis computes deterministic network metrics, and reading-path generation turns graph evidence into staged user-facing recommendations.

Semantic Scholar enrichment materially improves citation quality for AI/CS papers. For example, `Deep Counterfactual Regret Minimization` is now reported as `239` citations from Semantic Scholar instead of the earlier OpenAlex value of `21`. The count still differs from Google Search or Google Scholar snippets, so reports explicitly label citation sources.

Hybrid graphs are the best default. Citation-only graphs are precise but sparse, especially for CFR where API references are incomplete. Similarity graphs restore connectivity, and hybrid graphs preserve citation evidence while ensuring usable connected components for community detection and reading-path generation.

LLM usage is bounded and evidence-grounded. The LLM is used for task parsing, query planning, community labeling, and concise why-read explanations. PageRank, betweenness, community detection, role scoring, filtering, and graph construction remain deterministic.

## Report Artifacts

- `outputs/evaluation/cfr_live/group_eval_summary.md`
- `outputs/evaluation/cfr_live/retrieval_eval.md`
- `outputs/evaluation/cfr_live/graph_eval.md`
- `outputs/evaluation/cfr_live/reading_path_eval.md`
- `outputs/evaluation/vit_live/group_eval_summary.md`
- `outputs/evaluation/vit_live/retrieval_eval.md`
- `outputs/evaluation/vit_live/graph_eval.md`
- `outputs/evaluation/vit_live/reading_path_eval.md`
- `outputs/evaluation/skill_retrieval_report.md`
- `outputs/evaluation/skill_graph_report.md`
- `outputs/evaluation/skill_reading_path_report.md`
