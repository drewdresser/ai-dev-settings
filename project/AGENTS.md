# Agent Working Agreement

## Strategy-First Workflow

If a `/strategy/` folder exists in the project root, follow the **AI Agent Handoff Pattern**:

1. Read `/strategy/VISION.md` for strategic context
2. Read `/strategy/OKRs.md` to understand current priorities
3. Read `/strategy/EPICS.md` to see project status, work order, and what to work on next
4. Read relevant epic from `/strategy/epics/`
5. Read specific task from `/strategy/tasks/`
6. Check `/strategy/adrs/` for relevant architectural decisions

This ensures you have full context before making changes. The `EPICS.md` file is especially helpful when no specific task is assigned—it shows project status at a glance and recommends the next piece of work. ADRs prevent revisiting settled questions.

## Bias to Shipping

- If a refactor reduces future risk and is localized, do it.
- If a missing test is the only blocker, add the test.
- Prefer "make it correct, then fast".
- Don't let perfect be the enemy of good.

## Strong Conventions

- Keep public interfaces stable unless requested.
- Enforce typing / linting norms for touched code.
- If introducing a new module, include a minimal docstring header.
- Clean up obvious code smells in files you're already modifying.
- **No inline imports.** All imports go at the top of the file. Never import inside functions, methods, or conditional blocks.

## Output Style

- Provide copy-paste commands for verify steps.
- Summarize in: (1) what you changed, (2) how to test, (3) any follow-ups.

---

## Defaults

- Prefer small, reviewable diffs. No drive-by refactors.
- When unsure about intent, make a reasonable assumption and state it.
- Always keep changes consistent with existing style and architecture.
- Don't invent APIs or files that don't exist; search first.

## Dev Loop

- Before coding: state plan in 3-7 bullets.
- After coding: state what changed + how to verify (exact commands).
- Run the smallest relevant test subset. Add tests if coverage is missing.
- When completing a task, update its status in `/strategy/tasks/`.
- When making architectural decisions, create an ADR in `/strategy/adrs/`.
- ALWAYS use #context7 MCP Server to read relevant documentation. Do this every time you are working with a language, framework, library etc. Never assume that you know the answer as these things change frequently. Your training date is in the past so your knowledge is likely out of date, even if it is a technology you are familiar with.

## Risk Posture

- Localized refactors are OK if they improve the code you're touching.
- Avoid mass formatting / global renames unless explicitly asked.
- Don't modify lockfiles unless necessary.

## Security / Data

- Never print secrets. Treat `.env*`, credentials, keys, tokens as sensitive.
- Don't exfiltrate large proprietary files into chat.
- Respect `.gitignore` patterns.

---

## Stack: Python Backend

### Commands

```bash
# Run tests
uv run pytest

# Run specific test
uv run pytest tests/test_foo.py::test_bar -v

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty
```

### Conventions

- Use `uv` for dependency management (pyproject.toml).
- Prefer explicit type hints for public interfaces.
- Tests live in `tests/` directory, mirror source structure.
- Use `pytest` fixtures over setup/teardown.
- Add type hints to functions you modify.

### Standalone Scripts (PEP 723)

For one-off operations, data processing, or utility tasks, write Python scripts with inline dependencies:

```python
# /// script
# dependencies = ["requests", "pandas"]
# ///
import requests
import pandas as pd
# ... script code
```

Run with: `uv run scripts/my_script.py`

- Store all standalone scripts in `scripts/` folder
- Use inline dependencies—don't modify pyproject.toml for scripts
- Great for migrations, data checks, debugging, one-time tasks

---

## Stack: React Frontend

### Commands

```bash
# Install dependencies
pnpm install

# Dev server
pnpm dev

# Run tests
pnpm test

# Lint
pnpm lint

# Type check
pnpm typecheck

# Build
pnpm build
```

### Conventions

- TypeScript strict mode enabled.
- Functional components with hooks.
- Colocate tests with components (`Component.test.tsx`).
- Prefer named exports over default exports.

---

## AWS Deployment

- **Frontend**: AWS Amplify (auto-deploy from main branch)
- **Backend**: AWS Lambda (serverless) or ECS (containerized)
- Never hardcode AWS credentials; use environment variables or IAM roles.
- Prefer infrastructure-as-code (CDK, SAM, or Terraform).

