#!/usr/bin/env bash
set -euo pipefail

PROFILE="${1:-ship}"
SETTINGS_REPO_ROOT="${2:-}"

if [[ -z "$SETTINGS_REPO_ROOT" ]]; then
  echo "Usage: install_project.sh <profile> <settings_repo_root>"
  exit 1
fi

SRC="$SETTINGS_REPO_ROOT/profiles/$PROFILE"
if [[ ! -d "$SRC" ]]; then
  echo "Unknown profile: $PROFILE (expected $SRC to exist)"
  exit 1
fi

# Target is current working directory (project repo)
DST="$(pwd)"

copy_file() {
  local from="$1"
  local to="$2"
  mkdir -p "$(dirname "$to")"
  cp -f "$from" "$to"
  echo "  Copied: $to"
}

echo "Installing profile '$PROFILE' into: $DST"
echo ""

# Shared truth (AGENTS.md)
if [[ -f "$SRC/AGENTS.md" ]]; then
  copy_file "$SRC/AGENTS.md" "$DST/AGENTS.md"
fi

# Claude Code
if [[ -d "$SRC/claude" ]]; then
  echo "Installing Claude Code config..."
  if [[ -f "$SRC/claude/CLAUDE.md" ]]; then
    copy_file "$SRC/claude/CLAUDE.md" "$DST/CLAUDE.md"
  fi
  if [[ -f "$SRC/claude/.claude/settings.json" ]]; then
    copy_file "$SRC/claude/.claude/settings.json" "$DST/.claude/settings.json"
  fi
fi

# Cursor
if [[ -d "$SRC/cursor" ]]; then
  echo "Installing Cursor config..."
  if [[ -f "$SRC/cursor/.cursorrules" ]]; then
    copy_file "$SRC/cursor/.cursorrules" "$DST/.cursorrules"
  fi
  if [[ -f "$SRC/cursor/.cursor/rules/python-backend.mdc" ]]; then
    copy_file "$SRC/cursor/.cursor/rules/python-backend.mdc" "$DST/.cursor/rules/python-backend.mdc"
  fi
  if [[ -f "$SRC/cursor/.cursor/rules/react-frontend.mdc" ]]; then
    copy_file "$SRC/cursor/.cursor/rules/react-frontend.mdc" "$DST/.cursor/rules/react-frontend.mdc"
  fi
  if [[ -d "$SRC/cursor/.cursor/commands" ]]; then
    mkdir -p "$DST/.cursor/commands"
    for cmd in "$SRC/cursor/.cursor/commands/"*.md; do
      if [[ -f "$cmd" ]]; then
        copy_file "$cmd" "$DST/.cursor/commands/$(basename "$cmd")"
      fi
    done
  fi
fi

echo ""
echo "Done!"
echo ""
echo "Files to commit:"
echo "  - AGENTS.md"
echo "  - CLAUDE.md"
echo "  - .claude/settings.json"
echo "  - .cursorrules"
echo "  - .cursor/rules/*.mdc"
echo "  - .cursor/commands/*.md"

