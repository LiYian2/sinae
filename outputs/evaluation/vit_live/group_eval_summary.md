# Group Agent Evaluation: Vision Transformer

## Main Result Table

| Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers | Landmark Hit | Topic Precision | Ordering | Community Coverage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rule_only_agent | 84 | 829 | 1 | 100.0% | 5 | 0.2563 | 5 | 13 | 100.0% | 97.6% | 100.0% | 80.0% |
| llm_assisted_agent | 80 | 744 | 1 | 100.0% | 6 | 0.2723 | 5 | 13 | 100.0% | 96.2% | 100.0% | 83.3% |
| citation_graph | 29 | 36 | 12 | 62.1% | 15 | 0.2465 | 5 | 13 | 100.0% | 93.1% | 100.0% | 53.3% |
| similarity_graph | 29 | 152 | 2 | 96.6% | 5 | 0.1692 | 5 | 15 | 100.0% | 93.1% | 100.0% | 80.0% |
| hybrid_graph | 29 | 164 | 1 | 100.0% | 5 | 0.2623 | 5 | 13 | 100.0% | 93.1% | 100.0% | 100.0% |

## Reading-Path Quality Metrics

| Run | Landmark Hit Rate | Topic Precision | Ordering Quality | Community Coverage | Stage Coverage |
|---|---:|---:|---:|---:|---:|
| rule_only_agent | 100.0% | 97.6% | 100.0% | 80.0% | 100.0% |
| llm_assisted_agent | 100.0% | 96.2% | 100.0% | 83.3% | 100.0% |
| citation_graph | 100.0% | 93.1% | 100.0% | 53.3% | 100.0% |
| similarity_graph | 100.0% | 93.1% | 100.0% | 80.0% | 100.0% |
| hybrid_graph | 100.0% | 93.1% | 100.0% | 100.0% | 100.0% |

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
