# ai-ready-modern-python-template

An AI-ready Python 3.14.6 project template for fast, low-friction,
high-confidence development.

This template is built for developers who use AI coding assistants and want the
project to catch low-quality changes early. It combines a pinned toolchain,
fast dependency management, strict linting, tests, hooks, secret scanning, and
GitHub Actions so generated code gets immediate feedback before it reaches
manual review.

The goal is simple: after the configured checks pass, manual review should be
focused on product intent and architecture instead of formatting, obvious bugs,
unsafe patterns, or missing quality gates. Ideally, generated changes should not
need mechanical cleanup once the linters and tests are green.

## What this template optimizes for

- Fast setup with `uv` and `mise`.
- Reproducible local and CI tooling.
- Early feedback for common AI-generated code issues.
- Separate fast and full lint commands for active editing versus final gates.
- Guardrails that reduce the need for constant human supervision.

## Check surfaces

- `mise run lint-fast` is safe for active editing and agent feedback loops.
- `mise run lint` runs the full local and CI lint gate.
- `.pre-commit-config.yaml` owns commit-time guardrails.

See [docs/lint-strategy.md](docs/lint-strategy.md) for the policy behind this
split.

## Quick start

```bash
mise install            # install pinned tools
mise run install        # install Python dependencies
mise run install-hooks  # install prek-managed pre-commit and pre-push hooks
mise run lint-fast      # run edit-safe linters
mise run lint           # run the full lint gate
mise run test           # run the pytest suite
```
