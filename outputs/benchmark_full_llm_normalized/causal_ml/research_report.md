# ResearchTrail: Literature Reading Path Report

**Topic:** Causal Inference in Machine Learning
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 18
- Abstract coverage: 94.4%
- Citation/reference coverage: 94.4%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 1983-2026
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 18
- Edges: 39
- Citation edges: 10
- Similarity edges: 35
- Communities: 7
- Modularity: 0.1291
- Largest component ratio: 88.9%

## Detected Research Communities

- **Community 0: Causal / Data / Inference / Propensity** — Community 0 groups papers around causal, data, inference, propensity.
- **Community 1: Causal / Time / Series / Data** — Community 1 groups papers around causal, time, series, data.
- **Community 2: Causal / Inference / Statistics / Primer** — Community 2 groups papers around causal, inference, statistics, primer.
- **Community 3: Causal / Observational / Confounders / Inference** — Community 3 groups papers around causal, observational, confounders, inference.
- **Community 4: Machine / Causal / Environments / Causality** — Community 4 groups papers around machine, causal, environments, causality.
- **Community 5: Control / Causal / Data / Units** — Community 5 groups papers around control, causal, data, units.
- **Community 6: Conditional / Independence / Test / Data** — Community 6 groups papers around conditional, independence, test, data.

## Reading Path Metrics

- Stages: 3
- Unique papers: 10
- Explanation coverage: 100.0%

## Foundations

### 1. The central role of the propensity score in observational studies for causal effects
**Authors:** Paul R. Rosenbaum, Donald B. Rubin
**Year:** 1983 | **Citations (OpenAlex):** 30633
**URL:** https://doi.org/10.1093/biomet/70.1.41
**Abstract:** The propensity score is the conditional probability of assignment to a particular treatment given a vector of observed covariates. Both large and small sample theory show that adjustment for the scalar propensity score is sufficient to remove bias due to all observed covariates. Applications include: (i) matched sampling on the univariate propensity score, which is a generalization of discriminant matching, (ii) multivariate adjustment by subclassification on the propensity score where the same subclasses are used to estimate treatment effects for all outcome variables and in all subpopulations, and (iii) visual representation of multivariate covariance adjustment by a two- dimensional plot.
**Why read:** This paper establishes the theoretical basis for the propensity score, demonstrating how adjustment for this scalar removes bias due to all observed covariates in observational studies.

### 2. Causal inference in statistics: An overview
**Authors:** Judea Pearl
**Year:** 2009 | **Citations (OpenAlex):** 2290
**URL:** https://doi.org/10.1214/09-ss057
**Abstract:** This review presents empirical researchers with recent advances in causal inference, and stresses the paradigmatic shifts that must be undertaken in moving from traditional statistical analysis to causal analysis of multivariate data. Special emphasis is placed on the assumptions that underly all causal inferences, the languages used in formulating those assumptions, the conditional nature of all causal and counterfactual claims, and the methods that have been developed for the assessment of such claims. These advances are illustrated using a general theory of causation based on the Structural Causal Model (SCM) described in Pearl (2000a), which subsumes and unifies other approaches to ca...
**Why read:** This review introduces the Structural Causal Model (SCM) framework, providing the mathematical foundation and necessary paradigmatic shifts for moving from statistical to causal analysis.

### 3. Matching Methods for Causal Inference: A Review and a Look Forward
**Authors:** Elizabeth A. Stuart
**Year:** 2010 | **Citations (OpenAlex):** 5278
**URL:** https://doi.org/10.1214/09-sts313
**Abstract:** When estimating causal effects using observational data, it is desirable to replicate a randomized experiment as closely as possible by obtaining treated and control groups with similar covariate distributions. This goal can often be achieved by choosing well-matched samples of the original treated and control groups, thereby reducing bias due to the covariates. Since the 1970's, work on matching methods has examined how to best choose treated and control subjects for comparison. Matching methods are gaining popularity in fields such as economics, epidemiology, medicine, and political science. However, until now the literature and related advice has been scattered across disciplines. Rese...
**Why read:** This paper structures the scattered literature on matching methods, explaining how to select treated and control subjects to replicate randomized experiments and reduce bias.

## Core Algorithms

### 4. Detecting and quantifying causal associations in large nonlinear time series datasets
**Authors:** Jakob Runge, Peer Nowack, Marlene Kretschmer et al.
**Year:** 2019 | **Citations (OpenAlex):** 810
**URL:** https://doi.org/10.1126/sciadv.aau4996
**Abstract:** Identifying causal relationships and quantifying their strength from observational time series data are key problems in disciplines dealing with complex dynamical systems such as the Earth system or the human body. Data-driven causal inference in such systems is challenging since datasets are often high dimensional and nonlinear with limited sample sizes. Here, we introduce a novel method that flexibly combines linear or nonlinear conditional independence tests with a causal discovery algorithm to estimate causal networks from large-scale time series datasets. We validate the method on time series of well-understood physical mechanisms in the climate system and the human heart and using l...
**Why read:** This paper introduces a method that combines conditional independence tests with causal discovery algorithms to estimate causal networks from large-scale, nonlinear time series datasets.

## Key Developments

### 5. A Survey on Causal Inference
**Authors:** Liuyi Yao, Zhixuan Chu, Sheng Li et al.
**Year:** 2021 | **Citations (Semantic Scholar):** 655
**URL:** https://doi.org/10.1145/3444944
**Abstract:** Causal inference is a critical research topic across many domains, such as statistics, computer science, education, public policy, and economics, for decades. Nowadays, estimating causal effect from observational data has become an appealing research direction owing to the large amount of available data and low budget requirement, compared with randomized controlled trials. Embraced with the rapidly developed machine learning area, various causal effect estimation methods for observational data have sprung up. In this survey, we provide a comprehensive review of causal inference methods under the potential outcome framework, one of the well-known causal inference frameworks. The methods a...
**Why read:** This survey provides a comprehensive review of causal inference methods under the potential outcome framework, categorizing both traditional statistical and modern machine learning approaches.

### 6. Toward Causal Representation Learning
**Authors:** Bernhard Schölkopf, Francesco Locatello, Stefan Bauer et al.
**Year:** 2021 | **Citations (Semantic Scholar):** 1339
**URL:** https://doi.org/10.1109/jproc.2021.3058954
**Abstract:** The two fields of machine learning and graphical causality arose and are developed separately. However, there is, now, cross-pollination and increasing interest in both fields to benefit from the advances of the other. In this article, we review fundamental concepts of causal inference and relate them to crucial open problems of machine learning, including transfer and generalization, thereby assaying how causality can contribute to modern machine learning research. This also applies in the opposite direction: we note that most work in causality starts from the premise that the causal variables are given. A central problem for AI and causality is, thus, causal representation learning, tha...
**Why read:** This article connects causal inference with machine learning, addressing open problems like transfer learning and defining the research area of causal representation learning.

### 7. Positive-Unlabeled Learning for Control Group Construction in Observational Causal Inference
**Authors:** Ilias Tsoumas, Dimitrios Bormpoudakis, Vasileios Sitokonstantinou et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2507.14528v1
**Abstract:** In causal inference, whether through randomized controlled trials or observational studies, access to both treated and control units is essential for estimating the effect of a treatment on an outcome of interest. When treatment assignment is random, the average treatment effect (ATE) can be estimated directly by comparing outcomes between groups. In non-randomized settings, various techniques are employed to adjust for confounding and approximate the counterfactual scenario to recover an unbiased ATE. A common challenge, especially in observational studies, is the absence of units clearly labeled as controls-that is, units known not to have received the treatment. To address this, we pro...
**Why read:** This paper proposes a positive-unlabeled (PU) learning framework to identify control units from unlabeled data, addressing the absence of clear controls in observational studies.

### 8. A Kernel-Based Nonparametric Test for Conditional Independence of Functional Data
**Authors:** Yin Tang, Bing Li
**Year:** 2026 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2603.13704v1
**Abstract:** Conditional independence is a fundamental concept in many areas of statistical research, including, for example, sufficient dimension reduction, causal inference, and statistical graphical models. In many modern applications, data arise in the form of random functions, making it important to determine whether two random functions are conditionally independent given a third. However, to the best of our knowledge, existing conditional independence tests in the literature apply only to multivariate data, and extensions to the functional setting are not available. To fill this gap, we develop a kernel-based test for conditional independence of random functions based on the conjoined condition...
**Why read:** This paper develops a kernel-based test for conditional independence of random functions, extending causal inference capabilities to functional data settings.

### 9. A Scoping Review of Earth Observation and Machine Learning for Causal Inference: Implications for the Geography of Poverty
**Authors:** Kazuki Sakamoto, Connor T. Jerzak, Adel Daoud
**Year:** 2024 | **Citations (Semantic Scholar):** 8
**URL:** https://arxiv.org/abs/2406.02584v4
**Abstract:** Earth observation (EO) data such as satellite imagery can have far-reaching impacts on our understanding of the geography of poverty, especially when coupled with machine learning (ML) and computer vision. Early research used computer vision to predict living conditions in areas with limited data, but recent studies increasingly focus on causal analysis. Despite this shift, the use of EO-ML methods for causal inference lacks thorough documentation, and best practices are still developing. Through a comprehensive scoping review, we catalog the current literature on EO-ML methods in causal analysis. We synthesize five principal approaches to incorporating EO data in causal workflows: (1) ou...
**Why read:** This scoping review synthesizes five approaches for integrating Earth Observation data into causal workflows, documenting emerging best practices for this application.

### 10. Philip G. Wright, directed acyclic graphs, and instrumental variables
**Authors:** Jaap H. Abbring, Victor Chernozhukov, Iván Fernández-Val
**Year:** 2025 | **Citations (Semantic Scholar):** 3
**URL:** https://arxiv.org/abs/2501.16395v2
**Abstract:** Wright (1928) deals with demand and supply of oils and butter. In Appendix B of this book, Philip Wright made several fundamental contributions to causal inference. He introduced a structural equation model of supply and demand, established the identification of supply and demand elasticities via the method of moments and directed acyclical graphs, developed empirical methods for estimating demand elasticities using weather conditions as instruments, and proposed methods for counterfactual analysis of the welfare effect of imposing tariffs and taxes. Moreover, he took all of these methods to data. These ideas were far ahead, and much more profound than, any contemporary theoretical and em...
**Why read:** This editorial recontextualizes Philip G. Wright's early work on structural equations and instrumental variables, presenting these foundational concepts in a modern framework.

---

## Research Graph Statistics

- **Communities detected:** 7
- **Community sizes:** [5, 2, 1, 2, 3, 4, 1]

**Top papers by PageRank:**
- The central role of the propensity score in observational studies for causal effects (PR: 0.1916, 1983)
- Causal inference in statistics: An overview (PR: 0.1063, 2009)
- Detecting and quantifying causal associations in large nonlinear time series datasets (PR: 0.1048, 2019)

**Top bridge papers:**
- A Survey on Causal Inference (BC: 0.4779)
- Causal inference in statistics: An overview (BC: 0.2059)
- The central role of the propensity score in observational studies for causal effects (BC: 0.1912)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"