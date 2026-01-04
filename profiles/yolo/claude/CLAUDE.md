# Project Instructions for Claude Code

Read AGENTS.md first for the full working agreement.

## Strategy-First Workflow

If a `/strategy/` folder exists, read these files in order before starting work:

1. `/strategy/VISION.md` — Strategic context
2. `/strategy/OKRs.md` — Current priorities
3. `/strategy/epics/<relevant-epic>.md` — Epic details
4. `/strategy/tasks/<assigned-task>.md` — Specific task
5. `/strategy/adrs/` — Relevant architectural decisions

This gives you full context from strategy down to implementation. Proactively create ADRs and break down epics into tasks.

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

# Lint and fix
uv run ruff check . --fix

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

# Test with coverage
pnpm test --coverage

# Lint and fix
pnpm lint --fix

# Type check
pnpm typecheck

# Build
pnpm build
```

## Conventions

- Broad refactors are encouraged if they improve code quality.
- Add type hints to all functions you touch.
- Add tests for new and existing untested code paths.
- Proactively clean up dead code and tech debt.
- Suggest further improvements after completing tasks.
- When completing tasks, update status in `/strategy/tasks/`.
- Proactively create ADRs in `/strategy/adrs/` for architectural decisions.
- Break down epics into tasks in `/strategy/tasks/` as needed.

## AWS Deployment Notes

- Frontend deploys via AWS Amplify
- Backend runs on AWS Lambda or ECS
- Never commit AWS credentials
- Prefer infrastructure-as-code (CDK/SAM/Terraform)
- Keep infrastructure in sync with application changes

