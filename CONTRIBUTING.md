# Contributing to Agentic Workflow Manager

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/workflow-manager.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit: `git commit -m "Add your feature"`
7. Push: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

See [SETUP.md](./SETUP.md) for detailed setup instructions.

## Code Style

### Python (Backend)
- Follow PEP 8
- Use type hints
- Write docstrings for functions and classes
- Use async/await for I/O operations

### TypeScript (Frontend)
- Use TypeScript strict mode
- Follow React best practices
- Use functional components with hooks
- Write meaningful component names

## Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v --cov=app
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Adding New Tools

1. Create tool file in `backend/app/tools/`
2. Inherit from `BaseTool`
3. Implement `_run()` and `_arun()` methods
4. Register in `backend/app/tools/registry.py`
5. Add tests
6. Update documentation

Example:
```python
from langchain.tools import BaseTool

class MyCustomTool(BaseTool):
    name = "my_custom_tool"
    description = "What this tool does"
    
    def _run(self, param: str) -> str:
        # Implementation
        return result
    
    async def _arun(self, *args, **kwargs):
        return self._run(*args, **kwargs)
```

## Adding New Agents

1. Create agent file in `backend/app/agents/`
2. Implement agent logic
3. Update `backend/app/agents/graph.py`
4. Add tests
5. Update documentation

## Pull Request Guidelines

- Write clear, descriptive commit messages
- Include tests for new features
- Update documentation
- Ensure all tests pass
- Keep PRs focused on a single feature/fix

## Reporting Issues

When reporting issues, please include:
- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)

## Feature Requests

We welcome feature requests! Please:
- Check if the feature already exists
- Describe the use case
- Explain why it would be valuable
- Provide examples if possible

## Code Review Process

1. Automated tests must pass
2. Code review by maintainers
3. Address feedback
4. Approval and merge

## Community

- Be respectful and inclusive
- Help others learn
- Share knowledge
- Collaborate openly

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
