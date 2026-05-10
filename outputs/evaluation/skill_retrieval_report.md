# Literature Retrieval Skill Report

## Skill 1: Literature Retrieval Implementation

Skill 1 turns a research topic and user profile into a graph-ready paper corpus. It uses LLM-assisted query normalization when available, deterministic fallback queries otherwise, arXiv/OpenAlex retrieval, duplicate removal by normalized title, topic filtering, verified landmark recovery, Semantic Scholar citation/reference enrichment, and corpus quality metrics. The latest implementation also uses HTTPS arXiv API calls, global arXiv throttling with retry/backoff, and `S2_API_KEY` when available.

| Variant | Topics | Papers | Raw Records | Duplicates Removed | Abstract Coverage | Citation Metadata | Reference Coverage | Landmark Hit | Topic Precision | Graph Edges | Graph Edge Yield |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A_arxiv_only | 12 | 26.2 | 28.6 | 2.4 | 100.0% | 51.8% | 52.8% | 72.8% | 75.5% | 172.5 | 6.18 |
| B_openalex_only | 12 | 32.2 | 40.0 | 7.8 | 88.4% | 100.0% | 93.5% | 70.0% | 31.1% | 98.0 | 3.16 |
| C_arxiv_openalex | 12 | 45.0 | 68.6 | 12.6 | 96.7% | 92.8% | 89.1% | 90.3% | 60.6% | 224.8 | 5.00 |
| D_plus_topic_filtering | 12 | 40.0 | 68.6 | 12.6 | 98.6% | 92.8% | 88.8% | 90.3% | 66.6% | 241.4 | 5.93 |
| E_plus_verified_landmarks | 12 | 40.1 | 68.6 | 12.6 | 98.6% | 93.7% | 89.8% | 91.7% | 66.7% | 241.8 | 5.92 |

Skill 1 conclusion: combining arXiv and OpenAlex improves landmark recall over either source alone. Topic filtering reduces corpus size from 45.0 to about 40.0 papers while raising topic precision from 60.6% to 66.6% and graph edge yield from 5.00 to 5.93. Verified landmarks give a small additional recall gain, from 90.3% to 91.7%, without degrading precision.

Important nuance: E is not supposed to dominate every metric. It is optimized for milestone recall and downstream graph readiness, while arXiv-only can show higher topic precision because arXiv search returns narrower technical papers and OpenAlex has broader, noisier coverage.

## How to Use These Results

For the individual report, emphasize that Skill 1 is evaluated as corpus construction rather than simple search. The key downstream metric is graph edge yield, because the corpus must support citation/similarity graph construction.
