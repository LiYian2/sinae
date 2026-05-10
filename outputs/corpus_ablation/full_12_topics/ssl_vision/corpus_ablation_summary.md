# Corpus Construction Ablation: Self-Supervised Learning in Vision

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 26 | 3 | 100.0% | 53.8% | 53.8% | 83.3% | 96.2% | 200 | 7.69 |
| B_openalex_only | 27 | 13 | 96.3% | 100.0% | 100.0% | 83.3% | 37.0% | 94 | 3.48 |
| C_arxiv_openalex | 45 | 20 | 100.0% | 93.3% | 88.9% | 100.0% | 68.9% | 225 | 5.00 |
| D_plus_topic_filtering | 39 | 20 | 100.0% | 97.4% | 94.9% | 100.0% | 74.4% | 191 | 4.90 |
| E_plus_verified_landmarks | 39 | 20 | 100.0% | 97.4% | 94.9% | 100.0% | 74.4% | 191 | 4.90 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
