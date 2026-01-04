# Agent Working Agreement (SAFE)

## Strategy-First Workflow

If a `/strategy/` folder exists in the project root, follow the **AI Agent Handoff Pattern**:

1. Read `/strategy/VISION.md` for strategic context
2. Read `/strategy/OKRs.md` to understand current priorities
3. Read relevant epic from `/strategy/epics/`
4. Read specific task from `/strategy/tasks/`
5. Check `/strategy/adrs/` for relevant architectural decisions

This ensures you have full context before making changes. ADRs prevent revisiting settled questions.

## Defaults

- Prefer small, reviewable diffs. No drive-by refactors.
- When unsure about intent, ask 1 tight question; otherwise make a reasonable assumption and state it.
- Always keep changes consistent with existing style and architecture.
- Don't invent APIs or files that don't exist; search first.

## Dev Loop

- Before coding: state plan in 3-7 bullets.
- After coding: state what changed + how to verify (exact commands).
- If tests exist, run the smallest relevant subset; if not possible, explain what would be run.
- When completing a task, update its status in `/strategy/tasks/`.
- When making architectural decisions, propose an ADR in `/strategy/adrs/` (ask before creating).

## Risk Posture

- Avoid destructive actions.
- Avoid mass formatting / global renames unless explicitly asked.
- Don't modify lockfiles unless necessary.
- Ask before making changes that affect multiple files.

## Security / Data

- Never print secrets. Treat `.env*`, credentials, keys, tokens as sensitive.
- Don't exfiltrate large proprietary files into chat.
- Respect `.gitignore` patterns.

## Output Style

- Be terse.
- Prefer patch-style guidance and file paths.
- No long essays unless asked.

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

---

## AWS Deployment

- **Frontend**: AWS Amplify (auto-deploy from main branch)
- **Backend**: AWS Lambda (serverless) or ECS (containerized)
- Never hardcode AWS credentials; use environment variables or IAM roles.

