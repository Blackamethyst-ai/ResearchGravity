#!/usr/bin/env python3
"""
Log a URL to the current research session.

Usage:
  python3 log_url.py URL --used --relevance 3
  python3 log_url.py URL --skipped --notes "reason"
"""

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Optional


def get_local_agent_dir() -> Path:
    return Path.cwd() / ".agent"


def get_current_session() -> Optional[dict]:
    local_dir = get_local_agent_dir() / "research"
    session_file = local_dir / "session.json"
    if session_file.exists():
        return json.loads(session_file.read_text())
    return None


def detect_source(url: str) -> str:
    """Detect the source type from URL."""
    if "github.com" in url:
        return "GitHub"
    elif "arxiv.org" in url:
        return "arXiv"
    elif "huggingface.co" in url:
        return "HuggingFace"
    elif "twitter.com" in url or "x.com" in url:
        return "Twitter/X"
    elif "reddit.com" in url:
        return "Reddit"
    elif "youtube.com" in url or "youtu.be" in url:
        return "YouTube"
    elif "medium.com" in url:
        return "Medium"
    elif "dev.to" in url:
        return "Dev.to"
    else:
        return "Web"


def log_url(url: str, used: bool = False, skipped: bool = False,
            relevance: int = 0, notes: str = "", filter_type: str = ""):
    """Log a URL to the session."""
    session = get_current_session()
    if not session:
        print("No active session found. Run agent-init first.")
        return False

    local_dir = get_local_agent_dir() / "research"
    now = datetime.now().strftime("%H:%M")
    source = detect_source(url)

    # Determine status
    if used:
        status = "used"
        status_mark = "Yes"
    elif skipped:
        status = "skipped"
        status_mark = "No"
    else:
        status = "visited"
        status_mark = "-"

    # Log to sources.csv
    sources_file = local_dir / "sources.csv"
    file_exists = sources_file.exists()

    with open(sources_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "source", "url", "filter", "status", "relevance", "notes"])
        writer.writerow([
            datetime.now().isoformat(),
            source,
            url,
            filter_type,
            status,
            relevance if relevance else "",
            notes
        ])

    # Log to session_log.md
    session_log = local_dir / "session_log.md"

    # Check if URL table exists, if not create it
    if session_log.exists():
        content = session_log.read_text()
        if "## URLs Visited" not in content:
            content += "\n\n## URLs Visited\n\n"
            content += "| Time | Source | URL | Filter | Used | Relevance | Notes |\n"
            content += "|------|--------|-----|--------|------|-----------|-------|\n"
            session_log.write_text(content)

    # Append URL row
    with open(session_log, "a") as f:
        relevance_str = str(relevance) if relevance else "-"
        f.write(f"| {now} | {source} | {url} | {filter_type} | {status_mark} | {relevance_str} | {notes} |\n")

    # Print confirmation
    emoji = "link" if status == "visited" else ("white_check_mark" if used else "x")
    print(f"Logged: {url}")
    print(f"   Source: {source}")
    print(f"   Status: {status}")
    if relevance:
        print(f"   Relevance: {relevance}/5")
    if notes:
        print(f"   Notes: {notes}")

    return True


def main():
    parser = argparse.ArgumentParser(description="Log URL to research session")
    parser.add_argument("url", help="The URL to log")
    parser.add_argument("--used", action="store_true", help="Mark as used in output")
    parser.add_argument("--skipped", action="store_true", help="Mark as skipped")
    parser.add_argument("--relevance", type=int, choices=[1, 2, 3, 4, 5],
                        help="Relevance score (1-5)")
    parser.add_argument("--notes", default="", help="Additional notes")
    parser.add_argument("--filter", dest="filter_type", default="",
                        choices=["viral", "groundbreaker", "manual", ""],
                        help="Which filter found this")

    args = parser.parse_args()

    if args.used and args.skipped:
        print("Error: Cannot be both --used and --skipped")
        return

    log_url(
        url=args.url,
        used=args.used,
        skipped=args.skipped,
        relevance=args.relevance or 0,
        notes=args.notes,
        filter_type=args.filter_type
    )


if __name__ == "__main__":
    main()
