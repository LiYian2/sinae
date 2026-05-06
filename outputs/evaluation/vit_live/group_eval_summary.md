# Group Agent Evaluation: Vision Transformer

## Main Result Table

| Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| rule_only_agent | 84 | 829 | 1 | 100.0% | 5 | 0.2554 | 5 | 14 |
| llm_assisted_agent | 84 | 829 | 1 | 100.0% | 5 | 0.2554 | 5 | 14 |
| citation_graph | 29 | 36 | 12 | 62.1% | 15 | 0.2465 | 5 | 13 |
| similarity_graph | 29 | 152 | 2 | 96.6% | 5 | 0.1692 | 5 | 15 |
| hybrid_graph | 29 | 164 | 1 | 100.0% | 5 | 0.2623 | 5 | 14 |

## Agent Behavior

- Planner mode: `llm`
- LLM query plan available: `True`
- LLM community labels available: `True`
- Evidence packets available: `True`

## Interpretation

- The Agent composes retrieval, graph analysis, and reading-path generation into one reproducible workflow.
- The deterministic graph metrics provide the structural basis for selecting foundation, bridge, and frontier papers.
- LLM calls are used for task parsing, query planning, community naming, and evidence-grounded why-read text; centrality and community computation remain deterministic.
- Demo-mode outputs are only for pipeline reliability checks. Report-quality claims should use live-mode arXiv/OpenAlex/Semantic Scholar results.
