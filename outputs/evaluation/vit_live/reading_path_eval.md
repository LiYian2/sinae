# Reading Path and Report Skill Report: Vision Transformer

## Functionality

This Skill converts graph scores and community labels into a staged reading path. It generates evidence packets and asks the LLM for concise why-read explanations grounded in title, abstract, URL, stage, community, and graph scores.

## Reading Path Metrics

| Run | Stages | Unique Papers | Explanation Coverage | Role Counts |
|---|---:|---:|---:|---|
| rule_only_agent | 5 | 14 | 100.0% | {"prerequisite": 3, "foundation": 1, "core": 2, "development": 5, "frontier": 3} |
| llm_assisted_agent | 5 | 14 | 100.0% | {"prerequisite": 3, "foundation": 1, "core": 2, "development": 5, "frontier": 3} |

## Network-Aware Reading Path

### Prerequisites
- 1. Attention Is All You Need — This paper introduces the Transformer architecture based solely on attention mechanisms, providing the self-attention foundation needed to understand how Vision Transformer models process image patches as token sequences.
- 2. Deep Residual Learning for Image Recognition — ResNet established deep residual CNN backbones for image recognition and is a useful prerequisite because many Vision Transformer papers compare against, hybridize with, or replace convolutional visual backbones.
- 3. ImageNet Classification with Deep Convolutional Neural Networks — AlexNet marks the modern deep learning breakthrough for ImageNet classification, giving beginners the benchmark and CNN context that Vision Transformer papers use to position their contributions.

### Conceptual Foundations
- 4. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale — This paper demonstrates that a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks, establishing the Vision Transformer (ViT) as a conceptual foundation.

### Core Methods
- 5. Swin Transformer: Hierarchical Vision Transformer using Shifted Windows — This paper presents Swin Transformer, a hierarchical vision Transformer using shifted windows that serves as a general-purpose backbone and addresses challenges like scale variation and high resolution.
- 6. Emerging Properties in Self-Supervised Vision Transformers — This paper introduces DINO, a self-supervised method for Vision Transformers that reveals emerging properties like explicit semantic segmentation information and excellent k-NN classification capabilities.

### Key Developments
- 7. BEiT: BERT Pre-Training of Image Transformers — This paper introduces BEiT, a self-supervised vision representation model that uses a masked image modeling task to pretrain vision Transformers, following the BERT approach from NLP.
- 8. Masked Autoencoders Are Scalable Vision Learners — MAE introduces a simple masked autoencoding pretraining strategy for scalable vision transformer learning, becoming a major self-supervised pretraining direction for ViT backbones.
- 9. Training data-efficient image transformers and distillation through attention — DeiT studies how to train Vision Transformers efficiently on ImageNet without massive external datasets, introducing a distillation strategy that made ViT-style architectures more practical.
- 10. Learning Transferable Visual Models From Natural Language Supervision — CLIP connects visual representation learning with natural language supervision at scale, representing the vision-language branch that often uses ViT backbones.
- 11. Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions — Pyramid Vision Transformer builds a progressive pyramid structure for transformer-based vision backbones, connecting ViT-style models to dense prediction tasks that require multi-scale features.

### Recent Advances
- 12. Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion — This paper explores using high-dimensional features from self-supervised learning like DINO as conditioning signals for pretrained video diffusion models in content generation.
- 13. Unlocking Generalization in Polyp Segmentation with DINO Self-Attention "keys" — This paper presents a framework leveraging the intrinsic robustness of DINO self-attention 'key' features for robust polyp segmentation, enhancing performance and generalizability.
- 14. Deep Learning for Oral Health: Benchmarking ViT, DeiT, BEiT, ConvNeXt, and Swin Transformer — This study benchmarks state-of-the-art transformer-based architectures including ViT, DeiT, BEiT, and Swin Transformer for multi-class dental disease classification, addressing real-world data imbalance.

## Citation-Count Baseline

This baseline ranks papers only by citation count and ignores learning stage, community coverage, and bridge/frontier roles.

1. Deep Residual Learning for Image Recognition (2016, curated citations: 210000)
2. ImageNet Classification with Deep Convolutional Neural Networks (2012, curated citations: 180000)
3. Attention Is All You Need (2017, curated citations: 145000)
4. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (2020, curated citations: 38000)
5. Learning Transferable Visual Models From Natural Language Supervision (2021, curated citations: 35000)
6. Swin Transformer: Hierarchical Vision Transformer using Shifted Windows (2021, OpenAlex citations: 29208)
7. Masked Autoencoders Are Scalable Vision Learners (2022, curated citations: 16000)
8. Training data-efficient image transformers and distillation through attention (2021, curated citations: 12000)
9. A ConvNet for the 2020s (2022, OpenAlex citations: 6777)
10. Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions (2021, curated citations: 6500)
11. Emerging Properties in Self-Supervised Vision Transformers (2021, OpenAlex citations: 4853)
12. SwinIR: Image Restoration Using Swin Transformer (2021, OpenAlex citations: 4084)

## Analysis

- The network-aware path separates prerequisites/foundations, core methods, key developments, bridge papers, and frontier papers.
- The citation-count baseline often over-emphasizes old or broadly cited papers and does not guarantee a coherent learning order.
- Evidence-grounded why-read text is generated from structured packets, limiting LLM freedom to invent unsupported claims.
