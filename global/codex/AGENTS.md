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
- **No inline imports.** All imports at the top of the file, never inside functions or conditionals.

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

#### Standalone Scripts (PEP 723)

For one-off scripts, data processing, or utility tasks, use PEP 723 inline script metadata with `uv`:

```python
# /// script
# dependencies = ["requests", "pandas"]
# ///
import requests
import pandas as pd
# ... script code
```

Run with: `uv run scripts/my_script.py`

- Store scripts in `scripts/` folder
- Use inline dependencies instead of modifying project pyproject.toml
- Useful for migrations, data checks, one-time operations

### TypeScript/React

```bash
pnpm test              # Test
pnpm lint              # Lint
pnpm build             # Build
```

