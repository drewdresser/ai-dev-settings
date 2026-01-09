# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Strategy Dashboard Server

A lightweight HTTP server for viewing epics and tasks across multiple projects.

Usage:
    uv run python dashboard/server.py --projects proj1,proj2,proj3
    uv run python dashboard/server.py --dir /path/to/projects
    DASHBOARD_PROJECTS=proj1,proj2 uv run python dashboard/server.py

If no projects are specified, auto-discovers directories with /strategy/ folders.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

# Add dashboard directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parser import scan_all_projects

# Default configuration
DEFAULT_PORT = 8080
CACHE_TTL = 5  # seconds

# Runtime configuration (set in main())
PROJECTS_DIR: Path = Path(".")
PROJECT_NAMES: list[str] = []

# Cache for parsed data
_cache: dict = {"data": None, "timestamp": 0}


def get_data() -> dict:
    """Get project data, using cache if still valid."""
    now = time.time()
    if _cache["data"] is None or (now - _cache["timestamp"]) > CACHE_TTL:
        projects, epics, tasks = scan_all_projects(PROJECTS_DIR, PROJECT_NAMES)
        _cache["data"] = {
            "projects": [p.to_dict() for p in projects],
            "epics": [e.to_dict() for e in epics],
            "tasks": [t.to_dict() for t in tasks],
            "refreshedAt": datetime.now(timezone.utc).isoformat(),
        }
        _cache["timestamp"] = now
    return _cache["data"]


class DashboardHandler(SimpleHTTPRequestHandler):
    """Custom handler for the dashboard server."""

    def __init__(self, *args, **kwargs):
        # Set the directory to serve static files from
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.serve_index()
        elif self.path == "/api/data":
            self.serve_api_data()
        elif self.path == "/favicon.ico":
            # Return empty response for favicon requests
            self.send_response(204)
            self.end_headers()
        else:
            super().do_GET()

    def serve_index(self):
        """Serve the main index.html file."""
        index_path = Path(__file__).parent / "index.html"
        try:
            content = index_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", len(content))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "index.html not found")

    def serve_api_data(self):
        """Serve the JSON API data."""
        data = get_data()
        content = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(content))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        """Suppress default logging for cleaner output."""
        # args[0] might be a string (request path) or HTTPStatus (error code)
        if args and isinstance(args[0], str) and "/api/data" in args[0]:
            return  # Suppress API request logs
        super().log_message(format, *args)


def discover_projects(projects_dir: Path) -> list[str]:
    """Auto-discover projects with /strategy/ folders."""
    discovered = []
    if not projects_dir.exists():
        return discovered

    for item in projects_dir.iterdir():
        if item.is_dir() and (item / "strategy").is_dir():
            discovered.append(item.name)

    return sorted(discovered)


def main():
    """Run the dashboard server."""
    global PROJECTS_DIR, PROJECT_NAMES

    parser = argparse.ArgumentParser(
        description="Strategy Dashboard Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --projects myproject,another-project
  %(prog)s --dir ~/Code --projects proj1,proj2
  %(prog)s --dir ~/Code  # auto-discovers projects with /strategy/ folders
  DASHBOARD_PROJECTS=proj1,proj2 %(prog)s
        """,
    )
    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=int(os.environ.get("DASHBOARD_PORT", DEFAULT_PORT)),
        help=f"Port to run on (default: {DEFAULT_PORT}, or DASHBOARD_PORT env var)",
    )
    parser.add_argument(
        "--dir",
        "-d",
        type=Path,
        default=Path(
            os.environ.get(
                "DASHBOARD_DIR", str(Path(__file__).parent.parent.parent)
            )
        ),
        help="Directory containing projects (default: parent of ai-dev-settings, or DASHBOARD_DIR env var)",
    )
    parser.add_argument(
        "--projects",
        type=str,
        default=os.environ.get("DASHBOARD_PROJECTS", ""),
        help="Comma-separated list of project directory names (or DASHBOARD_PROJECTS env var). "
        "If not specified, auto-discovers projects with /strategy/ folders.",
    )
    args = parser.parse_args()

    # Set global configuration
    PROJECTS_DIR = args.dir.resolve()

    # Determine project names: CLI/env > auto-discovery
    if args.projects:
        PROJECT_NAMES = [p.strip() for p in args.projects.split(",") if p.strip()]
    else:
        PROJECT_NAMES = discover_projects(PROJECTS_DIR)
        if not PROJECT_NAMES:
            print(f"No projects with /strategy/ folders found in: {PROJECTS_DIR}")
            print("Specify projects with --projects or DASHBOARD_PROJECTS env var")
            sys.exit(1)

    # Initial scan to show stats
    projects, epics, tasks = scan_all_projects(PROJECTS_DIR, PROJECT_NAMES)

    print("Strategy Dashboard")
    print("=" * 40)
    print(f"Projects directory: {PROJECTS_DIR}")
    if args.projects:
        print(f"Scanning (specified): {', '.join(PROJECT_NAMES)}")
    else:
        print(f"Scanning (auto-discovered): {', '.join(PROJECT_NAMES)}")
    print(f"Found: {len(epics)} epics, {len(tasks)} tasks")
    print("=" * 40)
    print(f"Dashboard running at http://localhost:{args.port}")
    print("Press Ctrl+C to stop\n")

    server = HTTPServer(("", args.port), DashboardHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
