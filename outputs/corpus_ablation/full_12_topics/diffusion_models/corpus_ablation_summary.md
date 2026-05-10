# Corpus Construction Ablation: Diffusion Models / Score-Based Generative Models

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 34 | 0 | 100.0% | 44.1% | 32.4% | 100.0% | 73.5% | 255 | 7.50 |
| B_openalex_only | 36 | 4 | 91.7% | 100.0% | 100.0% | 80.0% | 22.2% | 75 | 2.08 |
| C_arxiv_openalex | 45 | 7 | 100.0% | 97.8% | 88.9% | 100.0% | 66.7% | 188 | 4.18 |
| D_plus_topic_filtering | 45 | 7 | 100.0% | 95.6% | 84.4% | 100.0% | 66.7% | 209 | 4.64 |
| E_plus_verified_landmarks | 45 | 7 | 100.0% | 95.6% | 84.4% | 100.0% | 66.7% | 209 | 4.64 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
