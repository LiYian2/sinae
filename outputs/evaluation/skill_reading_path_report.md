# Reading Path and Report Skill Report

## Skill 3: Reading Path and Report Implementation

Skill 3 converts graph scores and communities into staged reading paths. It assigns papers to prerequisite/foundation/core/development/bridge/frontier stages, uses role evidence packets for explanations, calls the LLM explanation writer when enabled, and generates Markdown reports with abstracts, URLs, role scores, why-read text, graph figures, score distributions, and follow-up suggestions. The GUI additionally lets users mark papers as read and fold completed items.

| Variant | Topics | Path Papers | Landmark Hit | Ordering | Community Coverage | Stage Coverage | Topic Precision | Explanation Coverage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| random_order | 11 | 10.5 | 63.0% | 55.4% | 95.1% | 0.0% | 94.9% | 100.0% |
| citation_count_order | 11 | 10.5 | 76.1% | 76.3% | 96.4% | 0.0% | 93.4% | 100.0% |
| pagerank_order | 11 | 10.5 | 68.5% | 59.9% | 91.9% | 0.0% | 93.7% | 100.0% |
| researchtrail_staged | 11 | 10.5 | 67.6% | 72.0% | 90.6% | 97.7% | 95.3% | 100.0% |

Skill 3 conclusion: citation-count and PageRank are strong baselines for landmark recall on some topics, but they do not create a pedagogical path. ResearchTrail staged paths are the only variant with high stage coverage, 97.7%, while keeping topic precision at 95.3% and ordering quality at 72.0%. This supports the claim that Skill 3 adds value by turning graph rankings into a usable learning sequence rather than just sorting papers.

## Suggested Manual Evaluation Dimensions

Use the files in `outputs/reading_path_ablation/full_11_topics/paths_for_human_eval/` and score each path 1-5 on: topical relevance, landmark coverage, reading-order coherence, community/subfield coverage, explanation usefulness, beginner friendliness, and whether bridge papers are plausible.

## How to Use These Results

For the individual report, emphasize that ResearchTrail staged paths trade off some raw landmark recall against high stage coverage and pedagogical ordering, which ranking-only baselines cannot provide.
