# ResearchTrail: Literature Reading Path Report

**Topic:** Diffusion Models / Score-Based Generative Models
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 31
- Abstract coverage: 100.0%
- Citation/reference coverage: 87.1%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 1973-2026
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 31
- Edges: 105
- Citation edges: 5
- Similarity edges: 102
- Communities: 6
- Modularity: 0.3515
- Largest component ratio: 90.3%

## Detected Research Communities

- **Community 0: Data / Diffusion / Samples / Methylation** — Community 0 groups papers around data, diffusion, samples, methylation.
- **Community 1: Diffusion / Generative / Data / Denoising** — Community 1 groups papers around diffusion, generative, data, denoising.
- **Community 2: Functions / Potential / Water / Tips** — Community 2 groups papers around functions, potential, water, tips.
- **Community 3: Acceptance / Technology / Eight / Theory** — Community 3 groups papers around acceptance, technology, eight, theory.
- **Community 4: Ties / Strength / Weak / Groups** — Community 4 groups papers around ties, strength, weak, groups.
- **Community 5: Diffusion / Image / Denoising / Generation** — Community 5 groups papers around diffusion, image, denoising, generation.

## Reading Path Metrics

- Stages: 4
- Unique papers: 13
- Explanation coverage: 100.0%

## Foundations

### 1. Comparison of simple potential functions for simulating liquid water
**Authors:** William L. Jorgensen, Jayaraman Chandrasekhar, Jeffry D. Madura et al.
**Year:** 1983 | **Citations (OpenAlex):** 41673
**URL:** https://doi.org/10.1063/1.445869
**Abstract:** Classical Monte Carlo simulations have been carried out for liquid water in the NPT ensemble at 25 °C and 1 atm using six of the simpler intermolecular potential functions for the water dimer: Bernal–Fowler (BF), SPC, ST2, TIPS2, TIP3P, and TIP4P. Comparisons are made with experimental thermodynamic and structural data including the recent neutron diffraction results of Thiessen and Narten. The computed densities and potential energies are in reasonable accord with experiment except for the original BF model, which yields an 18% overestimate of the density and poor structural results. The TIPS2 and TIP4P potentials yield oxygen–oxygen partial structure functions in good agreement with the...
**Why read:** This paper provides a foundational comparison of intermolecular potential functions like TIP3P and TIP4P for simulating liquid water, establishing core models used in computational chemistry.

### 2. The Strength of Weak Ties
**Authors:** Mark Granovetter
**Year:** 1973 | **Citations (OpenAlex):** 38201
**URL:** https://doi.org/10.1086/225469
**Abstract:** Analysis of social networks is suggested as a tool for linking micro and macro levels of sociological theory. The procedure is illustrated by elaboration of the macro implications of one aspect of small-scale interaction: the strength of dyadic ties. It is argued that the degree of overlap of two individuals' friendship networks varies directly with the strength of their tie to one another. The impact of this principle on diffusion of influence and information, mobility opportunity, and community organization is explored. Stress is laid on the cohesive power of weak ties. Most network models deal, implicitly, with strong ties, thus confining their applicability to small, well-defined grou...
**Why read:** This work introduces the concept of 'weak ties' in social network analysis, linking micro-level interactions to macro-level sociological structures and influencing diffusion theories.

### 3. User Acceptance of Information Technology: Toward A Unified View1
**Authors:** Venkatesh, Michael G. Morris, Gordon B. Davis et al.
**Year:** 2003 | **Citations (OpenAlex):** 41447
**URL:** https://doi.org/10.2307/30036540
**Abstract:** Information technology (IT) acceptance research has yielded many competing models, each with different sets of acceptance determinants. In this paper, we (1) review user acceptance literature and discuss eight prominent models, (2) empirically compare the eight models and their extensions, (3) formulate a unified model that integrates elements across the eight models, and (4) empirically validate the unified model. The eight models reviewed are the theory of reasoned action, the technology acceptance model, the motivational model, the theory of planned behavior, a model combining the technology acceptance model and the theory of planned behavior, the model of PC utilization, the innovatio...
**Why read:** This study unifies eight competing models of user acceptance of information technology into a single validated framework, providing a comprehensive theoretical basis for IT adoption.

## Core Algorithms

### 4. Denoising Diffusion Probabilistic Models
**Authors:** Yan, Steven
**Year:** 2020 | **Citations (OpenAlex):** 5604
**URL:** http://arxiv.org/abs/2006.11239
**Abstract:** DiffuCpG 1. Introduction In this study, we used a generative AI diffusion model to address missing methylation data. We trained the model with Whole-Genome Bisulfite Sequencing data from 26 acute myeloid leukemia samples and validated it with Reduced Representation Bisulfite Sequencing data from 93 myelodysplastic syndrome and 13 normal samples. Additional testing included data from the Illumina 450k methylation array and Single-Cell Reduced Representation Bisulfite Sequencing on HepG2 cells. Our model, DiffuCpG, outperformed previous methods by integrating a broader range of genomic features, utilizing both short- and long-range interactions without increasing input complexity. It demons...
**Why read:** This paper introduces DiffuCpG, a generative AI diffusion model designed to address missing methylation data, demonstrating superior accuracy across various genomic technologies.

### 5. Palette: Image-to-Image Diffusion Models
**Authors:** Chitwan Saharia, William Chan, Huiwen Chang et al.
**Year:** 2022 | **Citations (OpenAlex):** 1460
**URL:** https://doi.org/10.1145/3528233.3530757
**Abstract:** This paper develops a unified framework for image-to-image translation based on conditional diffusion models and evaluates this framework on four challenging image-to-image translation tasks, namely colorization, inpainting, uncropping, and JPEG restoration. Our simple implementation of image-to-image diffusion models outperforms strong GAN and regression baselines on all tasks, without task-specific hyper-parameter tuning, architecture customization, or any auxiliary loss or sophisticated new techniques needed. We uncover the impact of an L2 vs. L1 loss in the denoising diffusion objective on sample diversity, and demonstrate the importance of self-attention in the neural architecture th...
**Why read:** This paper presents a unified framework for image-to-image translation using conditional diffusion models, outperforming GANs on tasks like colorization and inpainting without task-specific tuning.

### 6. Image Super-Resolution Via Iterative Refinement
**Authors:** Chitwan Saharia, Jonathan Ho, William Chan et al.
**Year:** 2022 | **Citations (OpenAlex):** 1615
**URL:** https://doi.org/10.1109/tpami.2022.3204461
**Abstract:** We present SR3, an approach to image Super-Resolution via Repeated Refinement. SR3 adapts denoising diffusion probabilistic models (Ho et al. 2020), (Sohl-Dickstein et al. 2015) to image-to-image translation, and performs super-resolution through a stochastic iterative denoising process. Output images are initialized with pure Gaussian noise and iteratively refined using a U-Net architecture that is trained on denoising at various noise levels, conditioned on a low-resolution input image. SR3 exhibits strong performance on super-resolution tasks at different magnification factors, on faces and natural images. We conduct human evaluation on a standard 8× face super-resolution task on Celeb...
**Why read:** This paper proposes SR3, an image super-resolution method using denoising diffusion probabilistic models, achieving photo-realistic outputs through iterative refinement.

## Key Developments

### 7. Diffusion Models in Vision: A Survey
**Authors:** Florinel-Alin Croitoru, Vlad Hondru, Radu Tudor Ionescu et al.
**Year:** 2023 | **Citations (OpenAlex):** 1539
**URL:** https://doi.org/10.1109/tpami.2023.3261988
**Abstract:** Denoising diffusion models represent a recent emerging topic in computer vision, demonstrating remarkable results in the area of generative modeling. A diffusion model is a deep generative model that is based on two stages, a forward diffusion stage and a reverse diffusion stage. In the forward diffusion stage, the input data is gradually perturbed over several steps by adding Gaussian noise. In the reverse stage, a model is tasked at recovering the original input data by learning to gradually reverse the diffusion process, step by step. Diffusion models are widely appreciated for the quality and diversity of the generated samples, despite their known computational burdens, i.e., low spee...
**Why read:** This survey offers a comprehensive review of denoising diffusion models in computer vision, covering theoretical foundations and applications in generative modeling.

### 8. High-Resolution Image Synthesis with Latent Diffusion Models
**Authors:** Robin Rombach, Andreas Blattmann, Dominik Lorenz et al.
**Year:** 2021 | **Citations:** 13113
**URL:** https://arxiv.org/abs/2112.10752v2
**Abstract:** By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast t...
**Why read:** This paper introduces Latent Diffusion Models, which operate in the latent space of pretrained autoencoders to enable high-resolution image synthesis with reduced computational cost.

### 9. Score-Based Generative Modeling through Stochastic Differential Equations
**Authors:** Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma et al.
**Year:** 2020 | **Citations:** 1270
**URL:** https://arxiv.org/abs/2011.13456v2
**Abstract:** Creating noise from data is easy; creating data from noise is generative modeling. We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a corresponding reverse-time SDE that transforms the prior distribution back into the data distribution by slowly removing the noise. Crucially, the reverse-time SDE depends only on the time-dependent gradient field (\aka, score) of the perturbed data distribution. By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples. We show th...
**Why read:** This work formulates generative modeling through stochastic differential equations, unifying score-based and diffusion probabilistic models to enable new sampling procedures.

### 10. Balanced conic rectified flow
**Authors:** Shin Seong Kim, Mingi Kwon, Jaeseok Jeong et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 3
**URL:** https://arxiv.org/abs/2510.25229v1
**Abstract:** Rectified flow is a generative model that learns smooth transport mappings between two distributions through an ordinary differential equation (ODE). Unlike diffusion-based generative models, which require costly numerical integration of a generative ODE to sample images with state-of-the-art quality, rectified flow uses an iterative process called reflow to learn smooth and straight ODE paths. This allows for relatively simple and efficient generation of high-quality images. However, rectified flow still faces several challenges. 1) The reflow process requires a large number of generative pairs to preserve the target distribution, leading to significant computational costs. 2) Since the...
**Why read:** This paper proposes Balanced Conic Rectified Flow, a generative model that learns smooth transport mappings via ODEs to improve efficiency and reduce bias in image generation.

### 11. UNIT-DDPM: UNpaired Image Translation with Denoising Diffusion Probabilistic Models
**Authors:** Hiroshi Sasaki, Chris G. Willcocks, Toby P. Breckon
**Year:** 2021 | **Citations (Semantic Scholar):** 206
**URL:** https://arxiv.org/abs/2104.05358v1
**Abstract:** We propose a novel unpaired image-to-image translation method that uses denoising diffusion probabilistic models without requiring adversarial training. Our method, UNpaired Image Translation with Denoising Diffusion Probabilistic Models (UNIT-DDPM), trains a generative model to infer the joint distribution of images over both domains as a Markov chain by minimising a denoising score matching objective conditioned on the other domain. In particular, we update both domain translation models simultaneously, and we generate target domain images by a denoising Markov Chain Monte Carlo approach that is conditioned on the input source domain images, based on Langevin dynamics. Our approach prov...
**Why read:** This paper presents UNIT-DDPM, a method for unpaired image-to-image translation using denoising diffusion probabilistic models without adversarial training.

## Recent Frontier

### 12. Unrestrained Simplex Denoising for Discrete Data. A Non-Markovian Approach Applied to Graph Generation
**Authors:** Yoann Boget, Alexandros Kalousis
**Year:** 2026 | **Citations (Semantic Scholar):** 1
**URL:** https://arxiv.org/abs/2603.28572v1
**Abstract:** Denoising models such as Diffusion or Flow Matching have recently advanced generative modeling for discrete structures, yet most approaches either operate directly in the discrete state space, causing abrupt state changes. We introduce simplex denoising, a simple yet effective generative framework that operates on the probability simplex. The key idea is a non-Markovian noising scheme in which, for a given clean data point, noisy representations at different times are conditionally independent. While preserving the theoretical guarantees of denoising-based generative models, our method removes unnecessary constraints, thereby improving performance and simplifying the formulation. Empirica...
**Why read:** This paper introduces unrestrained simplex denoising, a non-Markovian framework for discrete data generation that outperforms baselines on graph benchmarks.

### 13. Riemannian Denoising Diffusion Probabilistic Models
**Authors:** Zichen Liu, Wei Zhang, Christof Schütte et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 5
**URL:** https://arxiv.org/abs/2505.04338v2
**Abstract:** We propose Riemannian Denoising Diffusion Probabilistic Models (RDDPMs) for learning distributions on submanifolds of Euclidean space that are level sets of functions, including most of the manifolds relevant to applications. Existing methods for generative modeling on manifolds rely on substantial geometric information such as geodesic curves or eigenfunctions of the Laplace-Beltrami operator and, as a result, they are limited to manifolds where such information is available. In contrast, our method, built on a projection scheme, can be applied to more general manifolds, as it only requires being able to evaluate the value and the first order derivatives of the function that defines the...
**Why read:** This paper proposes Riemannian Denoising Diffusion Probabilistic Models (RDDPMs) for learning distributions on submanifolds, requiring only function evaluations rather than extensive geometric information.

---

## Research Graph Statistics

- **Communities detected:** 6
- **Community sizes:** [11, 4, 13, 1, 1, 1]

**Top papers by PageRank:**
- Denoising Diffusion Probabilistic Models (PR: 0.0555, 2020)
- Palette: Image-to-Image Diffusion Models (PR: 0.0555, 2022)
- Image Super-Resolution Via Iterative Refinement (PR: 0.0390, 2022)

**Top bridge papers:**
- Diffusion Models in Vision: A Survey (BC: 0.3632)
- Score-Based Generative Modeling through Stochastic Differential Equations (BC: 0.0943)
- Image Super-Resolution Via Iterative Refinement (BC: 0.0920)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"