# ResearchTrail: Literature Reading Path Report

**Topic:** Diffusion Models / Score-Based Generative Models
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 28
- Abstract coverage: 100.0%
- Citation/reference coverage: 85.7%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2020-2026
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 28
- Edges: 106
- Citation edges: 5
- Similarity edges: 103
- Communities: 4
- Modularity: 0.3486
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Data / Diffusion / Samples / Methylation** — Community 0 groups papers around data, diffusion, samples, methylation.
- **Community 1: Diffusion / Noise / Denoising / Distribution** — Community 1 groups papers around diffusion, noise, denoising, distribution.
- **Community 2: Diffusion / Discrete / Data / Generative** — Community 2 groups papers around diffusion, discrete, data, generative.
- **Community 3: Diffusion / Image / Denoising / Generation** — Community 3 groups papers around diffusion, image, denoising, generation.

## Reading Path Metrics

- Stages: 4
- Unique papers: 10
- Explanation coverage: 100.0%

## Foundations

### 1. Denoising Diffusion Probabilistic Models
**Authors:** Yan, Steven
**Year:** 2020 | **Citations (OpenAlex):** 5604
**URL:** http://arxiv.org/abs/2006.11239
**Abstract:** DiffuCpG 1. Introduction In this study, we used a generative AI diffusion model to address missing methylation data. We trained the model with Whole-Genome Bisulfite Sequencing data from 26 acute myeloid leukemia samples and validated it with Reduced Representation Bisulfite Sequencing data from 93 myelodysplastic syndrome and 13 normal samples. Additional testing included data from the Illumina 450k methylation array and Single-Cell Reduced Representation Bisulfite Sequencing on HepG2 cells. Our model, DiffuCpG, outperformed previous methods by integrating a broader range of genomic features, utilizing both short- and long-range interactions without increasing input complexity. It demons...
**Why read:** Read this early because it is structurally central in the graph and heavily cited (5604 citations), making it a foundation for later work.

### 2. Score-Based Generative Modeling through Stochastic Differential Equations
**Authors:** Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma et al.
**Year:** 2020 | **Citations:** 1270
**URL:** https://arxiv.org/abs/2011.13456v2
**Abstract:** Creating noise from data is easy; creating data from noise is generative modeling. We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a corresponding reverse-time SDE that transforms the prior distribution back into the data distribution by slowly removing the noise. Crucially, the reverse-time SDE depends only on the time-dependent gradient field (\aka, score) of the perturbed data distribution. By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples. We show th...
**Why read:** Read this early to establish the core vocabulary and assumptions before moving to later specialized papers.

### 3. Palette: Image-to-Image Diffusion Models
**Authors:** Chitwan Saharia, William Chan, Huiwen Chang et al.
**Year:** 2022 | **Citations (OpenAlex):** 1460
**URL:** https://doi.org/10.1145/3528233.3530757
**Abstract:** This paper develops a unified framework for image-to-image translation based on conditional diffusion models and evaluates this framework on four challenging image-to-image translation tasks, namely colorization, inpainting, uncropping, and JPEG restoration. Our simple implementation of image-to-image diffusion models outperforms strong GAN and regression baselines on all tasks, without task-specific hyper-parameter tuning, architecture customization, or any auxiliary loss or sophisticated new techniques needed. We uncover the impact of an L2 vs. L1 loss in the denoising diffusion objective on sample diversity, and demonstrate the importance of self-attention in the neural architecture th...
**Why read:** Read this early because it is structurally central in the graph and heavily cited (1460 citations), making it a foundation for later work.

## Core Algorithms

### 4. Image Super-Resolution Via Iterative Refinement
**Authors:** Chitwan Saharia, Jonathan Ho, William Chan et al.
**Year:** 2022 | **Citations (OpenAlex):** 1615
**URL:** https://doi.org/10.1109/tpami.2022.3204461
**Abstract:** We present SR3, an approach to image Super-Resolution via Repeated Refinement. SR3 adapts denoising diffusion probabilistic models (Ho et al. 2020), (Sohl-Dickstein et al. 2015) to image-to-image translation, and performs super-resolution through a stochastic iterative denoising process. Output images are initialized with pure Gaussian noise and iteratively refined using a U-Net architecture that is trained on denoising at various noise levels, conditioned on a low-resolution input image. SR3 exhibits strong performance on super-resolution tasks at different magnification factors, on faces and natural images. We conduct human evaluation on a standard 8× face super-resolution task on Celeb...
**Why read:** Read this as a core method paper because it has high graph centrality (PageRank 0.043) and anchors later developments in the path.

## Key Developments

### 5. High-Resolution Image Synthesis with Latent Diffusion Models
**Authors:** Robin Rombach, Andreas Blattmann, Dominik Lorenz et al.
**Year:** 2021 | **Citations:** 13113
**URL:** https://arxiv.org/abs/2112.10752v2
**Abstract:** By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast t...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (attention mechanisms) with strong impact (13113 citations) and bridge score 0.285.

### 6. Diffusion Models in Vision: A Survey
**Authors:** Florinel-Alin Croitoru, Vlad Hondru, Radu Tudor Ionescu et al.
**Year:** 2023 | **Citations (OpenAlex):** 1539
**URL:** https://doi.org/10.1109/tpami.2023.3261988
**Abstract:** Denoising diffusion models represent a recent emerging topic in computer vision, demonstrating remarkable results in the area of generative modeling. A diffusion model is a deep generative model that is based on two stages, a forward diffusion stage and a reverse diffusion stage. In the forward diffusion stage, the input data is gradually perturbed over several steps by adding Gaussian noise. In the reverse stage, a model is tasked at recovering the original input data by learning to gradually reverse the diffusion process, step by step. Diffusion models are widely appreciated for the quality and diversity of the generated samples, despite their known computational burdens, i.e., low spee...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (diffusion models in vision research) with strong impact (1539 citations) and bridge score 0.967.

### 7. Improved Denoising Diffusion Probabilistic Models
**Authors:** Alex Nichol, Prafulla Dhariwal
**Year:** 2021 | **Citations (Semantic Scholar):** 5224
**URL:** https://arxiv.org/abs/2102.09672v1
**Abstract:** Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples. We show that with a few simple modifications, DDPMs can also achieve competitive log-likelihoods while maintaining high sample quality. Additionally, we find that learning variances of the reverse diffusion process allows sampling with an order of magnitude fewer forward passes with a negligible difference in sample quality, which is important for the practical deployment of these models. We additionally use precision and recall to compare how well DDPMs and GANs cover the target distribution. Finally, we show that the sample quality and likelihood...
**Why read:** Read this after the foundation papers because it represents a major follow-up branch (improved denoising diffusion probabilistic models research) with strong impact (5224 citations) and bridge score 0.209.

## Recent Frontier

### 8. Unrestrained Simplex Denoising for Discrete Data. A Non-Markovian Approach Applied to Graph Generation
**Authors:** Yoann Boget, Alexandros Kalousis
**Year:** 2026 | **Citations (Semantic Scholar):** 1
**URL:** https://arxiv.org/abs/2603.28572v1
**Abstract:** Denoising models such as Diffusion or Flow Matching have recently advanced generative modeling for discrete structures, yet most approaches either operate directly in the discrete state space, causing abrupt state changes. We introduce simplex denoising, a simple yet effective generative framework that operates on the probability simplex. The key idea is a non-Markovian noising scheme in which, for a given clean data point, noisy representations at different times are conditionally independent. While preserving the theoretical guarantees of denoising-based generative models, our method removes unnecessary constraints, thereby improving performance and simplifying the formulation. Empirica...
**Why read:** Read this near the end to see recent directions from 2026; its frontier score (0.679) indicates current research momentum.

### 9. Balanced conic rectified flow
**Authors:** Shin Seong Kim, Mingi Kwon, Jaeseok Jeong et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 3
**URL:** https://arxiv.org/abs/2510.25229v1
**Abstract:** Rectified flow is a generative model that learns smooth transport mappings between two distributions through an ordinary differential equation (ODE). Unlike diffusion-based generative models, which require costly numerical integration of a generative ODE to sample images with state-of-the-art quality, rectified flow uses an iterative process called reflow to learn smooth and straight ODE paths. This allows for relatively simple and efficient generation of high-quality images. However, rectified flow still faces several challenges. 1) The reflow process requires a large number of generative pairs to preserve the target distribution, leading to significant computational costs. 2) Since the...
**Why read:** Read this near the end to see recent directions from 2025; its frontier score (0.633) indicates current research momentum.

### 10. Denoising Functional Maps: Diffusion Models for Shape Correspondence
**Authors:** Aleksei Zhuravlev, Zorah Lähner, Vladislav Golyanik
**Year:** 2025 | **Citations (Semantic Scholar):** 9
**URL:** https://arxiv.org/abs/2503.01845v2
**Abstract:** Estimating correspondences between pairs of deformable shapes remains a challenging problem. Despite substantial progress, existing methods lack broad generalization capabilities and require category-specific training data. To address these limitations, we propose a fundamentally new approach to shape correspondence based on denoising diffusion models. In our method, a diffusion model learns to directly predict the functional map, a low-dimensional representation of a point-wise map between shapes. We use a large dataset of synthetic human meshes for training and employ two steps to reduce the number of functional maps that need to be learned. First, the maps refer to a template rather th...
**Why read:** Read this near the end to see recent directions from 2025; its frontier score (0.633) indicates current research momentum.

---

## Research Graph Statistics

- **Communities detected:** 4
- **Community sizes:** [10, 4, 7, 7]

**Top papers by PageRank:**
- Denoising Diffusion Probabilistic Models (PR: 0.0611, 2020)
- Palette: Image-to-Image Diffusion Models (PR: 0.0611, 2022)
- Image Super-Resolution Via Iterative Refinement (PR: 0.0429, 2022)

**Top bridge papers:**
- Diffusion Models in Vision: A Survey (BC: 0.4558)
- Score-Based Generative Modeling through Stochastic Differential Equations (BC: 0.1168)
- Image Super-Resolution Via Iterative Refinement (BC: 0.1111)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"