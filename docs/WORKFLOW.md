# Multi-Project AI Agent Development Framework

## Philosophy

Enable 5 parallel AI-coded projects with minimal overhead while giving AI agents the strategic and technical context they need to make good decisions autonomously.

## Directory Structure

Each project should contain a `/strategy/` folder at its root:

```
/strategy/
  VISION.md
  OKRs.md
  
  /epics/
    epic-name.md
    another-epic.md
  
  /tasks/
    epic-name-001-task-description.md
    epic-name-002-another-task.md
    another-epic-001-task-description.md
  
  /adrs/
    001-architecture-decision-title.md
    002-another-decision.md
```

---

## Strategy Files

### `/strategy/VISION.md` — Strategic Foundation

| Section | Description |
|---------|-------------|
| **North Star** | Single aspirational statement (what the world looks like if you succeed) |
| **Vision** | 12-24 month success state (what does "winning" look like) |
| **Mission** | 2-3 bullets on what this product does and for whom |
| **Strategic Bets** | 3-5 key assumptions or approaches you're betting on |
| **Non-Goals** | Explicit things you're NOT doing (prevents scope creep) |
| **Success Metrics** | 2-4 measurable outcomes that matter |

### `/strategy/OKRs.md` — Current Quarter Objectives

- Quarterly objectives (1-3 max)
- Each with 2-4 key results (measurable, time-bound)
- Links to relevant epics implementing them

---

## Epics Format

**File:** `/strategy/epics/<epic-name>.md`

| Section | Description |
|---------|-------------|
| **Epic Title** | User-facing outcome |
| **User Value** | Why this matters |
| **Success Criteria** | How we know it's done |
| **Technical Approach** | 2-4 sentences on implementation strategy |
| **Tasks** | List of task files in `/strategy/tasks/` that belong to this epic |
| **Status** | `Not Started` \| `In Progress` \| `Done` |

---

## Tasks Format

**File:** `/strategy/tasks/<epic-name>-###-<description>.md`

| Section | Description |
|---------|-------------|
| **Task** | Specific, actionable work item |
| **Epic** | Link back to parent epic |
| **Estimate** | Rough time estimate |
| **Acceptance Criteria** | Specific requirements for done |
| **Technical Notes** | Any constraints, approaches, or context for the AI agent |
| **Status** | `Todo` \| `In Progress` \| `Done` |

---

## ADRs Format (Architecture Decision Records)

**File:** `/strategy/adrs/###-<decision-title>.md`

| Section | Description |
|---------|-------------|
| **Status** | `Proposed` \| `Accepted` \| `Deprecated` \| `Superseded` |
| **Context** | What situation necessitates this decision |
| **Decision** | What you're doing |
| **Consequences** | Trade-offs and implications |
| **Date** | When decided |

---

## AI Agent Handoff Pattern

When starting work on a project, agents should read files in this order:

1. **`/strategy/VISION.md`** — Strategic context
2. **`/strategy/OKRs.md`** — Current priorities
3. **`/strategy/epics/<relevant-epic>.md`** — Epic details
4. **`/strategy/tasks/<assigned-task>.md`** — Specific task
5. **`/strategy/adrs/`** — Relevant architectural decisions

This sequence provides agents with full context: from high-level strategy down to specific implementation guidance.

---

## Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| **Epics** | `kebab-case-description.md` | `user-authentication.md` |
| **Tasks** | `<epic-name>-###-description.md` | `user-authentication-001-setup-auth0.md` |
| **ADRs** | `###-kebab-case-title.md` | `001-use-nextjs-app-router.md` |

---

## Workflow

```
┌─────────────────┐
│  1. Strategy    │  Define in /strategy/VISION.md (rarely changes)
└────────┬────────┘
         ▼
┌─────────────────┐
│  2. Quarterly   │  Set OKRs in /strategy/OKRs.md
│     Planning    │
└────────┬────────┘
         ▼
┌─────────────────┐
│  3. Break Down  │  Create epic in /strategy/epics/
└────────┬────────┘
         ▼
┌─────────────────┐
│  4. Task        │  Create task files in /strategy/tasks/ (just-in-time)
│     Creation    │
└────────┬────────┘
         ▼
┌─────────────────┐
│  5. Implement   │  AI agent works from task file
└────────┬────────┘
         ▼
┌─────────────────┐
│  6. Decisions   │  Document in /strategy/adrs/ when making
│                 │  architectural choices
└─────────────────┘
```

---

## Key Principles

| Principle | Description |
|-----------|-------------|
| **Just-in-time documentation** | Create task files when you're about to work on them, not upfront |
| **Single source of truth** | Each piece of information lives in exactly one place |
| **Agent-first** | Structure optimized for AI agent context consumption |
| **Minimal maintenance** | No duplicate tracking systems or heavy ceremony |
| **Decision preservation** | ADRs prevent agents from revisiting settled questions |
| **Clean project root** | All strategic docs isolated in `/strategy/` folder |

---

## Templates

### VISION.md Template

```markdown
# Vision

## North Star

[Single aspirational statement]

## Vision (12-24 months)

[What does winning look like?]

## Mission

- [What this product does]
- [For whom]
- [Core value proposition]

## Strategic Bets

1. [Key assumption or approach #1]
2. [Key assumption or approach #2]
3. [Key assumption or approach #3]

## Non-Goals

- [Explicit thing we're NOT doing]
- [Another thing we're NOT doing]

## Success Metrics

- [ ] [Measurable outcome #1]
- [ ] [Measurable outcome #2]
```

### OKRs.md Template

```markdown
# OKRs — Q[X] [YEAR]

## Objective 1: [Objective Title]

- [ ] KR1: [Measurable key result]
- [ ] KR2: [Measurable key result]
- [ ] KR3: [Measurable key result]

**Related Epics:** [epic-name.md](epics/epic-name.md)

## Objective 2: [Objective Title]

- [ ] KR1: [Measurable key result]
- [ ] KR2: [Measurable key result]

**Related Epics:** [another-epic.md](epics/another-epic.md)
```

### Epic Template

```markdown
# Epic: [Epic Title]

## User Value

[Why this matters to users]

## Success Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Technical Approach

[2-4 sentences on implementation strategy]

## Tasks

- [ ] [epic-name-001-description.md](../tasks/epic-name-001-description.md)
- [ ] [epic-name-002-description.md](../tasks/epic-name-002-description.md)

## Status

`Not Started` | `In Progress` | `Done`
```

### Task Template

```markdown
# Task: [Task Title]

**Epic:** [epic-name.md](../epics/epic-name.md)  
**Estimate:** [X hours/days]  
**Status:** `Todo` | `In Progress` | `Done`

## Acceptance Criteria

- [ ] [Specific requirement 1]
- [ ] [Specific requirement 2]
- [ ] [Specific requirement 3]

## Technical Notes

[Any constraints, approaches, or context for the AI agent]
```

### ADR Template

```markdown
# ADR-###: [Decision Title]

**Status:** `Proposed` | `Accepted` | `Deprecated` | `Superseded`  
**Date:** YYYY-MM-DD

## Context

[What situation necessitates this decision?]

## Decision

[What are you doing?]

## Consequences

[Trade-offs and implications]
```

