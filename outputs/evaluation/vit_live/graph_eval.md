# Research Graph Analysis Skill Report: Vision Transformer

## Functionality

This Skill builds paper networks and computes deterministic SNA metrics. Citation edges capture explicit references when available; similarity edges use TF-IDF cosine similarity over abstracts to reduce sparsity.

## Graph Ablation Results

| Graph Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Communities | Modularity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 29 | 36 | 36 | 0 | 12 | 62.1% | 15 | 0.2465 |
| similarity | 29 | 152 | 0 | 152 | 2 | 96.6% | 5 | 0.1692 |
| hybrid | 29 | 164 | 36 | 152 | 1 | 100.0% | 5 | 0.2623 |

## LLM-Labeled Communities

- **Community 0: Transformer / Vision / Tasks / Image** — Community 0 groups papers around transformer, vision, tasks, image.
- **Community 1: Code / Vision / Transformer / Image** — Community 1 groups papers around code, vision, transformer, image.
- **Community 2: Vision / Transformer / Transformers / Image** — Community 2 groups papers around vision, transformer, transformers, image.
- **Community 3: Vision / Transformers / Image / Transformer** — Community 3 groups papers around vision, transformers, image, transformer.
- **Community 4: Segmentation / Transformer / Vision / Self-Supervised** — Community 4 groups papers around segmentation, transformer, vision, self-supervised.

## Analysis

- Citation-only graphs are precise but sparse when references are missing from APIs.
- Similarity-only graphs improve connectivity but can over-cluster papers by language rather than citation structure.
- Hybrid graphs are the default because they preserve citation evidence while adding enough semantic edges for stable community detection.
- PageRank, betweenness, Louvain communities, and role scores are deterministic and are not computed by the LLM.
