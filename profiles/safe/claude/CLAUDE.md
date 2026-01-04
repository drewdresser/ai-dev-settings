# Project Instructions for Claude Code

Read AGENTS.md first for the full working agreement.

## Project Map

<!-- Fill in your project structure -->

```
project/
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

## AWS Deployment Notes

- Frontend deploys via AWS Amplify
- Backend runs on AWS Lambda or ECS
- Never commit AWS credentials

