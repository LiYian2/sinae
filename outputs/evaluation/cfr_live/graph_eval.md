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

- **Community 0: Deep Counterfactual Regret Minimization** — This community focuses on integrating deep neural networks with counterfactual regret minimization to solve imperfect-information games.
- **Community 1: Poker Agents and Imperfect Recall** — Research in this area applies regret minimization techniques to build champion-level poker agents and addresses challenges like imperfect recall in extensive-form games.
- **Community 2: Theoretical Regret Minimization Algorithms** — This community investigates theoretical improvements and algorithmic variants such as optimistic and discounted regret minimization for extensive-form games.
- **Community 3: Monte Carlo Sampling and Game Solving** — These papers explore Monte Carlo sampling methods and hardware acceleration for solving specific extensive games like heads-up limit Texas Hold'em.
- **Community 4: Incomplete Information and Search** — This community focuses on regret minimization strategies for games with incomplete information and unknown environments, often utilizing search methods.

## Analysis

- Citation-only graphs are precise but sparse when references are missing from APIs.
- Similarity-only graphs improve connectivity but can over-cluster papers by language rather than citation structure.
- Hybrid graphs are the default because they preserve citation evidence while adding enough semantic edges for stable community detection.
- PageRank, betweenness, Louvain communities, and role scores are deterministic and are not computed by the LLM.
