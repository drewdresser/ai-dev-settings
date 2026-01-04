# Global Agent Defaults

These are global defaults. Project-level AGENTS.md overrides these.

## Strategy-First Workflow

If a `/strategy/` folder exists in the project root, follow the **AI Agent Handoff Pattern**:

1. Read `/strategy/VISION.md` for strategic context
2. Read `/strategy/OKRs.md` to understand current priorities
3. Read relevant epic from `/strategy/epics/`
4. Read specific task from `/strategy/tasks/`
5. Check `/strategy/adrs/` for relevant architectural decisions

This provides full context from high-level strategy down to specific implementation guidance.

## Defaults

- Prefer small, reviewable diffs.
- Always provide how to verify changes (exact commands).
- Never print secrets. Treat `.env*`, credentials, keys, tokens as sensitive.
- When unsure about intent, make a reasonable assumption and state it.

## Dev Loop

- Before coding: state plan in 3-7 bullets.
- After coding: state what changed + how to verify.
- When completing a task, update its status in `/strategy/tasks/`.
- When making architectural decisions, document in `/strategy/adrs/`.

## Output Style

- Be terse.
- Prefer patch-style guidance and file paths.
- No long essays unless asked.

## Stack Hints

### Python

```bash
uv run pytest          # Test
uv run ruff check .    # Lint
uv run ruff format .   # Format
```

### TypeScript/React

```bash
pnpm test              # Test
pnpm lint              # Lint
pnpm build             # Build
```

