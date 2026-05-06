# Reading Path and Report Skill Report: Counterfactual regret minimization

## Functionality

This Skill converts graph scores and community labels into a staged reading path. It generates evidence packets and asks the LLM for concise why-read explanations grounded in title, abstract, URL, stage, community, and graph scores.

## Reading Path Metrics

| Run | Stages | Unique Papers | Explanation Coverage | Role Counts |
|---|---:|---:|---:|---|
| rule_only_agent | 4 | 11 | 100.0% | {"foundation": 3, "core": 1, "development": 5, "frontier": 2} |
| llm_assisted_agent | 4 | 11 | 100.0% | {"foundation": 3, "core": 1, "development": 5, "frontier": 2} |

## Network-Aware Reading Path

### Foundations
- 1. Regret Minimization in Games with Incomplete Information — This paper introduces counterfactual regret minimization (CFR), the foundational algorithm for computing Nash equilibria in large extensive games with incomplete information like poker.
- 2. Monte Carlo Sampling for Regret Minimization in Extensive Games — This paper introduces Monte Carlo CFR (MCCFR), a critical extension that uses sampling to handle larger game trees by reducing the cost per iteration.
- 3. Using counterfactual regret minimization to create competitive multiplayer poker agents — This paper applies CFR to multiplayer poker agents, exploring the performance of the algorithm when theoretical guarantees for Nash equilibrium are lost in non-two-player settings.

### Core Algorithms
- 4. Solving imperfect-information games via exponential counterfactual regret minimization — This paper proposes Exponential CFR (ECFR), which improves convergence efficiency by using exponential weighting to reweight instantaneous regret values.

### Key Developments
- 5. Deep Counterfactual Regret Minimization — This paper introduces Deep CFR, a major development that replaces manual abstraction with deep neural networks to approximate CFR behavior in full games.
- 6. Deep (Predictive) Discounted Counterfactual Regret Minimization — This paper presents a model-free neural CFR algorithm that integrates variance reduction and bootstrapping to approximate advanced CFR variants more effectively.
- 7. D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network — This paper proposes D2CFR, which utilizes deep dueling neural networks to approximate Nash equilibria without the need for manual game abstraction.
- 8. Equivalence Analysis between Counterfactual Regret Minimization and Online Mirror Descent — This paper establishes a theoretical equivalence between CFR and Online Mirror Descent (OMD), providing a mathematical foundation for understanding CFR variants.
- 9. Stochastic Regret Minimization in Extensive-Form Games — This paper develops a general framework for stochastic regret minimization in extensive-form games, analyzing MCCFR as a special case and yielding stronger theoretical convergence results.

### Recent Frontier
- 10. Scale-Invariant Regret Matching and Online Learning with Optimal Convergence: Bridging Theory and Practice in Zero-Sum Games — This paper proposes IREG-PRM+, a scale-invariant variant of predictive regret matching that achieves optimal convergence guarantees while maintaining practical performance.
- 11. Minimizing Weighted Counterfactual Regret with Optimistic Online Mirror Descent — This paper introduces PDCFR+, a novel CFR variant that integrates optimistic online mirror descent with weighted counterfactual regret to mitigate the effects of dominated actions.

## Citation-Count Baseline

This baseline ranks papers only by citation count and ignores learning stage, community coverage, and bridge/frontier roles.

1. Regret Minimization in Games with Incomplete Information (2007, OpenAlex citations: 502)
2. Deep Counterfactual Regret Minimization (2018, Semantic Scholar citations: 239)
3. Solving Imperfect-Information Games via Discounted Regret Minimization (2018, Semantic Scholar citations: 191)
4. Monte Carlo Sampling for Regret Minimization in Extensive Games (2009, OpenAlex citations: 191)
5. Solving Large Imperfect Information Games Using CFR+ (2014, Semantic Scholar citations: 161)
6. No-Regret Learning in Extensive-Form Games with Imperfect Recall (2012, Semantic Scholar citations: 84)
7. Solving heads-up limit Texas Hold'em (2015, OpenAlex citations: 79)
8. Double Neural Counterfactual Regret Minimization (2018, Semantic Scholar citations: 54)
9. Using counterfactual regret minimization to create competitive multiplayer poker agents (2010, OpenAlex citations: 53)
10. Hierarchical Abstraction, Distributed Equilibrium Computation, and Post-Processing, with Application to a Champion No-Limit Texas Hold'em Agent (2015, OpenAlex citations: 50)
11. Efficient Nash equilibrium approximation through Monte Carlo counterfactual regret minimization (2012, OpenAlex citations: 50)
12. Optimistic Regret Minimization for Extensive-Form Games via Dilated Distance-Generating Functions (2019, Semantic Scholar citations: 49)

## Analysis

- The network-aware path separates prerequisites/foundations, core methods, key developments, bridge papers, and frontier papers.
- The citation-count baseline often over-emphasizes old or broadly cited papers and does not guarantee a coherent learning order.
- Evidence-grounded why-read text is generated from structured packets, limiting LLM freedom to invent unsupported claims.
