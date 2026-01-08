# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Strategy Dashboard Server

A lightweight HTTP server for viewing epics and tasks across multiple projects.
Run with: uv run python dashboard/server.py
"""

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

# Add dashboard directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parser import scan_all_projects

# Configuration
PROJECTS_DIR = Path(__file__).parent.parent.parent  # ../../ (parent of ai-dev-settings)
PROJECT_NAMES = ["aws-solutions-architect-bench", "signal-shift", "biotech-game"]
PORT = 8080
CACHE_TTL = 5  # seconds

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


def main():
    """Run the dashboard server."""
    parser = argparse.ArgumentParser(description="Strategy Dashboard Server")
    parser.add_argument(
        "--port", "-p", type=int, default=PORT, help=f"Port to run on (default: {PORT})"
    )
    args = parser.parse_args()
    port = args.port

    # Initial scan to show stats
    projects, epics, tasks = scan_all_projects(PROJECTS_DIR, PROJECT_NAMES)

    print("Strategy Dashboard")
    print("=" * 40)
    print(f"Projects directory: {PROJECTS_DIR}")
    print(f"Scanning: {', '.join(PROJECT_NAMES)}")
    print(f"Found: {len(epics)} epics, {len(tasks)} tasks")
    print("=" * 40)
    print(f"Dashboard running at http://localhost:{port}")
    print("Press Ctrl+C to stop\n")

    server = HTTPServer(("", port), DashboardHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
