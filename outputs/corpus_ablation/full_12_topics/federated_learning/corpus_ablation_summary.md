# Corpus Construction Ablation: Federated Learning and Privacy-Preserving ML

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 29 | 2 | 100.0% | 58.6% | 55.2% | 80.0% | 89.7% | 231 | 7.97 |
| B_openalex_only | 27 | 13 | 85.2% | 100.0% | 92.6% | 80.0% | 51.9% | 107 | 3.96 |
| C_arxiv_openalex | 45 | 17 | 95.6% | 97.8% | 93.3% | 100.0% | 84.4% | 338 | 7.51 |
| D_plus_topic_filtering | 44 | 17 | 97.7% | 97.7% | 93.2% | 100.0% | 84.1% | 344 | 7.82 |
| E_plus_verified_landmarks | 44 | 17 | 97.7% | 97.7% | 93.2% | 100.0% | 84.1% | 344 | 7.82 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
