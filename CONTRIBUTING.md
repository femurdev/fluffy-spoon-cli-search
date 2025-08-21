# Contributing to CLI Search Engine

Thank you for considering contributing to this project! Your help is greatly appreciated.

## How to Contribute

### Reporting Bugs
If you find a bug, please open an issue on the repository with the following details:
- A clear and descriptive title.
- Steps to replicate the issue.
- Expected behavior vs. actual behavior.
- Any relevant error messages or logs.

### Suggesting Features
We welcome feature suggestions! To propose a new feature:
1. Open an issue with the label `enhancement`.
2. Provide a detailed description of the feature and its use case.
3. If possible, suggest a high-level implementation approach.

### Submitting Code Changes
To contribute code:
1. Fork the repository.
2. Create a new branch for your feature or bug fix (e.g., `feature/add-logging` or `bugfix/fix-crawl-error`).
3. Write clear and descriptive commit messages.
4. Submit a pull request (PR) with a detailed description of your changes.

### Code Style
Please adhere to the following guidelines:
- Use descriptive variable and function names.
- Write inline comments for complex logic.
- Ensure your code passes Python linters like `flake8` or `pylint`.

### Testing
If applicable, add tests for your changes. Ensure all existing tests pass before submitting your PR.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Project
- Use `crawler.py` to crawl websites and store data.
- Use `cli_search.py` to search the SQLite database.

### Running Tests
- Add tests in the `tests` directory.
- Run tests using `pytest`:
  ```bash
  pytest
  ```

## Code of Conduct
Be respectful and constructive in your interactions. Follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Thank you for contributing!