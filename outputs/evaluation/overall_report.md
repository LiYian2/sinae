# ResearchTrail Overall Evaluation Report

## Evaluation Setup

We evaluated ResearchTrail on two live topics:

- `Counterfactual regret minimization` with an intermediate user profile.
- `Vision Transformer` with a beginner user profile.

Each topic was evaluated with five runs: a rule-only Agent, an LLM-assisted Agent, and three graph ablations (`citation`, `similarity`, and `hybrid`). Citation enrichment used Semantic Scholar when `S2_API_KEY` was available, then OpenAlex or curated landmark metadata as fallback.

The evaluation now includes both structural graph metrics and reading-path quality metrics:

- `landmark_hit_rate`: whether the path contains known essential papers.
- `topic_precision`: deterministic topical relevance over retrieved papers.
- `ordering_quality`: whether foundation papers appear before follow-up/frontier papers.
- `community_coverage`: how many detected communities are represented in the reading path.
- `path_stage_coverage`: whether the path contains foundation/core/development/frontier stages.

## Main Results

| Topic | Run | Papers | Edges | Components | Largest Component | Communities | Modularity | Stages | Path Papers | Landmark Hit | Topic Precision | Ordering | Community Coverage |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CFR | rule_only_agent | 43 | 394 | 1 | 100.0% | 4 | 0.1978 | 5 | 12 | 100.0% | 100.0% | 100.0% | 100.0% |
| CFR | llm_assisted_agent | 43 | 394 | 1 | 100.0% | 5 | 0.1941 | 5 | 13 | 100.0% | 100.0% | 100.0% | 100.0% |
| CFR | citation_graph | 15 | 3 | 13 | 20.0% | 13 | 0.0000 | 3 | 9 | 100.0% | 100.0% | 100.0% | 61.5% |
| CFR | similarity_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 4 | 10 | 100.0% | 100.0% | 100.0% | 100.0% |
| CFR | hybrid_graph | 15 | 53 | 1 | 100.0% | 3 | 0.0877 | 4 | 11 | 100.0% | 100.0% | 100.0% | 100.0% |
| ViT | rule_only_agent | 84 | 829 | 1 | 100.0% | 5 | 0.2563 | 5 | 13 | 100.0% | 97.6% | 100.0% | 80.0% |
| ViT | llm_assisted_agent | 80 | 744 | 1 | 100.0% | 6 | 0.2723 | 5 | 13 | 100.0% | 96.2% | 100.0% | 83.3% |
| ViT | citation_graph | 29 | 36 | 12 | 62.1% | 15 | 0.2465 | 5 | 13 | 100.0% | 93.1% | 100.0% | 53.3% |
| ViT | similarity_graph | 29 | 152 | 2 | 96.6% | 5 | 0.1692 | 5 | 15 | 100.0% | 93.1% | 100.0% | 80.0% |
| ViT | hybrid_graph | 29 | 164 | 1 | 100.0% | 5 | 0.2623 | 5 | 13 | 100.0% | 93.1% | 100.0% | 100.0% |

## Findings

The new metrics better support the claim that ResearchTrail helps users read papers, not just build a graph. Both topics achieve 100% landmark hit rate and 100% ordering quality in the LLM-assisted path, meaning the generated path includes key papers and places foundation work before follow-up work.

Hybrid graph construction is the most reliable default. In ViT, citation-only graph coverage is weak because the reading path covers only 53.3% of detected communities, while the hybrid graph reaches 100.0% community coverage. This shows that similarity edges improve path diversity rather than only increasing edge count.

Directed citation semantics are now more defensible. Citation PageRank is computed on a directed graph where citing papers point to cited papers, so foundational papers receive rank from later work. Betweenness uses `distance = 1 / weight`, so stronger similarity corresponds to shorter graph distance.

Semantic Scholar enrichment materially improves citation quality for AI/CS papers. `Deep Counterfactual Regret Minimization` is now reported as `239` citations from Semantic Scholar instead of the earlier OpenAlex value of `21`. Counts still differ from Google Search or Google Scholar snippets, so reports explicitly label citation sources.

Curated landmark sources are transparent. ViT includes curated prerequisite and landmark records to stabilize known foundational coverage; reports expose source mix separately. This makes it possible to run a no-curated ablation with the same metrics if needed, while avoiding hidden manual intervention.

## Report Artifacts

- `outputs/evaluation/cfr_live/group_eval_summary.md`
- `outputs/evaluation/cfr_live/retrieval_eval.md`
- `outputs/evaluation/cfr_live/graph_eval.md`
- `outputs/evaluation/cfr_live/reading_path_eval.md`
- `outputs/evaluation/vit_live/group_eval_summary.md`
- `outputs/evaluation/vit_live/retrieval_eval.md`
- `outputs/evaluation/vit_live/graph_eval.md`
- `outputs/evaluation/vit_live/reading_path_eval.md`
- `outputs/evaluation/skill_retrieval_report.md`
- `outputs/evaluation/skill_graph_report.md`
- `outputs/evaluation/skill_reading_path_report.md`
