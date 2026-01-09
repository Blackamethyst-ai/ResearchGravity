---
name: agent-core
description: Unified agent orchestration for research, innovation scouting, and memory across CLI (Claude Code), Antigravity (VSCode OSS), and web. Use for multi-environment coordination, parallel sessions, persistent URL logging, and long-term memory. Triggers on "/innovation-scout", "/deep-research", "/remember", "/recall", "/sync", "/archive", "/parallel", or research requests.
---

# Agent Core v2.0

Unified orchestration layer for agentic workflows across environments.

## Quick Reference

```
Mode:        Auto-accept (always)
Model:       Opus 4.5 with thinking
Plan first:  Shift+Tab twice → iterate → execute
Parallel:    Up to 5 terminal tabs
```

## Environments

| Environment | Type | Shortcuts | Best For |
|-------------|------|-----------|----------|
| **CLI** | `claude` command | — | Planning, parallel sessions, synthesis |
| **Antigravity** | VSCode OSS | ⌘E ⌘L ⌘I | Coding, preview, browser research |
| **Web** | claude.ai/code | — | Handoff, visual review |

### Antigravity Shortcuts
- **⌘E** — Switch to Agent Manager
- **⌘L** — Code with Agent
- **⌘I** — Edit code inline

## Architecture

```
CLAUDE.md                         # Project root (commit to git)

~/.agent-core/                    # Global (synced)
├── config.json                   # Settings
├── sessions/
│   ├── index.md                  # All sessions
│   └── [session-id]/             # Archived sessions
├── memory/
│   ├── global.md                 # Permanent facts
│   └── learnings.md              # Research insights
├── workflows/
├── scripts/
└── assets/

.agent/                           # Project-local
├── memory.md                     # Project memory
├── research/
│   ├── session.json              # Current session
│   ├── session_log.md            # Narrative + URL table
│   ├── scratchpad.json           # Machine-readable
│   └── [topic]_sources.csv       # Export
└── workflows/
```

## Commands

| Command | Script | Description |
|---------|--------|-------------|
| `/innovation-scout [topic]` | workflows/ | arXiv + GitHub dual-filter |
| `/deep-research [topic]` | workflows/ | Multi-source investigation |
| `/remember [fact]` | workflows/ | Store to memory |
| `/recall [query]` | workflows/ | Query memory |
| `/parallel [task]` | workflows/ | Coordinate parallel sessions |
| `/sync` | sync_environments.py | Push/pull state |
| `/archive` | archive_session.py | Close session |
| `/status` | sync_environments.py status | Show state |

## Session Workflow

### 1. Initialize
```bash
python3 ~/.agent-core/scripts/init_session.py "topic"
# OR: agent-init "topic"
```

### 2. Research
- Use queries from session_log.md
- Log EVERY URL: `python3 log_url.py <url> [--used] [--relevance N]`
- Checkpoint findings in scratchpad.json

### 3. Archive
```bash
python3 ~/.agent-core/scripts/archive_session.py
# OR: agent-archive
```

## URL Logging (Critical)

**Log ALL URLs** — used or not, succeeded or failed:

```bash
# Log a URL you used
python3 log_url.py https://github.com/user/repo --used --relevance 3

# Log a URL you skipped
python3 log_url.py https://example.com --skipped --notes "Outdated"

# Log with auto-detection
python3 log_url.py https://arxiv.org/abs/2401.12345
```

## Parallel Sessions (Boris's Pattern)

```
Tab 1: Planning/Orchestration
Tab 2: Feature A
Tab 3: Feature B
Tab 4: Testing
Tab 5: Documentation
```

## Search Filters

### Viral Filter
```
[topic] stars:>500 pushed:>[30 days ago]
```

### Groundbreaker Filter
```
[topic] stars:10..200 created:>[90 days ago]
```

## Output Standards

Every finding MUST include:
- `[Name](URL)` — Direct link
- Quantitative signal (stars, citations)
- One-line rationale

## Setup

```bash
chmod +x setup.sh && ./setup.sh
```
