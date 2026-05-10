# Corpus Construction Ablation: Retrieval-Augmented Generation

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 30 | 4 | 100.0% | 43.3% | 46.7% | 100.0% | 86.7% | 190 | 6.33 |
| B_openalex_only | 34 | 6 | 79.4% | 100.0% | 100.0% | 20.0% | 14.7% | 27 | 0.79 |
| C_arxiv_openalex | 45 | 10 | 97.8% | 93.3% | 86.7% | 100.0% | 68.9% | 246 | 5.47 |
| D_plus_topic_filtering | 42 | 10 | 97.6% | 92.9% | 88.1% | 100.0% | 73.8% | 329 | 7.83 |
| E_plus_verified_landmarks | 42 | 10 | 97.6% | 92.9% | 88.1% | 100.0% | 73.8% | 329 | 7.83 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
