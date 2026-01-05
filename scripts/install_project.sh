#!/usr/bin/env bash
set -euo pipefail

SETTINGS_REPO_ROOT="${1:-}"
TARGET_DIR="${2:-}"

if [[ -z "$SETTINGS_REPO_ROOT" ]]; then
  echo "Usage: install_project.sh <settings_repo_root> <target_dir>"
  exit 1
fi

if [[ -z "$TARGET_DIR" ]]; then
  echo "Usage: install_project.sh <settings_repo_root> <target_dir>"
  exit 1
fi

SRC="$SETTINGS_REPO_ROOT/project"
if [[ ! -d "$SRC" ]]; then
  echo "Project source not found: $SRC"
  exit 1
fi

# Target is the directory where just was invoked from
DST="$TARGET_DIR"

copy_file() {
  local from="$1"
  local to="$2"
  mkdir -p "$(dirname "$to")"
  cp -f "$from" "$to"
  echo "  Copied: $to"
}

echo "Installing project config into: $DST"
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
  
  # Copy agents
  if [[ -d "$SRC/claude/agents" ]]; then
    for agent in "$SRC/claude/agents/"*.md; do
      if [[ -f "$agent" ]]; then
        copy_file "$agent" "$DST/.claude/agents/$(basename "$agent")"
      fi
    done
  fi
  
  # Copy commands
  if [[ -d "$SRC/claude/commands" ]]; then
    for cmd in "$SRC/claude/commands/"*.md; do
      if [[ -f "$cmd" ]]; then
        copy_file "$cmd" "$DST/.claude/commands/$(basename "$cmd")"
      fi
    done
  fi
  
  # Copy hooks
  if [[ -f "$SRC/claude/hooks/hooks.json" ]]; then
    copy_file "$SRC/claude/hooks/hooks.json" "$DST/.claude/hooks/hooks.json"
  fi
  if [[ -d "$SRC/claude/hooks/scripts" ]]; then
    for script in "$SRC/claude/hooks/scripts/"*.sh; do
      if [[ -f "$script" ]]; then
        copy_file "$script" "$DST/.claude/hooks/scripts/$(basename "$script")"
      fi
    done
  fi
  
  # Copy skills
  if [[ -d "$SRC/claude/skills" ]]; then
    for skill_dir in "$SRC/claude/skills/"*/; do
      if [[ -d "$skill_dir" ]]; then
        skill_name=$(basename "$skill_dir")
        if [[ -f "$skill_dir/skill.md" ]]; then
          copy_file "$skill_dir/skill.md" "$DST/.claude/skills/$skill_name/skill.md"
        fi
      fi
    done
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
echo "  - .claude/agents/*.md"
echo "  - .claude/commands/*.md"
echo "  - .claude/hooks/"
echo "  - .claude/skills/"
echo "  - .cursorrules"
echo "  - .cursor/rules/*.mdc"
echo "  - .cursor/commands/*.md"
