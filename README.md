# ai-dev-settings

Reusable, versioned configuration for AI coding tools:

- **AGENTS.md** (shared truth): Codex + Cursor (+ referenced by Claude)
- **Claude Code**: CLAUDE.md + agents, commands, hooks, skills
- **Cursor**: .cursorrules + .cursor/rules/*.mdc + reusable command prompts
- **Codex**: Global config + AGENTS.md
- **Workflow**: Multi-project AI agent development framework (see [docs/WORKFLOW.md](docs/WORKFLOW.md))
- **Dashboard**: Visual strategy dashboard for tracking epics/tasks across projects

## Quick Start

### Install into a project

From inside your target project directory:

```bash
# Using just (recommended)
just -f /path/to/ai-dev-settings/justfile install

# Or directly with the script
/path/to/ai-dev-settings/scripts/install_project.sh /path/to/ai-dev-settings
```

### Link global configs

```bash
cd /path/to/ai-dev-settings
just link-global
```

This symlinks global configs into:
- `~/.codex/AGENTS.md`
- `~/.codex/config.toml`
- `~/.claude/settings.json`

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
- Bash shell

## Reference Repos

Inspired by:
- [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)
- [yixin0829/ai-coding-templates](https://github.com/yixin0829/ai-coding-templates)
- [inmve/awesome-ai-coding-techniques](https://github.com/inmve/coding-with-ai)
