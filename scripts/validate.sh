#!/usr/bin/env bash
# Validate the marketplace, every plugin, skill frontmatter, and example data.
# Needs: claude (Claude Code CLI), python3 with pyyaml and jsonschema.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

echo "== Marketplace"
claude plugin validate .

for plugin in plugins/*/; do
  echo "== Plugin $plugin"
  claude plugin validate "$plugin"
done

echo "== Skills and example data"
python3 scripts/check_content.py
