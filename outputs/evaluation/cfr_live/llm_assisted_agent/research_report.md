# ResearchTrail: Literature Reading Path Report

**Topic:** Counterfactual regret minimization
**Level:** intermediate
**Goal:** Understand Counterfactual regret minimization
**Preferred Length:** 10 papers

---

## Corpus Summary

- Papers: 43
- Abstract coverage: 100.0%
- Citation/reference coverage: 69.8%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2007-2025
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 43
- Edges: 394
- Citation edges: 14
- Similarity edges: 390
- Communities: 5
- Modularity: 0.1941
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Imperfect Recall and Abstraction in Games** — This community focuses on regret minimization algorithms in extensive-form games, specifically addressing challenges like imperfect recall, bounded memory, and the construction of abstractions.
- **Community 1: Deep Counterfactual Regret Minimization** — Research in this area applies deep learning and function approximation techniques to counterfactual regret minimization for solving games.
- **Community 2: Optimistic Regret Minimization and Convergence** — This community investigates theoretical improvements to regret minimization algorithms, focusing on optimistic methods, convergence rates, and techniques like mirror descent.
- **Community 3: Sampling and Accelerated Regret Minimization** — This community develops methods to accelerate counterfactual regret minimization through Monte Carlo sampling, GPU acceleration, and neural network integration.
- **Community 4: Regret Minimization for Incomplete Information and Search** — This community explores regret minimization strategies for games with incomplete information, emphasizing search algorithms, information gain, and efficient Nash equilibrium approximation.

## Reading Path Metrics

- Stages: 5
- Unique papers: 13
- Explanation coverage: 100.0%

## Foundations

### 1. Regret Minimization in Games with Incomplete Information
**Authors:** Michael Bowling, Michael Johanson, Martin Zinkevich et al.
**Year:** 2007 | **Citations (OpenAlex):** 502
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.160.8576
**Abstract:** Extensive games are a powerful model of multiagent decision-making scenarios with incomplete information. Finding a Nash equilibrium for very large instances of these games has received a great deal of recent attention. In this paper, we describe a new technique for solving large games based on regret minimization. In particular, we introduce the notion of counterfactual regret, which exploits the degree of incomplete information in an extensive game. We show how minimizing counterfactual regret minimizes overall regret, and therefore in self-play can be used to compute a Nash equilibrium. We demonstrate this technique in the domain of poker, showing we can solve abstractions of limit Tex...
**Why read:** This paper introduces counterfactual regret minimization (CFR), the foundational algorithm for computing Nash equilibria in extensive games with incomplete information, and demonstrates its effectiveness on large-scale poker abstractions.

### 2. Monte Carlo Sampling for Regret Minimization in Extensive Games
**Authors:** Michael Bowling, Martin Zinkevich, Kevin Waugh et al.
**Year:** 2009 | **Citations (OpenAlex):** 191
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.4143
**Abstract:** One efficient method for computing Nash equilibria in large, zero-sum extensive games is counterfactual regret minimization (CFR). In the domain of poker, CFR has proven effective, particularly when using a domain-specific augmentation involving chance outcome sampling. In this paper we introduce MCCFR, a Monte Carlo version of the algorithm capable of applying equivalent updates (in expectation) on sampled histories which has bounded overall regret with high probability. We show empirically that, although MCCFR requires more iterations, its lower cost per iteration results in overall faster convergence, particularly as the game size increases. 1
**Why read:** This paper introduces Monte Carlo Counterfactual Regret Minimization (MCCFR), a sampling-based variant of CFR that significantly reduces computational cost per iteration, enabling faster convergence in large games.

### 3. Using counterfactual regret minimization to create competitive multiplayer poker agents
**Authors:** Nick Abou Risk, Duane Szafron
**Year:** 2010 | **Citations (OpenAlex):** 53
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.6241
**Abstract:** Games are used to evaluate and advance Multiagent and Artificial Intelligence techniques. Most of these games are deterministic with perfect information (e.g. Chess and Checkers). A deterministic game has no chance element and in a perfect information game, all information is visible to all players. However, many real-world scenarios with competing agents are stochastic (non-deterministic) with imperfect information. For two-player zero-sum perfect recall games, a recent technique called Counterfactual Regret Minimization (CFR) computes strategies that are provably convergent to an ε-Nash equilibrium. A Nash equilibrium strategy is useful in two-player games since it maximizes its utility...
**Why read:** This paper applies CFR to multiplayer poker, demonstrating that while theoretical guarantees are lost in non-zero-sum games, CFR-generated agents can still perform competitively in complex stochastic environments.

## Core Algorithms

### 4. Hierarchical Abstraction, Distributed Equilibrium Computation, and Post-Processing, with Application to a Champion No-Limit Texas Hold'em Agent
**Authors:** Noam Brown, Sam Ganzfried, Tüomas Sandholm
**Year:** 2015 | **Citations (OpenAlex):** 50
**URL:** http://www.aamas2015.com/en/AAMAS_2015_USB/aamas/p7.pdf
**Abstract:** The leading approach for solving large imperfect-information games is automated abstraction followed by running an equilibrium-finding algorithm. We introduce a distributed version of the most commonly used equilibrium-finding algorithm, counterfactual regret minimization (CFR), which enables CFR to scale to dramatically larger abstractions and numbers of cores. The new algorithm begets constraints on the abstraction so as to make the pieces running on different computers disjoint. We introduce an algorithm for generating such abstractions while capitalizing on state-of-the-art abstraction ideas such as imperfect recall and earth-mover's distance. Our techniques enabled an equilibrium com...
**Why read:** This paper presents a distributed version of CFR combined with hierarchical abstraction, enabling equilibrium computation of unprecedented scale for a champion No-Limit Texas Hold'em agent.

## Key Developments

### 5. Deep Counterfactual Regret Minimization
**Authors:** Noam Brown, Adam Lerer, Sam Gross et al.
**Year:** 2018 | **Citations (Semantic Scholar):** 239
**URL:** https://arxiv.org/abs/1811.00164v3
**Abstract:** Counterfactual Regret Minimization (CFR) is the leading framework for solving large imperfect-information games. It converges to an equilibrium by iteratively traversing the game tree. In order to deal with extremely large games, abstraction is typically applied before running CFR. The abstracted game is solved with tabular CFR, and its solution is mapped back to the full game. This process can be problematic because aspects of abstraction are often manual and domain specific, abstraction algorithms may miss important strategic nuances of the game, and there is a chicken-and-egg problem because determining a good abstraction requires knowledge of the equilibrium of the game. This paper in...
**Why read:** This paper introduces Deep Counterfactual Regret Minimization (Deep CFR), which replaces manual abstraction with deep neural networks to approximate CFR behavior directly in the full game.

### 6. Solving imperfect-information games via exponential counterfactual regret minimization
**Authors:** Huale Li, Xuan Wang, Shuhan Qi et al.
**Year:** 2020 | **Citations (Semantic Scholar):** 8
**URL:** https://arxiv.org/abs/2008.02679v2
**Abstract:** In general, two-agent decision-making problems can be modeled as a two-player game, and a typical solution is to find a Nash equilibrium in such game. Counterfactual regret minimization (CFR) is a well-known method to find a Nash equilibrium strategy in a two-player zero-sum game with imperfect information. The CFR method adopts a regret matching algorithm iteratively to reduce regret values progressively, enabling the average strategy to approach a Nash equilibrium. Although CFR-based methods have achieved significant success in the field of imperfect information games, there is still scope for improvement in the efficiency of convergence. To address this challenge, we propose a novel CF...
**Why read:** This paper proposes Exponential CFR (ECFR), which uses exponential weighting on instantaneous regret values to improve the convergence efficiency of standard CFR methods.

### 7. Deep (Predictive) Discounted Counterfactual Regret Minimization
**Authors:** Hang Xu, Kai Li, Haobo Fu et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2511.08174v1
**Abstract:** Counterfactual regret minimization (CFR) is a family of algorithms for effectively solving imperfect-information games. To enhance CFR's applicability in large games, researchers use neural networks to approximate its behavior. However, existing methods are mainly based on vanilla CFR and struggle to effectively integrate more advanced CFR variants. In this work, we propose an efficient model-free neural CFR algorithm, overcoming the limitations of existing methods in approximating advanced CFR variants. At each iteration, it collects variance-reduced sampled advantages based on a value network, fits cumulative advantages by bootstrapping, and applies discounting and clipping operations t...
**Why read:** This paper proposes a model-free neural CFR algorithm that integrates variance reduction and bootstrapping to simulate advanced CFR variants, achieving faster convergence in large imperfect-information games.

### 8. D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network
**Authors:** Huale Li, Xuan Wang, Zengyue Guo et al.
**Year:** 2021 | **Citations:** 0
**URL:** https://arxiv.org/abs/2105.12328v2
**Abstract:** Counterfactual Regret Minimization (CFR)} is the popular method for finding approximate Nash equilibrium in two-player zero-sum games with imperfect information. CFR solves games by travsersing the full game tree iteratively, which limits its scalability in larger games. When applying CFR to solve large-scale games in previously, large-scale games are abstracted into small-scale games firstly. Secondly, CFR is used to solve the abstract game. And finally, the solution strategy is mapped back to the original large-scale game. However, this process requires considerable expert knowledge, and the accuracy of abstraction is closely related to expert knowledge. In addition, the abstraction als...
**Why read:** This paper introduces D2CFR, which utilizes a deep dueling neural network to approximate CFR, alleviating the need for manual abstraction and expert knowledge in large-scale games.

### 9. Sync Pure Counterfactual Regret Minimization in Incomplete Information Extensive Form Games
**Authors:** Qi Ju
**Year:** 2023 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2311.07155v1
**Abstract:** Counterfactual Regret Minimization (CFR) and its variants developed based upon Regret Matching (RM) have been considered to be the best method to solve incomplete information extensive form games. In addition to RM and CFR, Fictitious Play (FP) is another equilibrium computation algorithm in normal form games. Previous experience has shown that the convergence rate of FP is slower than RM and FP is difficult to use in extensive form games. However, recent research has made improvements in both issues. Firstly, Abernethy proposed a new FP variant sync FP, which has faster convergence rate than RM+. Secondly, Qi introduced FP into extensive form games and proposed Pure CFR (PCFR). This pape...
**Why read:** This paper combines Fictitious Play improvements with Pure CFR to create sync PCFR, demonstrating a convergence rate approximately an order of magnitude faster than the state-of-the-art CFR+.

### 10. Stochastic Regret Minimization in Extensive-Form Games
**Authors:** Gabriele Farina, Christian Kroer, Tuomas Sandholm
**Year:** 2020 | **Citations (Semantic Scholar):** 32
**URL:** https://arxiv.org/abs/2002.08493v1
**Abstract:** Monte-Carlo counterfactual regret minimization (MCCFR) is the state-of-the-art algorithm for solving sequential games that are too large for full tree traversals. It works by using gradient estimates that can be computed via sampling. However, stochastic methods for sequential games have not been investigated extensively beyond MCCFR. In this paper we develop a new framework for developing stochastic regret minimization methods. This framework allows us to use any regret-minimization algorithm, coupled with any gradient estimator. The MCCFR algorithm can be analyzed as a special case of our framework, and this analysis leads to significantly-stronger theoretical on convergence, while simu...
**Why read:** This paper develops a general framework for stochastic regret minimization in extensive-form games, providing stronger theoretical convergence guarantees and instantiating new methods beyond MCCFR.

## Bridge Papers

### 11. Regret Minimization in Non-Zero-Sum Games with Applications to Building Champion Multiplayer Computer Poker Agents
**Authors:** Richard Gibson
**Year:** 2013 | **Citations (Semantic Scholar):** 15
**URL:** https://arxiv.org/abs/1305.0034v1
**Abstract:** In two-player zero-sum games, if both players minimize their average external regret, then the average of the strategy profiles converges to a Nash equilibrium. For n-player general-sum games, however, theoretical guarantees for regret minimization are less understood. Nonetheless, Counterfactual Regret Minimization (CFR), a popular regret minimization algorithm for extensive-form games, has generated winning three-player Texas Hold'em agents in the Annual Computer Poker Competition (ACPC). In this paper, we provide the first set of theoretical properties for regret minimization algorithms in non-zero-sum games by proving that solutions eliminate iterative strict domination. We formally d...
**Why read:** This paper bridges theory and practice by providing theoretical properties for regret minimization in non-zero-sum games, proving that CFR eliminates iteratively strictly dominated actions.

## Recent Frontier

### 12. Scale-Invariant Regret Matching and Online Learning with Optimal Convergence: Bridging Theory and Practice in Zero-Sum Games
**Authors:** Brian Hu Zhang, Ioannis Anagnostides, Tuomas Sandholm
**Year:** 2025 | **Citations (Semantic Scholar):** 2
**URL:** https://arxiv.org/abs/2510.04407v3
**Abstract:** A considerable chasm has been looming for decades between theory and practice in zero-sum game solving through first-order methods. Although a convergence rate of $T^{-1}$ has long been established, the most effective paradigm in practice is counterfactual regret minimization (CFR), which is based on regret matching and its modern variants. In particular, the state of the art across most benchmarks is predictive regret matching$^+$ (PRM$^+$). Yet, such algorithms can exhibit slower $T^{-1/2}$ convergence even in self-play. In this paper, we close the gap between theory and practice. We propose a new scale-invariant and parameter-free variant of PRM$^+$, which we call IREG-PRM$^+$. We show...
**Why read:** This paper proposes IREG-PRM+, a scale-invariant variant of predictive regret matching that closes the gap between theoretical optimal convergence and practical performance in zero-sum games.

### 13. GPU-Accelerated Counterfactual Regret Minimization
**Authors:** Juho Kim
**Year:** 2024 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2408.14778v5
**Abstract:** Counterfactual regret minimization is a family of algorithms of no-regret learning dynamics capable of solving large-scale imperfect information games. We propose implementing this algorithm as a series of dense and sparse matrix and vector operations, thereby making it highly parallelizable for a graphical processing unit, at a cost of higher memory usage. Our experiments show that our implementation performs up to about 401.2 times faster than OpenSpiel's Python implementation and, on an expanded set of games, up to about 203.6 times faster than OpenSpiel's C++ implementation and the speedup becomes more pronounced as the size of the game being solved grows.
**Why read:** This paper presents a GPU-accelerated implementation of CFR using matrix operations, achieving speedups of over 400x compared to standard implementations and scaling efficiently with game size.

---

## Research Graph Statistics

- **Communities detected:** 5
- **Community sizes:** [11, 13, 9, 5, 5]

**Top papers by PageRank:**
- Regret Minimization in Games with Incomplete Information (PR: 0.1444, 2007)
- Monte Carlo Sampling for Regret Minimization in Extensive Games (PR: 0.0514, 2009)
- Hierarchical Abstraction, Distributed Equilibrium Computation, and Post-Processing, with Application to a Champion No-Limit Texas Hold'em Agent (PR: 0.0248, 2015)

**Top bridge papers:**
- Regret Minimization in Games with Incomplete Information (BC: 0.1452)
- Regret Minimization in Non-Zero-Sum Games with Applications to Building Champion Multiplayer Computer Poker Agents (BC: 0.1161)
- Efficient Nash equilibrium approximation through Monte Carlo counterfactual regret minimization (BC: 0.0859)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"