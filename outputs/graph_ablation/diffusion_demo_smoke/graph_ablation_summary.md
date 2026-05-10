# Skill 2 Graph Mode Ablation: Diffusion Models / Score-Based Generative Models

| Mode | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Top Bridge Plausibility | Foundation Landmark Hit | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 78 | 78 | 0 | 1 | 100.0% | 0.2691 | 3 | 100.0% | 86.0% | 0.0% | 3.12 |
| similarity | 125 | 0 | 125 | 1 | 100.0% | 0.4422 | 5 | 80.0% | 69.2% | 0.0% | 5.00 |
| hybrid | 203 | 78 | 125 | 1 | 100.0% | 0.2325 | 5 | 100.0% | 91.7% | 0.0% | 8.12 |

## Interpretation Guide

- Citation-only is most faithful to scholarly dependency, but can be sparse when references are missing.
- Similarity-only improves connectivity and community coverage, but can over-connect papers with similar vocabulary.
- Hybrid is expected to balance citation evidence with semantic coverage.
- Top bridge plausibility is a deterministic proxy based on betweenness, cross-community neighbor ratio, and degree.
- Foundation landmark hit checks whether top foundation-score papers include known foundational landmarks.
