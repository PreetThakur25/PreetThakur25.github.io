# Offline Reasoning AI Agent

A fully offline, privacy-first AI reasoning agent powered by **DeepSeek-R1** running locally via **Ollama**. No cloud API calls, no data leaving your machine — just raw reasoning intelligence on your own hardware.

---

## Overview

This project wraps a locally hosted DeepSeek-R1 language model (via Ollama) into two interfaces:

- **CLI Agent** (`agent.py`) — An interactive terminal chat loop with built-in tool execution support
- **Web UI Agent** (`web_agent.py`) — A Gradio-powered browser interface for a friendlier chat experience

The agent supports structured tool commands for real-time utility tasks like fetching the current date and managing persistent notes — all without touching the internet.

---

## Features

- **100% Offline** — Runs entirely on your local machine via Ollama
- **Reasoning Model** — Powered by DeepSeek-R1 (7B quantized or 14B variants)
- **Dual Interface** — Terminal CLI and Gradio web UI
- **Tool System** — Extensible command dispatcher for built-in agent tools
- **Persistent Memory** — Save and recall notes across sessions via `memory.json`
- **Rich Terminal Output** — Styled panels and colored output via the `rich` library

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language Model | DeepSeek-R1 7B (Q4_K_M quantized) |
| LLM Runtime | [Ollama](https://ollama.com) |
| Web UI | [Gradio](https://gradio.app) |
| Terminal UI | [Rich](https://github.com/Textualize/rich) |
| Language | Python 3.10+ |

---

## Project Structure

```
reasoning_agent/
├── agent.py          # CLI chat loop with tool dispatch
├── web_agent.py      # Gradio web interface
├── tools.py          # Built-in tool implementations
└── memory.json       # Persistent note storage (auto-created)
```

---

## Prerequisites

1. **Python 3.10+** installed
2. **Ollama** installed and running — [Download here](https://ollama.com/download)
3. Pull the DeepSeek-R1 model:

```bash
ollama pull deepseek-r1:7b-qwen-distill-q4_K_M
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/reasoning_agent.git
cd reasoning_agent

# Create and activate a virtual environment
python -m venv agentic
agentic\Scripts\activate      # Windows
# source agentic/bin/activate # macOS/Linux

# Install dependencies
pip install requests rich gradio
```

---

## Usage

### CLI Mode

```bash
python agent.py
```

**Chat normally:**
```
Ask me something (or type 'exit'): Explain quantum entanglement simply
```

**Use built-in tools with the `tool:` prefix:**
```
Ask me something (or type 'exit'): tool: date
Ask me something (or type 'exit'): tool: note Remember to review the agent loop tomorrow
Ask me something (or type 'exit'): tool: show notes
```

### Web UI Mode

```bash
python web_agent.py
```

Then open your browser at `http://localhost:7860` for a full chat interface with conversation history.

---

## Available Tools

| Command | Description |
|---|---|
| `tool: date` | Returns the current date and time |
| `tool: note <text>` | Saves a note to `memory.json` |
| `tool: show notes` | Displays all saved notes |

---

## Model Variants

You can switch the model by editing the `MODEL` constant in `agent.py` or `web_agent.py`:

| Model | Notes |
|---|---|
| `deepseek-r1:7b-qwen-distill-q4_K_M` | Default — fast, runs on most machines |
| `tom_himanen/deepseek-r1-roo-cline-tools:14b` | Deeper reasoning, requires more VRAM |

---

## License

MIT License — free to use, modify, and distribute.
