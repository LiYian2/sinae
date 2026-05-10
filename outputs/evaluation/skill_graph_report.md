# Research Graph Analysis Skill Report

## Skill 2: Research Graph Analysis Implementation

Skill 2 builds citation and semantic-similarity graph structure. Citation edges preserve scholarly dependency, while TF-IDF similarity edges recover connectivity when citation/reference metadata is sparse. Analysis computes PageRank on a directed citation graph, undirected/hybrid community structure, betweenness with inverse-distance semantics for weighted similarity edges, Louvain/greedy communities, and foundation/bridge/frontier role scores. LLM is used only for community labels, not for centrality computation.

| Mode | Topics | Edges | Components | Largest Component | Modularity | Communities | Path Community Coverage | Bridge Plausibility | Foundation Landmark Hit | Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 12 | 7.2 | 17.2 | 20.2% | 0.0996 | 10.8 | 70.1% | 17.5% | 75.0% | 0.25 |
| similarity | 12 | 118.5 | 1.8 | 95.7% | 0.1712 | 4.0 | 89.2% | 77.6% | 75.0% | 4.81 |
| hybrid | 12 | 125.8 | 1.4 | 96.9% | 0.1792 | 3.9 | 91.4% | 81.9% | 66.7% | 5.06 |

Graph ablation conclusion: citation-only is theoretically clean but too sparse in this dataset, averaging only 7.2 edges and 20.2% largest component ratio. Similarity-only gives strong connectivity, but lacks citation direction. Hybrid is the production choice because it keeps citation evidence while improving largest component ratio to 96.9%, path community coverage to 91.4%, and bridge plausibility to 81.9%.

Secondary average excluding the low-corpus protein run shows the same trend: hybrid reaches 97.7% largest component ratio and 90.6% path community coverage.

## How to Use These Results

For the individual report, emphasize why citation-only is theoretically appealing but empirically sparse, and why the hybrid graph is justified for modern AI topics with incomplete reference metadata.
