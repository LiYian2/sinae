# Literature Retrieval Skill Report: Vision Transformer

## Functionality

This Skill turns a natural-language research topic into a structured academic corpus. It combines LLM or rule-based query planning with deterministic arXiv/OpenAlex retrieval, title deduplication, topic-specific filtering, and metadata enrichment.

## Inputs and Outputs

- Inputs: topic, user level, time range, maximum papers, optional query plan.
- Outputs: paper corpus, source URLs, abstracts, citation counts with source labels, reference lists, corpus quality metrics, and query-plan metadata.

## Quantitative Results

| Run | Planner | Papers | Abstract Coverage | Citation/Reference Coverage | Year Range | Dedup Removed | Main Queries |
|---|---|---:|---:|---:|---|---:|---:|
| rule_only_agent | rule | 84 | 98.8% | 77.4% | 2012-2026 | 0 | 12 |
| llm_assisted_agent | llm | 84 | 98.8% | 77.4% | 2012-2026 | 0 | 12 |

## LLM Query Plan

- Main queries: Vision Transformer, "Vision Transformer", "An Image is Worth 16x16 Words", DeiT data-efficient image transformers, Swin Transformer hierarchical vision transformer, DINO self-supervised vision transformers, Masked Autoencoders scalable vision learners, BEiT masked image modeling transformer, Vision Transformer survey, Vision Transformer tutorial, Vision Transformer overview, Vision Transformer foundations
- Prerequisite queries: N/A
- Exclude terms: N/A
- Expected communities: N/A

## Analysis

- The key measurable outputs are corpus size, abstract coverage, citation/reference coverage, and year range.
- Topic-specific filtering is important for ambiguous terms and short acronyms. CFR retrieval filters out unrelated uses of `regret` and `counterfactual`; Vision Transformer retrieval uses word-boundary matching for acronyms such as `ViT`, `DeiT`, `DINO`, `MAE`, and `BEiT` to avoid unrelated high-citation OpenAlex records.
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata. They may still differ from Google Scholar snapshots.
