# Project Instructions for Claude Code

Read AGENTS.md first for the full working agreement.

## Strategy-First Workflow

If a `/strategy/` folder exists, read these files in order before starting work:

1. `/strategy/VISION.md` — Strategic context
2. `/strategy/OKRs.md` — Current priorities
3. `/strategy/epics/<relevant-epic>.md` — Epic details
4. `/strategy/tasks/<assigned-task>.md` — Specific task
5. `/strategy/adrs/` — Relevant architectural decisions

This gives you full context from strategy down to implementation. Ask before creating ADRs.

## Project Map

<!-- Fill in your project structure -->

```
project/
├── strategy/         # Strategic documentation (if using workflow)
│   ├── VISION.md
│   ├── OKRs.md
│   ├── epics/
│   ├── tasks/
│   └── adrs/
├── src/              # Python backend source
│   └── ...
├── tests/            # Python tests
├── frontend/         # React frontend
│   ├── src/
│   └── ...
├── pyproject.toml    # Python dependencies (uv)
└── package.json      # Frontend dependencies (pnpm)
```

## Common Commands

### Python Backend

```bash
# Test
uv run pytest

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty
```

### React Frontend

```bash
# Dev
pnpm dev

# Test
pnpm test

# Lint
pnpm lint

# Build
pnpm build
```

## Conventions

- Keep diffs small and reviewable.
- Prefer explicit types for public interfaces.
- Don't change lockfiles unless necessary.
- Ask before making changes to multiple files.
- When completing tasks, update status in `/strategy/tasks/`.
- Check `/strategy/adrs/` before making architectural decisions.

## AWS Deployment Notes

- Frontend deploys via AWS Amplify
- Backend runs on AWS Lambda or ECS
- Never commit AWS credentials

