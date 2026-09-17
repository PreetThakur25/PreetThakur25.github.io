# ARIP Engine — AI Routing & Optimization Server

> The intelligent core of the ARIP platform — an on-device routing engine that analyzes prompts, predicts costs, and selects the optimal AI model for every request.

ARIP Engine is the backend reasoning layer of the ARIP system. It exposes a REST API that accepts any AI prompt, classifies its task type and complexity, estimates token usage and cost, and returns a scored routing decision — pointing the request to the best available model.

---

## System Architecture

ARIP Engine is the server component of the two-part ARIP system:

| Component | Purpose |
|---|---|
| **ARIP VS Code Extension** (`arip/`) | Passive IDE observer, telemetry collector, sidebar dashboard |
| **ARIP Engine** (`arip_engine/`) | Intelligent routing, prompt optimization, and learning engine |

---

## Core Capabilities

- **Task Classification** — Identifies whether a prompt is a coding, writing, reasoning, math, or vision task
- **Complexity Analysis** — Scores prompt complexity to match it to the right model tier
- **Token Estimation** — Predicts token usage locally before the request hits any API
- **Cost Prediction** — Estimates per-request cost across providers (OpenAI, Anthropic, etc.)
- **Intelligent Routing** — Scores all registered models and selects the best fit based on task, cost, and reliability
- **Prompt Optimization** — Rewrites or condenses prompts to reduce token cost without losing intent
- **Learning Engine** — Observes routing outcomes and adjusts model capability scores over time

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | TypeScript 6 |
| Runtime | Node.js |
| Framework | Express 5 |
| Architecture | Dependency Injection via `ServiceLocator` |
| Model Data | In-memory capability repository (seeded at startup) |
| Execution | `ts-node` for direct TypeScript execution |

---

## Project Structure

```
arip_engine/
└── src/
    └── engine/
        ├── server.ts                   # Express server, DI bootstrap, route registration
        ├── core/
        │   ├── analyzers/
        │   │   ├── task/               # TaskAnalyzer — classifies prompt intent
        │   │   ├── prompt/             # PromptAnalyzer — extracts prompt features
        │   │   └── complexity/         # ComplexityAnalyzer — scores complexity
        │   ├── prediction/
        │   │   ├── token/              # TokenEstimator — local token count prediction
        │   │   └── cost/               # CostPredictor — per-model cost estimation
        │   ├── routing/
        │   │   ├── ScoringEngine.ts    # Scores each candidate model
        │   │   └── RoutingDecisionEngine.ts  # Selects the best model
        │   ├── optimization/
        │   │   └── PromptOptimizer.ts  # Rewrites prompts for efficiency
        │   └── learning/
        │       └── LearningEngine.ts   # Adjusts scores based on feedback
        ├── controllers/
        │   └── RoutingController.ts    # HTTP handler for /api/route
        ├── database/
        │   └── repositories/           # InMemoryCapabilityRepository
        ├── providers/                  # Model provider definitions
        ├── services/                   # Business logic services
        ├── types/                      # Shared TypeScript interfaces
        └── utils/
            └── logger.ts              # EngineLogger
```

---

## Installation

```bash
git clone https://github.com/your-username/arip_engine.git
cd arip_engine
npm install
```

---

## Running the Server

```bash
# Development (ts-node, no build step needed)
npm run dev

# Or directly
npx ts-node src/engine/server.ts
```

The engine starts on **port 3008** by default:
```
ARIP Optimization & Routing Engine listening on port 3008
```

---

## API Reference

### `POST /api/route`

Analyzes a prompt and returns the optimal model routing decision.

**Request body:**
```json
{
  "prompt": "Write a recursive Fibonacci function in Python with memoization",
  "context": {
    "preferLowCost": false,
    "maxBudget": 0.05
  }
}
```

**Response:**
```json
{
  "selectedModel": "claude-3-5-sonnet",
  "provider": "Anthropic",
  "reasoning": "High coding complexity score; model has 95/100 coding capability",
  "estimatedTokens": 340,
  "estimatedCost": 0.0018,
  "optimizedPrompt": "..."
}
```

---

### `GET /health`

Returns engine health status.

```json
{ "status": "OK" }
```

---

## Registered Models (Default Seed)

The engine seeds two example models at startup. Extend `setupDependencies()` in `server.ts` to add more:

| Model | Provider | Context | Coding | Reasoning | Reliability |
|---|---|---|---|---|---|
| `claude-3-5-sonnet` | Anthropic | 200K | 95 | 92 | 98% |
| `gpt-4o-mini` | OpenAI | 128K | 80 | 82 | 99% |

---

## How the Routing Pipeline Works

```
Incoming Prompt
      │
      ▼
 TaskAnalyzer ──────► Classify intent (coding / writing / reasoning / math / vision)
      │
      ▼
 ComplexityAnalyzer ─► Score complexity (1–10)
      │
      ▼
 TokenEstimator ─────► Estimate token count
      │
      ▼
 CostPredictor ──────► Estimate per-model cost
      │
      ▼
 ScoringEngine ──────► Score all candidate models
      │
      ▼
RoutingDecisionEngine ► Select best model
      │
      ▼
 PromptOptimizer ────► Optionally rewrite prompt for efficiency
      │
      ▼
    Response
```

---

## License

MIT License — free to use, modify, and distribute.
