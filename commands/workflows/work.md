---
name: ai-dev:work
description: Execute an implementation plan using TodoWrite for task tracking and incremental commits to main.
argument-hint: "[plan-file-path]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Task
  - TodoWrite
  - AskUserQuestion
---

# Work Execution Workflow

Execute an implementation plan systematically, using TodoWrite for tracking and committing directly to main with quality gates.

## Philosophy

This workflow embodies trunk-based development:
- Work happens on main (or current branch)
- Each completed step is committed
- Quality gates before final push
- Revert plan always ready

## Process

### Step 1: Load the Plan

```bash
# Read the plan file
cat plans/{plan-file}.md
```

Extract:
- Implementation steps
- Affected files
- Test requirements
- Acceptance criteria

### Step 2: Create Todo List

Use TodoWrite to create a task list from the plan steps:

```
[pending] Step 1: Create module structure
[pending] Step 2: Implement core logic
[pending] Step 3: Add API endpoint
[pending] Step 4: Write unit tests
[pending] Step 5: Write integration tests
[pending] Step 6: Update documentation
[pending] Final: Run all tests and quality checks
```

### Step 3: Execute Task Loop

For each task:

1. **Mark in progress:** Update TodoWrite status
   ```
   [in_progress] Step 2: Implement core logic
   ```

2. **Do the work:** Implement the task
   - Read relevant files
   - Make changes using Edit/Write
   - Verify changes work

3. **Stage changes:**
   ```bash
   git add [changed-files]
   ```

4. **Micro-commit:** Commit this increment
   ```bash
   git commit -m "feat(scope): [what this step accomplished]"
   ```

5. **Mark complete:** Update TodoWrite status
   ```
   [completed] Step 2: Implement core logic
   ```

6. **Proceed to next task**

### Step 4: Quality Gates

Before final push, run quality checks:

1. **Run tests:**
   ```bash
   # Python
   uv run pytest

   # Node
   npm test
   ```

2. **Run linting:**
   ```bash
   # Python
   uv run ruff check .

   # Node
   npm run lint
   ```

3. **Check for secrets:**
   ```bash
   git diff origin/main...HEAD | grep -iE "(api[_-]?key|secret|password|token)"
   ```

### Step 5: Final Push

If all quality gates pass:

```bash
git push origin $(git branch --show-current)
```

Display:
```
Work Complete!
─────────────

Commits made: 6
Files changed: 12
Tests: 24 passed

Pushed to: origin/main

To revert all changes:
  git revert HEAD~6..HEAD
  git push
```

### Step 6: Update Issue (if applicable)

If this work was for a GitHub issue:

```bash
gh issue comment $ISSUE_NUMBER --body "## Implementation Complete

All acceptance criteria met:
- [x] Criterion 1
- [x] Criterion 2
- [x] Criterion 3

Commits: abc1234..def5678

Ready for review and testing."
```

## Error Handling

### If Tests Fail

```
Tests failed in step 4.

Options:
1. Fix the failing tests (recommended)
2. Skip tests and proceed (risky)
3. Abort and revert all changes

[AskUserQuestion with options]
```

If user chooses to fix, create new todo item for the fix.

### If Stuck on a Task

```
I'm having trouble with [task description].

Options:
1. Show me what you've tried
2. Skip this task for now
3. Break it into smaller tasks
4. Get help (search documentation)

[AskUserQuestion with options]
```

### If Unexpected Changes Needed

If implementation reveals the plan needs updating:

```
During implementation, I discovered [issue].

The plan assumed [X] but actually [Y].

Options:
1. Update the plan and continue
2. Add this as a new task
3. Stop and discuss before proceeding

[AskUserQuestion with options]
```

## Progress Visibility

Throughout execution, TodoWrite provides visibility:

```
Work Progress: plans/user-auth.md
────────────────────────────────────

[completed] Step 1: Create module structure (abc1234)
[completed] Step 2: Implement core logic (def5678)
[in_progress] Step 3: Add API endpoint
[pending] Step 4: Write unit tests
[pending] Step 5: Write integration tests
[pending] Step 6: Update documentation
[pending] Final: Run all tests and quality checks

Current: Adding API endpoint in src/api/routes.py
```

## Commit Message Format

Each step gets a conventional commit:

```
type(scope): description

[Step X of Y from plan: plan-file-name]
```

Types based on work:
- `feat` - New feature code
- `test` - Test additions
- `docs` - Documentation
- `refactor` - Code restructuring
- `fix` - Bug fixes discovered during implementation

## Integration

This command works with:
- `/ai-dev:plan` - Creates plans this executes
- `/ai-dev:plan-issue` - Creates plans from issues
- `/ai-dev:commit-push` - Final push with quality gates
- `/ai-dev:review` - Post-implementation review

## Key Behaviors

1. **Incremental** - Commit after each step, not at the end
2. **Tracked** - TodoWrite shows progress at all times
3. **Recoverable** - Every commit is revertible
4. **Quality-gated** - Tests must pass before final push
5. **Trunk-based** - Work directly on main

Key message: "Small, committed steps are safer than big-bang changes. This workflow ensures you can always see progress and recover from mistakes."
