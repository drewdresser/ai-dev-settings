#!/usr/bin/env bash
set -euo pipefail

SETTINGS_REPO_ROOT="${1:-}"
if [[ -z "$SETTINGS_REPO_ROOT" ]]; then
  echo "Usage: link_global.sh <settings_repo_root>"
  exit 1
fi

echo "Linking global configs from: $SETTINGS_REPO_ROOT"
echo ""

# Codex global
if [[ -d "$SETTINGS_REPO_ROOT/global/codex" ]]; then
  mkdir -p "$HOME/.codex"
  
  if [[ -f "$SETTINGS_REPO_ROOT/global/codex/AGENTS.md" ]]; then
    ln -sf "$SETTINGS_REPO_ROOT/global/codex/AGENTS.md" "$HOME/.codex/AGENTS.md"
    echo "  Linked: ~/.codex/AGENTS.md"
  fi
  
  if [[ -f "$SETTINGS_REPO_ROOT/global/codex/config.toml" ]]; then
    ln -sf "$SETTINGS_REPO_ROOT/global/codex/config.toml" "$HOME/.codex/config.toml"
    echo "  Linked: ~/.codex/config.toml"
  fi
fi

# Claude global
if [[ -d "$SETTINGS_REPO_ROOT/global/claude" ]]; then
  mkdir -p "$HOME/.claude"
  
  if [[ -f "$SETTINGS_REPO_ROOT/global/claude/settings.json" ]]; then
    ln -sf "$SETTINGS_REPO_ROOT/global/claude/settings.json" "$HOME/.claude/settings.json"
    echo "  Linked: ~/.claude/settings.json"
  fi
fi

echo ""
echo "Done!"
echo ""
echo "Linked global configs:"
echo "  ~/.codex/AGENTS.md -> global/codex/AGENTS.md"
echo "  ~/.codex/config.toml -> global/codex/config.toml"
echo "  ~/.claude/settings.json -> global/claude/settings.json"

