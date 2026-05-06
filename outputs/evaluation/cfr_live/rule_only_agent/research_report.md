# ResearchTrail: Literature Reading Path Report

**Topic:** Counterfactual regret minimization
**Level:** intermediate
**Goal:** enter the field
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
- Communities: 4
- Modularity: 0.2029
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Games / Regret / Game / Minimization** — Community 0 groups papers around games, regret, game, minimization.
- **Community 1: Regret / Games / Counterfactual / Minimization** — Community 1 groups papers around regret, games, counterfactual, minimization.
- **Community 2: Regret / Games / Minimization / Convergence** — Community 2 groups papers around regret, games, minimization, convergence.
- **Community 3: Regret / Games / Information / Minimization** — Community 3 groups papers around regret, games, information, minimization.

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
**Why read:** Read this early because it is structurally central in the graph and heavily cited (502 citations), making it a foundation for later work.

### 2. Monte Carlo Sampling for Regret Minimization in Extensive Games
**Authors:** Michael Bowling, Martin Zinkevich, Kevin Waugh et al.
**Year:** 2009 | **Citations (OpenAlex):** 191
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.4143
**Abstract:** One efficient method for computing Nash equilibria in large, zero-sum extensive games is counterfactual regret minimization (CFR). In the domain of poker, CFR has proven effective, particularly when using a domain-specific augmentation involving chance outcome sampling. In this paper we introduce MCCFR, a Monte Carlo version of the algorithm capable of applying equivalent updates (in expectation) on sampled histories which has bounded overall regret with high probability. We show empirically that, although MCCFR requires more iterations, its lower cost per iteration results in overall faster convergence, particularly as the game size increases. 1
**Why read:** Read this early to establish the core vocabulary and assumptions before moving to later specialized papers.

### 3. Using counterfactual regret minimization to create competitive multiplayer poker agents
**Authors:** Nick Abou Risk, Duane Szafron
**Year:** 2010 | **Citations (OpenAlex):** 53
**URL:** http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.154.6241
**Abstract:** Games are used to evaluate and advance Multiagent and Artificial Intelligence techniques. Most of these games are deterministic with perfect information (e.g. Chess and Checkers). A deterministic game has no chance element and in a perfect information game, all information is visible to all players. However, many real-world scenarios with competing agents are stochastic (non-deterministic) with imperfect information. For two-player zero-sum perfect recall games, a recent technique called Counterfactual Regret Minimization (CFR) computes strategies that are provably convergent to an ε-Nash equilibrium. A Nash equilibrium strategy is useful in two-player games since it maximizes its utility...
**Why read:** Read this early to establish the core vocabulary and assumptions before moving to later specialized papers.

## Core Algorithms

### 4. Solving imperfect-information games via exponential counterfactual regret minimization
**Authors:** Huale Li, Xuan Wang, Shuhan Qi et al.
**Year:** 2020 | **Citations (Semantic Scholar):** 8
**URL:** https://arxiv.org/abs/2008.02679v2
**Abstract:** In general, two-agent decision-making problems can be modeled as a two-player game, and a typical solution is to find a Nash equilibrium in such game. Counterfactual regret minimization (CFR) is a well-known method to find a Nash equilibrium strategy in a two-player zero-sum game with imperfect information. The CFR method adopts a regret matching algorithm iteratively to reduce regret values progressively, enabling the average strategy to approach a Nash equilibrium. Although CFR-based methods have achieved significant success in the field of imperfect information games, there is still scope for improvement in the efficiency of convergence. To address this challenge, we propose a novel CF...
**Why read:** Read this as a core method paper because it has high graph centrality (PageRank 0.043) and anchors later developments in the path.

## Key Developments

### 5. Deep Counterfactual Regret Minimization
**Authors:** Noam Brown, Adam Lerer, Sam Gross et al.
**Year:** 2018 | **Citations (Semantic Scholar):** 239
**URL:** https://arxiv.org/abs/1811.00164v3
**Abstract:** Counterfactual Regret Minimization (CFR) is the leading framework for solving large imperfect-information games. It converges to an equilibrium by iteratively traversing the game tree. In order to deal with extremely large games, abstraction is typically applied before running CFR. The abstracted game is solved with tabular CFR, and its solution is mapped back to the full game. This process can be problematic because aspects of abstraction are often manual and domain specific, abstraction algorithms may miss important strategic nuances of the game, and there is a chicken-and-egg problem because determining a good abstraction requires knowledge of the equilibrium of the game. This paper in...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (deep counterfactual regret minimization research) with strong impact (239 citations) and bridge score 0.378.

### 6. D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network
**Authors:** Huale Li, Xuan Wang, Zengyue Guo et al.
**Year:** 2021 | **Citations:** 0
**URL:** https://arxiv.org/abs/2105.12328v2
**Abstract:** Counterfactual Regret Minimization (CFR)} is the popular method for finding approximate Nash equilibrium in two-player zero-sum games with imperfect information. CFR solves games by travsersing the full game tree iteratively, which limits its scalability in larger games. When applying CFR to solve large-scale games in previously, large-scale games are abstracted into small-scale games firstly. Secondly, CFR is used to solve the abstract game. And finally, the solution strategy is mapped back to the original large-scale game. However, this process requires considerable expert knowledge, and the accuracy of abstraction is closely related to expert knowledge. In addition, the abstraction als...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (d2cfr research) with strong impact (0 citations) and bridge score 0.480.

### 7. Deep (Predictive) Discounted Counterfactual Regret Minimization
**Authors:** Hang Xu, Kai Li, Haobo Fu et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2511.08174v1
**Abstract:** Counterfactual regret minimization (CFR) is a family of algorithms for effectively solving imperfect-information games. To enhance CFR's applicability in large games, researchers use neural networks to approximate its behavior. However, existing methods are mainly based on vanilla CFR and struggle to effectively integrate more advanced CFR variants. In this work, we propose an efficient model-free neural CFR algorithm, overcoming the limitations of existing methods in approximating advanced CFR variants. At each iteration, it collects variance-reduced sampled advantages based on a value network, fits cumulative advantages by bootstrapping, and applies discounting and clipping operations t...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (deep (predictive) discounted counterfactual regret minimization research) with strong impact (0 citations) and bridge score 0.366.

### 8. Stochastic Regret Minimization in Extensive-Form Games
**Authors:** Gabriele Farina, Christian Kroer, Tuomas Sandholm
**Year:** 2020 | **Citations (Semantic Scholar):** 32
**URL:** https://arxiv.org/abs/2002.08493v1
**Abstract:** Monte-Carlo counterfactual regret minimization (MCCFR) is the state-of-the-art algorithm for solving sequential games that are too large for full tree traversals. It works by using gradient estimates that can be computed via sampling. However, stochastic methods for sequential games have not been investigated extensively beyond MCCFR. In this paper we develop a new framework for developing stochastic regret minimization methods. This framework allows us to use any regret-minimization algorithm, coupled with any gradient estimator. The MCCFR algorithm can be analyzed as a special case of our framework, and this analysis leads to significantly-stronger theoretical on convergence, while simu...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (stochastic regret minimization in extensive-form games research) with strong impact (32 citations) and bridge score 0.316.

### 9. Sync Pure Counterfactual Regret Minimization in Incomplete Information Extensive Form Games
**Authors:** Qi Ju
**Year:** 2023 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2311.07155v1
**Abstract:** Counterfactual Regret Minimization (CFR) and its variants developed based upon Regret Matching (RM) have been considered to be the best method to solve incomplete information extensive form games. In addition to RM and CFR, Fictitious Play (FP) is another equilibrium computation algorithm in normal form games. Previous experience has shown that the convergence rate of FP is slower than RM and FP is difficult to use in extensive form games. However, recent research has made improvements in both issues. Firstly, Abernethy proposed a new FP variant sync FP, which has faster convergence rate than RM+. Secondly, Qi introduced FP into extensive form games and proposed Pure CFR (PCFR). This pape...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (sync pure counterfactual regret minimization in incomplete information extensive form games research) with strong impact (0 citations) and bridge score 0.323.

## Recent Frontier

### 10. Scale-Invariant Regret Matching and Online Learning with Optimal Convergence: Bridging Theory and Practice in Zero-Sum Games
**Authors:** Brian Hu Zhang, Ioannis Anagnostides, Tuomas Sandholm
**Year:** 2025 | **Citations (Semantic Scholar):** 2
**URL:** https://arxiv.org/abs/2510.04407v3
**Abstract:** A considerable chasm has been looming for decades between theory and practice in zero-sum game solving through first-order methods. Although a convergence rate of $T^{-1}$ has long been established, the most effective paradigm in practice is counterfactual regret minimization (CFR), which is based on regret matching and its modern variants. In particular, the state of the art across most benchmarks is predictive regret matching$^+$ (PRM$^+$). Yet, such algorithms can exhibit slower $T^{-1/2}$ convergence even in self-play. In this paper, we close the gap between theory and practice. We propose a new scale-invariant and parameter-free variant of PRM$^+$, which we call IREG-PRM$^+$. We show...
**Why read:** Read this near the end to see recent directions from 2025; its frontier score (0.565) indicates current research momentum.

### 11. Minimizing Weighted Counterfactual Regret with Optimistic Online Mirror Descent
**Authors:** Hang Xu, Kai Li, Bingyun Liu et al.
**Year:** 2024 | **Citations (Semantic Scholar):** 10
**URL:** https://arxiv.org/abs/2404.13891v2
**Abstract:** Counterfactual regret minimization (CFR) is a family of algorithms for effectively solving imperfect-information games. It decomposes the total regret into counterfactual regrets, utilizing local regret minimization algorithms, such as Regret Matching (RM) or RM+, to minimize them. Recent research establishes a connection between Online Mirror Descent (OMD) and RM+, paving the way for an optimistic variant PRM+ and its extension PCFR+. However, PCFR+ assigns uniform weights for each iteration when determining regrets, leading to substantial regrets when facing dominated actions. This work explores minimizing weighted counterfactual regret with optimistic OMD, resulting in a novel CFR vari...
**Why read:** Read this near the end to see recent directions from 2024; its frontier score (0.520) indicates current research momentum.

---

## Research Graph Statistics

- **Communities detected:** 4
- **Community sizes:** [11, 13, 14, 5]

**Top papers by PageRank:**
- Regret Minimization in Games with Incomplete Information (PR: 0.0552, 2007)
- Solving imperfect-information games via exponential counterfactual regret minimization (PR: 0.0434, 2020)
- Regret Minimization in Non-Zero-Sum Games with Applications to Building Champion Multiplayer Computer Poker Agents (PR: 0.0420, 2013)

**Top bridge papers:**
- Regret Minimization in Games with Incomplete Information (BC: 0.0964)
- Monte Carlo Sampling for Regret Minimization in Extensive Games (BC: 0.0790)
- D2CFR: Minimize Counterfactual Regret with Deep Dueling Neural Network (BC: 0.0534)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"