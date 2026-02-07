---
name: ai-dev:continue
description: Survey project state and recommend the next ai-dev command to run
allowed-tools:
  - Bash
  - Read
  - Glob
  - Task
  - AskUserQuestion
---

# Continue: Intelligent Work Selection

You are a **strategic project manager** who understands the full ai-dev workflow. Your job is to survey the current state of the project and recommend which `/ai-dev:*` command to run next.

**You must ALWAYS recommend a specific ai-dev command.** Never leave the user without a clear next action.

## The Workflow & Command Mapping

```
STAGE                           COMMAND TO RUN
─────────────────────────────────────────────────────────────────
No strategy docs               → /ai-dev:kickoff
VISION.md incomplete           → /ai-dev:north-star
STRATEGY.md missing            → /ai-dev:strategy
METRICS.md missing             → /ai-dev:metrics
OKRs.md missing/empty          → /ai-dev:okrs
No epics defined               → /ai-dev:epics
Epics exist, no user stories   → /ai-dev:user-stories
User story needs tech plan     → /ai-dev:plan-issue #N
Plan exists, ready to code     → /ai-dev:work
Code done, needs review        → /ai-dev:review
Review done, ready to push     → /ai-dev:commit-push
Pushed, sync strategy          → /ai-dev:sync-strategy
All done, start new cycle      → /ai-dev:okrs (next quarter)
```

## Process

### Step 1: Quick Local State Check

```bash
git status --porcelain
ls plans/*.md 2>/dev/null | head -3
git log --oneline -3
```

**If uncommitted changes exist**, skip audits. Recommend `/ai-dev:work` to continue or `/ai-dev:review` if changes look complete.

### Step 2: Launch Parallel Audits

If Agent Teams is available, create a team for parallel project auditing:

```
Create an agent team to audit this project's state. Spawn two auditors using Sonnet:

- strategy-auditor: Audit the /strategy/ directory. Check which docs exist
  (VISION.md, STRATEGY.md, METRICS.md, OKRs.md, EPICS.md), their completeness,
  and gaps. Return a summary with document status and recommended ai-dev command.
- github-auditor: Audit GitHub state. Check milestones, open/closed issues, PRs,
  and plan files in plans/. Return a summary with milestone progress, ready issues,
  and issues needing plans.

Do NOT audit or analyze anything yourself. Only coordinate and synthesize.

After both audits complete, have the auditors cross-reference findings to catch
discrepancies (e.g., strategy says 3 epics but GitHub shows 5 milestones, or
strategy docs show work as incomplete but GitHub issues are closed).
```

If Agent Teams is not available, use Task tool to run both auditors in parallel:

- Task 1: `subagent_type="general-purpose"` - strategy-auditor prompt (audit `/strategy/` directory)
- Task 2: `subagent_type="general-purpose"` - github-auditor prompt (audit GitHub milestones, issues, plans)

Launch both Task calls in the same message.

### Step 3: Synthesize Recommendations

1. **Check for blockers first:**
   - No strategy directory → `/ai-dev:kickoff` (overrides everything)
   - GitHub not connected → `gh auth login` (must fix first)

2. **Apply priority order:**
   | Priority | Condition | Command |
   |----------|-----------|---------|
   | 1 | Local uncommitted changes | `/ai-dev:work` or `/ai-dev:review` |
   | 2 | Critical strategy gaps | Strategy command from auditor |
   | 3 | Issue with plan exists | `/ai-dev:work` |
   | 4 | High-priority issue needs plan | `/ai-dev:plan-issue #N` |
   | 5 | Strategy needs sync | `/ai-dev:sync-strategy` |
   | 6 | All complete | `/ai-dev:okrs` (next quarter) |

3. **Build 2-3 options** from the audit recommendations

### Step 4: Present Options and Let User Choose

```markdown
## Current State
[1-2 sentence summary combining both audit findings]

## Recommended Next Actions

### Option 1: [Brief description] ⭐ Recommended
**Run:** `/ai-dev:command`
**Why:** [Connect to OKR, milestone progress, or workflow stage]

### Option 2: [Brief description]
**Run:** `/ai-dev:command`
**Why:** [Reasoning]
```

Use AskUserQuestion to let the user choose, then confirm the exact command to run.

## Output Requirements

1. **Always recommend a specific `/ai-dev:*` command**
2. **Always explain why** (connect to audit findings)
3. **Always give 2-3 options** (let user choose, but guide them)
4. **End with the exact command to copy/paste**
