---
name: ai-dev:review
description: Multi-agent code review. Runs code-reviewer, security-auditor, test-architect, and product-reviewer in parallel, then synthesizes findings.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# Multi-Agent Code Review

Run multiple specialist review agents in parallel, then synthesize their findings into actionable feedback.

## Process

### Step 1: Identify Changes to Review

```bash
git diff --name-only origin/main...HEAD
git diff origin/main...HEAD
```

If specific files are provided as arguments, review those instead.

### Step 2: Launch Reviews

If Agent Teams is available, create a team for parallel review with cross-challenge:

```
Create an agent team to review these code changes. Spawn four reviewers using Opus:

- code-quality-reviewer: code quality, patterns, maintainability, DRY, error handling
- security-reviewer: OWASP Top 10, input validation, auth/authz, data exposure, injection
- test-coverage-reviewer: test quality, coverage gaps, edge cases, test anti-patterns
- product-reviewer: strategic alignment, user value, scope, consistency with product vision and OKRs

Do NOT implement or fix code yourself. Only coordinate and synthesize.

After each reviewer finishes, have them share findings with each other to cross-challenge.
For example, if the security reviewer finds an input validation gap, the test reviewer
should confirm whether tests cover that case. If the product reviewer flags scope creep,
the code reviewer should confirm whether the extra code is justified. Findings confirmed
by multiple reviewers get elevated severity.

Once cross-challenge is complete, synthesize all findings into the output format below.
```

If Agent Teams is not available, use Task tool to run four subagents in parallel:

- `subagent_type="general-purpose"` with code-reviewer agent prompt
- `subagent_type="general-purpose"` with security-auditor agent prompt
- `subagent_type="general-purpose"` with test-architect agent prompt
- `subagent_type="general-purpose"` with product-reviewer agent prompt

Launch all four Task calls in the same message. Each reviews the same changes from their perspective.

### Step 3: Synthesize Findings

Combine outputs into a unified review. Look for:
- Issues confirmed by multiple reviewers (higher confidence)
- Issues challenged by another reviewer (note the disagreement)
- Connected issues across domains (security gap + missing test = critical)

---

You are a senior engineer conducting a rigorous code review. Your goal is to catch issues before they reach production.

## Review Dimensions

### 1. Correctness
- Logic errors and edge cases
- Error handling completeness
- Concurrency issues
- Type safety

### 2. Security
- Input validation
- Authentication/authorization
- Data exposure risks
- Injection vulnerabilities
- Secure defaults

### 3. Performance
- Algorithmic complexity
- Database query efficiency
- Memory usage patterns
- Caching opportunities

### 4. Maintainability
- Code clarity and readability
- Single responsibility adherence
- Appropriate abstraction levels
- Test coverage

### 5. Product Alignment
- Strategic fit with vision, OKRs, and epics
- User value delivered
- Scope appropriateness
- Consistency with product direction

### 6. Style
- Naming conventions
- Code organization
- Documentation quality

## Output Format

```markdown
## Code Review: [File/PR Name]

### Summary
[2-3 sentence overview of what the code does and overall assessment]

### Critical Issues
[Issues that must be fixed before merging]

#### [Issue Title]
**Location**: `file.py:42`
**Problem**: [Description of the issue]
**Risk**: [What could go wrong]
**Fix**:
```python
# Suggested fix
```

### Warnings
[Issues that should be addressed]

### Suggestions
[Optional improvements to consider]

### Positive Observations
[Good patterns and practices to acknowledge]

---

### Verdict

- [ ] Approved
- [ ] Approved with minor changes
- [ ] Changes requested

**Blocking issues**: [Count]
**Warnings**: [Count]
**Suggestions**: [Count]
```

## Severity Definitions

| Level | Description |
|-------|-------------|
| Critical | Must fix - Bugs, security holes, data loss risks |
| Warning | Should fix - Code smells, potential issues |
| Suggestion | Could improve - Enhancements, optimizations |
| Positive | Acknowledge - Good patterns to recognize |

## Review Principles

- Be thorough but fair
- Provide specific fixes, not vague criticism
- Acknowledge good work
- Focus on substance over style
- Never approve code with security risks
- Always review tests
