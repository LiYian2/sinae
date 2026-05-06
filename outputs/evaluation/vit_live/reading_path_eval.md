# Reading Path and Report Skill Report: Vision Transformer

## Functionality

This Skill converts graph scores and community labels into a staged reading path. It generates evidence packets and asks the LLM for concise why-read explanations grounded in title, abstract, URL, stage, community, and graph scores.

## Reading Path Metrics

| Run | Stages | Unique Papers | Explanation Coverage | Role Counts |
|---|---:|---:|---:|---|
| rule_only_agent | 5 | 13 | 100.0% | {"prerequisite": 3, "foundation": 1, "core": 2, "development": 4, "frontier": 3} |
| llm_assisted_agent | 5 | 13 | 100.0% | {"prerequisite": 3, "foundation": 1, "core": 1, "development": 5, "frontier": 3} |

## Path Quality Metrics

| Run | Landmark Hit Rate | Topic Precision | Ordering Quality | Community Coverage | Stage Coverage |
|---|---:|---:|---:|---:|---:|
| rule_only_agent | 100.0% | 97.6% | 100.0% | 80.0% | 100.0% |
| llm_assisted_agent | 100.0% | 96.2% | 100.0% | 83.3% | 100.0% |

## Network-Aware Reading Path

### Prerequisites
- 1. Attention Is All You Need — This paper introduces the Transformer architecture, which dispenses with recurrence and convolutions to rely solely on attention mechanisms. It is a prerequisite because it establishes the core attention mechanism that Vision Transformers later adapt for computer vision tasks.
- 2. Deep Residual Learning for Image Recognition — ResNet established deep residual CNN backbones for image recognition. It is a useful prerequisite because many Vision Transformer papers compare against, hybridize with, or replace convolutional visual backbones.
- 3. ImageNet Classification with Deep Convolutional Neural Networks — AlexNet marks the modern deep learning breakthrough for ImageNet classification. It gives beginners the benchmark and CNN context that Vision Transformer papers use to position their contributions.

### Conceptual Foundations
- 4. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale — This paper demonstrates that a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. It serves as a conceptual foundation by showing that reliance on CNNs is not necessary for vision tasks.

### Core Methods
- 5. Swin Transformer: Hierarchical Vision Transformer using Shifted Windows — This paper presents Swin Transformer, a hierarchical vision Transformer using shifted windows to address differences between language and vision domains. It is a core method because it provides a general-purpose backbone with linear computational complexity regarding image size.

### Key Developments
- 6. BEiT: BERT Pre-Training of Image Transformers — BEiT adapts masked language modeling ideas to image transformers through masked image modeling, forming an important bridge between BERT-style pretraining and ViT representation learning.
- 7. Emerging Properties in Self-Supervised Vision Transformers — This paper explores self-supervised learning properties in Vision Transformers, introducing DINO, a self-distillation method with no labels. It is a key development because it shows that self-supervised ViT features contain explicit semantic segmentation information.
- 8. Masked Autoencoders Are Scalable Vision Learners — MAE introduces a simple masked autoencoding pretraining strategy for scalable vision transformer learning, becoming a major self-supervised pretraining direction for ViT backbones.
- 9. Training data-efficient image transformers and distillation through attention — DeiT studies how to train Vision Transformers efficiently on ImageNet without massive external datasets. It introduces a distillation strategy that made ViT-style architectures more practical for standard vision benchmarks.
- 10. Learning Transferable Visual Models From Natural Language Supervision — CLIP connects visual representation learning with natural language supervision at scale. In a ViT reading path, it represents the vision-language branch that often uses ViT backbones.

### Recent Advances
- 11. Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion — This paper proposes Control-DINO, which uses features from self-supervised learning like DINO as a conditioning signal for pretrained video diffusion models. It represents a recent advance by applying ViT-derived features to controllable video generation.
- 12. Deep Learning for Oral Health: Benchmarking ViT, DeiT, BEiT, ConvNeXt, and Swin Transformer — This study benchmarks transformer-based architectures including ViT, DeiT, BEiT, and Swin Transformer for multi-class dental disease classification. It is a recent advance that evaluates these models on real-world challenges like data imbalance.
- 13. Steering CLIP's vision transformer with sparse autoencoders — This paper trains sparse autoencoders on CLIP's vision transformer to analyze its internal mechanisms and steerability. It is a recent advance that provides the first systematic analysis on steering CLIP's ViT using SAEs.

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
9. BEiT: BERT Pre-Training of Image Transformers (2021, curated citations: 7000)
10. A ConvNet for the 2020s (2022, OpenAlex citations: 6777)
11. Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions (2021, curated citations: 6500)
12. Emerging Properties in Self-Supervised Vision Transformers (2021, OpenAlex citations: 4853)

## Analysis

- The network-aware path separates prerequisites/foundations, core methods, key developments, bridge papers, and frontier papers.
- The citation-count baseline often over-emphasizes old or broadly cited papers and does not guarantee a coherent learning order.
- Evidence-grounded why-read text is generated from structured packets, limiting LLM freedom to invent unsupported claims.
- Landmark hit rate, ordering quality, and community coverage directly evaluate whether the Agent creates a useful reading path rather than only a connected graph.
