# Copilot Instructions for Python Project

## Project Overview
This is a Python project starting from scratch. As the codebase evolves, this document will guide AI agents through its architecture, conventions, and workflows.

## Current State
- **Structure**: Early-stage project with `main.py` as the entry point
- **Dependencies**: None installed yet

## Conventions to Adopt

### Code Organization
- Place core logic in `main.py` or split into modules as the project grows
- Use descriptive function and variable names following PEP 8
- Group related functions into classes where appropriate

### Python Version
- Target: Python 3.8+
- Use type hints for all functions to improve code clarity

### Error Handling
- Use specific exception types rather than generic `Exception`
- Include logging for debugging and monitoring

### Testing
- Tests should be placed in a `tests/` directory
- Use `pytest` as the test framework when added
- Aim for >80% code coverage on new modules

## Key Files
- **main.py**: Primary application entry point (currently empty)

## Development Workflow
- No build system configured yet
- No CI/CD pipeline established

## Next Steps When Adding Features
1. Define project scope and dependencies in a `requirements.txt`
2. Create module structure under `main.py` if complexity grows
3. Add a `README.md` documenting project purpose and usage
4. Establish testing practices early

---
**Note**: This guide will evolve as the codebase grows. Update it when:
- New architectural decisions are made
- New external dependencies are introduced
- Project patterns emerge that differ from standard practices
