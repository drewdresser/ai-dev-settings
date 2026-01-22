---
name: ai-dev:plan
description: Interactive technical planning workflow. Gathers requirements through Q&A, researches patterns, and outputs a detailed implementation plan.
argument-hint: "[feature description or issue reference]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - Task
  - AskUserQuestion
---

# Technical Planning Workflow

An interactive workflow that helps you plan technical implementations through structured Q&A and codebase research.

## When to Use This

- Before implementing a non-trivial feature
- When you need to understand existing patterns
- When multiple implementation approaches exist
- When you want a documented plan before coding

## Process

### Phase 1: Requirements Clarification

Start by understanding what needs to be built:

1. "What are you trying to build? Describe the user-facing behavior."

2. "Who will use this? What problem does it solve for them?"

3. "What should happen in error cases?"

4. "Are there any constraints I should know about?"
   - Performance requirements
   - Security considerations
   - Compatibility requirements

Use AskUserQuestion to validate understanding:
- "I understand the requirements" → Proceed
- "I have more questions" → Continue clarifying
- "Let me show you a similar feature" → Research first

### Phase 2: Codebase Research

Use Task tool with subagent_type="Explore" to understand the codebase:

**Architecture Analysis:**
- Project structure and conventions
- Relevant modules and files
- Existing patterns for similar features

**Pattern Discovery:**
- How similar features are implemented
- Test patterns in use
- Error handling conventions

**Dependency Mapping:**
- What this feature will interact with
- External dependencies needed
- Potential breaking changes

### Phase 3: Approach Selection

If multiple valid approaches exist, present them:

Use AskUserQuestion:
```
Which approach would you prefer?

1. [Approach A] - [tradeoffs]
2. [Approach B] - [tradeoffs]
3. Discuss further before deciding
```

Document the decision and rationale.

### Phase 4: Plan Generation

Create a detailed plan with:

```markdown
# Implementation Plan: [Feature Name]

## Overview
[What this feature does and why]

## Requirements Summary
- [Requirement 1]
- [Requirement 2]
- [Error handling requirement]

## Technical Approach
[Chosen approach and rationale]

### Alternative Considered
[Why we didn't choose this]

## Affected Files

### New Files
- `src/features/new_feature.py` - [Purpose]
- `tests/test_new_feature.py` - [Test coverage]

### Modified Files
- `src/api/routes.py` - [Changes needed]
- `src/models/user.py` - [Changes needed]

## Implementation Steps

### Step 1: [Foundation]
- [ ] Create new module structure
- [ ] Add necessary imports
- [ ] Set up configuration

### Step 2: [Core Implementation]
- [ ] Implement main logic in `src/features/new_feature.py`
- [ ] Add API endpoint in `src/api/routes.py`
- [ ] Update models if needed

### Step 3: [Integration]
- [ ] Wire up dependencies
- [ ] Add error handling
- [ ] Add logging

### Step 4: [Testing]
- [ ] Unit tests for core logic
- [ ] Integration tests for API
- [ ] Edge case tests

### Step 5: [Documentation]
- [ ] Update API docs
- [ ] Add inline comments for complex logic

## Test Plan
| Scenario | Expected Result |
|----------|----------------|
| Happy path | [Result] |
| Error case 1 | [Result] |
| Edge case | [Result] |

## Risks & Mitigations
- **Risk:** [Potential issue]
  **Mitigation:** [How to handle]

## Open Questions
- [ ] [Question that may need answering during implementation]
```

### Phase 5: Plan Review

Present the plan summary and ask:

Use AskUserQuestion:
- "Plan looks good, proceed to implementation" → Save plan, offer `/ai-dev:work`
- "I have feedback on the plan" → Refine based on feedback
- "Let's research more before finalizing" → Return to Phase 2

## Output

Save plan to: `plans/{feature-slug}.md`

```
Plan saved to: plans/user-authentication.md

Next steps:
1. Review the plan
2. Run `/ai-dev:work plans/user-authentication.md` to begin implementation
```

## Integration with Other Commands

This command integrates with:
- `/ai-dev:plan-issue` - Automated planning from GitHub issues
- `/ai-dev:work` - Execution of the generated plan
- `/ai-dev:review` - Post-implementation review

## Key Behaviors

1. **Interactive** - Use AskUserQuestion throughout
2. **Research-driven** - Always analyze codebase before planning
3. **Documented** - Every decision recorded with rationale
4. **Actionable** - Output is ready for `/ai-dev:work`

Key message: "Good plans prevent rework. This workflow ensures you understand what you're building and how before writing code."
