# Corpus Construction Ablation: Causal Inference in Machine Learning

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 15 | 0 | 100.0% | 60.0% | 86.7% | 20.0% | 60.0% | 37 | 2.47 |
| B_openalex_only | 33 | 7 | 84.8% | 100.0% | 93.9% | 80.0% | 33.3% | 71 | 2.15 |
| C_arxiv_openalex | 45 | 8 | 88.9% | 93.3% | 95.6% | 80.0% | 42.2% | 114 | 2.53 |
| D_plus_topic_filtering | 41 | 8 | 95.1% | 95.1% | 95.1% | 80.0% | 46.3% | 107 | 2.61 |
| E_plus_verified_landmarks | 41 | 8 | 95.1% | 95.1% | 95.1% | 80.0% | 46.3% | 107 | 2.61 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
