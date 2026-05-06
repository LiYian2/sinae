# ResearchTrail: Literature Reading Path Report

**Topic:** Counterfactual regret minimization
**Level:** intermediate
**Goal:** Understand Counterfactual regret minimization
**Preferred Length:** 10 papers

---

## Corpus Summary

- Papers: 46
- Abstract coverage: 100.0%
- Citation/reference coverage: 69.6%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2007-2025
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 46
- Edges: 441
- Citation edges: 14
- Similarity edges: 436
- Communities: 5
- Modularity: 0.2079
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Deep Counterfactual Regret Minimization** — This community focuses on integrating deep neural networks with counterfactual regret minimization to solve imperfect-information games.
- **Community 1: Poker Agents and Imperfect Recall** — Research in this area applies regret minimization techniques to build champion-level poker agents and addresses challenges like imperfect recall in extensive-form games.
- **Community 2: Theoretical Regret Minimization Algorithms** — This community investigates theoretical improvements and algorithmic variants such as optimistic and discounted regret minimization for extensive-form games.
- **Community 3: Monte Carlo Sampling and Game Solving** — These papers explore Monte Carlo sampling methods and hardware acceleration for solving specific extensive games like heads-up limit Texas Hold'em.
- **Community 4: Incomplete Information and Search** — This community focuses on regret minimization strategies for games with incomplete information and unknown environments, often utilizing search methods.

## Reading Path Metrics

- Stages: 4
- Unique papers: 11
- Explanation coverage: 100.0%

## Foundations

### 1. Regret Minimization in Games with Incomplete Information
**Authors:** Michael Bowling, Michael Johanson, Martin Zinkevich et al.
**Year:** 2007 | **Citations (OpenAlex):** 502
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.160.8576
**Abstract:** Extensive games are a powerful model of multiagent decision-making scenarios with incomplete information. Finding a Nash equilibrium for very large instances of these games has received a great deal of recent attention. In this paper, we describe a new technique for solving large games based on regret minimization. In particular, we introduce the notion of counterfactual regret, which exploits the degree of incomplete information in an extensive game. We show how minimizing counterfactual regret minimizes overall regret, and therefore in self-play can be used to compute a Nash equilibrium. We demonstrate this technique in the domain of poker, showing we can solve abstractions of limit Tex...
**Why read:** This paper introduces counterfactual regret minimization (CFR), the foundational algorithm for computing Nash equilibria in large extensive games with incomplete information like poker.

### 2. Monte Carlo Sampling for Regret Minimization in Extensive Games
**Authors:** Michael Bowling, Martin Zinkevich, Kevin Waugh et al.
**Year:** 2009 | **Citations (OpenAlex):** 191
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.4143
**Abstract:** One efficient method for computing Nash equilibria in large, zero-sum extensive games is counterfactual regret minimization (CFR). In the domain of poker, CFR has proven effective, particularly when using a domain-specific augmentation involving chance outcome sampling. In this paper we introduce MCCFR, a Monte Carlo version of the algorithm capable of applying equivalent updates (in expectation) on sampled histories which has bounded overall regret with high probability. We show empirically that, although MCCFR requires more iterations, its lower cost per iteration results in overall faster convergence, particularly as the game size increases. 1
**Why read:** This paper introduces Monte Carlo CFR (MCCFR), a critical extension that uses sampling to handle larger game trees by reducing the cost per iteration.

### 3. Using counterfactual regret minimization to create competitive multiplayer poker agents
**Authors:** Nick Abou Risk, Duane Szafron
**Year:** 2010 | **Citations (OpenAlex):** 53
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.6241
**Abstract:** Games are used to evaluate and advance Multiagent and Artificial Intelligence techniques. Most of these games are deterministic with perfect information (e.g. Chess and Checkers). A deterministic game has no chance element and in a perfect information game, all information is visible to all players. However, many real-world scenarios with competing agents are stochastic (non-deterministic) with imperfect information. For two-player zero-sum perfect recall games, a recent technique called Counterfactual Regret Minimization (CFR) computes strategies that are provably convergent to an ε-Nash equilibrium. A Nash equilibrium strategy is useful in two-player games since it maximizes its utility...
**Why read:** This paper applies CFR to multiplayer poker agents, exploring the performance of the algorithm when theoretical guarantees for Nash equilibrium are lost in non-two-player settings.

## Core Algorithms

### 4. Solving imperfect-information games via exponential counterfactual regret minimization
**Authors:** Huale Li, Xuan Wang, Shuhan Qi et al.
**Year:** 2020 | **Citations (Semantic Scholar):** 8
**URL:** https://arxiv.org/abs/2008.02679v2
**Abstract:** In general, two-agent decision-making problems can be modeled as a two-player game, and a typical solution is to find a Nash equilibrium in such game. Counterfactual regret minimization (CFR) is a well-known method to find a Nash equilibrium strategy in a two-player zero-sum game with imperfect information. The CFR method adopts a regret matching algorithm iteratively to reduce regret values progressively, enabling the average strategy to approach a Nash equilibrium. Although CFR-based methods have achieved significant success in the field of imperfect information games, there is still scope for improvement in the efficiency of convergence. To address this challenge, we propose a novel CF...
**Why read:** This paper proposes Exponential CFR (ECFR), which improves convergence efficiency by using exponential weighting to reweight instantaneous regret values.

## Key Developments

### 5. Deep Counterfactual Regret Minimization
**Authors:** Noam Brown, Adam Lerer, Sam Gross et al.
**Year:** 2018 | **Citations (Semantic Scholar):** 239
**URL:** https://arxiv.org/abs/1811.00164v3
**Abstract:** Counterfactual Regret Minimization (CFR) is the leading framework for solving large imperfect-information games. It converges to an equilibrium by iteratively traversing the game tree. In order to deal with extremely large games, abstraction is typically applied before running CFR. The abstracted game is solved with tabular CFR, and its solution is mapped back to the full game. This process can be problematic because aspects of abstraction are often manual and domain specific, abstraction algorithms may miss important strategic nuances of the game, and there is a chicken-and-egg problem because determining a good abstraction requires knowledge of the equilibrium of the game. This paper in...
**Why read:** This paper introduces Deep CFR, a major development that replaces manual abstraction with deep neural networks to approximate CFR behavior in full games.

### 6. Deep (Predictive) Discounted Counterfactual Regret Minimization
**Authors:** Hang Xu, Kai Li, Haobo Fu et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2511.08174v1
**Abstract:** Counterfactual regret minimization (CFR) is a family of algorithms for effectively solving imperfect-information games. To enhance CFR's applicability in large games, researchers use neural networks to approximate its behavior. However, existing methods are mainly based on vanilla CFR and struggle to effectively integrate more advanced CFR variants. In this work, we propose an efficient model-free neural CFR algorithm, overcoming the limitations of existing methods in approximating advanced CFR variants. At each iteration, it collects variance-reduced sampled advantages based on a value network, fits cumulative advantages by bootstrapping, and applies discounting and clipping operations t...
**Why read:** This paper presents a model-free neural CFR algorithm that integrates variance reduction and bootstrapping to approximate advanced CFR variants more effectively.

### 7. D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network
**Authors:** Huale Li, Xuan Wang, Zengyue Guo et al.
**Year:** 2021 | **Citations:** 0
**URL:** https://arxiv.org/abs/2105.12328v2
**Abstract:** Counterfactual Regret Minimization (CFR)} is the popular method for finding approximate Nash equilibrium in two-player zero-sum games with imperfect information. CFR solves games by travsersing the full game tree iteratively, which limits its scalability in larger games. When applying CFR to solve large-scale games in previously, large-scale games are abstracted into small-scale games firstly. Secondly, CFR is used to solve the abstract game. And finally, the solution strategy is mapped back to the original large-scale game. However, this process requires considerable expert knowledge, and the accuracy of abstraction is closely related to expert knowledge. In addition, the abstraction als...
**Why read:** This paper proposes D2CFR, which utilizes deep dueling neural networks to approximate Nash equilibria without the need for manual game abstraction.

### 8. Equivalence Analysis between Counterfactual Regret Minimization and Online Mirror Descent
**Authors:** Weiming Liu, Huacong Jiang, Bin Li et al.
**Year:** 2021 | **Citations (Semantic Scholar):** 13
**URL:** https://arxiv.org/abs/2110.04961v2
**Abstract:** Follow-the-Regularized-Lead (FTRL) and Online Mirror Descent (OMD) are regret minimization algorithms for Online Convex Optimization (OCO), they are mathematically elegant but less practical in solving Extensive-Form Games (EFGs). Counterfactual Regret Minimization (CFR) is a technique for approximating Nash equilibria in EFGs. CFR and its variants have a fast convergence rate in practice, but their theoretical results are not satisfactory. In recent years, researchers have been trying to link CFRs with OCO algorithms, which may provide new theoretical results and inspire new algorithms. However, existing analysis is restricted to local decision points. In this paper, we show that CFRs wi...
**Why read:** This paper establishes a theoretical equivalence between CFR and Online Mirror Descent (OMD), providing a mathematical foundation for understanding CFR variants.

### 9. Stochastic Regret Minimization in Extensive-Form Games
**Authors:** Gabriele Farina, Christian Kroer, Tuomas Sandholm
**Year:** 2020 | **Citations (Semantic Scholar):** 32
**URL:** https://arxiv.org/abs/2002.08493v1
**Abstract:** Monte-Carlo counterfactual regret minimization (MCCFR) is the state-of-the-art algorithm for solving sequential games that are too large for full tree traversals. It works by using gradient estimates that can be computed via sampling. However, stochastic methods for sequential games have not been investigated extensively beyond MCCFR. In this paper we develop a new framework for developing stochastic regret minimization methods. This framework allows us to use any regret-minimization algorithm, coupled with any gradient estimator. The MCCFR algorithm can be analyzed as a special case of our framework, and this analysis leads to significantly-stronger theoretical on convergence, while simu...
**Why read:** This paper develops a general framework for stochastic regret minimization in extensive-form games, analyzing MCCFR as a special case and yielding stronger theoretical convergence results.

## Recent Frontier

### 10. Scale-Invariant Regret Matching and Online Learning with Optimal Convergence: Bridging Theory and Practice in Zero-Sum Games
**Authors:** Brian Hu Zhang, Ioannis Anagnostides, Tuomas Sandholm
**Year:** 2025 | **Citations (Semantic Scholar):** 2
**URL:** https://arxiv.org/abs/2510.04407v3
**Abstract:** A considerable chasm has been looming for decades between theory and practice in zero-sum game solving through first-order methods. Although a convergence rate of $T^{-1}$ has long been established, the most effective paradigm in practice is counterfactual regret minimization (CFR), which is based on regret matching and its modern variants. In particular, the state of the art across most benchmarks is predictive regret matching$^+$ (PRM$^+$). Yet, such algorithms can exhibit slower $T^{-1/2}$ convergence even in self-play. In this paper, we close the gap between theory and practice. We propose a new scale-invariant and parameter-free variant of PRM$^+$, which we call IREG-PRM$^+$. We show...
**Why read:** This paper proposes IREG-PRM+, a scale-invariant variant of predictive regret matching that achieves optimal convergence guarantees while maintaining practical performance.

### 11. Minimizing Weighted Counterfactual Regret with Optimistic Online Mirror Descent
**Authors:** Hang Xu, Kai Li, Bingyun Liu et al.
**Year:** 2024 | **Citations (Semantic Scholar):** 10
**URL:** https://arxiv.org/abs/2404.13891v2
**Abstract:** Counterfactual regret minimization (CFR) is a family of algorithms for effectively solving imperfect-information games. It decomposes the total regret into counterfactual regrets, utilizing local regret minimization algorithms, such as Regret Matching (RM) or RM+, to minimize them. Recent research establishes a connection between Online Mirror Descent (OMD) and RM+, paving the way for an optimistic variant PRM+ and its extension PCFR+. However, PCFR+ assigns uniform weights for each iteration when determining regrets, leading to substantial regrets when facing dominated actions. This work explores minimizing weighted counterfactual regret with optimistic OMD, resulting in a novel CFR vari...
**Why read:** This paper introduces PDCFR+, a novel CFR variant that integrates optimistic online mirror descent with weighted counterfactual regret to mitigate the effects of dominated actions.

---

## Research Graph Statistics

- **Communities detected:** 5
- **Community sizes:** [12, 12, 14, 3, 5]

**Top papers by PageRank:**
- Regret Minimization in Games with Incomplete Information (PR: 0.0509, 2007)
- Solving imperfect-information games via exponential counterfactual regret minimization (PR: 0.0415, 2020)
- Regret Minimization in Non-Zero-Sum Games with Applications to Building Champion Multiplayer Computer Poker Agents (PR: 0.0403, 2013)

**Top bridge papers:**
- Regret Minimization in Games with Incomplete Information (BC: 0.0980)
- Monte Carlo Sampling for Regret Minimization in Extensive Games (BC: 0.0606)
- D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network (BC: 0.0465)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"