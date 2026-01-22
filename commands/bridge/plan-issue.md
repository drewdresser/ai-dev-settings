---
name: plan-issue
description: Bridge GitHub Issue to Technical Implementation Plan. Reads issue context, strategic documents, and generates a detailed technical plan.
argument-hint: "#123 or issue URL or /strategy/tasks/ path"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - Task
  - AskUserQuestion
---

# Plan Issue Command

Bridge a GitHub Issue (user story) to a detailed technical implementation plan. This command connects strategic planning to engineering execution.

## What This Does

1. Reads the GitHub Issue and extracts requirements
2. Reads strategic context from `/strategy/` directory
3. Runs research agents to analyze the codebase
4. Generates a technical implementation plan
5. Links the plan back to the issue

## Argument Parsing

Accept any of these formats:
- `#123` - GitHub issue number
- `https://github.com/owner/repo/issues/123` - Full URL
- `/strategy/tasks/task-name.md` - Local task file path

## Process

### Step 1: Extract Issue Information

```bash
# Get issue details
gh issue view $ISSUE_NUMBER --json title,body,labels,milestone,comments

# Get related milestone (epic) context
gh api repos/{owner}/{repo}/milestones/{milestone_number}
```

Parse:
- User story (As a... I want... So that...)
- Acceptance criteria (Given/When/Then)
- Labels (priority, size)
- Comments (additional context)

### Step 2: Read Strategic Context

Read relevant `/strategy/` files for context:

```
/strategy/
├── VISION.md         # North star and vision
├── STRATEGY.md       # Strategy and non-goals
├── OKRs.md          # Current objectives
├── EPICS.md         # Epic overview
└── adrs/            # Architectural decisions
```

Extract:
- How this issue connects to OKRs
- Relevant non-goals (what NOT to do)
- Architectural constraints from ADRs

### Step 3: Codebase Research

Run research agents to understand the codebase:

1. **Codebase Analyst** - Understand project structure
   - Identify relevant files and modules
   - Map dependencies
   - Find similar implementations

2. **Pattern Researcher** - Find existing patterns
   - How similar features are implemented
   - Coding conventions in use
   - Test patterns

Use the Task tool with subagent_type="Explore":
```
"Analyze the codebase to understand how to implement [feature].
Find related files, existing patterns, and dependencies."
```

### Step 4: Generate Implementation Plan

Create a detailed plan in `plans/issue-{number}-{slug}.md`:

```markdown
# Implementation Plan: [Issue Title]

**Issue:** #123
**Epic:** [Milestone Name]
**Priority:** [Must/Should/Could]
**Size:** [XS/S/M/L]

## User Story
[Copy from issue]

## Acceptance Criteria
[Copy from issue with checkboxes]

## Strategic Context

### Connection to OKRs
- Supports: O1 - [Objective Name]
- Key Result: [Specific KR this impacts]

### Non-Goals (from strategy)
- [Relevant non-goals that constrain implementation]

### Relevant ADRs
- ADR-001: [Decision that affects this]

## Technical Analysis

### Affected Files
- `src/feature/component.py` - [What changes]
- `src/api/routes.py` - [What changes]
- `tests/test_feature.py` - [New tests needed]

### Dependencies
- Internal: [modules this depends on]
- External: [packages needed]

### Existing Patterns
- Similar feature in `src/other/` uses [pattern]
- Tests follow [pattern] convention

## Implementation Steps

### Phase 1: Foundation
- [ ] [Specific task with file path]
- [ ] [Specific task with file path]

### Phase 2: Core Feature
- [ ] [Specific task with file path]
- [ ] [Specific task with file path]

### Phase 3: Tests & Polish
- [ ] [Test task]
- [ ] [Documentation task]

## Test Plan
[How to verify each acceptance criterion]

## Risks & Mitigations
- Risk: [Potential issue]
  Mitigation: [How to handle]

## Questions / Decisions Needed
- [ ] [Question that needs answering]

---
*Generated from GitHub Issue #123 via /ai-dev:plan-issue*
```

### Step 5: Link Plan to Issue

Add a comment to the GitHub issue linking to the plan:

```bash
gh issue comment $ISSUE_NUMBER --body "## Implementation Plan Created

A detailed technical plan has been created: \`plans/issue-${ISSUE_NUMBER}-${SLUG}.md\`

**Key files affected:**
- \`src/...\`
- \`tests/...\`

**Next steps:**
Run \`/ai-dev:work plans/issue-${ISSUE_NUMBER}-${SLUG}.md\` to begin implementation."
```

## User Interaction

Use AskUserQuestion to clarify when needed:

1. **If issue lacks acceptance criteria:**
   "This issue doesn't have clear acceptance criteria. Let me suggest some based on the user story..."
   - Accept suggested criteria
   - Add your own criteria
   - Discuss with the team first

2. **If multiple implementation approaches exist:**
   "I see two ways to implement this..."
   - Option A: [Approach with tradeoffs]
   - Option B: [Approach with tradeoffs]

3. **If architectural decision needed:**
   "This feature requires an architectural decision about..."
   - Create an ADR
   - Use existing pattern
   - Discuss before proceeding

## Output

1. **Plan file:** `plans/issue-{number}-{slug}.md`
2. **GitHub comment:** Links plan to issue
3. **Summary:** Key implementation points

## Transitions

After plan is created:
1. Show the plan summary
2. Offer: "Ready to implement? Run `/ai-dev:work plans/issue-{number}-{slug}.md`"
3. Or: "Need to clarify requirements first? Update the issue and re-run `/ai-dev:plan-issue`"

Key message: "This plan connects your user story to specific code changes. Every task can be traced back to an acceptance criterion."
