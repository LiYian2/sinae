# Corpus Construction Ablation: Graph Neural Networks / Geometric Deep Learning

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 24 | 1 | 100.0% | 66.7% | 62.5% | 83.3% | 66.7% | 132 | 5.50 |
| B_openalex_only | 31 | 9 | 87.1% | 100.0% | 90.3% | 66.7% | 38.7% | 137 | 4.42 |
| C_arxiv_openalex | 45 | 14 | 91.1% | 97.8% | 93.3% | 83.3% | 53.3% | 220 | 4.89 |
| D_plus_topic_filtering | 42 | 14 | 97.6% | 97.6% | 97.6% | 83.3% | 57.1% | 228 | 5.43 |
| E_plus_verified_landmarks | 43 | 14 | 97.7% | 97.7% | 97.7% | 100.0% | 58.1% | 232 | 5.40 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
