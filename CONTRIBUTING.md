# Contributing to ai-dev-settings

Thank you for your interest in contributing! This project aims to help developers quickly set up and configure AI coding tools with best practices.

## How to Contribute

### Reporting Issues

If you encounter bugs or have feature requests:

1. Check existing issues to avoid duplicates
2. Use the issue templates provided
3. Include relevant details:
   - Your OS and shell environment
   - The AI tool you're using (Claude Code, Cursor, Codex)
   - Steps to reproduce the issue
   - Expected vs actual behavior

### Suggesting Improvements

We welcome suggestions for:
- New agent configurations
- Additional command templates
- New skills or hooks
- Documentation improvements
- Stack-specific configurations

### Pull Requests

1. **Fork and clone** the repository
2. **Create a branch** for your changes: `git checkout -b feature/your-feature-name`
3. **Make your changes**:
   - Follow existing patterns and conventions
   - Keep configurations generic and reusable
   - Test in at least one real project
4. **Document your changes**:
   - Update README.md if adding new features
   - Add comments to explain complex logic
   - Update CHANGELOG.md
5. **Submit a PR** with:
   - Clear description of what changed and why
   - Reference any related issues
   - Screenshots/examples if applicable

## Guidelines

### Configuration Files

- **Markdown-first**: Use markdown for all agent/command/skill definitions
- **Generic names**: Avoid hardcoded project-specific values
- **Comments**: Explain non-obvious patterns or decisions
- **Tested**: Verify configurations work in real projects

### Code Style

- **Python**: Follow PEP 8, use type hints
- **Shell scripts**: Use bash, include error handling
- **Markdown**: Use consistent heading levels and formatting

### Commit Messages

Use clear, descriptive commit messages:
- `feat: add security-auditor agent`
- `fix: correct hook script permissions`
- `docs: update dashboard configuration options`
- `refactor: simplify install script logic`

## Project Structure

When adding new configurations:

- **Agents**: Add to `project/claude/agents/`
- **Commands**: Add to `project/claude/commands/`
- **Skills**: Add to `project/claude/skills/`
- **Hooks**: Add scripts to `project/claude/hooks/scripts/`
- **Global configs**: Update `global/` directory

## Testing

Before submitting:

1. Test installation in a fresh project: `just install`
2. Verify global linking works: `just link-global`
3. Test any new scripts for errors
4. Ensure dashboard still works if modifying parser/models

## Questions?

Feel free to open an issue for questions or discussions about:
- Best practices for AI agent configurations
- New feature ideas
- Architecture decisions

## Code of Conduct

- Be respectful and constructive
- Focus on what's best for the project and community
- Help create a welcoming environment for all contributors

Thank you for contributing!
