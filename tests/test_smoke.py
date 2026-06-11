"""Smoke tests for the repository template."""

from pathlib import Path


def test_repo_has_pyproject() -> None:
    assert (Path(__file__).parent.parent / "pyproject.toml").is_file()
