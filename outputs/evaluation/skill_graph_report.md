# Research Graph Analysis Skill Final Report

## Functionality

The Research Graph Analysis Skill builds paper networks and computes deterministic social network analysis metrics. Citation edges encode explicit references; similarity edges use abstract/title similarity to reduce sparsity. The Skill computes PageRank, betweenness centrality, Louvain communities, and foundation/bridge/frontier role scores.

## Graph Modeling Fixes

The implementation now treats citation and similarity edges with different semantics:

- Citation edges preserve direction: citing paper -> cited paper.
- PageRank/foundation scoring uses the directed citation graph when citation edges exist.
- Community detection uses the undirected similarity/hybrid projection.
- Betweenness centrality uses `distance = 1 / max(weight, eps)`, because NetworkX treats weighted betweenness weights as path lengths.

## Graph Ablation Results

| Topic | Graph Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Communities | Modularity | Community Coverage |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CFR | citation | 15 | 3 | 3 | 0 | 13 | 20.0% | 13 | 0.0000 | 61.5% |
| CFR | similarity | 15 | 53 | 0 | 53 | 1 | 100.0% | 3 | 0.0877 | 100.0% |
| CFR | hybrid | 15 | 53 | 3 | 53 | 1 | 100.0% | 3 | 0.0877 | 100.0% |
| ViT | citation | 29 | 36 | 36 | 0 | 12 | 62.1% | 15 | 0.2465 | 53.3% |
| ViT | similarity | 29 | 152 | 0 | 152 | 2 | 96.6% | 5 | 0.1692 | 80.0% |
| ViT | hybrid | 29 | 164 | 36 | 152 | 1 | 100.0% | 5 | 0.2623 | 100.0% |

## Analysis

Citation-only graphs are interpretable but sparse. This is clearest in CFR, where the citation graph has only 3 edges and 13 components among 15 nodes. Similarity edges solve this connectivity problem and make community-aware reading paths possible.

Hybrid graphs are the best default. In ViT, the hybrid graph has full largest-component coverage and reaches 100.0% reading-path community coverage, while citation-only reaches only 53.3%. This supports the claim that the hybrid graph improves path diversity and field coverage, not just graph density.

LLM community labeling is used only after deterministic graph computation. It names and describes communities using top papers and keywords; centrality, modularity, and role scores remain code-computed.
