#!/usr/bin/env python3
"""
Show ResearchGravity session status.
Used for cold start protocol — check state before proceeding.

Usage:
  python3 status.py
"""

import json
from datetime import datetime
from pathlib import Path


def get_agent_core_dir() -> Path:
    return Path.home() / ".agent-core"


def get_local_agent_dir() -> Path:
    return Path.cwd() / ".agent"


def get_active_session():
    """Check for active session in current project."""
    session_file = get_local_agent_dir() / "research" / "session.json"
    if session_file.exists():
        return json.loads(session_file.read_text())
    return None


def get_archived_sessions(limit: int = 5):
    """Get recent archived sessions."""
    sessions_dir = get_agent_core_dir() / "sessions"
    if not sessions_dir.exists():
        return []

    sessions = []
    for session_dir in sorted(sessions_dir.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if session_dir.is_dir():
            metadata_file = session_dir / "session.json"
            if metadata_file.exists():
                try:
                    data = json.loads(metadata_file.read_text())
                    sessions.append({
                        "id": session_dir.name,
                        "topic": data.get("topic", "Unknown"),
                        "started": data.get("started", "Unknown"),
                        "status": data.get("status", "unknown"),
                        "workflow": data.get("workflow", "research")
                    })
                except:
                    pass
        if len(sessions) >= limit:
            break

    return sessions


def format_time(iso_time: str) -> str:
    """Format ISO time to human readable."""
    try:
        dt = datetime.fromisoformat(iso_time)
        return dt.strftime("%Y-%m-%d %H:%M")
    except:
        return iso_time


def main():
    print()
    print("=" * 50)
    print("  ResearchGravity — Metaventions AI")
    print("=" * 50)
    print()

    # Check active session
    active = get_active_session()
    if active:
        print("📍 ACTIVE SESSION")
        print(f"   Topic: {active.get('topic', 'Unknown')}")
        print(f"   ID: {active.get('session_id', 'Unknown')}")
        print(f"   Started: {format_time(active.get('started', ''))}")
        print(f"   Workflow: {active.get('workflow', 'research')}")
        print(f"   Status: {active.get('status', 'unknown')}")

        # Check scratchpad for progress
        scratchpad_file = get_local_agent_dir() / "research" / "scratchpad.json"
        if scratchpad_file.exists():
            scratchpad = json.loads(scratchpad_file.read_text())
            urls_count = len(scratchpad.get("urls_visited", []))
            findings_count = len(scratchpad.get("findings", []))
            thesis = scratchpad.get("synthesis", {}).get("thesis")
            print(f"   URLs logged: {urls_count}")
            print(f"   Findings: {findings_count}")
            print(f"   Thesis: {'Yes' if thesis else 'Not yet'}")
    else:
        print("☐ No active session")

    print()

    # Check archived sessions
    archived = get_archived_sessions(5)
    if archived:
        print("📚 RECENT SESSIONS")
        for i, session in enumerate(archived, 1):
            print(f"   {i}. {session['topic']}")
            print(f"      ID: {session['id']}")
            print(f"      Date: {format_time(session['started'])}")
            print()
    else:
        print("📚 No archived sessions")

    print()
    print("-" * 50)
    print("OPTIONS:")
    if active:
        print("  → Continue active session")
    if archived:
        print("  → Resume archived: python3 init_session.py --continue [ID]")
    print("  → Start fresh: python3 init_session.py \"[topic]\"")
    print("-" * 50)
    print()


if __name__ == "__main__":
    main()
