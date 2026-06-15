"""Smoke tests for the repository template."""

import tomllib
from pathlib import Path

ROOT = Path(__file__).parent.parent
PYTHON_VERSION = "3.14.6"


def test_repo_has_pyproject() -> None:
    assert (ROOT / "pyproject.toml").is_file()


def test_python_version_is_current_stable() -> None:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text())
    mise = tomllib.loads((ROOT / "mise.toml").read_text())
    ruff = tomllib.loads((ROOT / ".ruff.toml").read_text())

    assert (ROOT / ".python-version").read_text().strip() == PYTHON_VERSION
    assert pyproject["project"]["requires-python"] == ">=3.14"
    assert pyproject["tool"]["ty"]["environment"]["python-version"] == "3.14"
    assert mise["tools"]["python"] == PYTHON_VERSION
    assert ruff["target-version"] == "py314"


def test_template_scaffold_files_are_present() -> None:
    assert not (ROOT / "Makefile").exists()
    assert (ROOT / "LICENSE").read_text().startswith("MIT License")
    assert (ROOT / "Dockerfile").is_file()
    assert (ROOT / ".dockerignore").is_file()
    assert (ROOT / ".github" / "dependabot.yml").is_file()
