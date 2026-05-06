# Group Agent Evaluation: Counterfactual regret minimization

## Main Result Table

| Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers | Landmark Hit | Topic Precision | Ordering | Community Coverage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rule_only_agent | 43 | 394 | 1 | 100.0% | 4 | 0.1978 | 5 | 12 | 100.0% | 100.0% | 100.0% | 100.0% |
| llm_assisted_agent | 43 | 394 | 1 | 100.0% | 5 | 0.1941 | 5 | 13 | 100.0% | 100.0% | 100.0% | 100.0% |
| citation_graph | 15 | 3 | 13 | 20.0% | 13 | 0.0000 | 3 | 9 | 100.0% | 100.0% | 100.0% | 61.5% |
| similarity_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 4 | 10 | 100.0% | 100.0% | 100.0% | 100.0% |
| hybrid_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 4 | 11 | 100.0% | 100.0% | 100.0% | 100.0% |

## Reading-Path Quality Metrics

| Run | Landmark Hit Rate | Topic Precision | Ordering Quality | Community Coverage | Stage Coverage |
|---|---:|---:|---:|---:|---:|
| rule_only_agent | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| llm_assisted_agent | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| citation_graph | 100.0% | 100.0% | 100.0% | 61.5% | 75.0% |
| similarity_graph | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| hybrid_graph | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

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
- Curated or landmark records are transparent source categories. They improve recall for known foundational papers but are reported separately from retrieved API records.
