# AGENTS.md

## Purpose
Small Python CLI utility (`Expense Calculator`) for calculating totals, filtering expenses by category, and loading JSON expense records.

## Architecture
- `calculator.py`: Core domain logic (`calculate_total`, `filter_by_category`, `summarize_by_category`, `load_expenses`).
- `test_calculator.py`: Automated unit tests using `pytest`.
- `requirements.txt`: Test runner dependency (`pytest`).

## Setup & Safe Commands
- Install test dependency: `pip install -r requirements.txt`
- Run tests: `pytest -v`
- Syntax check: `python -m py_compile calculator.py test_calculator.py`
- Check git status/diff: `git status`, `git diff`

## Coding Conventions
- Keep functions small, deterministic, and focused on single responsibilities.
- Validate inputs explicitly and raise clear `ValueError` exceptions on invalid domain values.
- Do not add external heavy frameworks or unrequested dependencies.

## Test Expectations
- All existing and new tests in `pytest -v` must pass before considering any task complete.
- Every bug fix or refactor must include corresponding unit tests.

## Forbidden Actions
- Never commit or expose secrets, API keys, tokens, credentials, or real personal data.
- Never perform production deployments or touch external infrastructure.
- Never run destructive commands (`rm -rf /`, `git reset --hard` on shared branches, dropping databases).
- Never install or modify dependencies without explicit human approval.

## Note on Tool Loading
If the AI assistant does not automatically read `AGENTS.md`, its rules are pasted directly into the prompt context before making suggestions.