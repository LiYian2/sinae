# Corpus Construction Ablation: Retrieval-Augmented Generation

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 0 | 0 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0 | 0.00 |
| B_openalex_only | 21 | 3 | 81.0% | 100.0% | 100.0% | 20.0% | 14.3% | 21 | 1.00 |
| C_arxiv_openalex | 21 | 3 | 81.0% | 100.0% | 100.0% | 20.0% | 14.3% | 21 | 1.00 |
| D_plus_topic_filtering | 8 | 3 | 87.5% | 100.0% | 100.0% | 20.0% | 37.5% | 9 | 1.12 |
| E_plus_verified_landmarks | 8 | 3 | 87.5% | 100.0% | 100.0% | 20.0% | 37.5% | 9 | 1.12 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
