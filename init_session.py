#!/usr/bin/env python3
"""
Initialize a new agent session with proper workspace structure.
Supports both CLI and Antigravity environments with sync capabilities.

Usage:
  python3 init_session.py <topic> [--workflow TYPE] [--env ENV] [--continue SESSION_ID]
"""

import argparse
import json
import os
import hashlib
from datetime import datetime, timedelta
from pathlib import Path


def get_agent_core_dir() -> Path:
    """Get the global agent-core directory."""
    return Path.home() / ".agent-core"


def get_local_agent_dir() -> Path:
    """Get the local .agent directory."""
    return Path.cwd() / ".agent"


def detect_environment() -> str:
    """Detect if running in CLI or Antigravity."""
    if os.environ.get("ANTIGRAVITY_SESSION"):
        return "antigravity"
    return "cli"


def generate_session_id(topic: str) -> str:
    """Generate unique session ID."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    topic_hash = hashlib.md5(topic.encode()).hexdigest()[:6]
    safe_topic = topic.lower().replace(" ", "-")[:20]
    return f"{safe_topic}-{timestamp}-{topic_hash}"


def create_search_queries(topic: str) -> dict:
    """Generate search queries for the topic."""
    today = datetime.now()
    viral_cutoff = (today - timedelta(days=30)).strftime("%Y-%m-%d")
    groundbreaker_cutoff = (today - timedelta(days=90)).strftime("%Y-%m-%d")
    
    return {
        "viral": {
            "github": f"{topic} stars:>500 pushed:>{viral_cutoff}",
            "description": "High-adoption, community-vetted"
        },
        "groundbreaker": {
            "github": f"{topic} stars:10..200 created:>{groundbreaker_cutoff}",
            "arxiv": topic,
            "description": "Novel, emerging innovations"
        }
    }


def init_session(
    topic: str,
    workflow: str = "research",
    env: str = None,
    continue_session: str = None
) -> dict:
    """Initialize a new research session."""
    
    env = env or detect_environment()
    
    # Handle continuing existing session
    if continue_session:
        return load_session(continue_session)
    
    session_id = generate_session_id(topic)
    timestamp = datetime.now()
    
    # Create directories
    local_dir = get_local_agent_dir() / "research"
    global_dir = get_agent_core_dir() / "sessions" / session_id
    
    local_dir.mkdir(parents=True, exist_ok=True)
    global_dir.mkdir(parents=True, exist_ok=True)
    
    # Session metadata
    session = {
        "session_id": session_id,
        "topic": topic,
        "workflow": workflow,
        "environment": env,
        "started": timestamp.isoformat(),
        "status": "active",
        "queries": create_search_queries(topic),
        "paths": {
            "local": str(local_dir),
            "global": str(global_dir),
            "session_log": str(local_dir / "session_log.md"),
            "scratchpad": str(local_dir / "scratchpad.json"),
            "report": str(local_dir / f"{topic.lower().replace(' ', '-')}_report.md"),
            "sources": str(local_dir / f"{topic.lower().replace(' ', '-')}_sources.csv")
        },
        "stats": {
            "urls_visited": 0,
            "urls_used": 0,
            "checkpoints": 0,
            "last_sync": None
        }
    }
    
    # Create session log
    create_session_log(session)
    
    # Create scratchpad
    create_scratchpad(session)
    
    # Create sources CSV header
    sources_path = Path(session["paths"]["sources"])
    sources_path.write_text("name,url,type,filter,stars,date,relevance,used,notes\n")
    
    # Save session metadata
    metadata_path = local_dir / "session.json"
    metadata_path.write_text(json.dumps(session, indent=2))
    
    # Also save to global
    global_metadata = global_dir / "session.json"
    global_metadata.write_text(json.dumps(session, indent=2))
    
    return session


def create_session_log(session: dict):
    """Create the session log markdown file."""
    content = f"""# Research Session: {session['topic']}

**Session ID:** `{session['session_id']}`
**Workflow:** {session['workflow']}
**Environment:** {session['environment']}
**Started:** {session['started']}
**Status:** {session['status']}

## Search Queries

### Viral Filter (High Adoption)
```
{session['queries']['viral']['github']}
```

### Groundbreaker Filter (Novel/Emerging)
```
{session['queries']['groundbreaker']['github']}
```

---

## URLs Visited

| Time | Source | URL | Filter | Used | Relevance | Notes |
|------|--------|-----|--------|------|-----------|-------|

---

## Key Findings

_Update during research..._

---

## Checkpoints

| Time | URLs | Findings | Notes |
|------|------|----------|-------|

"""
    Path(session["paths"]["session_log"]).write_text(content)


def create_scratchpad(session: dict):
    """Create the scratchpad JSON file."""
    scratchpad = {
        "session_id": session["session_id"],
        "topic": session["topic"],
        "workflow": session["workflow"],
        "environment": session["environment"],
        "viral_candidates": [],
        "groundbreaker_candidates": [],
        "arxiv_papers": [],
        "urls_visited": [],
        "findings": [],
        "checkpoints": [],
        "last_updated": session["started"]
    }
    Path(session["paths"]["scratchpad"]).write_text(json.dumps(scratchpad, indent=2))


def load_session(session_id: str) -> dict:
    """Load an existing session to continue."""
    global_dir = get_agent_core_dir() / "sessions" / session_id
    metadata_path = global_dir / "session.json"
    
    if not metadata_path.exists():
        raise FileNotFoundError(f"Session not found: {session_id}")
    
    session = json.loads(metadata_path.read_text())
    session["status"] = "resumed"
    
    # Restore to local directory
    local_dir = get_local_agent_dir() / "research"
    local_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy files from global to local
    for file in global_dir.iterdir():
        if file.is_file():
            dest = local_dir / file.name
            dest.write_text(file.read_text())
    
    session["paths"]["local"] = str(local_dir)
    return session


def main():
    parser = argparse.ArgumentParser(description="Initialize agent research session")
    parser.add_argument("topic", nargs="?", help="Research topic")
    parser.add_argument("--workflow", default="research", 
                        choices=["research", "innovation-scout", "deep-research"],
                        help="Workflow type")
    parser.add_argument("--env", choices=["cli", "antigravity"],
                        help="Override environment detection")
    parser.add_argument("--continue", dest="continue_session",
                        help="Continue existing session by ID")
    
    args = parser.parse_args()
    
    if not args.topic and not args.continue_session:
        parser.error("Either topic or --continue SESSION_ID is required")
    
    try:
        session = init_session(
            topic=args.topic or "",
            workflow=args.workflow,
            env=args.env,
            continue_session=args.continue_session
        )
        
        print(f"✅ Session initialized: {session['session_id']}")
        print(f"   Topic: {session['topic']}")
        print(f"   Workflow: {session['workflow']}")
        print(f"   Environment: {session['environment']}")
        print(f"   Local: {session['paths']['local']}")
        print()
        print("📝 Files created:")
        print(f"   - session_log.md")
        print(f"   - scratchpad.json")
        print(f"   - sources.csv")
        print()
        print("🔍 Suggested queries:")
        print(f"   Viral: {session['queries']['viral']['github']}")
        print(f"   Groundbreaker: {session['queries']['groundbreaker']['github']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
