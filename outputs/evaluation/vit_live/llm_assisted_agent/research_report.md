# ResearchTrail: Literature Reading Path Report

**Topic:** Vision Transformer
**Level:** beginner
**Goal:** Deeply understand Vision Transformer
**Preferred Length:** 10 papers

---

## Corpus Summary

- Papers: 84
- Abstract coverage: 98.8%
- Citation/reference coverage: 77.4%
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata.
- Year range: 2012-2026
- Deduplicated records: 0

## Field Map Metrics

- Nodes: 84
- Edges: 829
- Citation edges: 119
- Similarity edges: 785
- Communities: 5
- Modularity: 0.2554
- Largest component ratio: 100.0%

## Detected Research Communities

- **Community 0: Transformer / Vision / Tasks / Image** — Community 0 groups papers around transformer, vision, tasks, image.
- **Community 1: Code / Vision / Transformer / Image** — Community 1 groups papers around code, vision, transformer, image.
- **Community 2: Vision / Transformer / Transformers / Image** — Community 2 groups papers around vision, transformer, transformers, image.
- **Community 3: Vision / Transformers / Image / Transformer** — Community 3 groups papers around vision, transformers, image, transformer.
- **Community 4: Segmentation / Transformer / Vision / Self-Supervised** — Community 4 groups papers around segmentation, transformer, vision, self-supervised.

## Reading Path Metrics

- Stages: 5
- Unique papers: 14
- Explanation coverage: 100.0%

## Prerequisites

### 1. Attention Is All You Need
**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar et al.
**Year:** 2017 | **Citations (curated metadata):** 145000
**URL:** https://arxiv.org/abs/1706.03762
**Abstract:** This paper introduces the Transformer architecture based solely on attention mechanisms. It provides the self-attention foundation needed to understand how Vision Transformer models process image patches as token sequences.
**Why read:** This paper introduces the Transformer architecture based solely on attention mechanisms, providing the self-attention foundation needed to understand how Vision Transformer models process image patches as token sequences.

### 2. Deep Residual Learning for Image Recognition
**Authors:** Kaiming He, Xiangyu Zhang, Shaoqing Ren et al.
**Year:** 2016 | **Citations (curated metadata):** 210000
**URL:** https://arxiv.org/abs/1512.03385
**Abstract:** ResNet established deep residual CNN backbones for image recognition. It is a useful prerequisite because many Vision Transformer papers compare against, hybridize with, or replace convolutional visual backbones.
**Why read:** ResNet established deep residual CNN backbones for image recognition and is a useful prerequisite because many Vision Transformer papers compare against, hybridize with, or replace convolutional visual backbones.

### 3. ImageNet Classification with Deep Convolutional Neural Networks
**Authors:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
**Year:** 2012 | **Citations (curated metadata):** 180000
**URL:** https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
**Abstract:** AlexNet marks the modern deep learning breakthrough for ImageNet classification. It gives beginners the benchmark and CNN context that Vision Transformer papers use to position their contributions.
**Why read:** AlexNet marks the modern deep learning breakthrough for ImageNet classification, giving beginners the benchmark and CNN context that Vision Transformer papers use to position their contributions.

## Conceptual Foundations

### 4. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
**Authors:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov et al.
**Year:** 2020 | **Citations (curated metadata):** 38000
**URL:** http://arxiv.org/abs/2010.11929
**Abstract:** While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transfor...
**Why read:** This paper demonstrates that a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks, establishing the Vision Transformer (ViT) as a conceptual foundation.

## Core Methods

### 5. Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
**Authors:** Ze Liu, Yutong Lin, Yue Cao et al.
**Year:** 2021 | **Citations (OpenAlex):** 29208
**URL:** https://doi.org/10.1109/iccv48922.2021.00986
**Abstract:** This paper presents a new vision Transformer, called Swin Transformer, that capably serves as a general-purpose backbone for computer vision. Challenges in adapting Transformer from language to vision arise from differences between the two domains, such as large variations in the scale of visual entities and the high resolution of pixels in images compared to words in text. To address these differences, we propose a hierarchical Transformer whose representation is computed with Shifted windows. The shifted windowing scheme brings greater efficiency by limiting self-attention computation to non-overlapping local windows while also allowing for cross-window connection. This hierarchical arc...
**Why read:** This paper presents Swin Transformer, a hierarchical vision Transformer using shifted windows that serves as a general-purpose backbone and addresses challenges like scale variation and high resolution.

### 6. Emerging Properties in Self-Supervised Vision Transformers
**Authors:** Mathilde Caron, Hugo Touvron, Ishan Misra et al.
**Year:** 2021 | **Citations (OpenAlex):** 4853
**URL:** https://doi.org/10.1109/iccv48922.2021.00951
**Abstract:** In this paper, we question if self-supervised learning provides new properties to Vision Transformer (ViT) [16] that stand out compared to convolutional networks (convnets). Beyond the fact that adapting self-supervised methods to this architecture works particularly well, we make the following observations: first, self-supervised ViT features contain explicit information about the semantic segmentation of an image, which does not emerge as clearly with supervised ViTs, nor with convnets. Second, these features are also excellent k-NN classifiers, reaching 78.3% top-1 on ImageNet with a small ViT. Our study also underlines the importance of momentum encoder [26], multi-crop training [9],...
**Why read:** This paper introduces DINO, a self-supervised method for Vision Transformers that reveals emerging properties like explicit semantic segmentation information and excellent k-NN classification capabilities.

## Key Developments

### 7. BEiT: BERT Pre-Training of Image Transformers
**Authors:** Hangbo Bao, Dong Li, Piao, Songhao et al.
**Year:** 2021 | **Citations (OpenAlex):** 924
**URL:** http://arxiv.org/abs/2106.08254
**Abstract:** We introduce a self-supervised vision representation model BEiT, which stands for Bidirectional Encoder representation from Image Transformers. Following BERT developed in the natural language processing area, we propose a masked image modeling task to pretrain vision Transformers. Specifically, each image has two views in our pre-training, i.e, image patches (such as 16x16 pixels), and visual tokens (i.e., discrete tokens). We first "tokenize" the original image into visual tokens. Then we randomly mask some image patches and fed them into the backbone Transformer. The pre-training objective is to recover the original visual tokens based on the corrupted image patches. After pre-training...
**Why read:** This paper introduces BEiT, a self-supervised vision representation model that uses a masked image modeling task to pretrain vision Transformers, following the BERT approach from NLP.

### 8. Masked Autoencoders Are Scalable Vision Learners
**Authors:** Kaiming He, Xinlei Chen, Saining Xie et al.
**Year:** 2022 | **Citations (curated metadata):** 16000
**URL:** https://arxiv.org/abs/2111.06377
**Abstract:** MAE introduces a simple masked autoencoding pretraining strategy for scalable vision transformer learning, becoming a major self-supervised pretraining direction for ViT backbones.
**Why read:** MAE introduces a simple masked autoencoding pretraining strategy for scalable vision transformer learning, becoming a major self-supervised pretraining direction for ViT backbones.

### 9. Training data-efficient image transformers and distillation through attention
**Authors:** Hugo Touvron, Matthieu Cord, Matthijs Douze et al.
**Year:** 2021 | **Citations (curated metadata):** 12000
**URL:** https://arxiv.org/abs/2012.12877
**Abstract:** DeiT studies how to train Vision Transformers efficiently on ImageNet without massive external datasets. It introduces a distillation strategy that made ViT-style architectures more practical for standard vision benchmarks.
**Why read:** DeiT studies how to train Vision Transformers efficiently on ImageNet without massive external datasets, introducing a distillation strategy that made ViT-style architectures more practical.

### 10. Learning Transferable Visual Models From Natural Language Supervision
**Authors:** Alec Radford, Jong Wook Kim, Chris Hallacy et al.
**Year:** 2021 | **Citations (curated metadata):** 35000
**URL:** https://arxiv.org/abs/2103.00020
**Abstract:** CLIP connects visual representation learning with natural language supervision at scale. In a ViT reading path, it represents the vision-language branch that often uses ViT backbones.
**Why read:** CLIP connects visual representation learning with natural language supervision at scale, representing the vision-language branch that often uses ViT backbones.

### 11. Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions
**Authors:** Wenhai Wang, Enze Xie, Xiang Li et al.
**Year:** 2021 | **Citations (curated metadata):** 6500
**URL:** https://arxiv.org/abs/2102.12122
**Abstract:** Pyramid Vision Transformer builds a progressive pyramid structure for transformer-based vision backbones, connecting ViT-style models to dense prediction tasks that require multi-scale features.
**Why read:** Pyramid Vision Transformer builds a progressive pyramid structure for transformer-based vision backbones, connecting ViT-style models to dense prediction tasks that require multi-scale features.

## Recent Advances

### 12. Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion
**Authors:** Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis et al.
**Year:** 2026 | **Citations:** 0
**URL:** https://arxiv.org/abs/2604.01761v1
**Abstract:** Video models have recently been applied with success to problems in content generation, novel view synthesis, and, more broadly, world simulation. Many applications in generation and transfer rely on conditioning these models, typically through perceptual, geometric, or simple semantic signals, fundamentally using them as generative renderers. At the same time, high-dimensional features obtained from large-scale self-supervised learning on images or point clouds are increasingly used as a general-purpose interface for vision models. The connection between the two has been explored for subject specific editing, aligning and training video diffusion models, but not in the role of a more gen...
**Why read:** This paper explores using high-dimensional features from self-supervised learning like DINO as conditioning signals for pretrained video diffusion models in content generation.

### 13. Unlocking Generalization in Polyp Segmentation with DINO Self-Attention "keys"
**Authors:** Carla Monteiro, Valentina Corbetta, Regina Beets-Tan et al.
**Year:** 2025 | **Citations (Semantic Scholar):** 0
**URL:** https://arxiv.org/abs/2512.13376v2
**Abstract:** Automatic polyp segmentation is crucial for improving the clinical identification of colorectal cancer (CRC). While Deep Learning (DL) techniques have been extensively researched for this problem, current methods frequently struggle with generalization, particularly in data-constrained or challenging settings. Moreover, many existing polyp segmentation methods rely on complex, task-specific architectures. To address these limitations, we present a framework that leverages the intrinsic robustness of DINO self-attention "key" features for robust segmentation. Unlike traditional methods that extract tokens from the deepest layers of the Vision Transformer (ViT), our approach leverages the k...
**Why read:** This paper presents a framework leveraging the intrinsic robustness of DINO self-attention 'key' features for robust polyp segmentation, enhancing performance and generalizability.

### 14. Deep Learning for Oral Health: Benchmarking ViT, DeiT, BEiT, ConvNeXt, and Swin Transformer
**Authors:** Ajo Babu George, Sadhvik Bathini, Niranjana S R
**Year:** 2025 | **Citations:** 0
**URL:** https://arxiv.org/abs/2509.23100v1
**Abstract:** Objective: The aim of this study was to systematically evaluate and compare the performance of five state-of-the-art transformer-based architectures - Vision Transformer (ViT), Data-efficient Image Transformer (DeiT), ConvNeXt, Swin Transformer, and Bidirectional Encoder Representation from Image Transformers (BEiT) - for multi-class dental disease classification. The study specifically focused on addressing real-world challenges such as data imbalance, which is often overlooked in existing literature. Study Design: The Oral Diseases dataset was used to train and validate the selected models. Performance metrics, including validation accuracy, precision, recall, and F1-score, were measure...
**Why read:** This study benchmarks state-of-the-art transformer-based architectures including ViT, DeiT, BEiT, and Swin Transformer for multi-class dental disease classification, addressing real-world data imbalance.

---

## Research Graph Statistics

- **Communities detected:** 5
- **Community sizes:** [36, 16, 13, 9, 10]

**Top papers by PageRank:**
- An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (PR: 0.0536, 2020)
- Swin Transformer: Hierarchical Vision Transformer using Shifted Windows (PR: 0.0388, 2021)
- Emerging Properties in Self-Supervised Vision Transformers (PR: 0.0305, 2021)

**Top bridge papers:**
- Towards End-to-End Image Compression and Analysis with Transformers (BC: 0.0579)
- Emerging Properties in Self-Supervised Vision Transformers (BC: 0.0514)
- An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (BC: 0.0502)

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