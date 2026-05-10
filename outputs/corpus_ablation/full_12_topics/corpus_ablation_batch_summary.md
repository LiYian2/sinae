# Skill 1 Corpus Construction Ablation: Multi-Topic Benchmark

This ablation compares corpus construction variants used by the Literature Retrieval Skill.

## Average Metrics

| Variant | Topics | Papers | Raw Records | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 12 | 26.2 | 28.6 | 2.4 | 100.0% | 51.8% | 52.8% | 72.8% | 75.5% | 172.5 | 6.18 |
| B_openalex_only | 12 | 32.2 | 40.0 | 7.8 | 88.4% | 100.0% | 93.5% | 70.0% | 31.1% | 98.0 | 3.16 |
| C_arxiv_openalex | 12 | 45.0 | 68.6 | 12.6 | 96.7% | 92.8% | 89.1% | 90.3% | 60.6% | 224.8 | 5.00 |
| D_plus_topic_filtering | 12 | 40.0 | 68.6 | 12.6 | 98.6% | 92.8% | 88.8% | 90.3% | 66.6% | 241.4 | 5.93 |
| E_plus_verified_landmarks | 12 | 40.1 | 68.6 | 12.6 | 98.6% | 93.7% | 89.8% | 91.7% | 66.7% | 241.8 | 5.92 |

## Per-Topic Results

| Topic | Variant | Papers | Raw Records | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| protein_structure | A_arxiv_only | 14 | 20 | 6 | 100.0% | 85.7% | 78.6% | 0.0% | 57.1% | 47 | 3.36 |
| protein_structure | B_openalex_only | 36 | 40 | 4 | 83.3% | 100.0% | 100.0% | 80.0% | 41.7% | 127 | 3.53 |
| protein_structure | C_arxiv_openalex | 45 | 60 | 10 | 93.3% | 100.0% | 95.6% | 80.0% | 51.1% | 216 | 4.80 |
| protein_structure | D_plus_topic_filtering | 38 | 60 | 10 | 97.4% | 97.4% | 94.7% | 80.0% | 60.5% | 196 | 5.16 |
| protein_structure | E_plus_verified_landmarks | 38 | 60 | 10 | 97.4% | 97.4% | 94.7% | 80.0% | 60.5% | 196 | 5.16 |
| diffusion_models | A_arxiv_only | 34 | 34 | 0 | 100.0% | 44.1% | 32.4% | 100.0% | 73.5% | 255 | 7.50 |
| diffusion_models | B_openalex_only | 36 | 40 | 4 | 91.7% | 100.0% | 100.0% | 80.0% | 22.2% | 75 | 2.08 |
| diffusion_models | C_arxiv_openalex | 45 | 74 | 7 | 100.0% | 97.8% | 88.9% | 100.0% | 66.7% | 188 | 4.18 |
| diffusion_models | D_plus_topic_filtering | 45 | 74 | 7 | 100.0% | 95.6% | 84.4% | 100.0% | 66.7% | 209 | 4.64 |
| diffusion_models | E_plus_verified_landmarks | 45 | 74 | 7 | 100.0% | 95.6% | 84.4% | 100.0% | 66.7% | 209 | 4.64 |
| rag | A_arxiv_only | 30 | 34 | 4 | 100.0% | 43.3% | 46.7% | 100.0% | 86.7% | 190 | 6.33 |
| rag | B_openalex_only | 34 | 40 | 6 | 79.4% | 100.0% | 100.0% | 20.0% | 14.7% | 27 | 0.79 |
| rag | C_arxiv_openalex | 45 | 74 | 10 | 97.8% | 93.3% | 86.7% | 100.0% | 68.9% | 246 | 5.47 |
| rag | D_plus_topic_filtering | 42 | 74 | 10 | 97.6% | 92.9% | 88.1% | 100.0% | 73.8% | 329 | 7.83 |
| rag | E_plus_verified_landmarks | 42 | 74 | 10 | 97.6% | 92.9% | 88.1% | 100.0% | 73.8% | 329 | 7.83 |
| mechanistic_interpretability | A_arxiv_only | 20 | 26 | 6 | 100.0% | 50.0% | 50.0% | 40.0% | 70.0% | 81 | 4.05 |
| mechanistic_interpretability | B_openalex_only | 35 | 40 | 5 | 88.6% | 100.0% | 88.6% | 0.0% | 2.9% | 86 | 2.46 |
| mechanistic_interpretability | C_arxiv_openalex | 45 | 66 | 11 | 93.3% | 93.3% | 86.7% | 40.0% | 33.3% | 149 | 3.31 |
| mechanistic_interpretability | D_plus_topic_filtering | 24 | 66 | 11 | 100.0% | 87.5% | 83.3% | 40.0% | 58.3% | 94 | 3.92 |
| mechanistic_interpretability | E_plus_verified_landmarks | 24 | 66 | 11 | 100.0% | 87.5% | 83.3% | 40.0% | 58.3% | 94 | 3.92 |
| gnn | A_arxiv_only | 24 | 25 | 1 | 100.0% | 66.7% | 62.5% | 83.3% | 66.7% | 132 | 5.50 |
| gnn | B_openalex_only | 31 | 40 | 9 | 87.1% | 100.0% | 90.3% | 66.7% | 38.7% | 137 | 4.42 |
| gnn | C_arxiv_openalex | 45 | 65 | 14 | 91.1% | 97.8% | 93.3% | 83.3% | 53.3% | 220 | 4.89 |
| gnn | D_plus_topic_filtering | 42 | 65 | 14 | 97.6% | 97.6% | 97.6% | 83.3% | 57.1% | 228 | 5.43 |
| gnn | E_plus_verified_landmarks | 43 | 65 | 14 | 97.7% | 97.7% | 97.7% | 100.0% | 58.1% | 232 | 5.40 |
| causal_ml | A_arxiv_only | 15 | 15 | 0 | 100.0% | 60.0% | 86.7% | 20.0% | 60.0% | 37 | 2.47 |
| causal_ml | B_openalex_only | 33 | 40 | 7 | 84.8% | 100.0% | 93.9% | 80.0% | 33.3% | 71 | 2.15 |
| causal_ml | C_arxiv_openalex | 45 | 55 | 8 | 88.9% | 93.3% | 95.6% | 80.0% | 42.2% | 114 | 2.53 |
| causal_ml | D_plus_topic_filtering | 41 | 55 | 8 | 95.1% | 95.1% | 95.1% | 80.0% | 46.3% | 107 | 2.61 |
| causal_ml | E_plus_verified_landmarks | 41 | 55 | 8 | 95.1% | 95.1% | 95.1% | 80.0% | 46.3% | 107 | 2.61 |
| ssl_vision | A_arxiv_only | 26 | 29 | 3 | 100.0% | 53.8% | 53.8% | 83.3% | 96.2% | 200 | 7.69 |
| ssl_vision | B_openalex_only | 27 | 40 | 13 | 96.3% | 100.0% | 100.0% | 83.3% | 37.0% | 94 | 3.48 |
| ssl_vision | C_arxiv_openalex | 45 | 69 | 20 | 100.0% | 93.3% | 88.9% | 100.0% | 68.9% | 225 | 5.00 |
| ssl_vision | D_plus_topic_filtering | 39 | 69 | 20 | 100.0% | 97.4% | 94.9% | 100.0% | 74.4% | 191 | 4.90 |
| ssl_vision | E_plus_verified_landmarks | 39 | 69 | 20 | 100.0% | 97.4% | 94.9% | 100.0% | 74.4% | 191 | 4.90 |
| efficient_transformers | A_arxiv_only | 33 | 33 | 0 | 100.0% | 33.3% | 36.4% | 100.0% | 72.7% | 265 | 8.03 |
| efficient_transformers | B_openalex_only | 32 | 40 | 8 | 90.6% | 100.0% | 81.2% | 50.0% | 25.0% | 90 | 2.81 |
| efficient_transformers | C_arxiv_openalex | 45 | 73 | 10 | 100.0% | 82.2% | 80.0% | 100.0% | 66.7% | 213 | 4.73 |
| efficient_transformers | D_plus_topic_filtering | 45 | 73 | 10 | 100.0% | 82.2% | 75.6% | 100.0% | 66.7% | 497 | 11.04 |
| efficient_transformers | E_plus_verified_landmarks | 45 | 73 | 10 | 100.0% | 93.3% | 86.7% | 100.0% | 66.7% | 497 | 11.04 |
| rlhf | A_arxiv_only | 28 | 28 | 0 | 100.0% | 50.0% | 46.4% | 66.7% | 75.0% | 167 | 5.96 |
| rlhf | B_openalex_only | 40 | 40 | 0 | 90.0% | 100.0% | 85.0% | 100.0% | 5.0% | 104 | 2.60 |
| rlhf | C_arxiv_openalex | 45 | 68 | 1 | 100.0% | 91.1% | 88.9% | 100.0% | 48.9% | 205 | 4.56 |
| rlhf | D_plus_topic_filtering | 45 | 68 | 1 | 97.8% | 91.1% | 80.0% | 100.0% | 48.9% | 216 | 4.80 |
| rlhf | E_plus_verified_landmarks | 45 | 68 | 1 | 97.8% | 91.1% | 80.0% | 100.0% | 48.9% | 216 | 4.80 |
| nerf_3dgs | A_arxiv_only | 29 | 36 | 7 | 100.0% | 37.9% | 44.8% | 100.0% | 89.7% | 252 | 8.69 |
| nerf_3dgs | B_openalex_only | 24 | 40 | 16 | 100.0% | 100.0% | 100.0% | 100.0% | 62.5% | 133 | 5.54 |
| nerf_3dgs | C_arxiv_openalex | 45 | 76 | 30 | 100.0% | 88.9% | 91.1% | 100.0% | 75.6% | 304 | 6.76 |
| nerf_3dgs | D_plus_topic_filtering | 37 | 76 | 30 | 100.0% | 91.9% | 97.3% | 100.0% | 91.9% | 243 | 6.57 |
| nerf_3dgs | E_plus_verified_landmarks | 37 | 76 | 30 | 100.0% | 91.9% | 97.3% | 100.0% | 91.9% | 243 | 6.57 |
| marl | A_arxiv_only | 32 | 32 | 0 | 100.0% | 37.5% | 40.6% | 100.0% | 68.8% | 213 | 6.66 |
| marl | B_openalex_only | 31 | 40 | 9 | 83.9% | 100.0% | 90.3% | 100.0% | 38.7% | 125 | 4.03 |
| marl | C_arxiv_openalex | 45 | 72 | 13 | 100.0% | 84.4% | 80.0% | 100.0% | 66.7% | 280 | 6.22 |
| marl | D_plus_topic_filtering | 38 | 72 | 13 | 100.0% | 86.8% | 81.6% | 100.0% | 71.1% | 243 | 6.39 |
| marl | E_plus_verified_landmarks | 38 | 72 | 13 | 100.0% | 86.8% | 81.6% | 100.0% | 71.1% | 243 | 6.39 |
| federated_learning | A_arxiv_only | 29 | 31 | 2 | 100.0% | 58.6% | 55.2% | 80.0% | 89.7% | 231 | 7.97 |
| federated_learning | B_openalex_only | 27 | 40 | 13 | 85.2% | 100.0% | 92.6% | 80.0% | 51.9% | 107 | 3.96 |
| federated_learning | C_arxiv_openalex | 45 | 71 | 17 | 95.6% | 97.8% | 93.3% | 100.0% | 84.4% | 338 | 7.51 |
| federated_learning | D_plus_topic_filtering | 44 | 71 | 17 | 97.7% | 97.7% | 93.2% | 100.0% | 84.1% | 344 | 7.82 |
| federated_learning | E_plus_verified_landmarks | 44 | 71 | 17 | 97.7% | 97.7% | 93.2% | 100.0% | 84.1% | 344 | 7.82 |

## Interpretation

- Higher paper count is useful only when topic precision remains acceptable.
- Duplicate removal measures how much redundant API overlap was cleaned before graph construction.
- Citation/reference coverage measures whether the corpus can support citation-aware downstream analysis.
- Graph edge yield is the key downstream-readiness metric: it measures whether retrieved papers can form a usable graph rather than a disconnected list.
- The verified-landmark variant is designed to improve recall of known milestones, not to maximize every metric simultaneously.
