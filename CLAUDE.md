# hman-skills

A Claude Code plugin marketplace (name: `hman`). Each plugin lives in `plugins/<name>/` and is listed in `.claude-plugin/marketplace.json`.

## Conventions

- Skills follow `plugins/<name>/skills/<skill>/SKILL.md`. Keep SKILL.md short; move detailed procedures to `references/` and blank files to `templates/`, and refer to them by relative path in backticks so `scripts/check_content.py` can verify they exist.
- Skills must work in Claude Code and in the Claude apps (uploaded as a zip). Don't rely on Claude Code-only tools or environment variables without a fallback.
- Nothing personal goes in this repository: example data in `starter/` is fictional.
- Versions live in each `plugin.json`. Bump the version and add a CHANGELOG entry for every user-visible change. Release tags are `<name>--v<version>`.

## Before committing

Run `scripts/validate.sh`. It needs the `claude` CLI and Python with `pyyaml` and `jsonschema`.
