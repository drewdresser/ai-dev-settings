# ai-dev-settings

Personal, versioned configuration for AI coding tools:

- **AGENTS.md** (shared truth): Codex + Cursor (+ referenced by Claude)
- **Claude Code**: CLAUDE.md + .claude/settings.json
- **Cursor**: .cursorrules + .cursor/rules/*.mdc + reusable command prompts
- **Codex**: Global config + AGENTS.md

## Quick Start

### Install into a project

From inside your target project directory:

```bash
# Using just (recommended)
just -f /path/to/ai-dev-settings/justfile install ship

# Or directly with the script
/path/to/ai-dev-settings/scripts/install_project.sh ship /path/to/ai-dev-settings
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

## Profiles

| Profile | Risk Posture | Refactors | Tests |
|---------|--------------|-----------|-------|
| **safe** | Conservative, ask before changing | Only if explicit | Run existing |
| **ship** | Pragmatic, localized changes OK | If reduces risk | Add if missing |
| **yolo** | Assertive, broad changes allowed | Proactive cleanup | Required |

### safe

Best for: Late-night PRs, unfamiliar codebases, production hotfixes.

- Minimal diffs, no drive-by refactors
- Ask before multi-file changes
- Never modify lockfiles

### ship

Best for: Day-to-day development, feature work.

- Localized refactors are OK
- Add tests if missing
- Clean up code smells in touched files

### yolo

Best for: Tech debt cleanup, greenfield projects, major refactors.

- Broad refactors encouraged
- Proactively add type hints and tests
- Suggest further improvements

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
├── profiles/
│   ├── safe/
│   │   ├── AGENTS.md
│   │   ├── claude/
│   │   │   ├── CLAUDE.md
│   │   │   └── .claude/settings.json
│   │   └── cursor/
│   │       ├── .cursorrules
│   │       └── .cursor/
│   │           ├── rules/
│   │           │   ├── python-backend.mdc
│   │           │   └── react-frontend.mdc
│   │           └── commands/
│   │               ├── plan.md
│   │               ├── patch.md
│   │               └── test.md
│   ├── ship/
│   │   └── ... (same structure)
│   └── yolo/
│       └── ... (same structure)
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

## What Gets Installed

When you run `just install <profile>`, these files are copied to your project:

| File | Tool | Purpose |
|------|------|---------|
| `AGENTS.md` | Codex, Cursor | Universal behavior contract |
| `CLAUDE.md` | Claude Code | Project-specific instructions |
| `.claude/settings.json` | Claude Code | Permissions and hooks |
| `.cursorrules` | Cursor | IDE-level behavior |
| `.cursor/rules/*.mdc` | Cursor | Stack-specific rules |
| `.cursor/commands/*.md` | Cursor | Reusable prompt templates |

## Customization

After installing, customize the files for your specific project:

1. **CLAUDE.md**: Update the project map and common commands
2. **AGENTS.md**: Add project-specific conventions
3. **.cursor/rules/**: Add or modify stack-specific rules

## Prerequisites

- [just](https://github.com/casey/just) command runner (optional but recommended)
- Bash shell

## Reference Repos

Inspired by:
- [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)
- [yixin0829/ai-coding-templates](https://github.com/yixin0829/ai-coding-templates)
- [inmve/awesome-ai-coding-techniques](https://github.com/inmve/coding-with-ai)

