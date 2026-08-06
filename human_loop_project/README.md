# human_loop_project

A human-in-the-loop multi-agent AI system. A supervisor routes user questions to specialized agents, each agent selects a tool and input, and a human must approve before execution.

Built with LangGraph, LangChain, OpenRouter, Azure Cosmos DB, and Streamlit.

## How It Works

```
User Question
     │
     ▼
┌─────────────┐
│  Supervisor │  Classifies question → MATH, SQL, or GENERAL
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Planner   │  Selected agent picks a tool and input
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Human Review│  User approves or rejects the plan
└──────┬──────┘
       │ (approved)
       ▼
┌─────────────┐
│   Executor  │  Runs the tool, formats the final answer
└─────────────┘
```

**Streamlit UI** (`app.py`) runs the full planner → approval → executor flow with session memory, feedback logging, and a dashboard sidebar.

**CLI mode** (`main.py`) uses a simpler LangGraph workflow (`supervisor` → `routing`) for terminal-based interaction.

## Agents

| Agent | Handles | Tool |
|-------|---------|------|
| **MATH** | Arithmetic and calculations | `calculator` |
| **SQL** | Employee database queries | `database` (Cosmos DB) |
| **GENERAL** | General conversation | No tool — direct LLM response |

The supervisor (`agents/supervisor.py`) uses the LLM to classify each question into one of these agents.

## Prerequisites

- Python 3.11+
- An [OpenRouter](https://openrouter.ai/) API key
- Azure Cosmos DB (local emulator via Docker, or a cloud instance)

## Environment Variables

Create a `.env` file in this directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
MODEL=qwen/qwen-2.5-7b-instruct:free

# Cosmos DB — defaults work with the local emulator
COSMOS_ENDPOINT=https://localhost:8081/
COSMOS_KEY=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==
```

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENROUTER_API_KEY` | Yes | API key for OpenRouter LLM calls |
| `MODEL` | No | Model ID (default: `qwen/qwen-2.5-7b-instruct:free`) |
| `COSMOS_ENDPOINT` | No | Cosmos DB endpoint (default: emulator URL) |
| `COSMOS_KEY` | No | Cosmos DB key (default: emulator master key) |

Verify your config:

```bash
python check_env.py
```

## Local Setup

### 1. Install dependencies

```bash
cd human_loop_project
pip install -r requirements.txt
```

### 2. Start Cosmos DB emulator

**Option A — Docker Compose** (starts emulator + app):

```bash
docker compose up -d cosmos-emulator
```

**Option B — Standalone emulator image:**

```bash
docker run -p 8081:8081 -p 1234:1234 \
  -e ACCEPT_EULA=Y \
  mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest
```

For local (non-Docker) Python, set `COSMOS_ENDPOINT=https://localhost:8081/` in `.env`.

### 3. Initialize databases

```bash
# Seed employee data into Cosmos DB
python database/init_db.py

# Create the feedback container
python database/create_feedback_container.py

# Optional: create local SQLite database
python database/create_db.py
```

### 4. Run the app

**Streamlit UI** (recommended):

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501).

**CLI chat loop:**

```bash
python main.py
```

Type `exit` to quit.

## Docker (full stack)

Runs the Streamlit app and Cosmos emulator together:

```bash
docker compose up --build
```

The app is available at [http://localhost:8501](http://localhost:8501).

## Testing

Individual test scripts live at the project root:

```bash
python test_supervisor.py
python test_math_agent.py
python test_sql.py
python test_planner.py
python test_executor.py
python test_workflow.py
python test_cosmos.py
python test_llm.py
```

## Project Structure

```
human_loop_project/
├── app.py                  # Streamlit UI (main entry point)
├── main.py                 # CLI chat loop
├── agents/                 # Supervisor and domain agents
├── workflow/               # LangGraph graph, nodes, human approval
├── planner/                # Plan creation from questions
├── executor/               # Approved plan execution
├── tools/                  # Calculator and database tools
├── llm/                    # OpenRouter LLM client
├── memory/                 # Conversation and feedback memory
├── database/               # Cosmos DB, SQLite, feedback, analytics
├── prompts/                # System prompts for agents
├── cosmos/                 # Cosmos client utilities
├── logs/                   # Action logging
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Human Approval Flow

In the Streamlit UI, after you submit a question:

1. The **planner** selects an agent and tool.
2. The UI shows the agent, tool, tool input, and confidence.
3. You **approve** or **reject** the plan.
4. On approval, the **executor** runs the tool and returns the answer.
5. Feedback is saved to Cosmos DB for analytics and memory reuse.

Previously approved similar questions can be matched from memory and still require human approval before execution.

## Dependencies

Key packages (see `requirements.txt` for the full list):

- `streamlit` — web UI
- `langgraph` / `langchain` — agent workflow orchestration
- `openai` — OpenRouter API client
- `azure-cosmos` — Cosmos DB integration
- `python-dotenv` — environment variable loading
