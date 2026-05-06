# ResearchTrail LLM-Assisted Benchmark

| ID | Papers | Landmark Hit | Topic Precision | Ordering | Community Coverage | Stage Coverage | Report |
|---|---:|---:|---:|---:|---:|---:|---|
| diffusion_models | 31 | 80.0% | 100.0% | 100.0% | 100.0% | 100.0% | `diffusion_models/research_report.md` |
| rag | 21 | 60.0% | 100.0% | 66.7% | 75.0% | 100.0% | `rag/research_report.md` |
| mechanistic_interpretability | 11 | 40.0% | 100.0% | 0.0% | 75.0% | 100.0% | `mechanistic_interpretability/research_report.md` |

## Notes

- This benchmark uses fixed benchmark topics and verified landmark candidates to avoid prompt parsing drift.
- Retrieval, graph analysis, community labeling, explanation writing, and report generation still run through the normal skills.
- It is intended to inspect report quality and research-trail coherence, not graph-mode ablations.
- Expected landmarks come from `evaluation/benchmark_registry.py` and are used only for evaluation.
