# Literature Retrieval Skill Report: Counterfactual regret minimization

## Functionality

This Skill turns a natural-language research topic into a structured academic corpus. It combines LLM or rule-based query planning with deterministic arXiv/OpenAlex retrieval, title deduplication, topic-specific filtering, and metadata enrichment.

## Inputs and Outputs

- Inputs: topic, user level, time range, maximum papers, optional query plan.
- Outputs: paper corpus, source URLs, abstracts, citation counts with source labels, reference lists, corpus quality metrics, and query-plan metadata.

## Quantitative Results

| Run | Planner | Papers | Abstract Coverage | Citation/Reference Coverage | Year Range | Dedup Removed | Main Queries |
|---|---|---:|---:|---:|---|---:|---:|
| rule_only_agent | rule | 43 | 100.0% | 69.8% | 2007-2025 | 0 | 10 |
| llm_assisted_agent | llm | 46 | 100.0% | 69.6% | 2007-2025 | 0 | 4 |

## LLM Query Plan

- Main queries: Counterfactual regret minimization, Counterfactual regret minimization extensive form games, CFR+ algorithm, Deep counterfactual regret minimization
- Prerequisite queries: Regret matching game theory, Nash equilibrium extensive form games
- Exclude terms: Causal inference, Structural causal models, Causal effect
- Expected communities: Algorithmic Game Theory, Multi-Agent Systems, Computer Poker Research, Reinforcement Learning

## Analysis

- The key measurable outputs are corpus size, abstract coverage, citation/reference coverage, and year range.
- Topic-specific filtering is important for ambiguous terms and short acronyms. CFR retrieval filters out unrelated uses of `regret` and `counterfactual`; Vision Transformer retrieval uses word-boundary matching for acronyms such as `ViT`, `DeiT`, `DINO`, `MAE`, and `BEiT` to avoid unrelated high-citation OpenAlex records.
- Citation counts prefer Semantic Scholar `citationCount` when `S2_API_KEY` is available, then fall back to OpenAlex `cited_by_count` or curated landmark metadata. They may still differ from Google Scholar snapshots.
