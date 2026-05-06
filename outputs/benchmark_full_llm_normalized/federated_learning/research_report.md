# ResearchTrail: Literature Reading Path Report

**Topic:** Federated Learning and Privacy-Preserving ML
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 41
- Abstract coverage: 95.1%
- Citation/reference coverage: 80.5%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2016-2026
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 41
- Edges: 339
- Citation edges: 20
- Similarity edges: 326
- Communities: 4
- Modularity: 0.2714
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Secure Federated Learning Protocols and Applications** — This community focuses on secure aggregation protocols, general federated learning frameworks, and their applications in domains like healthcare, as indicated by titles on secure aggregation and surveys on challenges.
- **Community 1: Privacy-Preserving and Differential Privacy in Federated Learning** — Research in this area addresses privacy preservation through differential privacy, analyzes inference attacks, and explores communication-efficient learning methods for deep networks.
- **Community 2: Personalized Federated Learning and Convergence Analysis** — This community investigates the convergence of algorithms like FedAvg on non-IID data and develops methods for personalized federated learning involving client selection and local training.
- **Community 3: Decentralized Federated Learning and IoT Applications** — The papers explore decentralized and server-free federated learning architectures, transfer learning, and privacy-preserving mechanisms specifically tailored for Internet-of-Things environments.

## Reading Path Metrics

- Stages: 4
- Unique papers: 13
- Explanation coverage: 100.0%

## Foundations

### 1. Practical Secure Aggregation for Privacy-Preserving Machine Learning
**Authors:** Keith Bonawitz, Vladimir Ivanov, Ben Kreuter et al.
**Year:** 2017 | **Citations (OpenAlex):** 3343
**URL:** https://doi.org/10.1145/3133956.3133982
**Abstract:** We design a novel, communication-efficient, failure-robust protocol for secure aggregation of high-dimensional data. Our protocol allows a server to compute the sum of large, user-held data vectors from mobile devices in a secure manner (i.e. without learning each user's individual contribution), and can be used, for example, in a federated learning setting, to aggregate user-provided model updates for a deep neural network. We prove the security of our protocol in the honest-but-curious and active adversary settings, and show that security is maintained even if an arbitrarily chosen subset of users drop out at any time. We evaluate the efficiency of our protocol and show, by complexity a...
**Why read:** This paper establishes a foundational protocol for secure aggregation, enabling a server to compute sums of user-held data without revealing individual contributions. It is essential for understanding communication-efficient and failure-robust privacy mechanisms in federated learning.

### 2. Communication-Efficient Learning of Deep Networks from Decentralized\n Data
**Authors:** H. Brendan McMahan, Eider Moore, Daniel Ramage et al.
**Year:** 2016 | **Citations (OpenAlex):** 5606
**URL:** http://arxiv.org/abs/1602.05629
**Abstract:** Modern mobile devices have access to a wealth of data suitable for learning\nmodels, which in turn can greatly improve the user experience on the device.\nFor example, language models can improve speech recognition and text entry, and\nimage models can automatically select good photos. However, this rich data is\noften privacy sensitive, large in quantity, or both, which may preclude logging\nto the data center and training there using conventional approaches. We\nadvocate an alternative that leaves the training data distributed on the mobile\ndevices, and learns a shared model by aggregating locally-computed updates. We\nterm this decentralized approach Federated Learning.\n We present a...
**Why read:** As the seminal work introducing the Federated Learning framework, this paper proposes iterative model averaging to train deep networks on decentralized mobile data. It provides the core methodology for leaving training data distributed while learning a shared model.

### 3. Deep Learning with Differential Privacy
**Authors:** Martín Abadi, Andy Chu, Ian Goodfellow et al.
**Year:** 2016 | **Citations:** 5716
**URL:** https://arxiv.org/abs/1607.00133v2
**Abstract:** Machine learning techniques based on neural networks are achieving remarkable results in a wide variety of domains. Often, the training of models requires large, representative datasets, which may be crowdsourced and contain sensitive information. The models should not expose private information in these datasets. Addressing this goal, we develop new algorithmic techniques for learning and a refined analysis of privacy costs within the framework of differential privacy. Our implementation and experiments demonstrate that we can train deep neural networks with non-convex objectives, under a modest privacy budget, and at a manageable cost in software complexity, training efficiency, and mod...
**Why read:** This paper introduces algorithmic techniques for training deep neural networks with differential privacy, addressing the need to prevent models from exposing sensitive information. It is crucial for understanding the integration of privacy guarantees into non-convex optimization.

## Core Algorithms

### 4. Federated Machine Learning
**Authors:** Qiang Yang, Yang Liu, Tianjian Chen et al.
**Year:** 2019 | **Citations (OpenAlex):** 5694
**URL:** https://doi.org/10.1145/3298981
**Abstract:** Today’s artificial intelligence still faces two major challenges. One is that, in most industries, data exists in the form of isolated islands. The other is the strengthening of data privacy and security. We propose a possible solution to these challenges: secure federated learning. Beyond the federated-learning framework first proposed by Google in 2016, we introduce a comprehensive secure federated-learning framework, which includes horizontal federated learning, vertical federated learning, and federated transfer learning. We provide definitions, architectures, and applications for the federated-learning framework, and provide a comprehensive survey of existing works on this subject. I...
**Why read:** This work expands the federated learning framework to include horizontal, vertical, and federated transfer learning, providing definitions and architectures for broader application. It serves as a comprehensive survey for understanding how to build data networks among organizations without compromising privacy.

## Key Developments

### 5. Advances and Open Problems in Federated Learning
**Authors:** Peter Kairouz, H. Brendan McMahan
**Year:** 2020 | **Citations (OpenAlex):** 4510
**URL:** https://doi.org/10.1561/2200000083
**Abstract:** Federated learning (FL) is a machine learning setting where many clients (e.g., mobile devices or whole organizations) collaboratively train a model under the orchestration of a central server (e.g., service provider), while keeping the training data decentralized. FL embodies the principles of focused data collection and minimization, and can mitigate many of the systemic privacy risks and costs resulting from traditional, centralized machine learning and data science approaches. Motivated by the explosive growth in FL research, this monograph discusses recent advances and presents an extensive collection of open problems and challenges.
**Why read:** This monograph provides a systematic overview of recent advances in federated learning and outlines an extensive collection of open problems. It is a key resource for understanding the current state of the field and identifying future research directions.

### 6. A Comprehensive Survey of Privacy-preserving Federated Learning
**Authors:** Xuefei Yin, Yanming Zhu, Jiankun Hu
**Year:** 2021 | **Citations (OpenAlex):** 570
**URL:** https://doi.org/10.1145/3460427
**Abstract:** The past four years have witnessed the rapid development of federated learning (FL). However, new privacy concerns have also emerged during the aggregation of the distributed intermediate results. The emerging privacy-preserving FL (PPFL) has been heralded as a solution to generic privacy-preserving machine learning. However, the challenge of protecting data privacy while maintaining the data utility through machine learning still remains. In this article, we present a comprehensive and systematic survey on the PPFL based on our proposed 5W-scenario-based taxonomy. We analyze the privacy leakage risks in the FL from five aspects, summarize existing methods, and identify future research di...
**Why read:** This survey offers a systematic taxonomy of privacy-preserving federated learning (PPFL), analyzing privacy leakage risks and summarizing existing methods. It is vital for understanding the landscape of techniques used to protect data privacy while maintaining utility.

### 7. The future of digital health with federated learning
**Authors:** Nicola Rieke, Jonny Hancox, Wenqi Li et al.
**Year:** 2020 | **Citations (OpenAlex):** 2367
**URL:** https://doi.org/10.1038/s41746-020-00323-1
**Abstract:** Data-driven machine learning (ML) has emerged as a promising approach for building accurate and robust statistical models from medical data, which is collected in huge volumes by modern healthcare systems. Existing medical data is not fully exploited by ML primarily because it sits in data silos and privacy concerns restrict access to this data. However, without access to sufficient data, ML will be prevented from reaching its full potential and, ultimately, from making the transition from research to clinical practice. This paper considers key factors contributing to this issue, explores how federated learning (FL) may provide a solution for the future of digital health and highlights th...
**Why read:** This paper explores the application of federated learning in digital health, addressing how FL can overcome data silos and privacy restrictions in medical systems. It highlights specific challenges and considerations for transitioning ML from research to clinical practice.

### 8. Federated Learning With Differential Privacy: Algorithms and Performance Analysis
**Authors:** Kang Wei, Jun Li, Ming Ding et al.
**Year:** 2020 | **Citations (OpenAlex):** 2152
**URL:** https://doi.org/10.1109/tifs.2020.2988575
**Abstract:** Federated learning (FL), as a type of distributed machine learning, is capable of significantly preserving clients’ private data from being exposed to adversaries. Nevertheless, private information can still be divulged by analyzing uploaded parameters from clients, e.g., weights trained in deep neural networks. In this paper, to effectively prevent information leakage, we propose a novel framework based on the concept of differential privacy (DP), in which artificial noise is added to parameters at the clients’ side before aggregating, namely, noising before model aggregation FL (NbAFL). First, we prove that the NbAFL can satisfy DP under distinct protection levels by properly adapting d...
**Why read:** This paper proposes a novel framework, NbAFL, which adds artificial noise to client parameters before aggregation to satisfy differential privacy. It provides a theoretical convergence bound, linking privacy levels to model performance.

### 9. Towards Personalized Federated Learning
**Authors:** Alysa Ziying Tan, Han Yu, Lizhen Cui et al.
**Year:** 2022 | **Citations (OpenAlex):** 979
**URL:** https://doi.org/10.1109/tnnls.2022.3160699
**Abstract:** In parallel with the rapid adoption of artificial intelligence (AI) empowered by advances in AI research, there has been growing awareness and concerns of data privacy. Recent significant developments in the data regulation landscape have prompted a seismic shift in interest toward privacy-preserving AI. This has contributed to the popularity of Federated Learning (FL), the leading paradigm for the training of machine learning models on data silos in a privacy-preserving manner. In this survey, we explore the domain of personalized FL (PFL) to address the fundamental challenges of FL on heterogeneous data, a universal characteristic inherent in all real-world datasets. We analyze the key...
**Why read:** This survey addresses personalized federated learning (PFL), focusing on techniques to handle heterogeneous data distributions. It categorizes PFL strategies and analyzes key challenges, making it essential for understanding how to adapt FL to non-IID data.

### 10. A Comparative Evaluation of FedAvg and Per-FedAvg Algorithms for Dirichlet Distributed Heterogeneous Data
**Authors:** Hamza Reguieg, Mohammed El Hanjri, Mohamed El Kamili et al.
**Year:** 2023 | **Citations (Semantic Scholar):** 30
**URL:** https://arxiv.org/abs/2309.01275v1
**Abstract:** In this paper, we investigate Federated Learning (FL), a paradigm of machine learning that allows for decentralized model training on devices without sharing raw data, there by preserving data privacy. In particular, we compare two strategies within this paradigm: Federated Averaging (FedAvg) and Personalized Federated Averaging (Per-FedAvg), focusing on their performance with Non-Identically and Independently Distributed (Non-IID) data. Our analysis shows that the level of data heterogeneity, modeled using a Dirichlet distribution, significantly affects the performance of both strategies, with Per-FedAvg showing superior robustness in conditions of high heterogeneity. Our results provide...
**Why read:** This paper compares FedAvg and Per-FedAvg algorithms on Non-IID data modeled by a Dirichlet distribution, demonstrating Per-FedAvg's robustness under high heterogeneity. It provides concrete insights into algorithm selection for decentralized settings.

## Recent Frontier

### 11. SRFed: Mitigating Poisoning Attacks in Privacy-Preserving Federated Learning with Heterogeneous Data
**Authors:** Yiwen Lu
**Year:** 2026 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2602.16480v1
**Abstract:** Federated Learning (FL) enables collaborative model training without exposing clients' private data, and has been widely adopted in privacy-sensitive scenarios. However, FL faces two critical security threats: curious servers that may launch inference attacks to reconstruct clients' private data, and compromised clients that can launch poisoning attacks to disrupt model aggregation. Existing solutions mitigate these attacks by combining mainstream privacy-preserving techniques with defensive aggregation strategies. However, they either incur high computation and communication overhead or perform poorly under non-independent and identically distributed (Non-IID) data settings. To tackle th...
**Why read:** This frontier research proposes SRFed, a framework that mitigates poisoning attacks and ensures privacy in Non-IID scenarios using decentralized efficient functional encryption. It addresses critical security threats like curious servers and compromised clients.

### 12. Widening the Network Mitigates the Impact of Data Heterogeneity on FedAvg
**Authors:** Like Jian, Dong Liu
**Year:** 2025 | **Citations (Semantic Scholar):** 2
**URL:** https://arxiv.org/abs/2508.12576v1
**Abstract:** Federated learning (FL) enables decentralized clients to train a model collaboratively without sharing local data. A key distinction between FL and centralized learning is that clients' data are non-independent and identically distributed, which poses significant challenges in training a global model that generalizes well across heterogeneous local data distributions. In this paper, we analyze the convergence of overparameterized FedAvg with gradient descent (GD). We prove that the impact of data heterogeneity diminishes as the width of neural networks increases, ultimately vanishing when the width approaches infinity. In the infinite-width regime, we further prove that both the global an...
**Why read:** This recent work analyzes the convergence of overparameterized FedAvg, proving that the impact of data heterogeneity diminishes as network width increases. It offers a theoretical perspective on improving generalization in the infinite-width regime.

### 13. A Novel Approach to Breast Cancer Segmentation using U-Net Model with Attention Mechanisms and FedProx
**Authors:** Eyad Gad, Mustafa Abou Khatwa, Mustafa A. Elattar et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 5
**URL:** https://arxiv.org/abs/2510.19118v1
**Abstract:** Breast cancer is a leading cause of death among women worldwide, emphasizing the need for early detection and accurate diagnosis. As such Ultrasound Imaging, a reliable and cost-effective tool, is used for this purpose, however the sensitive nature of medical data makes it challenging to develop accurate and private artificial intelligence models. A solution is Federated Learning as it is a promising technique for distributed machine learning on sensitive medical data while preserving patient privacy. However, training on non-Independent and non-Identically Distributed (non-IID) local datasets can impact the accuracy and generalization of the trained model, which is crucial for accurate t...
**Why read:** This study applies the FedProx method to non-IID ultrasound breast cancer imaging data to improve segmentation accuracy while preserving privacy. It demonstrates a practical application of federated learning techniques in a sensitive medical context.

---

## Research Graph Statistics

- **Communities detected:** 4
- **Community sizes:** [13, 6, 17, 5]

**Top papers by PageRank:**
- Practical Secure Aggregation for Privacy-Preserving Machine Learning (PR: 0.1348, 2017)
- Federated Machine Learning (PR: 0.0687, 2019)
- Communication-Efficient Learning of Deep Networks from Decentralized\n Data (PR: 0.0494, 2016)

**Top bridge papers:**
- Practical Secure Aggregation for Privacy-Preserving Machine Learning (BC: 0.3103)
- A Comprehensive Survey of Privacy-preserving Federated Learning (BC: 0.2244)
- Advances and Open Problems in Federated Learning (BC: 0.1654)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"