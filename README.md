# ai-hub

A monorepo for experimenting with AI systems — agents, workflows, human-in-the-loop patterns, and tooling. Each project lives in its own directory with independent dependencies, configuration, and documentation.

## Intention

`ai-hub` is a personal workspace for building and comparing AI projects without mixing concerns between them. The goals are:

- **Isolate experiments** — each project is self-contained so you can try different frameworks, models, and architectures side by side.
- **Learn by building** — practical implementations of multi-agent systems, LangGraph workflows, tool use, memory, and human approval loops.
- **Iterate quickly** — spin up a new project folder, prototype, test, and either evolve it or leave it as a reference.
- **Share patterns, not coupling** — projects may reuse similar ideas (supervisor routing, tool registries, etc.) but remain independently runnable.

This is not a single deployable product. It is a collection of related AI projects under one roof.

## Structure

```
ai-hub/
├── README.md
├── human_loop_project/     # Human-in-the-loop multi-agent system
└── <future-projects>/      # Additional projects as they are added
```

Each project should include:

| Item | Purpose |
|------|---------|
| `requirements.txt` | Python dependencies |
| `.env` | Local secrets and config (not committed) |
| `README.md` | Project-specific setup and usage |
| Tests | Validation scripts or test modules |

## Projects

### human_loop_project

A human-in-the-loop multi-agent AI system — supervisor routing, specialized agents (math, SQL, general), tool execution with human approval, and a Streamlit dashboard.

See [human_loop_project/README.md](human_loop_project/README.md) for setup, environment variables, Docker instructions, and testing.

## Adding a New Project

1. Create a new directory at the repo root (e.g. `my_new_project/`).
2. Add a `requirements.txt`, project `README.md`, and any config files.
3. Register the project in this README under **Projects**.

## Conventions

- **Python** is the primary language across projects.
- **Secrets** stay in per-project `.env` files — never commit credentials.
- **Naming** — use lowercase with underscores for project directories (e.g. `human_loop_project`).
- **Independence** — projects should run on their own without importing from sibling projects unless a shared library is explicitly introduced later.
