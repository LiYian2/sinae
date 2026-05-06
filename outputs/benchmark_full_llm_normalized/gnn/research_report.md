# ResearchTrail: Literature Reading Path Report

**Topic:** Graph Neural Networks / Geometric Deep Learning
**Level:** beginner
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 33
- Abstract coverage: 97.0%
- Citation/reference coverage: 93.9%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 1998-2025
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 33
- Edges: 219
- Citation edges: 37
- Similarity edges: 203
- Communities: 5
- Modularity: 0.278
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Graph Neural Network Applications and Optimization** — This community investigates the application of graph neural networks to combinatorial optimization, quantum chemistry, and collaborative filtering, while also analyzing theoretical issues like over-smoothing.
- **Community 1: Domain-Specific Graph Convolutional Networks** — Research in this group applies graph convolutional networks to distinct domains including text classification, skeleton-based action recognition, and molecular science, alongside methodological reviews.
- **Community 2: Spatio-Temporal Traffic and Time Series Forecasting** — This community focuses on utilizing graph neural networks and transformers for forecasting tasks involving spatio-temporal dependencies, particularly in traffic and multivariate time series data.
- **Community 3: Foundational Graph Neural Network Methods** — This cluster contains seminal papers that defined core graph neural network architectures such as Graph Convolutional Networks, GraphSAGE, and Graph Attention Networks for node and graph classification.
- **Community 4: Graph Neural Network Surveys and Relational Modeling** — This community includes comprehensive surveys of graph neural networks and explores the modeling of relational and heterogeneous data, as well as applications in emotion recognition and graph kernels.

## Reading Path Metrics

- Stages: 6
- Unique papers: 13
- Explanation coverage: 100.0%

## Prerequisites

### 1. Weisfeiler-lehman graph kernels
**Authors:** Nino Shervashidze, Pascal Schweitzer, Erik Jan Van Leeuwen et al.
**Year:** 2010 | **Citations (OpenAlex):** 1593
**URL:** http://hdl.handle.net/11858/00-001M-0000-0013-BA34-D
**Abstract:** In this article, we address the problem of defining scalable kernels on large graphs with discrete node labels. Key to our approach is the Weisfeiler-Lehman test of isomorphism, which allows us to compute a sequence of graphs which capture the topological and label information of the original graph in a runtime which is linear in the number of edges. We can apply existing graph kernels on this graph sequence and make them take into account the structural information which they ignored before. We can also define new, efficient graph kernels: In particular, a subtree kernel whose runtime is linear in the number of edges in the input graphs and in the maximum height of the subtrees considered.
**Why read:** This paper introduces the Weisfeiler-Lehman test of isomorphism to compute scalable graph kernels, providing a prerequisite method for capturing topological and label information in linear runtime.

## Conceptual Foundations

### 2. Gradient-based learning applied to document recognition
**Authors:** Yann LeCun, Léon Bottou, Yoshua Bengio et al.
**Year:** 1998 | **Citations (OpenAlex):** 57535
**URL:** https://doi.org/10.1109/5.726791
**Abstract:** Multilayer neural networks trained with the back-propagation algorithm constitute the best example of a successful gradient based learning technique. Given an appropriate network architecture, gradient-based learning algorithms can be used to synthesize a complex decision surface that can classify high-dimensional patterns, such as handwritten characters, with minimal preprocessing. This paper reviews various methods applied to handwritten character recognition and compares them on a standard handwritten digit recognition task. Convolutional neural networks, which are specifically designed to deal with the variability of 2D shapes, are shown to outperform all other techniques. Real-life d...
**Why read:** As a foundational text, this paper establishes gradient-based learning and convolutional neural networks, which are essential for understanding the deep learning techniques applied in graph neural networks.

### 3. Deep Graph Kernels
**Authors:** Pinar Yanardag, S. V. N. Vishwanathan
**Year:** 2015 | **Citations (OpenAlex):** 1047
**URL:** https://doi.org/10.1145/2783258.2783417
**Abstract:** In this paper, we present Deep Graph Kernels, a unified framework to learn latent representations of sub-structures for graphs, inspired by latest advancements in language modeling and deep learning. Our framework leverages the dependency information between sub-structures by learning their latent representations. We demonstrate instances of our framework on three popular graph kernels, namely Graphlet kernels, Weisfeiler-Lehman subtree kernels, and Shortest-Path graph kernels. Our experiments on several benchmark datasets show that Deep Graph Kernels achieve significant improvements in classification accuracy over state-of-the-art graph kernels.
**Why read:** This work unifies graph kernels with deep learning by learning latent representations of sub-structures, serving as a conceptual bridge between traditional graph kernels and neural network approaches.

## Core Methods

### 4. Targeted Branching for the Maximum Independent Set Problem Using Graph Neural Networks
**Authors:** Silva, Gabriel, Rodrigues, Mário, Teixeira, António et al.
**Year:** 2024 | **Citations (OpenAlex):** 5371
**URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2024.20
**Abstract:** Identifying a maximum independent set is a fundamental NP-hard problem. This problem has several real-world applications and requires finding the largest possible set of vertices not adjacent to each other in an undirected graph. Over the past few years, branch-and-bound and branch-and-reduce algorithms have emerged as some of the most effective methods for solving the problem exactly. Specifically, the branch-and-reduce approach, which combines branch-and-bound principles with reduction rules, has proven particularly successful in tackling previously unmanageable real-world instances. This progress was largely made possible by the development of more effective reduction rules. Neverthele...
**Why read:** This paper applies graph neural networks to the NP-hard Maximum Independent Set problem, demonstrating a core method for using GNNs to improve branching strategies in combinatorial optimization.

### 5. Neural Message Passing for Quantum Chemistry
**Authors:** Justin Gilmer, Samuel S. Schoenholz, Patrick Riley et al.
**Year:** 2017 | **Citations (OpenAlex):** 2994
**URL:** http://arxiv.org/abs/1704.01212
**Abstract:** Supervised learning on molecules has incredible potential to be useful in chemistry, drug discovery, and materials science. Luckily, several promising and closely related neural network models invariant to molecular symmetries have already been described in the literature. These models learn a message passing algorithm and aggregation procedure to compute a function of their entire input graph. At this point, the next step is to find a particularly effective variant of this general approach and apply it to chemical prediction benchmarks until we either solve them or reach the limits of the approach. In this paper, we reformulate existing models into a single common framework we call Messa...
**Why read:** This paper reformulates neural network models for molecular prediction into a common Message Passing Neural Network (MPNN) framework, establishing a core method for learning on graph-structured data.

## Key Developments

### 6. Graph neural networks: A review of methods and applications
**Authors:** Jie Zhou, Ganqu Cui, Shengding Hu et al.
**Year:** 2020 | **Citations (OpenAlex):** 5366
**URL:** https://doi.org/10.1016/j.aiopen.2021.01.001
**Abstract:** Lots of learning tasks require dealing with graph data which contains rich relation information among elements. Modeling physics systems, learning molecular fingerprints, predicting protein interface, and classifying diseases demand a model to learn from graph inputs. In other domains such as learning from non-structural data like texts and images, reasoning on extracted structures (like the dependency trees of sentences and the scene graphs of images) is an important research topic which also needs graph reasoning models. Graph neural networks (GNNs) are neural models that capture the dependence of graphs via message passing between the nodes of graphs. In recent years, variants of GNNs...
**Why read:** This survey reviews graph neural network variants like GCN and GAT, categorizing methods and applications to provide a comprehensive overview of key developments in the field.

### 7. A Comprehensive Survey on Graph Neural Networks
**Authors:** Zonghan Wu, Shirui Pan, Fengwen Chen et al.
**Year:** 2020 | **Citations (OpenAlex):** 8902
**URL:** https://doi.org/10.1109/tnnls.2020.2978386
**Abstract:** Deep learning has revolutionized many machine learning tasks in recent years, ranging from image classification and video processing to speech recognition and natural language understanding. The data in these tasks are typically represented in the Euclidean space. However, there is an increasing number of applications, where data are generated from non-Euclidean domains and are represented as graphs with complex relationships and interdependency between objects. The complexity of graph data has imposed significant challenges on the existing machine learning algorithms. Recently, many studies on extending deep learning approaches for graph data have emerged. In this article, we provide a c...
**Why read:** This comprehensive survey proposes a taxonomy for graph neural networks, covering recurrent, convolutional, and graph autoencoders, and is a key development for understanding the breadth of GNN architectures.

### 8. Revisiting Graph Based Collaborative Filtering: A Linear Residual Graph Convolutional Network Approach
**Authors:** Lei Chen, Le Wu, Richang Hong et al.
**Year:** 2020 | **Citations (OpenAlex):** 614
**URL:** https://doi.org/10.1609/aaai.v34i01.5330
**Abstract:** Graph Convolutional Networks~(GCNs) are state-of-the-art graph based representation learning models by iteratively stacking multiple layers of convolution aggregation operations and non-linear activation operations. Recently, in Collaborative Filtering~(CF) based Recommender Systems~(RS), by treating the user-item interaction behavior as a bipartite graph, some researchers model higher-layer collaborative signals with GCNs. These GCN based recommender models show superior performance compared to traditional works. However, these models suffer from training difficulty with non-linear activations for large user-item graphs. Besides, most GCN based models could not model deeper layers due to...
**Why read:** This paper revisits graph-based collaborative filtering by proposing a Linear Residual Graph Convolutional Network, addressing training difficulties and over-smoothing in recommender systems.

### 9. Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks
**Authors:** Zonghan Wu, Shirui Pan, Guodong Long et al.
**Year:** 2020 | **Citations (OpenAlex):** 1716
**URL:** https://doi.org/10.1145/3394486.3403118
**Abstract:** Modeling multivariate time series has long been a subject that has attracted researchers from a diverse range of fields including economics, finance, and traffic. A basic assumption behind multivariate time series forecasting is that its variables depend on one another but, upon looking closely, it is fair to say that existing methods fail to fully exploit latent spatial dependencies between pairs of variables. In recent years, meanwhile, graph neural networks (GNNs) have shown high capability in handling relational dependencies. GNNs require well-defined graph structures for information propagation which means they cannot be applied directly for multivariate time series where the depende...
**Why read:** This paper introduces a graph neural network framework for multivariate time series forecasting that automatically extracts latent spatial dependencies, representing a key development in spatio-temporal modeling.

### 10. Measuring and Relieving the Over-Smoothing Problem for Graph Neural Networks from the Topological View
**Authors:** Deli Chen, Yankai Lin, Wei Li et al.
**Year:** 2020 | **Citations (OpenAlex):** 975
**URL:** https://doi.org/10.1609/aaai.v34i04.5747
**Abstract:** Graph Neural Networks (GNNs) have achieved promising performance on a wide range of graph-based tasks. Despite their success, one severe limitation of GNNs is the over-smoothing issue (indistinguishable representations of nodes in different classes). In this work, we present a systematic and quantitative study on the over-smoothing issue of GNNs. First, we introduce two quantitative metrics, MAD and MADGap, to measure the smoothness and over-smoothness of the graph nodes representations, respectively. Then, we verify that smoothing is the nature of GNNs and the critical factor leading to over-smoothness is the low information-to-noise ratio of the message received by the nodes, which is p...
**Why read:** This work addresses the over-smoothing problem in GNNs by introducing quantitative metrics and topological regularization methods, contributing to the understanding of representation limitations.

## Bridge Papers

### 11. Heterogeneous Graph Attention Network
**Authors:** Xiao Wang, Houye Ji, Chuan Shi et al.
**Year:** 2019 | **Citations (OpenAlex):** 2798
**URL:** https://doi.org/10.1145/3308558.3313562
**Abstract:** Graph neural network, as a powerful graph representation technique based on deep learning, has shown superior performance and attracted considerable research interest. However, it has not been fully considered in graph neural network for heterogeneous graph which contains different types of nodes and links. The heterogeneity and rich semantic information bring great challenges for designing a graph neural network for heterogeneous graph. Recently, one of the most exciting advancements in deep learning is the attention mechanism, whose great potential has been well demonstrated in various areas. In this paper, we first propose a novel heterogeneous graph neural network based on the hierarc...
**Why read:** This paper proposes a Heterogeneous Graph Attention Network using hierarchical attention to handle different node and link types, bridging standard GNNs with complex semantic modeling.

## Recent Advances

### 12. T-Graphormer: Using Transformers for Spatiotemporal Forecasting
**Authors:** Hao Yuan Bai, Xue Liu
**Year:** 2025 | **Citations (Semantic Scholar):** 6
**URL:** https://arxiv.org/abs/2501.13274v3
**Abstract:** Spatiotemporal data is ubiquitous, and forecasting it has important applications in many domains. However, its complex cross-component dependencies and non-linear temporal dynamics can be challenging for traditional techniques. Existing methods address this by learning the two dimensions separately. Here, we introduce Temporal Graphormer (T-Graphormer), a Transformer-based approach capable of modelling spatiotemporal correlations simultaneously. By adding temporal encodings in the Graphormer architecture, each node attends to all other tokens within the graph sequence, enabling the model to learn rich spacetime patterns with minimal predefined inductive biases. We show the effectiveness o...
**Why read:** This recent advance introduces Temporal Graphormer, a Transformer-based architecture that models spatiotemporal correlations simultaneously for improved forecasting performance.

### 13. E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials
**Authors:** Simon Batzner, Albert Musaelian, Lixin Sun et al.
**Year:** 2022 | **Citations (OpenAlex):** 1589
**URL:** https://doi.org/10.1038/s41467-022-29939-5
**Abstract:** This work presents Neural Equivariant Interatomic Potentials (NequIP), an E(3)-equivariant neural network approach for learning interatomic potentials from ab-initio calculations for molecular dynamics simulations. While most contemporary symmetry-aware models use invariant convolutions and only act on scalars, NequIP employs E(3)-equivariant convolutions for interactions of geometric tensors, resulting in a more information-rich and faithful representation of atomic environments. The method achieves state-of-the-art accuracy on a challenging and diverse set of molecules and materials while exhibiting remarkable data efficiency. NequIP outperforms existing models with up to three orders o...
**Why read:** This paper presents NequIP, an E(3)-equivariant graph neural network for interatomic potentials that achieves high data efficiency and accuracy, representing a frontier in molecular dynamics.

---

## Research Graph Statistics

- **Communities detected:** 5
- **Community sizes:** [13, 5, 3, 6, 6]

**Top papers by PageRank:**
- Targeted Branching for the Maximum Independent Set Problem Using Graph Neural Networks (PR: 0.0970, 2024)
- Weisfeiler-lehman graph kernels (PR: 0.0790, 2010)
- Neural Message Passing for Quantum Chemistry (PR: 0.0625, 2017)

**Top bridge papers:**
- Targeted Branching for the Maximum Independent Set Problem Using Graph Neural Networks (BC: 0.2974)
- Heterogeneous Graph Attention Network (BC: 0.2560)
- Modeling Relational Data with Graph Convolutional Networks (BC: 0.1895)

---

## Follow-up Questions You Can Ask

- "Add more survey and tutorial papers"
- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"