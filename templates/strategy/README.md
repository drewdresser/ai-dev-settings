# Strategy Directory

This directory contains your project's strategic planning documents.

## Files

| File | Purpose | Created By |
|------|---------|------------|
| `VISION.md` | North Star, Vision, Mission | `/ai-dev:north-star` |
| `STRATEGY.md` | Strategy, Non-Goals, Competitive Position | `/ai-dev:strategy` |
| `METRICS.md` | Success Metrics, Leading Indicators | `/ai-dev:metrics` |
| `OKRs.md` | Objectives and Key Results | `/ai-dev:okrs` |
| `EPICS.md` | Epic Overview and GitHub Milestones | `/ai-dev:epics` |
| `USER-STORIES.md` | User Stories Summary | `/ai-dev:user-stories` |

## Subdirectories

- `epics/` - Detailed epic descriptions
- `tasks/` - Individual task tracking (synced with GitHub Issues)
- `adrs/` - Architectural Decision Records

## Workflow

1. **Start planning:** `/ai-dev:kickoff`
2. **Individual phases:** `/ai-dev:north-star`, `/ai-dev:strategy`, etc.
3. **Bridge to execution:** `/ai-dev:plan-issue #123`
4. **Sync with GitHub:** `/ai-dev:sync-strategy`

## Integration with GitHub

- Epics → GitHub Milestones
- User Stories → GitHub Issues
- Status syncs bidirectionally via `/ai-dev:sync-strategy`

## Reading Order

When starting work, read these files in order:
1. `VISION.md` - Understand the "why"
2. `STRATEGY.md` - Understand constraints and focus
3. `OKRs.md` - Understand current priorities
4. `EPICS.md` - Find what to work on
