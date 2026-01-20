# Contributing to ai-dev-settings

Thank you for your interest in contributing to ai-dev-settings! This project helps developers quickly set up AI coding tools across their projects.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in [GitHub Issues](https://github.com/drewdresser/ai-dev-settings/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, shell, etc.)

### Submitting Changes

1. **Fork the repository** and create a new branch from `main`
2. **Make your changes**:
   - Keep changes focused and minimal
   - Follow the existing code style
   - Test your changes thoroughly
3. **Test the installation**:
   ```bash
   # Test project installation
   cd /tmp/test-project
   just -f /path/to/your/fork/justfile install
   
   # Test global linking
   cd /path/to/your/fork
   just link-global
   ```
4. **Update documentation** if you've changed functionality
5. **Submit a pull request** with:
   - Clear description of changes
   - Link to related issue (if applicable)
   - Any breaking changes highlighted

## Development Guidelines

### File Structure

- `project/` - Files to install into projects
- `global/` - Global configuration files
- `scripts/` - Installation scripts
- `dashboard/` - Strategy dashboard
- `docs/` - Documentation

### Adding New Features

When adding new agent definitions, commands, or hooks:

1. Place files in the appropriate directory under `project/`
2. Update the README.md if it's a significant feature
3. Ensure the install script copies the new files correctly
4. Test the installation in a sample project

### Code Style

- **Shell scripts**: Follow existing patterns, use `set -euo pipefail`
- **Markdown**: Use clear headings, code blocks with language tags
- **Python**: Follow PEP 8 (for dashboard code)

### Testing Checklist

Before submitting a PR, verify:

- [ ] Installation script works correctly
- [ ] Global linking script works correctly
- [ ] All new files are copied to the right locations
- [ ] Documentation is updated
- [ ] No sensitive or personal information included
- [ ] Changes work on Linux/macOS (Windows if applicable)

## Questions?

Feel free to open an issue for discussion before starting major changes.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
