# ResearchTrail: Literature Reading Path Report

**Topic:** Diffusion Models / Score-Based Generative Models
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 21
- Abstract coverage: 100.0%
- Citation/reference coverage: 85.7%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2020-2025
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 21
- Edges: 77
- Citation edges: 5
- Similarity edges: 74
- Communities: 3
- Modularity: 0.2953
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Data / Diffusion / Samples / Methylation** — Community 0 groups papers around data, diffusion, samples, methylation.
- **Community 1: Generative / Data / Modeling / Flow** — Community 1 groups papers around generative, data, modeling, flow.
- **Community 2: Diffusion / Image / Denoising / Training** — Community 2 groups papers around diffusion, image, denoising, training.

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
**Why read:** This paper introduces DiffuCpG, a generative AI diffusion model designed to address missing methylation data, demonstrating superior accuracy and scalability across various genomic technologies.

### 2. Score-Based Generative Modeling through Stochastic Differential Equations
**Authors:** Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma et al.
**Year:** 2020 | **Citations:** 1270
**URL:** https://arxiv.org/abs/2011.13456v2
**Abstract:** Creating noise from data is easy; creating data from noise is generative modeling. We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a corresponding reverse-time SDE that transforms the prior distribution back into the data distribution by slowly removing the noise. Crucially, the reverse-time SDE depends only on the time-dependent gradient field (\aka, score) of the perturbed data distribution. By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples. We show th...
**Why read:** This work establishes a foundational framework using stochastic differential equations (SDEs) to transform data distributions by injecting and removing noise, encapsulating previous score-based and diffusion modeling approaches.

### 3. Palette: Image-to-Image Diffusion Models
**Authors:** Chitwan Saharia, William Chan, Huiwen Chang et al.
**Year:** 2022 | **Citations (OpenAlex):** 1460
**URL:** https://doi.org/10.1145/3528233.3530757
**Abstract:** This paper develops a unified framework for image-to-image translation based on conditional diffusion models and evaluates this framework on four challenging image-to-image translation tasks, namely colorization, inpainting, uncropping, and JPEG restoration. Our simple implementation of image-to-image diffusion models outperforms strong GAN and regression baselines on all tasks, without task-specific hyper-parameter tuning, architecture customization, or any auxiliary loss or sophisticated new techniques needed. We uncover the impact of an L2 vs. L1 loss in the denoising diffusion objective on sample diversity, and demonstrate the importance of self-attention in the neural architecture th...
**Why read:** This paper develops a unified framework for image-to-image translation using conditional diffusion models, outperforming GANs on tasks like colorization and inpainting without task-specific tuning.

## Core Algorithms

### 4. Image Super-Resolution Via Iterative Refinement
**Authors:** Chitwan Saharia, Jonathan Ho, William Chan et al.
**Year:** 2022 | **Citations (OpenAlex):** 1615
**URL:** https://doi.org/10.1109/tpami.2022.3204461
**Abstract:** We present SR3, an approach to image Super-Resolution via Repeated Refinement. SR3 adapts denoising diffusion probabilistic models (Ho et al. 2020), (Sohl-Dickstein et al. 2015) to image-to-image translation, and performs super-resolution through a stochastic iterative denoising process. Output images are initialized with pure Gaussian noise and iteratively refined using a U-Net architecture that is trained on denoising at various noise levels, conditioned on a low-resolution input image. SR3 exhibits strong performance on super-resolution tasks at different magnification factors, on faces and natural images. We conduct human evaluation on a standard 8× face super-resolution task on Celeb...
**Why read:** This core algorithm paper presents SR3, an approach to image super-resolution that adapts denoising diffusion probabilistic models to iteratively refine images from Gaussian noise conditioned on low-resolution inputs.

## Key Developments

### 5. High-Resolution Image Synthesis with Latent Diffusion Models
**Authors:** Robin Rombach, Andreas Blattmann, Dominik Lorenz et al.
**Year:** 2021 | **Citations:** 13113
**URL:** https://arxiv.org/abs/2112.10752v2
**Abstract:** By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast t...
**Why read:** This key development introduces Latent Diffusion Models (LDMs), which operate in the latent space of pretrained autoencoders to significantly reduce computational complexity while retaining high-quality synthesis.

### 6. Diffusion Models in Vision: A Survey
**Authors:** Florinel-Alin Croitoru, Vlad Hondru, Radu Tudor Ionescu et al.
**Year:** 2023 | **Citations (OpenAlex):** 1539
**URL:** https://doi.org/10.1109/tpami.2023.3261988
**Abstract:** Denoising diffusion models represent a recent emerging topic in computer vision, demonstrating remarkable results in the area of generative modeling. A diffusion model is a deep generative model that is based on two stages, a forward diffusion stage and a reverse diffusion stage. In the forward diffusion stage, the input data is gradually perturbed over several steps by adding Gaussian noise. In the reverse stage, a model is tasked at recovering the original input data by learning to gradually reverse the diffusion process, step by step. Diffusion models are widely appreciated for the quality and diversity of the generated samples, despite their known computational burdens, i.e., low spee...
**Why read:** This survey provides a comprehensive review of denoising diffusion models in computer vision, covering theoretical foundations and applications to contextualize the field's progress.

### 7. Improved Denoising Diffusion Probabilistic Models
**Authors:** Alex Nichol, Prafulla Dhariwal
**Year:** 2021 | **Citations (Semantic Scholar):** 5224
**URL:** https://arxiv.org/abs/2102.09672v1
**Abstract:** Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples. We show that with a few simple modifications, DDPMs can also achieve competitive log-likelihoods while maintaining high sample quality. Additionally, we find that learning variances of the reverse diffusion process allows sampling with an order of magnitude fewer forward passes with a negligible difference in sample quality, which is important for the practical deployment of these models. We additionally use precision and recall to compare how well DDPMs and GANs cover the target distribution. Finally, we show that the sample quality and likelihood...
**Why read:** This paper improves upon DDPMs by achieving competitive log-likelihoods and enabling faster sampling with fewer forward passes, enhancing the practical deployment of these models.

## Recent Frontier

### 8. Riemannian Denoising Diffusion Probabilistic Models
**Authors:** Zichen Liu, Wei Zhang, Christof Schütte et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 5
**URL:** https://arxiv.org/abs/2505.04338v2
**Abstract:** We propose Riemannian Denoising Diffusion Probabilistic Models (RDDPMs) for learning distributions on submanifolds of Euclidean space that are level sets of functions, including most of the manifolds relevant to applications. Existing methods for generative modeling on manifolds rely on substantial geometric information such as geodesic curves or eigenfunctions of the Laplace-Beltrami operator and, as a result, they are limited to manifolds where such information is available. In contrast, our method, built on a projection scheme, can be applied to more general manifolds, as it only requires being able to evaluate the value and the first order derivatives of the function that defines the...
**Why read:** This frontier research proposes Riemannian Denoising Diffusion Probabilistic Models (RDDPMs) to learn distributions on submanifolds using a projection scheme that requires only function evaluations and derivatives.

### 9. Balanced conic rectified flow
**Authors:** Shin Seong Kim, Mingi Kwon, Jaeseok Jeong et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 3
**URL:** https://arxiv.org/abs/2510.25229v1
**Abstract:** Rectified flow is a generative model that learns smooth transport mappings between two distributions through an ordinary differential equation (ODE). Unlike diffusion-based generative models, which require costly numerical integration of a generative ODE to sample images with state-of-the-art quality, rectified flow uses an iterative process called reflow to learn smooth and straight ODE paths. This allows for relatively simple and efficient generation of high-quality images. However, rectified flow still faces several challenges. 1) The reflow process requires a large number of generative pairs to preserve the target distribution, leading to significant computational costs. 2) Since the...
**Why read:** This recent work introduces Balanced Conic Rectified Flow, addressing challenges in the reflow process to learn smooth and straight ODE paths for efficient high-quality image generation.

### 10. Diffusion-4K: Ultra-High-Resolution Image Synthesis with Latent Diffusion Models
**Authors:** Jinjin Zhang, Qiuyu Huang, Junjie Liu et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 43
**URL:** https://arxiv.org/abs/2503.18352v2
**Abstract:** In this paper, we present Diffusion-4K, a novel framework for direct ultra-high-resolution image synthesis using text-to-image diffusion models. The core advancements include: (1) Aesthetic-4K Benchmark: addressing the absence of a publicly available 4K image synthesis dataset, we construct Aesthetic-4K, a comprehensive benchmark for ultra-high-resolution image generation. We curated a high-quality 4K dataset with carefully selected images and captions generated by GPT-4o. Additionally, we introduce GLCM Score and Compression Ratio metrics to evaluate fine details, combined with holistic measures such as FID, Aesthetics and CLIPScore for a comprehensive assessment of ultra-high-resolution...
**Why read:** This paper presents Diffusion-4K, a framework for direct ultra-high-resolution image synthesis that includes a new 4K benchmark and a wavelet-based fine-tuning approach for photorealistic generation.

---

## Research Graph Statistics

- **Communities detected:** 3
- **Community sizes:** [10, 4, 7]

**Top papers by PageRank:**
- Denoising Diffusion Probabilistic Models (PR: 0.0797, 2020)
- Palette: Image-to-Image Diffusion Models (PR: 0.0797, 2022)
- Image Super-Resolution Via Iterative Refinement (PR: 0.0559, 2022)

**Top bridge papers:**
- Diffusion Models in Vision: A Survey (BC: 0.4684)
- Score-Based Generative Modeling through Stochastic Differential Equations (BC: 0.1368)
- Image Super-Resolution Via Iterative Refinement (BC: 0.1263)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"