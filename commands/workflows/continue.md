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

Each stage of the workflow maps to specific commands:

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

Before launching sub-agents, do a fast local check:

```bash
# Check for uncommitted changes (work in progress)
git status --porcelain

# Check for existing plan files
ls plans/*.md 2>/dev/null | head -3

# Recent commits to understand momentum
git log --oneline -3
```

**If uncommitted changes exist:**
- This takes priority over audits
- Likely mid-work: suggest `/ai-dev:work` to continue
- Or if changes look complete: suggest `/ai-dev:review`

**If no local WIP, proceed to sub-agent audits.**

### Step 2: Launch Parallel Audits

Use the Task tool to run two auditor agents **in parallel**:

#### Task 1: Strategy Auditor
```
subagent_type: "general-purpose"
prompt: |
  You are the strategy-auditor agent. Audit the /strategy/ directory for this project.

  Check:
  1. Which strategy docs exist (VISION.md, STRATEGY.md, METRICS.md, OKRs.md, EPICS.md)
  2. Completeness of each document (are required sections present?)
  3. Depth (how many epics, tasks, ADRs exist?)
  4. Gaps (what's missing or incomplete?)

  Return a concise summary in this format:

  ## Strategy Audit
  ### Document Status
  [Table of docs with status: Complete/Partial/Missing]

  ### Gaps
  [Numbered list of gaps, most critical first]

  ### Recommended Command
  [Single ai-dev command to address the most important gap]
```

#### Task 2: GitHub Auditor
```
subagent_type: "general-purpose"
prompt: |
  You are the github-auditor agent. Audit the GitHub state for this project.

  Run these commands:
  1. gh api repos/:owner/:repo/milestones - Get milestone progress
  2. gh issue list --state open --json number,title,milestone,labels - Get open issues
  3. Check for plan files in plans/*.md that reference issues

  Return a concise summary in this format:

  ## GitHub Audit
  ### Milestones
  [Table with milestone name, progress %, open/closed counts]

  ### Issues Ready for Work
  [List of issues that have plans or are labeled "ready"]

  ### Issues Needing Plans
  [List of high-priority issues without plans]

  ### Recommended Command
  [Single ai-dev command with specific issue number if applicable]
```

**Important:** Launch both Task calls in the same message to run them in parallel.

### Step 3: Synthesize Recommendations

Once both audits return, synthesize their findings:

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

### Step 4: Present Options

Format your output:

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

### Option 3: [Brief description]
**Run:** `/ai-dev:command`
**Why:** [Reasoning]
```

### Step 5: Let User Choose

Use AskUserQuestion:

```yaml
question: "What would you like to work on next?"
options:
  - label: "Option 1: [brief] (Recommended)"
    description: "Run /ai-dev:command"
  - label: "Option 2: [brief]"
    description: "Run /ai-dev:command"
  - label: "Option 3: [brief]"
    description: "Run /ai-dev:command"
```

### Step 6: Confirm the Command

After the user chooses, respond with the exact command:

```
Run this command:

/ai-dev:plan-issue #47

This will analyze issue #47 and create a detailed technical implementation plan.
```

## State → Command Quick Reference

Use this table when synthesizing audit results:

| What You Observe | Command | Why |
|-----------------|---------|-----|
| No strategy directory | `/ai-dev:kickoff` | Need strategic foundation first |
| VISION.md empty/missing | `/ai-dev:north-star` | Define north star and vision |
| STRATEGY.md missing | `/ai-dev:strategy` | Define strategy and non-goals |
| METRICS.md missing | `/ai-dev:metrics` | Define success metrics |
| OKRs.md empty/missing | `/ai-dev:okrs` | Set quarterly objectives |
| No epics in EPICS.md | `/ai-dev:epics` | Break OKRs into epics |
| Epics exist, no GitHub milestones | `/ai-dev:epics` | Sync epics to GitHub |
| Milestones exist, no issues | `/ai-dev:user-stories` | Create user stories as issues |
| Open issue, no plan file | `/ai-dev:plan-issue #N` | Create technical plan |
| Plan file exists, not started | `/ai-dev:work` | Execute the plan |
| Uncommitted changes mid-task | `/ai-dev:work` | Continue executing |
| Code complete, not reviewed | `/ai-dev:review` | Run quality review |
| Review passed, not pushed | `/ai-dev:commit-push` | Push with quality gates |
| Pushed, strategy outdated | `/ai-dev:sync-strategy` | Update strategy from GitHub |
| All issues closed | `/ai-dev:okrs` | Plan next quarter |

## Special Cases

### GitHub Not Connected
If the github-auditor reports auth failure:
```
GitHub is not connected.

**Run:** `gh auth login`

Then run `/ai-dev:continue` again.
```

### No Strategy AND No GitHub
If both auditors find nothing:
```
This project has no strategic planning or GitHub tracking.

**Run:** `/ai-dev:kickoff`

This will guide you through establishing vision, strategy, OKRs, and create GitHub milestones.
```

### Everything Complete
If both auditors report all work done:
```
All tracked work is complete!

**Run:** `/ai-dev:okrs`

Time to plan your next quarter's objectives.
```

## Output Requirements

1. **Always recommend a specific `/ai-dev:*` command**
2. **Always explain why** (connect to audit findings)
3. **Always give 2-3 options** (let user choose, but guide them)
4. **End with the exact command to copy/paste**
5. **Keep summaries concise** (auditors already did the deep analysis)
