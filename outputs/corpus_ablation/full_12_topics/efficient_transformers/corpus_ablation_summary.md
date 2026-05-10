# Corpus Construction Ablation: Efficient Transformers / Long-Context Modeling

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 33 | 0 | 100.0% | 33.3% | 36.4% | 100.0% | 72.7% | 265 | 8.03 |
| B_openalex_only | 32 | 8 | 90.6% | 100.0% | 81.2% | 50.0% | 25.0% | 90 | 2.81 |
| C_arxiv_openalex | 45 | 10 | 100.0% | 82.2% | 80.0% | 100.0% | 66.7% | 213 | 4.73 |
| D_plus_topic_filtering | 45 | 10 | 100.0% | 82.2% | 75.6% | 100.0% | 66.7% | 497 | 11.04 |
| E_plus_verified_landmarks | 45 | 10 | 100.0% | 93.3% | 86.7% | 100.0% | 66.7% | 497 | 11.04 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
