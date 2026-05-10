# Corpus Construction Ablation: Multi-Agent Reinforcement Learning

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 32 | 0 | 100.0% | 37.5% | 40.6% | 100.0% | 68.8% | 213 | 6.66 |
| B_openalex_only | 31 | 9 | 83.9% | 100.0% | 90.3% | 100.0% | 38.7% | 125 | 4.03 |
| C_arxiv_openalex | 45 | 13 | 100.0% | 84.4% | 80.0% | 100.0% | 66.7% | 280 | 6.22 |
| D_plus_topic_filtering | 38 | 13 | 100.0% | 86.8% | 81.6% | 100.0% | 71.1% | 243 | 6.39 |
| E_plus_verified_landmarks | 38 | 13 | 100.0% | 86.8% | 81.6% | 100.0% | 71.1% | 243 | 6.39 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
