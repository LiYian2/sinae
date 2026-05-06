# Research Graph Analysis Skill Report: Counterfactual regret minimization

## Functionality

This Skill builds paper networks and computes deterministic SNA metrics. Citation edges capture explicit references when available; similarity edges use TF-IDF cosine similarity over abstracts to reduce sparsity.

## Graph Ablation Results

| Graph Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Communities | Modularity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 15 | 3 | 3 | 0 | 13 | 20.0% | 13 | 0.0000 |
| similarity | 15 | 53 | 0 | 53 | 1 | 100.0% | 3 | 0.0877 |
| hybrid | 15 | 53 | 3 | 53 | 1 | 100.0% | 3 | 0.0877 |

## LLM-Labeled Communities

- **Community 0: Imperfect Recall and Abstraction in Games** — This community focuses on regret minimization algorithms in extensive-form games, specifically addressing challenges like imperfect recall, bounded memory, and the construction of abstractions.
- **Community 1: Deep Counterfactual Regret Minimization** — Research in this area applies deep learning and function approximation techniques to counterfactual regret minimization for solving games.
- **Community 2: Optimistic Regret Minimization and Convergence** — This community investigates theoretical improvements to regret minimization algorithms, focusing on optimistic methods, convergence rates, and techniques like mirror descent.
- **Community 3: Sampling and Accelerated Regret Minimization** — This community develops methods to accelerate counterfactual regret minimization through Monte Carlo sampling, GPU acceleration, and neural network integration.
- **Community 4: Regret Minimization for Incomplete Information and Search** — This community explores regret minimization strategies for games with incomplete information, emphasizing search algorithms, information gain, and efficient Nash equilibrium approximation.

## Analysis

- Citation-only graphs are precise but sparse when references are missing from APIs.
- Similarity-only graphs improve connectivity but can over-cluster papers by language rather than citation structure.
- Hybrid graphs are the default because they preserve citation evidence while adding enough semantic edges for stable community detection.
- Citation PageRank is computed on a directed citation graph where citing papers point to cited papers. Community detection uses the undirected semantic/hybrid projection.
- Betweenness centrality uses `distance = 1 / weight` so stronger similarity means shorter graph distance.
- PageRank, betweenness, Louvain communities, and role scores are deterministic and are not computed by the LLM.
