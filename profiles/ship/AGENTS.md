# Agent Working Agreement (SHIP)

All SAFE rules apply, plus:

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

