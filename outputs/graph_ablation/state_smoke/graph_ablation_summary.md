# Skill 2 Graph Mode Ablation: Multi-Topic Benchmark

This ablation rebuilds citation-only, similarity-only, and hybrid graphs from the same saved corpora used in the full-agent benchmark.

## Average Metrics

| Mode | Topics | Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Top Bridge Plausibility | Foundation Landmark Hit | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 2 | 2.5 | 19.0 | 12.0% | 0.0000 | 9.5 | 72.2% | 4.0% | 100.0% | 0.12 |
| similarity | 2 | 87.0 | 1.5 | 97.5% | 0.1768 | 3.5 | 87.5% | 76.6% | 100.0% | 4.26 |
| hybrid | 2 | 89.5 | 1.5 | 97.5% | 0.2106 | 3.5 | 87.5% | 80.0% | 100.0% | 4.38 |

## Average Metrics Excluding Protein Structure

Protein structure had a low-paper corpus in the saved full-agent benchmark, so this secondary average reports the same metrics without that low-confidence topic.

| Mode | Topics | Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Top Bridge Plausibility | Foundation Landmark Hit | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 2 | 2.5 | 19.0 | 12.0% | 0.0000 | 9.5 | 72.2% | 4.0% | 100.0% | 0.12 |
| similarity | 2 | 87.0 | 1.5 | 97.5% | 0.1768 | 3.5 | 87.5% | 76.6% | 100.0% | 4.26 |
| hybrid | 2 | 89.5 | 1.5 | 97.5% | 0.2106 | 3.5 | 87.5% | 80.0% | 100.0% | 4.38 |

## Per-Topic Results

| Topic | Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Foundation Landmark Hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| diffusion_models | citation | 21 | 5 | 5 | 0 | 18 | 19.0% | 0.0000 | 18 | 44.4% | 100.0% |
| diffusion_models | similarity | 21 | 74 | 0 | 74 | 1 | 100.0% | 0.2277 | 3 | 100.0% | 100.0% |
| diffusion_models | hybrid | 21 | 79 | 5 | 74 | 1 | 100.0% | 0.2953 | 3 | 100.0% | 100.0% |
| rag | citation | 20 | 0 | 0 | 0 | 20 | 5.0% | 0.0000 | 1 | 100.0% | 100.0% |
| rag | similarity | 20 | 100 | 0 | 100 | 2 | 95.0% | 0.1258 | 4 | 75.0% | 100.0% |
| rag | hybrid | 20 | 100 | 0 | 100 | 2 | 95.0% | 0.1258 | 4 | 75.0% | 100.0% |

## Interpretation

- Citation-only is the cleanest dependency graph, but sparse metadata can fragment the graph.
- Similarity-only usually increases connectivity and graph edge yield, but its edges are semantic association rather than scholarly dependency.
- Hybrid graph is the production choice because it preserves citation edges and uses semantic edges to recover structure when references are incomplete.
