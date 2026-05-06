# Group Agent Evaluation: Counterfactual regret minimization

## Main Result Table

| Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| rule_only_agent | 43 | 394 | 1 | 100.0% | 4 | 0.2029 | 4 | 11 |
| llm_assisted_agent | 46 | 441 | 1 | 100.0% | 5 | 0.2079 | 4 | 11 |
| citation_graph | 15 | 3 | 13 | 20.0% | 13 | 0.0000 | 2 | 9 |
| similarity_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 5 | 11 |
| hybrid_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 5 | 11 |

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
