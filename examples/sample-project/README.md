# Example Project Structure

This directory shows what your project will look like after running the installation.

## What Gets Installed

After running `just install` from your project directory, you'll have these files:

```
your-project/
├── AGENTS.md                      # Universal AI agent behavior contract
├── CLAUDE.md                      # Claude Code project-specific instructions
│
├── .claude/                       # Claude Code configuration
│   ├── agents/                    # Specialized agent definitions
│   │   ├── code-reviewer.md
│   │   ├── debugger.md
│   │   ├── docs-writer.md
│   │   ├── orchestrator.md
│   │   ├── refactorer.md
│   │   ├── security-auditor.md
│   │   └── test-architect.md
│   │
│   ├── commands/                  # Reusable command templates
│   │   ├── add-tests.md           # Generate tests
│   │   ├── architect.md           # Design decisions
│   │   ├── code-simplifier.md     # Refactor code
│   │   ├── commit.md              # Smart commits
│   │   ├── commit-push-pr.md      # Full workflow
│   │   ├── create-epics.md        # Strategy: Create epics
│   │   ├── create-tasks.md        # Strategy: Create tasks
│   │   ├── lint-check.md          # Check linting
│   │   ├── lint-fix.md            # Fix linting
│   │   ├── mentor.md              # Learning mode
│   │   ├── quick-fix.md           # Fast fixes
│   │   ├── rapid.md               # Rapid development
│   │   ├── review.md              # Code review
│   │   ├── run-tests.md           # Run tests
│   │   ├── security-scan.md       # Security audit
│   │   ├── summarize-changes.md   # Git summary
│   │   ├── sync-branch.md         # Branch management
│   │   ├── validate-build.md      # Build validation
│   │   └── verify-changes.md      # Change verification
│   │
│   ├── hooks/                     # Event hooks and scripts
│   │   ├── hooks.json             # Hook configuration
│   │   └── scripts/
│   │       ├── check-file-protection.sh
│   │       ├── format-on-save.sh
│   │       ├── log-command.sh
│   │       ├── notify.sh
│   │       ├── on-complete.sh
│   │       ├── validate-environment.sh
│   │       └── validate-prompt.sh
│   │
│   └── skills/                    # Skill definitions
│       ├── analyzing-projects/
│       ├── designing-apis/
│       ├── designing-architecture/
│       ├── designing-tests/
│       ├── managing-git/
│       └── optimizing-performance/
│
├── .cursorrules                   # Cursor IDE-level behavior
│
├── .cursor/                       # Cursor configuration
│   ├── rules/                     # Stack-specific rules
│   │   ├── python-backend.mdc
│   │   └── react-frontend.mdc
│   └── commands/                  # Reusable prompt templates
│
└── ... (rest of your project)
```

## Using the Commands

After installation, you can use commands in Claude Code like:

- `/rapid` - Fast development mode with minimal discussion
- `/architect` - Get help with design decisions
- `/add-tests` - Generate tests for your code
- `/lint-fix` - Fix linting issues
- `/security-scan` - Audit for security vulnerabilities
- `/review` - Get code review feedback
- `/commit` - Create smart commit messages

## Customizing

After installation, customize these files for your project:

1. **CLAUDE.md** - Update the "Project Map" section to match your structure
2. **AGENTS.md** - Add project-specific conventions and rules
3. **.cursor/rules/** - Modify or add stack-specific rules

## Strategy Workflow (Optional)

If you want to use the strategy-first workflow, create a `/strategy/` folder:

```
your-project/
├── strategy/
│   ├── VISION.md              # Strategic foundation
│   ├── OKRs.md                # Current quarter objectives
│   ├── EPICS.md               # Project status tracker
│   ├── epics/
│   │   └── epic-name.md       # Feature/initiative epics
│   ├── tasks/
│   │   └── epic-name-001-task.md  # Specific tasks
│   └── adrs/
│       └── 001-decision.md    # Architecture decisions
└── ...
```

See [docs/WORKFLOW.md](../../docs/WORKFLOW.md) for details on the strategy workflow.
