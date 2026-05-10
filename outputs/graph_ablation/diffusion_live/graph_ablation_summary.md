# Skill 2 Graph Mode Ablation: Diffusion Models / Score-Based Generative Models

| Mode | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Top Bridge Plausibility | Foundation Landmark Hit | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 9 | 9 | 0 | 4 | 72.7% | 0.2222 | 5 | 80.0% | 75.8% | 100.0% | 0.82 |
| similarity | 13 | 0 | 13 | 3 | 81.8% | 0.2048 | 5 | 80.0% | 78.5% | 0.0% | 1.18 |
| hybrid | 22 | 9 | 13 | 3 | 81.8% | 0.1978 | 5 | 80.0% | 85.5% | 100.0% | 2.00 |

## Interpretation Guide

- Citation-only is most faithful to scholarly dependency, but can be sparse when references are missing.
- Similarity-only improves connectivity and community coverage, but can over-connect papers with similar vocabulary.
- Hybrid is expected to balance citation evidence with semantic coverage.
- Top bridge plausibility is a deterministic proxy based on betweenness, cross-community neighbor ratio, and degree.
- Foundation landmark hit checks whether top foundation-score papers include known foundational landmarks.
