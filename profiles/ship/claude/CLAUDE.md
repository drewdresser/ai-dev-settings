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

# Test with coverage
uv run pytest --cov

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

## AWS Deployment Notes

- Frontend deploys via AWS Amplify
- Backend runs on AWS Lambda or ECS
- Never commit AWS credentials
- Prefer infrastructure-as-code (CDK/SAM/Terraform)

