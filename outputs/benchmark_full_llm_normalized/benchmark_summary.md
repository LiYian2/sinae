# ResearchTrail LLM-Assisted Benchmark

| ID | Papers | Landmark Hit | Topic Precision | Ordering | Community Coverage | Stage Coverage | Report |
|---|---:|---:|---:|---:|---:|---:|---|
| diffusion_models | 21 | 80.0% | 71.4% | 100.0% | 100.0% | 100.0% | `diffusion_models/research_report.md` |
| rag | 20 | 60.0% | 95.0% | 66.7% | 75.0% | 100.0% | `rag/research_report.md` |
| mechanistic_interpretability | 11 | 40.0% | 100.0% | 0.0% | 75.0% | 100.0% | `mechanistic_interpretability/research_report.md` |
| gnn | 33 | 33.3% | 87.9% | 100.0% | 100.0% | 100.0% | `gnn/research_report.md` |
| causal_ml | 18 | 40.0% | 100.0% | 100.0% | 71.4% | 75.0% | `causal_ml/research_report.md` |
| ssl_vision | 24 | 100.0% | 95.8% | 81.8% | 100.0% | 100.0% | `ssl_vision/research_report.md` |
| efficient_transformers | 14 | 100.0% | 85.7% | 45.5% | 100.0% | 100.0% | `efficient_transformers/research_report.md` |
| rlhf | 16 | 50.0% | 93.8% | 100.0% | 100.0% | 100.0% | `rlhf/research_report.md` |
| nerf_3dgs | 26 | 80.0% | 100.0% | 100.0% | 100.0% | 100.0% | `nerf_3dgs/research_report.md` |
| marl | 26 | 80.0% | 96.2% | 60.0% | 100.0% | 100.0% | `marl/research_report.md` |
| federated_learning | 41 | 80.0% | 100.0% | 66.7% | 75.0% | 100.0% | `federated_learning/research_report.md` |
| protein_structure | 8 | 0.0% | 75.0% | 0.0% | 100.0% | 75.0% | `protein_structure/research_report.md` |

## Notes

- This benchmark uses fixed benchmark topics and verified landmark candidates to avoid prompt parsing drift.
- Retrieval, graph analysis, community labeling, explanation writing, and report generation still run through the normal skills.
- It is intended to inspect report quality and research-trail coherence, not graph-mode ablations.
- Expected landmarks come from `evaluation/benchmark_registry.py` and are used only for evaluation.
