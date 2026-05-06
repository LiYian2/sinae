# Research Graph Analysis Skill Final Report

## Functionality

The Research Graph Analysis Skill builds paper networks and computes deterministic social network analysis metrics. Citation edges encode explicit references when available; similarity edges use abstract/title similarity to reduce graph sparsity. The Skill computes PageRank, betweenness centrality, Louvain communities, and foundation/bridge/frontier role scores.

## Graph Ablation Results

| Topic | Graph Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Communities | Modularity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CFR | citation | 15 | 3 | 3 | 0 | 13 | 20.0% | 13 | 0.0000 |
| CFR | similarity | 15 | 53 | 0 | 53 | 1 | 100.0% | 3 | 0.0877 |
| CFR | hybrid | 15 | 53 | 3 | 53 | 1 | 100.0% | 3 | 0.0877 |
| ViT | citation | 29 | 36 | 36 | 0 | 12 | 62.1% | 15 | 0.2465 |
| ViT | similarity | 29 | 152 | 0 | 152 | 2 | 96.6% | 5 | 0.1692 |
| ViT | hybrid | 29 | 164 | 36 | 152 | 1 | 100.0% | 5 | 0.2623 |

## Analysis

Citation-only graphs are interpretable but sparse. This is clearest in CFR, where the citation graph has only 3 edges and 13 components among 15 nodes. Similarity edges solve this connectivity problem, producing a connected graph suitable for community detection and reading-path generation.

Hybrid graphs are the best default for the final Agent because they keep citation evidence while adding semantic connectivity. In ViT, the hybrid graph reaches a fully connected largest component and the highest modularity among the three graph modes. In CFR, hybrid and similarity are equivalent in this run because citation coverage is limited, which itself is useful evidence for the report: API reference coverage affects graph quality.

LLM community labeling is used only after deterministic graph computation. It names and describes communities using top papers and keywords, while PageRank, betweenness, modularity, and role scores remain code-computed.
