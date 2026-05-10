# Corpus Construction Ablation: RLHF and Preference Optimization

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 28 | 0 | 100.0% | 50.0% | 46.4% | 66.7% | 75.0% | 167 | 5.96 |
| B_openalex_only | 40 | 0 | 90.0% | 100.0% | 85.0% | 100.0% | 5.0% | 104 | 2.60 |
| C_arxiv_openalex | 45 | 1 | 100.0% | 91.1% | 88.9% | 100.0% | 48.9% | 205 | 4.56 |
| D_plus_topic_filtering | 45 | 1 | 97.8% | 91.1% | 80.0% | 100.0% | 48.9% | 216 | 4.80 |
| E_plus_verified_landmarks | 45 | 1 | 97.8% | 91.1% | 80.0% | 100.0% | 48.9% | 216 | 4.80 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
