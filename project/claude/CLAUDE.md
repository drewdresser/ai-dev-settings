# Project Instructions for Claude Code

Read AGENTS.md first for the full working agreement.

## Strategy-First Workflow

If a `/strategy/` folder exists, read these files in order before starting work:

1. `/strategy/VISION.md` — Strategic context
2. `/strategy/OKRs.md` — Current priorities
3. `/strategy/EPICS.md` — Project status, work order, and recommended next epic
4. `/strategy/epics/<relevant-epic>.md` — Epic details
5. `/strategy/tasks/<assigned-task>.md` — Specific task
6. `/strategy/adrs/` — Relevant architectural decisions

This gives you full context from strategy down to implementation. The `EPICS.md` file is your go-to for understanding project status and deciding what to work on next. Create ADRs when making significant architectural decisions.

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

# Test with coverage
uv run pytest --cov

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty

# Run standalone script
uv run scripts/my_script.py
```

#### Standalone Scripts (PEP 723)

For one-off tasks, data processing, or utility operations, write scripts with inline dependencies:

```python
# /// script
# dependencies = ["requests", "pandas"]
# ///
import requests
import pandas as pd
# ... script code
```

- Store scripts in `scripts/` folder
- Use inline dependencies instead of modifying pyproject.toml
- Ideal for migrations, data checks, debugging, one-time operations

### React Frontend

```bash
# Dev
pnpm dev

# Test
pnpm test

# Lint
pnpm lint

# Type check
pnpm typecheck

# Build
pnpm build
```

## Conventions

- Keep diffs small and reviewable.
- Prefer explicit types for public interfaces.
- Add tests for new functionality.
- Clean up code smells in files you're modifying.
- **No inline imports.** All imports at the top of the file, never inside functions or conditionals.
- When completing tasks, update status in `/strategy/tasks/`.
- Create ADRs in `/strategy/adrs/` for significant architectural decisions.
- ALWAYS use #context7 MCP Server to read relevant documentation. Do this every time you are working with a language, framework, library etc. Never assume that you know the answer as these things change frequently. Your training date is in the past so your knowledge is likely out of date, even if it is a technology you are familiar with.

## AWS Deployment Notes

- Frontend deploys via AWS Amplify
- Backend runs on AWS Lambda or ECS
- Never commit AWS credentials
- Prefer infrastructure-as-code using AWS CDK in Python

