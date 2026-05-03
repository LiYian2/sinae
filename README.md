# ResearchTrail

A Citation-Network Agent for Personalized Literature Entry and Reading Path Planning.

## Overview

ResearchTrail is an AI Agent system for social network analysis. Given a high-level research goal (e.g., "I want to enter the field of Deep CFR"), the Agent automatically:

1. **Generates a search query plan** from natural language
2. **Retrieves candidate papers** from arXiv and Semantic Scholar
3. **Builds a citation/similarity graph**
4. **Analyzes the graph** with PageRank, betweenness centrality, and community detection
5. **Generates a personalized reading path** organized by stages (Foundations → Core → Frontier)
6. **Produces reports and visualizations**
7. **Supports follow-up queries** (bridge papers, 7-day plans, author recommendations, etc.)

## Architecture

```
User Input → Agent Planner → Skills Pipeline → Output

Skills:
  1. Literature Retrieval Skill    (skill_retrieval/)
  2. Research Graph Analysis Skill (skill_graph/)
  3. Reading Path & Report Skill   (skill_reading_path/)

Shared Layer: shared/data_layer.py  (all Skills communicate via this)
```

## Installation

```bash
uv sync
```

## Usage

```bash
# Single query
uv run researchtrail "I want to enter the field of Deep CFR for imperfect-information games"

# Interactive mode
uv run researchtrail -i

# Save output
uv run researchtrail -o output.md "Build a reading path for graph anomaly detection"
```

### Interactive commands
- `/help` — Show available commands
- `/visualize` — Render network visualization
- `/report` — Generate full briefing report
- `/bridge` — Find bridge papers
- `/7day` — Generate a 7-day reading plan
- `/authors` — Show top authors
- `/foundation` — Show foundational papers
- `/gaps` — Show research gaps

## Project Structure

```
project/
├── agent/                  # Agent orchestrator
│   ├── __init__.py
│   ├── planner.py          # Rule-based intent router & workflow engine
│   └── main.py             # CLI entry point
├── shared/                 # Shared data layer
│   ├── __init__.py
│   ├── data_layer.py       # Central data store for inter-Skill communication
│   └── types.py            # Common type definitions
├── skill_retrieval/        # Skill 1: Literature Retrieval
│   ├── __init__.py
│   └── retrieval.py        # arXiv + Semantic Scholar API integration
├── skill_graph/            # Skill 2: Graph Analysis
│   ├── __init__.py
│   ├── graph_builder.py    # Citation + semantic similarity graph construction
│   └── analysis.py          # PageRank, betweenness, community detection
├── skill_reading_path/     # Skill 3: Reading Path & Report
│   ├── __init__.py
│   ├── path_generator.py   # Stage-based reading path generation
│   ├── report.py           # Markdown report generation
│   └── visualization.py    # Network visualization (matplotlib)
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_shared.py
│   ├── test_graph.py
│   ├── test_reading_path.py
│   └── test_agent.py
├── pyproject.toml
└── README.md
```

## Running Tests

```bash
uv run pytest tests/ -v
```

## Requirements

- Python >= 3.12
- networkx, matplotlib, numpy, scikit-learn, requests, arxiv, tqdm
- Internet connection for API calls (arXiv, Semantic Scholar)
