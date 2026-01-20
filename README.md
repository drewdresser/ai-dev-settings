# ai-dev-settings

> Reusable, versioned configuration for AI coding tools — get up and running with AI agents in new projects quickly.

**Supported AI Tools:**
- **Claude Code** - CLAUDE.md + agents, commands, hooks, skills
- **Cursor** - .cursorrules + stack-specific rules + command templates
- **Codex** - Global config + AGENTS.md
- **Multi-Project Workflow** - Strategy dashboard for tracking epics/tasks

## Why Use This?

Managing AI coding tool configurations across multiple projects is tedious. This repository provides:

✅ **Consistent AI behavior** across all your projects  
✅ **Pre-configured commands** for common development tasks  
✅ **Strategy-first workflow** for AI-driven development  
✅ **One-command installation** into any project  
✅ **Stack-specific rules** for Python, React, and more  

## Quick Start

### 1. Clone this repository

```bash
# Clone to a location you'll keep it
git clone https://github.com/drewdresser/ai-dev-settings.git ~/ai-dev-settings
cd ~/ai-dev-settings
```

### 2. Install prerequisites

You'll need [just](https://github.com/casey/just) (optional but recommended):

```bash
# macOS
brew install just

# Linux
cargo install just
# or
wget -qO - 'https://proget.makedeb.org/debian-feeds/prebuilt-mpr.pub' | gpg --dearmor | sudo tee /usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg 1> /dev/null
echo "deb [arch=all,$(dpkg --print-architecture) signed-by=/usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg] https://proget.makedeb.org prebuilt-mpr $(lsb_release -cs)" | sudo tee /etc/apt/sources.list.d/prebuilt-mpr.list
sudo apt update
sudo apt install just
```

### 3. Install into your project

From inside your target project directory:

```bash
# Using just (recommended)
just -f ~/ai-dev-settings/justfile install

# Or directly with the script
~/ai-dev-settings/scripts/install_project.sh ~/ai-dev-settings $(pwd)
```

### 4. Link global configs (optional)

```bash
cd ~/ai-dev-settings
just link-global
```

This symlinks global configs into:
- `~/.codex/AGENTS.md`
- `~/.codex/config.toml`
- `~/.claude/settings.json`

### 5. Customize for your project

After installation, edit these files in your project:
1. **CLAUDE.md** - Update project map and common commands
2. **AGENTS.md** - Add project-specific conventions
3. **.cursor/rules/** - Modify stack-specific rules as needed

## Workflow Framework

This repo incorporates the **Multi-Project AI Agent Development Framework** — a structured approach for managing AI-driven development across multiple projects.

**Key concepts:**
- `/strategy/` folder in each project root for strategic documentation
- Vision → OKRs → Epics → Tasks hierarchy
- Architecture Decision Records (ADRs) for preserving decisions
- Agent-first context consumption pattern

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the complete framework specification.

## Stack Configuration

Preconfigured for:

**Python Backend**
- `uv` for dependency management
- `pytest` for testing
- `ruff` for linting/formatting
- `ty` for type checking
- AWS Lambda / ECS deployment

**React Frontend**
- `pnpm` for dependency management
- TypeScript strict mode
- Colocated tests
- AWS Amplify deployment

## File Structure

```
ai-dev-settings/
├── README.md
├── justfile
├── dashboard/                 # Strategy dashboard (optional)
│   ├── server.py              # Dashboard server
│   ├── parser.py              # Markdown parser
│   ├── models.py              # Data models
│   └── index.html             # Dashboard UI
├── docs/
│   └── WORKFLOW.md            # Multi-project AI workflow framework
├── project/                   # Files to install into projects
│   ├── AGENTS.md
│   └── claude/
│       ├── CLAUDE.md
│       ├── agents/            # Specialized agent definitions
│       ├── commands/          # Reusable command templates
│       ├── hooks/             # Event hooks and scripts
│       └── skills/            # Skill definitions
├── global/
│   ├── codex/
│   │   ├── AGENTS.md
│   │   └── config.toml
│   └── claude/
│       └── settings.json
└── scripts/
    ├── install_project.sh
    └── link_global.sh
```

### Project Strategy Structure (installed per-project)

When following the workflow framework, each project should contain:

```
your-project/
├── strategy/
│   ├── VISION.md              # Strategic foundation
│   ├── OKRs.md                # Current quarter objectives
│   ├── epics/
│   │   └── epic-name.md       # Feature/initiative epics
│   ├── tasks/
│   │   └── epic-name-001-task.md  # Specific tasks
│   └── adrs/
│       └── 001-decision.md    # Architecture decisions
├── AGENTS.md
├── CLAUDE.md
├── .claude/
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   └── skills/
└── ... (rest of project)
```

## What Gets Installed

When you run `just install`, these files are copied to your project:

| File | Tool | Purpose |
|------|------|---------|
| `AGENTS.md` | Codex, Cursor | Universal behavior contract |
| `CLAUDE.md` | Claude Code | Project-specific instructions |
| `.claude/agents/*.md` | Claude Code | Specialized agent definitions |
| `.claude/commands/*.md` | Claude Code | Reusable command templates |
| `.claude/hooks/` | Claude Code | Event hooks and scripts |
| `.claude/skills/` | Claude Code | Skill definitions |
| `.cursorrules` | Cursor | IDE-level behavior |
| `.cursor/rules/*.mdc` | Cursor | Stack-specific rules |
| `.cursor/commands/*.md` | Cursor | Reusable prompt templates |

## Customization

After installing, customize the files for your specific project:

1. **CLAUDE.md**: Update the project map and common commands
2. **AGENTS.md**: Add project-specific conventions
3. **.cursor/rules/**: Add or modify stack-specific rules

## Example Walkthrough

Here's a complete example of setting up a new Python project:

```bash
# 1. Create your new project
mkdir my-awesome-api
cd my-awesome-api
git init

# 2. Install ai-dev-settings
just -f ~/ai-dev-settings/justfile install

# 3. Verify installation
ls -la
# You should see: AGENTS.md, CLAUDE.md, .claude/, .cursorrules, .cursor/

# 4. Customize CLAUDE.md for your project
# Edit the "Project Map" section to match your structure

# 5. Start using AI tools
# In Claude Code, you can now use commands like:
# - `/rapid` for fast iterations
# - `/architect` for design decisions
# - `/lint-fix` to fix linting issues
# - `/add-tests` to generate tests
```

## Troubleshooting

### Installation script fails

**Problem**: Permission denied when running install script

**Solution**:
```bash
chmod +x ~/ai-dev-settings/scripts/*.sh
```

### `just` command not found

**Problem**: `just` is not installed

**Solution**: Either install `just` (see Quick Start) or use the script directly:
```bash
~/ai-dev-settings/scripts/install_project.sh ~/ai-dev-settings $(pwd)
```

### Files not showing up in my project

**Problem**: Files weren't copied

**Solution**: Make sure you're running the command from your project directory:
```bash
cd /path/to/your/project
just -f ~/ai-dev-settings/justfile install
```

### Global configs not working

**Problem**: AI tools don't see global configs

**Solution**: Verify symlinks were created:
```bash
ls -la ~/.codex/
ls -la ~/.claude/
# You should see symlinks pointing to your ai-dev-settings directory
```

## Strategy Dashboard

The dashboard provides a visual overview of epics and tasks across multiple projects that use the `/strategy/` folder structure.

### Running the Dashboard

```bash
# Auto-discover projects with /strategy/ folders in parent directory
uv run python dashboard/server.py

# Specify projects explicitly
uv run python dashboard/server.py --projects myproject,another-project

# Specify a different projects directory
uv run python dashboard/server.py --dir ~/Code --projects proj1,proj2

# Using environment variables
DASHBOARD_PROJECTS=proj1,proj2 DASHBOARD_DIR=~/Code uv run python dashboard/server.py
```

### Configuration Options

| Option | Environment Variable | Description |
|--------|---------------------|-------------|
| `--port`, `-p` | `DASHBOARD_PORT` | Port to run on (default: 8080) |
| `--dir`, `-d` | `DASHBOARD_DIR` | Directory containing projects |
| `--projects` | `DASHBOARD_PROJECTS` | Comma-separated project names |

If `--projects` is not specified, the dashboard auto-discovers directories containing `/strategy/` folders.

## Prerequisites

- [just](https://github.com/casey/just) command runner (optional but recommended)
- Bash shell (Linux/macOS/WSL)
- One or more AI coding tools:
  - [Claude Code](https://www.anthropic.com/claude/code) (by Anthropic)
  - [Cursor](https://cursor.sh/) (AI-powered code editor)
  - [Codex](https://github.com/github/codex) (GitHub Copilot Workspace)
- For dashboard: Python 3.8+ and [uv](https://github.com/astral-sh/uv)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Reference Repos

Inspired by:
- [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)
- [yixin0829/ai-coding-templates](https://github.com/yixin0829/ai-coding-templates)
- [inmve/awesome-ai-coding-techniques](https://github.com/inmve/coding-with-ai)
