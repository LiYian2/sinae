# Corpus Construction Ablation: Mechanistic Interpretability of Transformers

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 20 | 6 | 100.0% | 50.0% | 50.0% | 40.0% | 70.0% | 81 | 4.05 |
| B_openalex_only | 35 | 5 | 88.6% | 100.0% | 88.6% | 0.0% | 2.9% | 86 | 2.46 |
| C_arxiv_openalex | 45 | 11 | 93.3% | 93.3% | 86.7% | 40.0% | 33.3% | 149 | 3.31 |
| D_plus_topic_filtering | 24 | 11 | 100.0% | 87.5% | 83.3% | 40.0% | 58.3% | 94 | 3.92 |
| E_plus_verified_landmarks | 24 | 11 | 100.0% | 87.5% | 83.3% | 40.0% | 58.3% | 94 | 3.92 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
