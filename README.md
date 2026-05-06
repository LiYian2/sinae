# ResearchTrail

**ResearchTrail: A Citation-Network Agent for Personalized Research Reading Paths**

ResearchTrail helps users enter a new research field by retrieving relevant papers, constructing a citation/similarity network, identifying foundational, bridging, and frontier papers, and generating a personalized reading path with explanations and visualizations.

The system is **markdown-described, code-backed, LLM-assisted, and graph-centered**:

- `SKILL.md` files define StudyClawHub-compatible Skill interfaces.
- Python backends perform deterministic retrieval, graph construction, scoring, reporting, and evaluation.
- LLM calls are optional and used only for semantic planning, query expansion, community labeling, and evidence-grounded explanations.
- NetworkX and scikit-learn provide verifiable SNA computation.

## Architecture

```text
User Goal
  -> Hybrid Agent Planner
  -> Literature Retrieval Skill
  -> Research Graph Analysis Skill
  -> Reading Path and Report Skill
  -> Evaluation and Visualizations
```

## Skills

| Skill | Folder | Responsibility |
|---|---|---|
| Literature Retrieval | `skill_retrieval/` | Query planning, arXiv/OpenAlex retrieval, deduplication, metadata enrichment, corpus quality |
| Research Graph Analysis | `skill_graph/` | Citation/similarity graph, PageRank, betweenness, Louvain, role scoring, community labeling |
| Reading Path and Report | `skill_reading_path/` | Personalized stages, evidence packets, grounded explanations, report, visualizations |

Each Skill folder contains a StudyClawHub-compatible `SKILL.md`.

## Environment

Use the course conda environment:

```bash
conda activate network
```

Optional LLM mode uses SiliconFlow:

```bash
export SILICON_FLOW_API="your_api_key"
```

Default model:

```text
Pro/zai-org/GLM-4.7
```

If the API key is missing or the LLM call fails, ResearchTrail falls back to deterministic rule-based behavior.

## Usage

Stable demo without external APIs:

```bash
python main.py "I am a beginner in deep learning and want to deeply understand Vision Transformer" \
  --demo \
  --llm off \
  --max-papers 80 \
  --output-dir outputs/vit_rule
```

LLM-assisted mode:

```bash
python main.py "I am a beginner in deep learning and want to deeply understand Vision Transformer" \
  --llm auto \
  --llm-provider siliconflow \
  --llm-model Pro/zai-org/GLM-4.7 \
  --max-papers 120 \
  --output-dir outputs/vit_llm
```

Interactive mode:

```bash
python main.py --interactive --demo --llm off
```

## Outputs

Each run writes:

- `research_report.md`
- `research_graph.png`
- `scores_distribution.png`
- `state.json`

The state file includes papers, graph scores, corpus quality, graph metrics, query plan, community labels, and reading path metrics.

## Evaluation

Run the built-in evaluation harness:

```bash
python -m evaluation.runner \
  --topic "Vision Transformer" \
  --demo \
  --max-papers 80 \
  --output-dir outputs/evaluation/vit
```

It produces:

- `evaluation_results.json`
- `evaluation_summary.md`

Current evaluation hooks compare:

- rule-only vs LLM-assisted Agent behavior
- citation-only vs similarity-only vs hybrid graph
- retrieval, graph, and reading path metrics

## Tests

```bash
conda activate network
python -m pytest tests -q
```
