# ARIP — AI Resource Intelligence Platform (VS Code Extension)

> Silent AI usage observability, resource intelligence, and productivity tracking — built right into your editor.

ARIP is a VS Code extension that passively monitors your AI assistant usage across all supported extensions, estimates token consumption and costs locally, and syncs structured telemetry to the ARIP central platform — without ever reading your actual code or prompts.

---

## System Architecture

ARIP is a two-part system:

| Component | Repo | Purpose |
|---|---|---|
| **ARIP VS Code Extension** | `arip/` | Passive IDE observer, telemetry collector, and sidebar dashboard |
| **ARIP Engine** | `arip_engine/` | Intelligent routing, cost prediction, and prompt optimization server |

---

## Features

- **Silent Observability** — Hooks into VS Code's AI extension APIs without interrupting your workflow
- **Local Token Estimation** — Estimates prompt and completion token sizes on-device with no data leakage
- **Cost Estimation** — Tracks per-query AI cost and aggregates session and daily totals locally
- **Anonymous Mode** — Replaces all filenames and workspace names with hashes before any data is transmitted
- **Telemetry Batching** — Queues events locally and uploads in configurable batches (default: every 30 seconds)
- **Sidebar Dashboard** — Embedded webview panel showing real-time usage analytics
- **Status Bar Integration** — At-a-glance AI usage indicators directly in the VS Code status bar
- **Multi-Provider Support** — Works across Copilot, Cursor, Continue, and other AI coding assistants

---

## Tech Stack

| Layer | Technology |
|---|---|
| Extension Runtime | VS Code Extension API (v1.85+) |
| Language | TypeScript 5 |
| Build | `tsc` (TypeScript compiler) |
| UI | VS Code Webview API |
| Packaging | `vsce` — `.vsix` distributable |
| Auth | JWT-based login with refresh token flow |
| Telemetry Transport | HTTP REST — batch POST to ARIP backend |

---

## Project Structure

```
arip/
├── src/
│   ├── activation/     # Extension entry point and lifecycle management
│   ├── authentication/ # JWT login / logout / refresh token flow
│   ├── commands/       # VS Code command handlers (login, sync, export, etc.)
│   ├── config/         # Settings reader and configuration manager
│   ├── cost/           # Local cost estimation per AI query
│   ├── events/         # Event capture and classification
│   ├── observers/      # AI extension observers (Copilot, Continue, etc.)
│   ├── queue/          # Local event queue and batch upload manager
│   ├── sidebar/        # Webview-based usage analytics dashboard
│   ├── statusbar/      # VS Code status bar integration
│   ├── tokenizer/      # Local token estimation utilities
│   └── utils/          # Shared utilities
├── mock-server.js      # Local development mock backend (no real API needed)
├── package.json        # Extension manifest, commands, settings contributions
└── arip-vscode-1.0.0.vsix  # Packaged distributable extension
```

---

## Installation

### From VSIX (direct install)

```bash
code --install-extension arip-vscode-1.0.0.vsix
```

Or via VS Code: `Extensions` panel → `...` menu → `Install from VSIX...`

### From Source

```bash
git clone https://github.com/your-username/arip.git
cd arip
npm install
npm run compile
```

Then press `F5` in VS Code to launch the Extension Development Host.

---

## Development

### Run mock backend (no real server needed)

```bash
node mock-server.js
```

The mock server starts at `http://localhost:3000` and simulates all ARIP API endpoints:
- `GET /health` — connection test
- `POST /auth/login` — returns mock JWT
- `POST /auth/refresh` — refreshes token
- `POST /telemetry/batch` — logs received events to console

### Update the backend URL in VS Code settings

```json
"arip.backendUrl": "http://localhost:3000"
```

---

## Available Commands

| Command | Description |
|---|---|
| `ARIP: Login` | Authenticate with the ARIP platform |
| `ARIP: Logout` | Clear stored credentials |
| `ARIP: Sync Now` | Immediately flush the event queue |
| `ARIP: View Analytics` | Open the sidebar analytics dashboard |
| `ARIP: Open Dashboard` | Launch the full web dashboard |
| `ARIP: Export Logs` | Export collected telemetry to a local file |
| `ARIP: Reset Queue` | Clear all pending unsynced events |
| `ARIP: Test Connection` | Verify connectivity to the ARIP backend |
| `ARIP: Enable Debug Mode` | Enable verbose output in the output channel |

---

## Configuration

All settings are available under `ARIP Telemetry Settings` in VS Code preferences:

| Setting | Default | Description |
|---|---|---|
| `arip.backendUrl` | `https://api.arip.io/v1` | ARIP API base URL |
| `arip.enableTelemetry` | `true` | Enable event collection |
| `arip.enableTokenEstimation` | `true` | Local token size estimation |
| `arip.enableCostEstimation` | `true` | Per-query cost tracking |
| `arip.anonymousMode` | `true` | Replace identifiers with hashes |
| `arip.uploadInterval` | `30` | Batch upload interval in seconds |
| `arip.maxQueueSize` | `1000` | Max local queue size before oldest events are dropped |
| `arip.excludedFolders` | `[node_modules, .git, ...]` | Folders to ignore |
| `arip.debugLogging` | `false` | Verbose output channel logging |

---

## Competitive Landscape

ARIP uniquely combines IDE-native observability with intelligent routing and productivity analytics — features no single existing tool provides:

| Feature | LiteLLM | Helicone | Langfuse | **ARIP** |
|---|---|---|---|---|
| IDE Extension | - | - | - | **Yes** |
| AI Usage Analytics | Limited | Yes | Yes | **Yes** |
| Productivity Analytics | - | - | - | **Yes** |
| AI Cost Prediction | - | - | - | **Yes** |
| Prompt Optimization | - | - | - | **Yes** |
| Autonomous Recommendations | - | - | - | **Yes** |
| Multi-Agent Orchestration | - | - | - | **Yes** |

---

## License

MIT License — free to use, modify, and distribute.
