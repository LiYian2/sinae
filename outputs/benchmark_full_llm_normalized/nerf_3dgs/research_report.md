# ResearchTrail: Literature Reading Path Report

**Topic:** Neural Radiance Fields and 3D Gaussian Splatting
**Level:** intermediate
**Goal:** benchmark_research_trail
**Preferred Length:** 12 papers

---

## Corpus Summary

- Papers: 26
- Abstract coverage: 100.0%
- Citation/reference coverage: 80.8%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2020-2024
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 26
- Edges: 215
- Citation edges: 4
- Similarity edges: 214
- Communities: 3
- Modularity: 0.2196
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Foundational Neural Radiance Fields** — This community focuses on the core Neural Radiance Fields (NeRF) method for view synthesis and scene representation, including foundational papers and multi-modal extensions like VIRUS-NeRF.
- **Community 1: Advanced NeRF Variants and Anti-Aliasing** — Research in this group improves upon the original NeRF model, emphasizing multiscale representations, anti-aliasing, and unbounded scene rendering through works such as Mip-NeRF and Zip-NeRF.
- **Community 2: Gaussian Splatting and Explicit Representations** — This community investigates efficient radiance field rendering using explicit representations and Gaussian primitives, highlighted by developments in 3D Gaussian Splatting and Plenoxels.

## Reading Path Metrics

- Stages: 4
- Unique papers: 9
- Explanation coverage: 100.0%

## Foundations

### 1. NeRF
**Authors:** Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik et al.
**Year:** 2021 | **Citations (OpenAlex):** 5557
**URL:** https://doi.org/10.1145/3503250
**Abstract:** We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of input views. Our algorithm represents a scene using a fully connected (nonconvolutional) deep network, whose input is a single continuous 5D coordinate (spatial location ( x , y , z ) and viewing direction ( θ, ϕ )) and whose output is the volume density and view-dependent emitted radiance at that spatial location. We synthesize views by querying 5D coordinates along camera rays and use classic volume rendering techniques to project the output colors and densities into an image. Because volume rende...
**Why read:** This paper introduces the core Neural Radiance Fields (NeRF) method, which uses a continuous volumetric scene function and 5D coordinates to synthesize novel views, serving as the essential foundation for the field.

### 2. NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis
**Authors:** Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik et al.
**Year:** 2020 | **Citations:** 4642
**URL:** https://arxiv.org/abs/2003.08934v2
**Abstract:** We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of input views. Our algorithm represents a scene using a fully-connected (non-convolutional) deep network, whose input is a single continuous 5D coordinate (spatial location $(x,y,z)$ and viewing direction $(θ, φ)$) and whose output is the volume density and view-dependent emitted radiance at that spatial location. We synthesize views by querying 5D coordinates along camera rays and use classic volume rendering techniques to project the output colors and densities into an image. Because volume renderin...
**Why read:** This is the original NeRF paper that established the method for optimizing a continuous volumetric scene function using sparse input views and differentiable volume rendering.

### 3. Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields
**Authors:** Jonathan T. Barron, Ben Mildenhall, Matthew Tancik et al.
**Year:** 2021 | **Citations (Semantic Scholar):** 2692
**URL:** https://arxiv.org/abs/2103.13415v3
**Abstract:** The rendering procedure used by neural radiance fields (NeRF) samples a scene with a single ray per pixel and may therefore produce renderings that are excessively blurred or aliased when training or testing images observe scene content at different resolutions. The straightforward solution of supersampling by rendering with multiple rays per pixel is impractical for NeRF, because rendering each ray requires querying a multilayer perceptron hundreds of times. Our solution, which we call "mip-NeRF" (a la "mipmap"), extends NeRF to represent the scene at a continuously-valued scale. By efficiently rendering anti-aliased conical frustums instead of rays, mip-NeRF reduces objectionable aliasi...
**Why read:** This paper addresses aliasing and blurring artifacts in the original NeRF by introducing a multiscale representation (mip-NeRF) that efficiently renders anti-aliased conical frustums.

## Core Algorithms

### 4. 2D Gaussian Splatting for Geometrically Accurate Radiance Fields
**Authors:** Binbin Huang, Zehao Yu, Anpei Chen et al.
**Year:** 2024 | **Citations (OpenAlex):** 412
**URL:** https://doi.org/10.1145/3641519.3657428
**Abstract:** 3D Gaussian Splatting (3DGS) has recently revolutionized radiance field reconstruction, achieving high quality novel view synthesis and fast rendering speed. However, 3DGS fails to accurately represent surfaces due to the multi-view inconsistent nature of 3D Gaussians. We present 2D Gaussian Splatting (2DGS), a novel approach to model and reconstruct geometrically accurate radiance fields from multi-view images. Our key idea is to collapse the 3D volume into a set of 2D oriented planar Gaussian disks. Unlike 3D Gaussians, 2D Gaussians provide view-consistent geometry while modeling surfaces intrinsically. To accurately recover thin surfaces and achieve stable optimization, we introduce a...
**Why read:** This paper introduces 2D Gaussian Splatting (2DGS), which collapses 3D volumes into 2D oriented planar disks to achieve geometrically accurate radiance fields and view-consistent surfaces.

## Key Developments

### 5. 3D Gaussian Splatting for Real-Time Radiance Field Rendering
**Authors:** Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler et al.
**Year:** 2023 | **Citations:** 4143
**URL:** https://arxiv.org/abs/2308.04079v1
**Abstract:** Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= 30 fps) novel-view synthesis at 1080p resolution. First, starti...
**Why read:** This paper presents 3D Gaussian Splatting (3DGS), a key development that achieves real-time radiance field rendering at 1080p resolution by representing scenes with 3D Gaussians.

### 6. Instant Neural Graphics Primitives with a Multiresolution Hash Encoding
**Authors:** Thomas Müller, Alex Evans, Christoph Schied et al.
**Year:** 2022 | **Citations (Semantic Scholar):** 5679
**URL:** https://arxiv.org/abs/2201.05989v2
**Abstract:** Neural graphics primitives, parameterized by fully connected neural networks, can be costly to train and evaluate. We reduce this cost with a versatile new input encoding that permits the use of a smaller network without sacrificing quality, thus significantly reducing the number of floating point and memory access operations: a small neural network is augmented by a multiresolution hash table of trainable feature vectors whose values are optimized through stochastic gradient descent. The multiresolution structure allows the network to disambiguate hash collisions, making for a simple architecture that is trivial to parallelize on modern GPUs. We leverage this parallelism by implementing...
**Why read:** This paper introduces a multiresolution hash encoding that significantly reduces the computational cost of neural graphics primitives, enabling faster training and evaluation.

### 7. NeRF: Neural Radiance Field in 3D Vision: A Comprehensive Review (Updated Post-Gaussian Splatting)
**Authors:** Kyle Gao, Yina Gao, Hongjie He et al.
**Year:** 2022 | **Citations (Semantic Scholar):** 295
**URL:** https://arxiv.org/abs/2210.00379v8
**Abstract:** In March 2020, Neural Radiance Field (NeRF) revolutionized Computer Vision, allowing for implicit, neural network-based scene representation and novel view synthesis. NeRF models have found diverse applications in robotics, urban mapping, autonomous navigation, virtual reality/augmented reality, and more. In August 2023, Gaussian Splatting, a direct competitor to the NeRF-based framework, was proposed, gaining tremendous momentum and overtaking NeRF-based research in terms of interest as the dominant framework for novel view synthesis. We present a comprehensive survey of NeRF papers from the past five years (2020-2025). These include papers from the pre-Gaussian Splatting era, where NeRF...
**Why read:** This comprehensive review surveys NeRF developments from 2020-2025, covering both the pre-Gaussian Splatting era and the shift towards hybrid representations.

## Recent Frontier

### 8. Recent advances in 3D Gaussian splatting
**Authors:** Tong Wu, Yu-Jie Yuan, Lingxiao Zhang et al.
**Year:** 2024 | **Citations (OpenAlex):** 174
**URL:** https://doi.org/10.1007/s41095-024-0436-y
**Abstract:** The emergence of 3D Gaussian splatting (3DGS) has greatly accelerated rendering in novel view synthesis. Unlike neural implicit representations like neural radiance fields (NeRFs) that represent a 3D scene with position and viewpoint-conditioned neural networks, 3D Gaussian splatting utilizes a set of Gaussian ellipsoids to model the scene so that efficient rendering can be accomplished by rasterizing Gaussian ellipsoids into images. Apart from fast rendering, the explicit representation of 3D Gaussian splatting also facilitates downstream tasks like dynamic reconstruction, geometry editing, and physical simulation. Considering the rapid changes and growing number of works in this field,...
**Why read:** This review covers recent advances in 3D Gaussian splatting, classifying methods into reconstruction, editing, and downstream applications to reflect the current state of the field.

### 9. Identifying Unnecessary 3D Gaussians using Clustering for Fast Rendering of 3D Gaussian Splatting
**Authors:** Joongho Jo, Hyeongwon Kim, Jongsun Park
**Year:** 2024 | **Citations (Semantic Scholar):** 9
**URL:** https://arxiv.org/abs/2402.13827v2
**Abstract:** 3D Gaussian splatting (3D-GS) is a new rendering approach that outperforms the neural radiance field (NeRF) in terms of both speed and image quality. 3D-GS represents 3D scenes by utilizing millions of 3D Gaussians and projects these Gaussians onto the 2D image plane for rendering. However, during the rendering process, a substantial number of unnecessary 3D Gaussians exist for the current view direction, resulting in significant computation costs associated with their identification. In this paper, we propose a computational reduction technique that quickly identifies unnecessary 3D Gaussians in real-time for rendering the current view without compromising image quality. This is accompli...
**Why read:** This frontier paper proposes a computational reduction technique for 3D Gaussian Splatting that uses offline clustering to identify and remove unnecessary Gaussians for faster real-time rendering.

---

## Research Graph Statistics

- **Communities detected:** 3
- **Community sizes:** [3, 14, 9]

**Top papers by PageRank:**
- NeRF (PR: 0.1418, 2021)
- 2D Gaussian Splatting for Geometrically Accurate Radiance Fields (PR: 0.0614, 2024)
- NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis (PR: 0.0332, 2020)

**Top bridge papers:**
- NeRF: Neural Radiance Field in 3D Vision: A Comprehensive Review (Updated Post-Gaussian Splatting) (BC: 0.1300)
- 3D Gaussian Splatting for Real-Time Radiance Field Rendering (BC: 0.1133)
- NeRF (BC: 0.0633)

---

## Follow-up Questions You Can Ask

- "Show bridge papers between key communities"
- "Generate a 7-day reading plan"
- "Show only papers after 2020"
- "Which authors should I follow?"
- "Replace theoretical papers with more applied papers"
- "Explain why these papers are foundational"
- "Show me the citation network visualization"