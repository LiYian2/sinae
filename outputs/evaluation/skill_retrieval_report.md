# Literature Retrieval Skill Final Report

## Functionality

The Literature Retrieval Skill converts a natural-language research goal into a structured paper corpus. It combines LLM or rule-based query planning with deterministic arXiv/OpenAlex retrieval, topic-specific filtering, title deduplication, Semantic Scholar/OpenAlex citation enrichment, and transparent curated landmark metadata.

## Inputs and Outputs

- Inputs: topic, user level, time range, maximum paper count, and optional LLM query plan.
- Outputs: paper records with titles, authors, years, abstracts, URLs, citation counts, citation sources, reference lists, source labels, and corpus quality metrics.

## Evaluation Results

| Topic | Run | Papers | Abstract Coverage | Citation/Reference Coverage | Year Range | Topic Precision |
|---|---|---:|---:|---:|---|---:|
| CFR | rule_only_agent | 43 | 100.0% | 69.8% | 2007-2025 | 100.0% |
| CFR | llm_assisted_agent | 43 | 100.0% | 69.8% | 2007-2025 | 100.0% |
| ViT | rule_only_agent | 84 | 98.8% | 77.4% | 2012-2026 | 97.6% |
| ViT | llm_assisted_agent | 80 | 98.8% | 76.2% | 2012-2026 | 96.2% |

## Source Transparency

Observed source mix:

| Topic | Run | Source Mix |
|---|---|---|
| CFR | rule_only_agent | `{"arxiv": 36, "openalex": 7}` |
| CFR | llm_assisted_agent | `{"arxiv": 36, "openalex": 7}` |
| ViT | rule_only_agent | `{"arxiv": 39, "openalex": 38, "curated_prerequisite": 3, "curated_landmark": 4}` |
| ViT | llm_assisted_agent | `{"arxiv": 37, "openalex": 35, "curated_prerequisite": 3, "curated_landmark": 5}` |

## Citation Enrichment

Citation counts prefer Semantic Scholar when `S2_API_KEY` is configured. The API is rate-limited to 1 request per second, so enrichment is focused on likely landmark and high-value papers. Remaining papers fall back to OpenAlex or curated metadata.

`Deep Counterfactual Regret Minimization` is now reported as `239` citations from Semantic Scholar instead of the earlier OpenAlex value of `21`. This is still different from Google Search/Scholar snippets, so reports label citation sources explicitly.

## Analysis

The retrieval skill now handles both topic ambiguity and citation reliability better than the earlier pipeline. CFR filtering prevents unrelated `counterfactual` or `CFIR` records from entering the corpus. ViT filtering uses word-boundary acronym matching for `ViT`, `DeiT`, `DINO`, `MAE`, and `BEiT`, preventing unrelated high-citation records from entering through accidental substring matches.

Curated landmarks are transparent source categories rather than hidden ranking decisions. They are used to stabilize known foundational recall, and the source mix table makes their effect visible for later no-curated ablation.
