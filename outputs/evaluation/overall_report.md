# ResearchTrail Overall Evaluation Report

## Artifact Map

- Overall 12-topic agent benchmark: `outputs/benchmark_full_llm_normalized/benchmark_summary.md` and `benchmark_results.json`.
- Skill 1 corpus ablation: `outputs/corpus_ablation/full_12_topics/corpus_ablation_batch_summary.md` and `corpus_ablation_batch_results.json`.
- Skill 2 graph ablation: `outputs/graph_ablation/full_12_topics/graph_ablation_summary.md` and `graph_ablation_results.json`.
- Skill 3 reading-path ablation: `outputs/reading_path_ablation/full_11_topics/reading_path_ablation_summary.md`, `reading_path_ablation_results.json`, and `paths_for_human_eval/`.
- Manual qualitative rubric: `evaluation/manual_quality_rubric.md`.

## Overall Agent Result

| Scope | Topics | Papers | Edges | Communities | Landmark Hit | Topic Precision | Ordering | Community Coverage | Stage Coverage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All benchmark topics | 12 | 21.5 | 121.8 | 3.9 | 61.9% | 91.7% | 68.4% | 91.4% | 95.8% |
| Excluding protein low-corpus case | 11 | 22.7 | 131.7 | 4.0 | 67.6% | 93.3% | 74.6% | 90.6% | 97.7% |

Interpretation: the full agent is strongest on topic precision, stage coverage, and community coverage. The main weakness is landmark recall/order on topics where scholarly metadata is incomplete or where the topic contains important non-arXiv/non-OpenAlex artifacts, especially mechanistic interpretability and the saved protein benchmark corpus.

## End-to-End Architecture

The agent is a markdown-described, code-backed, LLM-assisted workflow:

1. Agent planner parses the user request, topic, level, and desired output. LLM mode uses SiliconFlow/OpenAI-compatible chat completions with `SILICON_FLOW_API`; fallback mode uses deterministic rules.
2. Literature Retrieval Skill constructs a corpus through query expansion, retrieval, filtering, deduplication, landmark verification, and metadata enrichment.
3. Graph Skill builds citation/similarity/hybrid graphs and computes deterministic SNA metrics and paper role scores.
4. Community labeler optionally uses LLM to name graph communities from evidence packets.
5. Reading Path Skill creates staged reading paths and evidence-grounded explanations.
6. Report/visualization layer writes Markdown reports, graph visualizations, score distributions, state files, and GUI-ready outputs.

## Report Claims Supported by Evaluation

- Skill 1 is robust as a corpus builder because multi-source retrieval plus topic filtering improves precision and graph edge yield without sacrificing landmark recall.
- Skill 2 is necessary because citation-only metadata is too sparse for many modern topics; the hybrid graph materially improves connectivity and bridge-paper analysis.
- Skill 3 is necessary because ranking baselines do not provide stage structure; staged reading paths preserve high topicality while adding pedagogical organization.
- The full system is not just a summarizer: it retrieves papers, builds a research network, assigns structural paper roles, and generates a personalized reading path with visual evidence.

## Limitations to State Explicitly

- The benchmark landmark lists are curated for evaluation. In the system, verified landmarks are recovered through API metadata and should be described as a recall aid, not as manual insertion of final results.
- OpenAlex has broad coverage but lower topic precision on some engineering-heavy topics; arXiv is narrower and often cleaner but weaker on citation/reference metadata.
- Citation metadata remains incomplete for some domains, which is why the hybrid graph is more reliable than citation-only graph construction.
- The saved 12-topic overall benchmark has a weak protein structure run with only 8 papers; the Skill 1 rerun shows this topic can retrieve a much healthier corpus, so report the original end-to-end protein result as low-confidence or rerun the full agent if time permits.
- Role scores are still heuristic combinations of network metrics, recency, citation count, and community position. LLM helps explain evidence but does not replace the deterministic scores.

