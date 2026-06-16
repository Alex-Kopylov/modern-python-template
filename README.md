# modern-python-template

Python 3.14.6 project template: uv, mise, ruff, ty, pytest, pre-commit,
gitleaks, and a GitHub Actions CI pipeline.

Proper documentation will be written later.

## Quick start

```bash
mise install            # install pinned tools
mise run install        # install Python dependencies
mise run install-hooks  # install pre-commit and pre-push hooks
mise run lint           # run all linters in parallel
mise run test           # run the pytest suite
```
