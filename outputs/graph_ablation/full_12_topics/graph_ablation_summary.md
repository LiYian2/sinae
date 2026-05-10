# Skill 2 Graph Mode Ablation: Multi-Topic Benchmark

This ablation rebuilds citation-only, similarity-only, and hybrid graphs from the same saved corpora used in the full-agent benchmark.

## Average Metrics

| Mode | Topics | Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Top Bridge Plausibility | Foundation Landmark Hit | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 12 | 7.2 | 17.2 | 20.2% | 0.0996 | 10.8 | 70.1% | 17.5% | 75.0% | 0.25 |
| similarity | 12 | 118.5 | 1.8 | 95.7% | 0.1712 | 4.0 | 89.2% | 77.6% | 75.0% | 4.81 |
| hybrid | 12 | 125.8 | 1.4 | 96.9% | 0.1792 | 3.9 | 91.4% | 81.9% | 66.7% | 5.06 |

## Average Metrics Excluding Protein Structure

Protein structure had a low-paper corpus in the saved full-agent benchmark, so this secondary average reports the same metrics without that low-confidence topic.

| Mode | Topics | Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Top Bridge Plausibility | Foundation Landmark Hit | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 11 | 7.9 | 18.1 | 20.9% | 0.1086 | 11.6 | 67.3% | 19.1% | 81.8% | 0.27 |
| similarity | 11 | 128.2 | 1.8 | 96.5% | 0.1824 | 4.1 | 88.2% | 77.1% | 81.8% | 5.11 |
| hybrid | 11 | 136.1 | 1.4 | 97.7% | 0.1912 | 4.0 | 90.6% | 81.8% | 72.7% | 5.38 |

## Per-Topic Results

| Topic | Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Foundation Landmark Hit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| causal_ml | citation | 18 | 10 | 10 | 0 | 12 | 38.9% | 0.1667 | 14 | 57.1% | 100.0% |
| causal_ml | similarity | 18 | 35 | 0 | 35 | 3 | 88.9% | 0.3042 | 5 | 80.0% | 100.0% |
| causal_ml | hybrid | 18 | 45 | 10 | 35 | 3 | 88.9% | 0.1291 | 7 | 71.4% | 100.0% |
| diffusion_models | citation | 21 | 5 | 5 | 0 | 18 | 19.0% | 0.0000 | 18 | 44.4% | 100.0% |
| diffusion_models | similarity | 21 | 74 | 0 | 74 | 1 | 100.0% | 0.2277 | 3 | 100.0% | 100.0% |
| diffusion_models | hybrid | 21 | 79 | 5 | 74 | 1 | 100.0% | 0.2953 | 3 | 100.0% | 100.0% |
| efficient_transformers | citation | 14 | 0 | 0 | 0 | 14 | 7.1% | 0.0000 | 1 | 100.0% | 100.0% |
| efficient_transformers | similarity | 14 | 70 | 0 | 70 | 1 | 100.0% | 0.0871 | 3 | 100.0% | 100.0% |
| efficient_transformers | hybrid | 14 | 70 | 0 | 70 | 1 | 100.0% | 0.0871 | 3 | 100.0% | 100.0% |
| federated_learning | citation | 41 | 20 | 20 | 0 | 30 | 29.3% | 0.2750 | 31 | 22.6% | 0.0% |
| federated_learning | similarity | 41 | 326 | 0 | 326 | 4 | 92.7% | 0.2215 | 7 | 57.1% | 100.0% |
| federated_learning | hybrid | 41 | 346 | 20 | 326 | 1 | 100.0% | 0.2714 | 4 | 75.0% | 0.0% |
| gnn | citation | 33 | 37 | 37 | 0 | 14 | 60.6% | 0.2695 | 17 | 41.2% | 0.0% |
| gnn | similarity | 33 | 203 | 0 | 203 | 3 | 93.9% | 0.1661 | 6 | 83.3% | 0.0% |
| gnn | hybrid | 33 | 240 | 37 | 203 | 1 | 100.0% | 0.2780 | 5 | 100.0% | 0.0% |
| marl | citation | 26 | 10 | 10 | 0 | 19 | 26.9% | 0.2650 | 20 | 45.0% | 100.0% |
| marl | similarity | 26 | 140 | 0 | 140 | 1 | 100.0% | 0.2480 | 3 | 100.0% | 100.0% |
| marl | hybrid | 26 | 150 | 10 | 140 | 1 | 100.0% | 0.2799 | 4 | 100.0% | 100.0% |
| mechanistic_interpretability | citation | 11 | 0 | 0 | 0 | 11 | 9.1% | 0.0000 | 1 | 100.0% | 100.0% |
| mechanistic_interpretability | similarity | 11 | 24 | 0 | 24 | 2 | 90.9% | 0.1709 | 4 | 75.0% | 0.0% |
| mechanistic_interpretability | hybrid | 11 | 24 | 0 | 24 | 2 | 90.9% | 0.1709 | 4 | 75.0% | 0.0% |
| nerf_3dgs | citation | 26 | 4 | 4 | 0 | 22 | 19.2% | 0.2188 | 23 | 30.4% | 100.0% |
| nerf_3dgs | similarity | 26 | 214 | 0 | 214 | 1 | 100.0% | 0.2094 | 3 | 100.0% | 100.0% |
| nerf_3dgs | hybrid | 26 | 218 | 4 | 214 | 1 | 100.0% | 0.2196 | 3 | 100.0% | 100.0% |
| protein_structure | citation | 8 | 0 | 0 | 0 | 8 | 12.5% | 0.0000 | 1 | 100.0% | 0.0% |
| protein_structure | similarity | 8 | 12 | 0 | 12 | 2 | 87.5% | 0.0476 | 3 | 100.0% | 0.0% |
| protein_structure | hybrid | 8 | 12 | 0 | 12 | 2 | 87.5% | 0.0476 | 3 | 100.0% | 0.0% |
| rag | citation | 20 | 0 | 0 | 0 | 20 | 5.0% | 0.0000 | 1 | 100.0% | 100.0% |
| rag | similarity | 20 | 100 | 0 | 100 | 2 | 95.0% | 0.1258 | 4 | 75.0% | 100.0% |
| rag | hybrid | 20 | 100 | 0 | 100 | 2 | 95.0% | 0.1258 | 4 | 75.0% | 100.0% |
| rlhf | citation | 16 | 0 | 0 | 0 | 16 | 6.2% | 0.0000 | 1 | 100.0% | 100.0% |
| rlhf | similarity | 16 | 72 | 0 | 72 | 1 | 100.0% | 0.1021 | 3 | 100.0% | 100.0% |
| rlhf | hybrid | 16 | 72 | 0 | 72 | 1 | 100.0% | 0.1021 | 3 | 100.0% | 100.0% |
| ssl_vision | citation | 24 | 1 | 1 | 0 | 23 | 8.3% | 0.0000 | 1 | 100.0% | 100.0% |
| ssl_vision | similarity | 24 | 152 | 0 | 152 | 1 | 100.0% | 0.1438 | 4 | 100.0% | 100.0% |
| ssl_vision | hybrid | 24 | 153 | 1 | 152 | 1 | 100.0% | 0.1438 | 4 | 100.0% | 100.0% |

## Interpretation

- Citation-only is the cleanest dependency graph, but sparse metadata can fragment the graph.
- Similarity-only usually increases connectivity and graph edge yield, but its edges are semantic association rather than scholarly dependency.
- Hybrid graph is the production choice because it preserves citation edges and uses semantic edges to recover structure when references are incomplete.
