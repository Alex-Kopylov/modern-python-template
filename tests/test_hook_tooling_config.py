"""Tests for the repository hook tooling configuration."""

import tomllib
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_hook_runner_dependency_is_prek() -> None:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text())
    dev_dependencies = pyproject["dependency-groups"]["dev"]

    assert "prek" in dev_dependencies
    assert "pre-commit" not in dev_dependencies


def test_install_hooks_task_uses_prek_for_commit_and_push_hooks() -> None:
    mise = tomllib.loads((ROOT / "mise.toml").read_text())
    install_hooks = mise["tasks"]["install-hooks"]

    assert install_hooks["run"] == ("uv run prek install --hook-type pre-commit --hook-type pre-push")


def test_prek_uses_existing_pre_commit_config() -> None:
    assert (ROOT / ".pre-commit-config.yaml").is_file()


def test_python_hooks_run_through_uv() -> None:
    config = (ROOT / ".pre-commit-config.yaml").read_text()

    assert "entry: uv run ruff format --force-exclude" in config
    assert "entry: uv run ruff check --fix --force-exclude" in config
    assert "entry: uv run flake8 --select=ASYNC" in config
    assert "entry: uv run ty check" in config
    assert "entry: uv run yamllint -c .yamllint" in config
    assert "entry: uv run check-jsonschema --builtin-schema github-workflows" in config

    assert "entry: mise exec -- ruff" not in config
    assert "entry: mise exec -- flake8" not in config
    assert "entry: mise exec -- ty check" not in config
    assert "entry: mise exec -- yamllint" not in config
    assert "entry: mise exec -- check-jsonschema" not in config
