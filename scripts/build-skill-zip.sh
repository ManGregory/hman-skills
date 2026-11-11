#!/usr/bin/env bash
# Package each skill of a plugin as a zip for upload in Claude (Customize > Skills).
# Usage: scripts/build-skill-zip.sh <plugin-name> [out-dir]
set -euo pipefail

plugin="${1:?usage: build-skill-zip.sh <plugin-name> [out-dir]}"
root="$(cd "$(dirname "$0")/.." && pwd)"
out="$(mkdir -p "${2:-$root/dist}" && cd "${2:-$root/dist}" && pwd)"
skills_dir="$root/plugins/$plugin/skills"
version="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["version"])' "$root/plugins/$plugin/.claude-plugin/plugin.json")"

[ -d "$skills_dir" ] || { echo "No skills found in $skills_dir" >&2; exit 1; }

for skill in "$skills_dir"/*/; do
  name="$(basename "$skill")"
  zip_path="$out/$name-$version.zip"
  rm -f "$zip_path"
  # The zip holds the skill folder itself, which is what the Claude apps expect.
  (cd "$skills_dir" && zip -qr "$zip_path" "$name" -x '*.DS_Store')
  echo "$zip_path"
done
