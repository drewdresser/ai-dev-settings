---
name: ai-dev:commit-push
description: Commit staged changes and push directly to the current branch. Supports main-branch development workflow with quality gates.
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# Commit and Push Command

Commit changes and push directly to the current branch. Designed for main-branch (trunk-based) development workflow.

## Philosophy

This command supports trunk-based development where:
- All work happens on main (or the current branch)
- Commits are small, focused, and well-tested
- Pushing to main is the norm, not the exception
- Quality gates catch issues before push

## Pre-flight Checks

Before any commit, run these quality checks:

```bash
# Get current branch
BRANCH=$(git branch --show-current)

# Check for staged changes
git diff --cached --stat

# Check for unstaged changes
git diff --stat
```

## Quality Gates

Run these checks and report results (non-blocking but informative):

### 1. Check for secrets
```bash
# Quick scan for common secret patterns
git diff --cached | grep -iE "(api[_-]?key|secret|password|token|credential)" && echo "Warning: Possible secrets detected"
```

### 2. Run tests (if available)
```bash
# Detect and run tests based on project type
if [ -f "pyproject.toml" ]; then
  uv run pytest --tb=short -q 2>/dev/null || echo "Tests: Failed or not configured"
elif [ -f "package.json" ]; then
  npm test 2>/dev/null || echo "Tests: Failed or not configured"
fi
```

### 3. Run linting (if available)
```bash
# Detect and run linter based on project type
if [ -f "pyproject.toml" ]; then
  uv run ruff check . 2>/dev/null || echo "Lint: Issues found or not configured"
elif [ -f "package.json" ]; then
  npm run lint 2>/dev/null || echo "Lint: Issues found or not configured"
fi
```

## Process

### Step 1: Verify Branch and Changes
```bash
git branch --show-current
git diff --cached --stat
git status --short
```

### Step 2: Protected Branch Confirmation

If pushing to `main` or `master`, use AskUserQuestion to confirm:

Options:
- "Yes, push to main" - Proceed with push
- "No, create a feature branch" - Abort and suggest branch creation
- "Show me what will be pushed" - Display full diff first

### Step 3: Generate Commit Message

Analyze staged changes and generate conventional commit:

```bash
# View staged changes
git diff --cached

# View recent commit style
git log --oneline -5
```

Generate message following conventional commits:
```
type(scope): description

[optional body explaining what and why]
```

### Step 4: Commit and Push

```bash
# Commit
git commit -m "type(scope): description"

# Push with upstream tracking
git push -u origin $(git branch --show-current)
```

### Step 5: Post-Push Information

After successful push, display:
```
Pushed to: origin/[branch]
Commit: [hash]

To revert this commit:
  git revert [hash]
  git push
```

## User Arguments

- `commit-push "message hint"` - Use provided hint in commit message
- `commit-push fix` - Type is "fix"
- `commit-push --force` - Skip quality gate warnings (not force push!)

## Output Format

```
Pre-flight checks:
  Branch: main
  Staged: 3 files changed

Quality gates:
  Secrets scan: Pass
  Tests: 12 passed
  Lint: Clean

Commit message:
  feat(auth): add password reset flow

Pushing...
  Pushed: abc1234 → origin/main

Post-push:
  To revert: git revert abc1234 && git push
```

## Safeguards

- Always show what will be pushed before pushing to main/master
- Display revert command after every push
- Warn about uncommitted changes that won't be included
- Never use `--force` push (even with user argument)

## Main-Branch Best Practices

When working on main:
1. Pull before starting work: `git pull origin main`
2. Make small, atomic commits
3. Run tests locally before push
4. Push frequently to avoid merge conflicts
5. Use feature flags for incomplete features
