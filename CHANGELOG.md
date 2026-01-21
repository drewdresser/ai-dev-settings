# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- MIT License for open source distribution
- CONTRIBUTING.md with contribution guidelines
- This CHANGELOG.md file
- GitHub issue templates
- Enhanced .gitignore for Python bytecode files

## [1.0.0] - 2026-01-19

### Added
- Multi-project AI agent development framework (WORKFLOW.md)
- Strategy dashboard with auto-discovery and visualization
- 7 specialized Claude agents (code-reviewer, debugger, test-architect, security-auditor, refactorer, docs-writer, orchestrator)
- 25+ reusable command templates for common development tasks
- 6 skill modules for specialized knowledge
- Hooks system with 7 event types and shell scripts
- Global configuration system for Claude Code and Codex
- Project installation scripts (`install_project.sh`, `link_global.sh`)
- Just command runner integration
- Python backend configuration (uv, pytest, ruff, ty)
- React frontend configuration (pnpm, TypeScript)
- AWS deployment configuration (Amplify, Lambda/ECS, CDK)

### Documentation
- Comprehensive README with quick start guide
- Detailed WORKFLOW.md specification
- PEP 723 inline scripts guidance for agent configs
- Dashboard configuration and usage documentation
