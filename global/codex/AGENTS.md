# Global Agent Defaults

These are global defaults. Project-level AGENTS.md overrides these.

## Defaults

- Prefer small, reviewable diffs.
- Always provide how to verify changes (exact commands).
- Never print secrets. Treat `.env*`, credentials, keys, tokens as sensitive.
- When unsure about intent, make a reasonable assumption and state it.

## Dev Loop

- Before coding: state plan in 3-7 bullets.
- After coding: state what changed + how to verify.

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

