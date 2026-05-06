# Research Graph Analysis Skill Report: Vision Transformer

## Functionality

This Skill builds paper networks and computes deterministic SNA metrics. Citation edges capture explicit references when available; similarity edges use TF-IDF cosine similarity over abstracts to reduce sparsity.

## Graph Ablation Results

| Graph Mode | Nodes | Edges | Citation Edges | Similarity Edges | Components | Largest Component | Communities | Modularity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| citation | 29 | 36 | 36 | 0 | 12 | 62.1% | 15 | 0.2465 |
| similarity | 29 | 152 | 0 | 152 | 2 | 96.6% | 5 | 0.1692 |
| hybrid | 29 | 164 | 36 | 152 | 1 | 100.0% | 5 | 0.2623 |

## LLM-Labeled Communities

- **Community 0: Foundational Transformers and Attention Mechanisms** — This community explores the foundational attention mechanisms and their adaptation from machine translation to vision tasks, focusing on efficient training and pyramid architectures.
- **Community 1: General Vision Transformers and Self-Supervised Learning** — This large community focuses on the application of transformers to general image recognition and segmentation, including self-supervised pre-training methods like BEiT and architectures like ViT.
- **Community 2: Hybrid Convolutional-Transformer Architectures** — This community investigates hybrid architectures that combine convolutional designs with vision transformers to improve performance and accuracy across various image tasks.
- **Community 3: Specialized Vision Transformer Backbones** — Research in this area focuses on specialized transformer backbones such as Swin and CSWin, applying them to tasks like image restoration and video processing while exploring inductive biases.
- **Community 4: Robustness and Position Encoding in Vision Transformers** — This community examines the robustness of vision transformers against adversarial attacks, improves relative position encoding, and explores scaling up model capacity and resolution.
- **Community 5: Efficient Object Detection and Vision-Language Models** — This community focuses on efficient object detection models like YOLOv7 and adaptive token mechanisms, alongside masked vision-language transformers for scene text recognition.

## Analysis

- Citation-only graphs are precise but sparse when references are missing from APIs.
- Similarity-only graphs improve connectivity but can over-cluster papers by language rather than citation structure.
- Hybrid graphs are the default because they preserve citation evidence while adding enough semantic edges for stable community detection.
- Citation PageRank is computed on a directed citation graph where citing papers point to cited papers. Community detection uses the undirected semantic/hybrid projection.
- Betweenness centrality uses `distance = 1 / weight` so stronger similarity means shorter graph distance.
- PageRank, betweenness, Louvain communities, and role scores are deterministic and are not computed by the LLM.
