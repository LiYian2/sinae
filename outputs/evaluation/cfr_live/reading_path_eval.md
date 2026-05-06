# Reading Path and Report Skill Report: Counterfactual regret minimization

## Functionality

This Skill converts graph scores and community labels into a staged reading path. It generates evidence packets and asks the LLM for concise why-read explanations grounded in title, abstract, URL, stage, community, and graph scores.

## Reading Path Metrics

| Run | Stages | Unique Papers | Explanation Coverage | Role Counts |
|---|---:|---:|---:|---|
| rule_only_agent | 5 | 12 | 100.0% | {"foundation": 3, "core": 1, "development": 6, "bridge": 1, "frontier": 1} |
| llm_assisted_agent | 5 | 13 | 100.0% | {"foundation": 3, "core": 1, "development": 6, "bridge": 1, "frontier": 2} |

## Path Quality Metrics

| Run | Landmark Hit Rate | Topic Precision | Ordering Quality | Community Coverage | Stage Coverage |
|---|---:|---:|---:|---:|---:|
| rule_only_agent | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| llm_assisted_agent | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

## Network-Aware Reading Path

### Foundations
- 1. Regret Minimization in Games with Incomplete Information — This paper introduces counterfactual regret minimization (CFR), the foundational algorithm for computing Nash equilibria in extensive games with incomplete information, and demonstrates its effectiveness on large-scale poker abstractions.
- 2. Monte Carlo Sampling for Regret Minimization in Extensive Games — This paper introduces Monte Carlo Counterfactual Regret Minimization (MCCFR), a sampling-based variant of CFR that significantly reduces computational cost per iteration, enabling faster convergence in large games.
- 3. Using counterfactual regret minimization to create competitive multiplayer poker agents — This paper applies CFR to multiplayer poker, demonstrating that while theoretical guarantees are lost in non-zero-sum games, CFR-generated agents can still perform competitively in complex stochastic environments.

### Core Algorithms
- 4. Hierarchical Abstraction, Distributed Equilibrium Computation, and Post-Processing, with Application to a Champion No-Limit Texas Hold'em Agent — This paper presents a distributed version of CFR combined with hierarchical abstraction, enabling equilibrium computation of unprecedented scale for a champion No-Limit Texas Hold'em agent.

### Key Developments
- 5. Deep Counterfactual Regret Minimization — This paper introduces Deep Counterfactual Regret Minimization (Deep CFR), which replaces manual abstraction with deep neural networks to approximate CFR behavior directly in the full game.
- 6. Solving imperfect-information games via exponential counterfactual regret minimization — This paper proposes Exponential CFR (ECFR), which uses exponential weighting on instantaneous regret values to improve the convergence efficiency of standard CFR methods.
- 7. Deep (Predictive) Discounted Counterfactual Regret Minimization — This paper proposes a model-free neural CFR algorithm that integrates variance reduction and bootstrapping to simulate advanced CFR variants, achieving faster convergence in large imperfect-information games.
- 8. D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network — This paper introduces D2CFR, which utilizes a deep dueling neural network to approximate CFR, alleviating the need for manual abstraction and expert knowledge in large-scale games.
- 9. Sync Pure Counterfactual Regret Minimization in Incomplete Information Extensive Form Games — This paper combines Fictitious Play improvements with Pure CFR to create sync PCFR, demonstrating a convergence rate approximately an order of magnitude faster than the state-of-the-art CFR+.
- 10. Stochastic Regret Minimization in Extensive-Form Games — This paper develops a general framework for stochastic regret minimization in extensive-form games, providing stronger theoretical convergence guarantees and instantiating new methods beyond MCCFR.

### Bridge Papers
- 11. Regret Minimization in Non-Zero-Sum Games with Applications to Building Champion Multiplayer Computer Poker Agents — This paper bridges theory and practice by providing theoretical properties for regret minimization in non-zero-sum games, proving that CFR eliminates iteratively strictly dominated actions.

### Recent Frontier
- 12. Scale-Invariant Regret Matching and Online Learning with Optimal Convergence: Bridging Theory and Practice in Zero-Sum Games — This paper proposes IREG-PRM+, a scale-invariant variant of predictive regret matching that closes the gap between theoretical optimal convergence and practical performance in zero-sum games.
- 13. GPU-Accelerated Counterfactual Regret Minimization — This paper presents a GPU-accelerated implementation of CFR using matrix operations, achieving speedups of over 400x compared to standard implementations and scaling efficiently with game size.

## Citation-Count Baseline

This baseline ranks papers only by citation count and ignores learning stage, community coverage, and bridge/frontier roles.

1. Regret Minimization in Games with Incomplete Information (2007, OpenAlex citations: 502)
2. Deep Counterfactual Regret Minimization (2018, Semantic Scholar citations: 239)
3. Monte Carlo Sampling for Regret Minimization in Extensive Games (2009, OpenAlex citations: 191)
4. Solving Imperfect-Information Games via Discounted Regret Minimization (2018, Semantic Scholar citations: 191)
5. No-Regret Learning in Extensive-Form Games with Imperfect Recall (2012, Semantic Scholar citations: 84)
6. Solving heads-up limit Texas Hold'em (2015, OpenAlex citations: 79)
7. Double Neural Counterfactual Regret Minimization (2018, Semantic Scholar citations: 54)
8. Using counterfactual regret minimization to create competitive multiplayer poker agents (2010, OpenAlex citations: 53)
9. Hierarchical Abstraction, Distributed Equilibrium Computation, and Post-Processing, with Application to a Champion No-Limit Texas Hold'em Agent (2015, OpenAlex citations: 50)
10. Efficient Nash equilibrium approximation through Monte Carlo counterfactual regret minimization (2012, OpenAlex citations: 50)
11. Optimistic Regret Minimization for Extensive-Form Games via Dilated Distance-Generating Functions (2019, Semantic Scholar citations: 49)
12. Online Monte Carlo Counterfactual Regret Minimization for Search in Imperfect Information Games (2015, OpenAlex citations: 44)

## Analysis

- The network-aware path separates prerequisites/foundations, core methods, key developments, bridge papers, and frontier papers.
- The citation-count baseline often over-emphasizes old or broadly cited papers and does not guarantee a coherent learning order.
- Evidence-grounded why-read text is generated from structured packets, limiting LLM freedom to invent unsupported claims.
- Landmark hit rate, ordering quality, and community coverage directly evaluate whether the Agent creates a useful reading path rather than only a connected graph.
