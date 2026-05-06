# ResearchTrail: Literature Reading Path Report

**Topic:** Multi-Agent Reinforcement Learning
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 26
- Abstract coverage: 100.0%
- Citation/reference coverage: 76.9%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2017-2026
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 26
- Edges: 142
- Citation edges: 10
- Similarity edges: 140
- Communities: 4
- Modularity: 0.2799
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Cooperative and Competitive Multi-Agent Reinforcement Learning** — This community investigates reinforcement learning algorithms like PPO and Actor-Critic applied to cooperative, competitive, and mixed environments such as StarCraft, addressing challenges in privacy, interference control, and multi-stage tasks.
- **Community 1: Value Decomposition Networks in Cooperative MARL** — Research in this area focuses on Value-Decomposition Networks (VDN) and their extensions, such as distributed VDN and PPS-QMIX, to solve cooperative multi-agent reinforcement learning problems by factorizing team rewards.
- **Community 2: QMIX and Monotonic Value Factorization** — This community centers on the QMIX algorithm and its variants, such as Weighted QMIX, which utilize monotonic value function factorization to enable centralised training and decentralised execution in deep multi-agent reinforcement learning.
- **Community 3: Counterfactual and Independent Policy Gradients** — This community explores policy gradient methods for multi-agent systems, specifically comparing counterfactual multi-agent policy gradients (COMA) with independent learning approaches like IPPO within the StarCraft Multi-Agent Challenge.

## Reading Path Metrics

- Stages: 4
- Unique papers: 12
- Explanation coverage: 100.0%

## Foundations

### 1. Counterfactual Multi-Agent Policy Gradients
**Authors:** Jakob Foerster, Gregory Farquhar, Triantafyllos Afouras et al.
**Year:** 2018 | **Citations (OpenAlex):** 1610
**URL:** https://doi.org/10.1609/aaai.v32i1.11794
**Abstract:** Many real-world problems, such as network packet routing and the coordination of autonomous vehicles, are naturally modelled as cooperative multi-agent systems. There is a great need for new reinforcement learning methods that can efficiently learn decentralised policies for such systems. To this end, we propose a new multi-agent actor-critic method called counterfactual multi-agent (COMA) policy gradients. COMA uses a centralised critic to estimate the Q-function and decentralised actors to optimise the agents' policies. In addition, to address the challenges of multi-agent credit assignment, it uses a counterfactual baseline that marginalises out a single agent's action, while keeping t...
**Why read:** Read this early because it is structurally central in the graph and heavily cited (1610 citations), making it a foundation for later work.

### 2. Value-Decomposition Networks For Cooperative Multi-Agent Learning Based On Team Reward
**Authors:** Peter Sunehag, Guy Lever, Audrūnas Gruslys et al.
**Year:** 2018 | **Citations (OpenAlex):** 512
**URL:** https://doi.org/10.65109/jsrc7365
**Abstract:** We study the problem of cooperative multi-agent reinforcement learning with a single joint reward signal. This class of learning problems is difficult because of the often large combined action and observation spaces. In the fully centralized and decentralized approaches, we find the problem of spurious rewards and a phenomenon we call the "lazy agent'' problem, which arises due to partial observability. We address these problems by training individual agents with a novel value-decomposition network architecture, which learns to decompose the team value function into agent-wise value functions.
**Why read:** Read this early because it is structurally central in the graph and heavily cited (512 citations), making it a foundation for later work.

### 3. Value-Decomposition Networks For Cooperative Multi-Agent Learning
**Authors:** Peter Sunehag, Guy Lever, Audrunas Gruslys et al.
**Year:** 2017 | **Citations (Semantic Scholar):** 1282
**URL:** https://arxiv.org/abs/1706.05296v1
**Abstract:** We study the problem of cooperative multi-agent reinforcement learning with a single joint reward signal. This class of learning problems is difficult because of the often large combined action and observation spaces. In the fully centralized and decentralized approaches, we find the problem of spurious rewards and a phenomenon we call the "lazy agent" problem, which arises due to partial observability. We address these problems by training individual agents with a novel value decomposition network architecture, which learns to decompose the team value function into agent-wise value functions. We perform an experimental evaluation across a range of partially-observable multi-agent domains...
**Why read:** Read this early to establish the core vocabulary and assumptions before moving to later specialized papers.

## Core Algorithms

### 4. The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games
**Authors:** Chao Yu, Akash Velu, Eugene Vinitsky et al.
**Year:** 2021 | **Citations (OpenAlex):** 591
**URL:** http://arxiv.org/abs/2103.01955
**Abstract:** Proximal Policy Optimization (PPO) is a ubiquitous on-policy reinforcement learning algorithm but is significantly less utilized than off-policy learning algorithms in multi-agent settings. This is often due to the belief that PPO is significantly less sample efficient than off-policy methods in multi-agent systems. In this work, we carefully study the performance of PPO in cooperative multi-agent settings. We show that PPO-based multi-agent algorithms achieve surprisingly strong performance in four popular multi-agent testbeds: the particle-world environments, the StarCraft multi-agent challenge, Google Research Football, and the Hanabi challenge, with minimal hyperparameter tuning and w...
**Why read:** Read this as a core method paper because it has high graph centrality (PageRank 0.058) and anchors later developments in the path.

## Key Developments

### 5. Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning
**Authors:** Tabish Rashid, Mikayel Samvelyan, Christian Schröder de Witt et al.
**Year:** 2020 | **Citations (OpenAlex):** 429
**URL:** http://arxiv.org/abs/2003.08839
**Abstract:** In many real-world settings, a team of agents must coordinate its behaviour while acting in a decentralised fashion. At the same time, it is often possible to train the agents in a centralised fashion where global state information is available and communication constraints are lifted. Learning joint action-values conditioned on extra state information is an attractive way to exploit centralised learning, but the best strategy for then extracting decentralised policies is unclear. Our solution is QMIX, a novel value-based method that can train decentralised policies in a centralised end-to-end fashion. QMIX employs a mixing network that estimates joint action-values as a monotonic combina...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (monotonic value function factorisation for deep multi-agent reinforcement learning research) with strong impact (429 citations) and bridge score 0.667.

### 6. Weighted QMIX: Expanding Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning
**Authors:** Tabish Rashid, Gregory Farquhar, Bei Peng et al.
**Year:** 2020 | **Citations (Semantic Scholar):** 474
**URL:** https://arxiv.org/abs/2006.10800v2
**Abstract:** QMIX is a popular $Q$-learning algorithm for cooperative MARL in the centralised training and decentralised execution paradigm. In order to enable easy decentralisation, QMIX restricts the joint action $Q$-values it can represent to be a monotonic mixing of each agent's utilities. However, this restriction prevents it from representing value functions in which an agent's ordering over its actions can depend on other agents' actions. To analyse this representational limitation, we first formalise the objective QMIX optimises, which allows us to view QMIX as an operator that first computes the $Q$-learning targets and then projects them into the space representable by QMIX. This projection...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (weighted qmix research) with strong impact (474 citations) and bridge score 0.341.

### 7. Is Independent Learning All You Need in the StarCraft Multi-Agent Challenge?
**Authors:** Christian Schroeder de Witt, Tarun Gupta, Denys Makoviichuk et al.
**Year:** 2020 | **Citations (OpenAlex):** 183
**URL:** http://arxiv.org/abs/2011.09533
**Abstract:** Most recently developed approaches to cooperative multi-agent reinforcement learning in the \emph{centralized training with decentralized execution} setting involve estimating a centralized, joint value function. In this paper, we demonstrate that, despite its various theoretical shortcomings, Independent PPO (IPPO), a form of independent learning in which each agent simply estimates its local value function, can perform just as well as or better than state-of-the-art joint learning approaches on popular multi-agent benchmark suite SMAC with little hyperparameter tuning. We also compare IPPO to several variants; the results suggest that IPPO's strong performance may be due to its robustne...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (is independent learning all you need in the starcraft multi-agent challenge? research) with strong impact (183 citations) and bridge score 0.600.

### 8. Multi-Agent Game Abstraction via Graph Attention Neural Network
**Authors:** Yong Liu, Weixun Wang, Yujing Hu et al.
**Year:** 2020 | **Citations (OpenAlex):** 230
**URL:** https://doi.org/10.1609/aaai.v34i05.6211
**Abstract:** In large-scale multi-agent systems, the large number of agents and complex game relationship cause great difficulty for policy learning. Therefore, simplifying the learning process is an important research issue. In many multi-agent systems, the interactions between agents often happen locally, which means that agents neither need to coordinate with all other agents nor need to coordinate with others all the time. Traditional methods attempt to use pre-defined rules to capture the interaction relationship between agents. However, the methods cannot be directly used in a large-scale environment due to the difficulty of transforming the complex interactions between agents into rules. In thi...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (attention mechanisms) with strong impact (230 citations) and bridge score 0.498.

### 9. PPS-QMIX: Periodically Parameter Sharing for Accelerating Convergence of Multi-Agent Reinforcement Learning
**Authors:** Ke Zhang, DanDan Zhu, Qiuhan Xu et al.
**Year:** 2024 | **Citations (Semantic Scholar):** 1
**URL:** https://arxiv.org/abs/2403.02635v1
**Abstract:** Training for multi-agent reinforcement learning(MARL) is a time-consuming process caused by distribution shift of each agent. One drawback is that strategy of each agent in MARL is independent but actually in cooperation. Thus, a vertical issue in multi-agent reinforcement learning is how to efficiently accelerate training process. To address this problem, current research has leveraged a centralized function(CF) across multiple agents to learn contribution of the team reward for each agent. However, CF based methods introduce joint error from other agents in estimation of value network. In so doing, inspired by federated learning, we propose three simple novel approaches called Average P...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (pps-qmix research) with strong impact (1 citations) and bridge score 0.556.

## Recent Frontier

### 10. Interference-Aware K-Step Reachable Communication in Multi-Agent Reinforcement Learning
**Authors:** Ziyu Cheng, Jinsheng Ren, Zhouxian Jiang et al.
**Year:** 2026 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2603.15054v1
**Abstract:** Effective communication is pivotal for addressing complex collaborative tasks in multi-agent reinforcement learning (MARL). Yet, limited communication bandwidth and dynamic, intricate environmental topologies present significant challenges in identifying high-value communication partners. Agents must consequently select collaborators under uncertainty, lacking a priori knowledge of which partners can deliver task-critical information. To this end, we propose Interference-Aware K-Step Reachable Communication (IA-KRC), a novel framework that enhances cooperation via two core components: (1) a K-Step reachability protocol that confines message passing to physically accessible neighbors, and...
**Why read:** Read this near the end to see recent directions from 2026; its frontier score (0.640) indicates current research momentum.

### 11. Learning Bilateral Team Formation in Cooperative Multi-Agent Reinforcement Learning
**Authors:** Koorosh Moslemi, Chi-Guhn Lee
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2506.20039v1
**Abstract:** Team formation and the dynamics of team-based learning have drawn significant interest in the context of Multi-Agent Reinforcement Learning (MARL). However, existing studies primarily focus on unilateral groupings, predefined teams, or fixed-population settings, leaving the effects of algorithmic bilateral grouping choices in dynamic populations underexplored. To address this gap, we introduce a framework for learning two-sided team formation in dynamic multi-agent systems. Through this study, we gain insight into what algorithmic properties in bilateral team formation influence policy performance and generalization. We validate our approach using widely adopted multi-agent scenarios, dem...
**Why read:** Read this near the end to see recent directions from 2025; its frontier score (0.594) indicates current research momentum.

### 12. HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making
**Authors:** Xingxing Hong, Yungong Wang, Dexin Jin et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2509.12927v1
**Abstract:** Benchmarks are crucial for assessing multi-agent reinforcement learning (MARL) algorithms. While StarCraft II-related environments have driven significant advances in MARL, existing benchmarks like SMAC focus primarily on micromanagement, limiting comprehensive evaluation of high-level strategic intelligence. To address this, we introduce HLSMAC, a new cooperative MARL benchmark with 12 carefully designed StarCraft II scenarios based on classical stratagems from the Thirty-Six Stratagems. Each scenario corresponds to a specific stratagem and is designed to challenge agents with diverse strategic elements, including tactical maneuvering, timing coordination, and deception, thereby opening...
**Why read:** Read this near the end to see recent directions from 2025; its frontier score (0.594) indicates current research momentum.

---

## Research Graph Statistics

- **Communities detected:** 4
- **Community sizes:** [5, 12, 7, 2]

**Top papers by PageRank:**
- Counterfactual Multi-Agent Policy Gradients (PR: 0.1130, 2018)
- Value-Decomposition Networks For Cooperative Multi-Agent Learning Based On Team Reward (PR: 0.0778, 2018)
- The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games (PR: 0.0579, 2021)

**Top bridge papers:**
- The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games (BC: 0.1433)
- Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (BC: 0.1067)
- Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning (BC: 0.1067)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"