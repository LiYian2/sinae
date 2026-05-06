# Literature Retrieval Skill Final Report

## Functionality

The Literature Retrieval Skill converts a natural-language research goal into a structured paper corpus. It combines LLM or rule-based query planning with deterministic arXiv/OpenAlex retrieval, topic-specific filtering, title deduplication, and metadata enrichment.

## Inputs and Outputs

- Inputs: topic, user level, time range, maximum paper count, and optional LLM query plan.
- Outputs: paper records with titles, authors, years, abstracts, URLs, citation counts, citation sources, reference lists, and corpus quality metrics.

## Evaluation Results

| Topic | Run | Papers | Abstract Coverage | Citation/Reference Coverage | Year Range | Main Queries |
|---|---|---:|---:|---:|---|---:|
| CFR | rule_only_agent | 43 | 100.0% | 69.8% | 2007-2025 | 10 |
| CFR | llm_assisted_agent | 46 | 100.0% | 69.6% | 2007-2025 | 4 |
| ViT | rule_only_agent | 84 | 98.8% | 77.4% | 2012-2026 | 12 |
| ViT | llm_assisted_agent | 84 | 98.8% | 77.4% | 2012-2026 | 12 |

## Citation Enrichment

Citation counts now prefer Semantic Scholar when `S2_API_KEY` is configured. The API is rate-limited to 1 request per second, so enrichment is intentionally focused on likely landmark and high-value papers. Remaining papers fall back to OpenAlex or curated landmark metadata.

Observed citation sources in the LLM-assisted live runs:

| Topic | Semantic Scholar | OpenAlex | Curated | Missing/None |
|---|---:|---:|---:|---:|
| CFR | 23 | 10 | 0 | 13 |
| ViT | 21 | 45 | 8 | 10 |

## Analysis

The retrieval skill now handles both topic ambiguity and citation reliability better than the earlier pipeline. CFR filtering prevents unrelated `counterfactual` or `CFR/CFIR` records from entering the corpus. ViT filtering uses word-boundary acronym matching for terms such as `ViT`, `DeiT`, `DINO`, `MAE`, and `BEiT`, which prevents unrelated high-citation papers from being selected through accidental substring matches.

The main limitation is API availability. arXiv and OpenAlex can rate-limit live experiments, and Semantic Scholar requires strict pacing. The project therefore records citation source labels and uses curated landmark metadata only as a transparent fallback for known foundational papers.
