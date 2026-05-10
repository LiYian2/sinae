# Corpus Construction Ablation: Protein Structure Prediction / Scientific ML

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 14 | 6 | 100.0% | 85.7% | 78.6% | 0.0% | 57.1% | 47 | 3.36 |
| B_openalex_only | 36 | 4 | 83.3% | 100.0% | 100.0% | 80.0% | 41.7% | 127 | 3.53 |
| C_arxiv_openalex | 45 | 10 | 93.3% | 100.0% | 95.6% | 80.0% | 51.1% | 216 | 4.80 |
| D_plus_topic_filtering | 38 | 10 | 97.4% | 97.4% | 94.7% | 80.0% | 60.5% | 196 | 5.16 |
| E_plus_verified_landmarks | 38 | 10 | 97.4% | 97.4% | 94.7% | 80.0% | 60.5% | 196 | 5.16 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
