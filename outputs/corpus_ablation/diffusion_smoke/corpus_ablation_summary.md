# Corpus Construction Ablation: Diffusion Models / Score-Based Generative Models

| Variant | Papers | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 22 | 0 | 100.0% | 0.0% | 0.0% | 100.0% | 72.7% | 102 | 4.64 |
| B_openalex_only | 22 | 2 | 90.9% | 100.0% | 95.5% | 80.0% | 27.3% | 36 | 1.64 |
| C_arxiv_openalex | 25 | 5 | 96.0% | 56.0% | 44.0% | 100.0% | 52.0% | 116 | 4.64 |
| D_plus_topic_filtering | 25 | 5 | 100.0% | 44.0% | 32.0% | 100.0% | 64.0% | 123 | 4.92 |
| E_plus_verified_landmarks | 25 | 5 | 100.0% | 44.0% | 32.0% | 100.0% | 64.0% | 123 | 4.92 |

## Variant Definitions

- A: arXiv only.
- B: OpenAlex only.
- C: arXiv + OpenAlex.
- D: arXiv + OpenAlex + topic filtering.
- E: arXiv + OpenAlex + topic filtering + verified landmark recovery.

`Graph Edge Yield = hybrid graph edges / retained papers`; it measures how much graph-connectable structure Skill 1 provides to downstream graph analysis.
