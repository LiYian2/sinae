# Corpus Construction Ablation: Neural Radiance Fields and 3D Gaussian Splatting

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 29 | 7 | 100.0% | 37.9% | 44.8% | 100.0% | 89.7% | 252 | 8.69 |
| B_openalex_only | 24 | 16 | 100.0% | 100.0% | 100.0% | 100.0% | 62.5% | 133 | 5.54 |
| C_arxiv_openalex | 45 | 30 | 100.0% | 88.9% | 91.1% | 100.0% | 75.6% | 304 | 6.76 |
| D_plus_topic_filtering | 37 | 30 | 100.0% | 91.9% | 97.3% | 100.0% | 91.9% | 243 | 6.57 |
| E_plus_verified_landmarks | 37 | 30 | 100.0% | 91.9% | 97.3% | 100.0% | 91.9% | 243 | 6.57 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
