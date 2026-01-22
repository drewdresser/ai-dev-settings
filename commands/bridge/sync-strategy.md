---
name: ai-dev:sync-strategy
description: Sync GitHub state (closed issues, merged PRs) back to /strategy/ documentation
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
---

# Sync Strategy Command

Keep `/strategy/` documentation in sync with GitHub reality. This command detects closed issues, completed milestones, and updates the strategic documents accordingly.

## What This Does

1. Detects recently closed GitHub issues (user stories)
2. Updates corresponding `/strategy/` task files (if any)
3. Updates epic progress in `EPICS.md`
4. Flags completed milestones for review

## Process

### Step 1: Get GitHub State

```bash
# Get recently closed issues (last 7 days)
gh issue list --state closed --json number,title,closedAt,milestone,labels --limit 50

# Get milestone progress
gh api repos/{owner}/{repo}/milestones --jq '.[] | "\(.title): \(.closed_issues)/\(.open_issues + .closed_issues)"'

# Get merged PRs that reference issues
gh pr list --state merged --json number,title,body,mergedAt --limit 20
```

### Step 2: Update Task Status

For each closed issue that has a corresponding `/strategy/tasks/*.md` file:

1. Find the task file:
   ```bash
   grep -r "Issue: #${ISSUE_NUMBER}" /strategy/tasks/
   ```

2. Update status to completed:
   ```markdown
   ## Status: Completed ✓
   - Closed: [Date]
   - Closed by: PR #[number]
   ```

### Step 3: Update Epic Progress

Read `EPICS.md` and update progress:

```markdown
## Epic Progress

| Epic | Status | Issues | Progress |
|------|--------|--------|----------|
| Enable Seamless Checkout | In Progress | 8/12 closed | ████████░░░░ 67% |
| User Authentication | Complete ✓ | 15/15 closed | ████████████ 100% |
```

For each epic (milestone), calculate:
- Open issues count
- Closed issues count
- Progress percentage
- Estimated completion (if tracking velocity)

### Step 4: Flag Completed Milestones

If a milestone has all issues closed:

```bash
# Check if milestone should be closed
gh api repos/{owner}/{repo}/milestones/{number} --jq 'if .open_issues == 0 then "COMPLETE" else "IN_PROGRESS" end'
```

Prompt user:
"Milestone '[Epic Name]' has all issues closed. Should I close it in GitHub?"
- Yes, close the milestone
- No, keep it open (more work may be added)

### Step 5: Update OKRs Progress (Optional)

If OKRs track specific metrics that correspond to issue completion:

```markdown
## OKR Progress Update

### O1: Deliver core product value
- KR1: 80% of users complete checkout (Tracking: awaiting metrics)
- KR2: Ship 5 core features → **3/5 complete** (Updated based on milestone progress)
```

## Output

### Changes Made

```
Sync Strategy Results:
─────────────────────

Issues Updated:
  ✓ #42 → /strategy/tasks/user-auth.md (marked complete)
  ✓ #43 → /strategy/tasks/password-reset.md (marked complete)

Epics Progress:
  Enable Seamless Checkout: 67% (8/12 issues)
  User Authentication: 100% ✓ (milestone ready to close)

Files Modified:
  - /strategy/tasks/user-auth.md
  - /strategy/tasks/password-reset.md
  - /strategy/EPICS.md
```

### Discrepancies Found

Flag any inconsistencies:

```
Warnings:
  ⚠ Issue #45 closed but no matching task file found
  ⚠ /strategy/tasks/old-feature.md still marked "in progress" but issue #38 is closed
  ⚠ Milestone "MVP Launch" is 100% complete - consider closing
```

## Usage Patterns

### Regular Sync (Weekly)
```
/ai-dev:sync-strategy
```
Run weekly to keep docs in sync.

### After Sprint Completion
```
/ai-dev:sync-strategy
```
Run after closing sprint issues to update progress.

### Before Planning Sessions
```
/ai-dev:sync-strategy
```
Ensure strategy docs reflect current reality before planning.

## Integration

This command works with:
- `/ai-dev:kickoff` - Creates initial strategy structure
- `/ai-dev:epics` - Creates milestones that this tracks
- `/ai-dev:user-stories` - Creates issues that this syncs

## Key Behaviors

1. **Non-destructive** - Only updates status, never deletes
2. **Traceable** - All updates include timestamps and references
3. **Bidirectional awareness** - Notes discrepancies in both directions
4. **Human-in-loop** - Asks before closing milestones

Key message: "GitHub is the source of truth for issue status. This command ensures your strategy documentation reflects that reality."
