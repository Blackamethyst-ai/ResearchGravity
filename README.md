<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,100:00d9ff&height=200&section=header&text=ResearchGravity&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Metaventions%20AI%20Research%20Framework&descSize=20&descAlignY=55" />
</p>

<p align="center">
  <strong>Frontier intelligence for meta-invention. Research that compounds.</strong>
</p>

<p align="center">
  <em>"Let the invention be hidden in your vision"</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.0.0-00d9ff?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Metaventions_AI-Architected_Intelligence-1a1a2e?style=for-the-badge" alt="Metaventions AI" />
</p>

---

## Why • Architecture • Quick Start • Workflow • Sources • Contact

---

## Why ResearchGravity?

Traditional research workflows fail at the frontier:

| Problem | Impact |
|---------|--------|
| Single-source blindspots | Missing critical signals |
| No synthesis | Raw links ≠ research |
| No session continuity | Context lost between sessions |
| No quality standard | Inconsistent output |

**ResearchGravity** solves this with:

- **Multi-tier source hierarchy** — Tier 1 (primary), Tier 2 (amplifiers), Tier 3 (context)
- **Cold Start Protocol** — Never lose session context
- **Synthesis workflow** — Thesis → Gap → Innovation Direction
- **Quality checklist** — Consistent Metaventions-grade output

---

## Architecture

```
ResearchGravity/
├── init_session.py      # Initialize research sessions
├── log_url.py           # Log URLs with tier/category metadata
├── status.py            # Cold start session checker
├── archive_session.py   # Archive completed sessions
├── sync_environments.py # Cross-environment sync
├── SKILL.md             # Agent Core v3.0 documentation
│
├── .agent/research/     # Local session state
│   ├── session.json     # Current session metadata
│   ├── session_log.md   # Research narrative + URL table
│   ├── scratchpad.json  # Machine-readable findings
│   └── sources.csv      # Exportable source list
│
└── ~/.agent-core/       # Global (synced across projects)
    ├── sessions/        # Archived sessions
    └── memory/          # Long-term research memory
```

---

## Quick Start

### 1. Check Session State
```bash
python3 status.py
```

### 2. Initialize New Session
```bash
python3 init_session.py "your research topic"
```

### 3. Research & Log URLs
```bash
# Log a Tier 1 research paper
python3 log_url.py https://arxiv.org/abs/2601.05918 \
  --tier 1 --category research --relevance 5 --used

# Log industry news
python3 log_url.py https://techcrunch.com/... \
  --tier 1 --category industry --relevance 4 --used
```

### 4. Archive When Complete
```bash
python3 archive_session.py
```

---

## Research Workflow

### Phase 1: Signal Capture (30 min)
```
1. Scan Tier 1 sources for last 24-48 hours
2. Log ALL URLs (used or not) via log_url.py
3. Tag each with: tier, category, relevance (1-5)
```

### Phase 2: Synthesis (20 min)
```
1. Group findings by theme (not source)
2. Identify the GAP — what's missing?
3. Draft thesis: "X is happening because Y, which means Z"
```

### Phase 3: Editorial Frame (10 min)
```
1. Write 1-paragraph summary with thesis
2. Each finding: [Name](URL) + signal + rationale
3. End with: "Innovation opportunity: ..."
```

---

## Source Hierarchy

### Tier 1: Primary Sources (Check Daily)

| Category | Sources |
|----------|---------|
| **Research** | arXiv (cs.AI, cs.SE, cs.LG), HuggingFace Papers |
| **Labs** | OpenAI, Anthropic, Google AI, Meta AI, DeepMind |
| **Industry** | TechCrunch, The Verge, Ars Technica, Wired |

### Tier 2: Signal Amplifiers

| Category | Sources |
|----------|---------|
| **GitHub** | Trending, Topics, Releases |
| **Benchmarks** | METR, ARC Prize, LMSYS, PapersWithCode |
| **Social** | X/Twitter key accounts, HN, Reddit ML |

### Tier 3: Deep Context

| Category | Sources |
|----------|---------|
| **Newsletters** | Import AI, The Batch, Latent Space |
| **Forums** | LessWrong, Alignment Forum |

---

## Quality Checklist

Before archiving a session, verify:

- [ ] Scanned all Tier 1 sources for timeframe
- [ ] Logged 10+ URLs minimum
- [ ] Identified at least one GAP
- [ ] Wrote thesis statement
- [ ] Each finding has: link + signal + rationale
- [ ] Innovation direction is concrete, not vague

---

## Cold Start Protocol

When invoking ResearchGravity, always run `status.py` first:

```
==================================================
  ResearchGravity — Metaventions AI
==================================================

📍 ACTIVE SESSION
   Topic: [current topic]
   URLs logged: X | Findings: Y | Thesis: Yes/No

📚 RECENT SESSIONS
   1. [topic] — [date]
   2. [topic] — [date]

--------------------------------------------------
OPTIONS:
  → Continue active session
  → Resume archived session
  → Start fresh
--------------------------------------------------
```

---

## Integration

ResearchGravity integrates with the **Antigravity ecosystem**:

| Environment | Use Case |
|-------------|----------|
| **CLI** (Claude Code) | Planning, parallel sessions, synthesis |
| **Antigravity** (VSCode) | Coding, preview, browser research |
| **Web** (claude.ai) | Handoff, visual review |

---

## Roadmap

- [ ] MCP integration for tool context
- [ ] Auto-synthesis via LLM
- [ ] Browser extension for URL capture
- [ ] Team collaboration features

---

## License

MIT License — See [LICENSE](LICENSE)

---

## Contact

**Metaventions AI**
Dico Angelo
dicoangelo@metaventionsai.com

<p align="center">
  <a href="https://metaventions-ai-architected-intelligence-1061986917838.us-west1.run.app/">
    <img src="https://img.shields.io/badge/Metaventions_AI-Website-00d9ff?style=for-the-badge" alt="Website" />
  </a>
  <a href="https://github.com/Blackamethyst-ai">
    <img src="https://img.shields.io/badge/GitHub-Blackamethyst--ai-1a1a2e?style=for-the-badge&logo=github" alt="GitHub" />
  </a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,100:00d9ff&height=100&section=footer" />
</p>
