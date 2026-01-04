# Agent Working Agreement (YOLO)

All SHIP rules apply, plus:

## Strategy-First Workflow

If a `/strategy/` folder exists in the project root, follow the **AI Agent Handoff Pattern**:

1. Read `/strategy/VISION.md` for strategic context
2. Read `/strategy/OKRs.md` to understand current priorities
3. Read relevant epic from `/strategy/epics/`
4. Read specific task from `/strategy/tasks/`
5. Check `/strategy/adrs/` for relevant architectural decisions

This ensures you have full context before making changes. ADRs prevent revisiting settled questions.

## Permissions

- You may apply broad refactors if they clearly improve the codebase and are mechanically safe.
- You may update formatting/lint config if it unblocks consistency.
- Proactively clean up dead code, unused imports, and obvious tech debt.
- Consolidate duplicate code when you see it.
- You may create new ADRs in `/strategy/adrs/` when making significant architectural decisions.
- You may break down epics into tasks in `/strategy/tasks/` proactively.

## Guardrails

- Still do not expose secrets.
- Still keep diffs logically grouped (no "everything everywhere all at once").
- If changes are large, produce a staged plan (PR1, PR2, PR3) and implement PR1 only unless asked.
- Run tests after significant changes.

## Aggressive Improvements

- Add missing type hints throughout files you touch.
- Add missing tests for untested code paths.
- Improve error messages and logging.
- Refactor for clarity even if not explicitly asked.

---

## Defaults

- Prefer clear, well-structured diffs over minimal changes.
- Make reasonable assumptions and state them; don't block on minor uncertainties.
- Keep changes consistent with existing patterns, but improve patterns where beneficial.

## Dev Loop

- Before coding: state plan in 3-7 bullets.
- After coding: state what changed + how to verify (exact commands).
- Always run tests. Add tests for new code paths.
- When completing a task, update its status in `/strategy/tasks/`.
- When making architectural decisions, create an ADR in `/strategy/adrs/`.

## Risk Posture

- Broad refactors are allowed if they improve code quality.
- Mass formatting is OK if it improves consistency.
- Update lockfiles if dependencies need updating.
- Proactively fix issues you discover.

## Security / Data

- Never print secrets. Treat `.env*`, credentials, keys, tokens as sensitive.
- Don't exfiltrate large proprietary files into chat.
- Respect `.gitignore` patterns.

## Output Style

- Provide copy-paste commands for verify steps.
- Summarize in: (1) what you changed, (2) how to test, (3) any follow-ups.
- Include suggestions for further improvements.

---

## Stack: Python Backend

### Commands

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

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
- Explicit type hints required for all functions.
- Tests live in `tests/` directory, mirror source structure.
- Use `pytest` fixtures over setup/teardown.
- Aim for high test coverage on business logic.

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

# Run tests with coverage
pnpm test --coverage

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
- Use React Query or similar for data fetching.

---

## AWS Deployment

- **Frontend**: AWS Amplify (auto-deploy from main branch)
- **Backend**: AWS Lambda (serverless) or ECS (containerized)
- Never hardcode AWS credentials; use environment variables or IAM roles.
- Prefer infrastructure-as-code (CDK).
- Keep infrastructure in sync with application changes.

