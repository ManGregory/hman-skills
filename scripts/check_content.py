"""Content checks that `claude plugin validate` doesn't cover.

- Every SKILL.md has a name matching its folder and a description of at most 1024 characters.
- Every file a SKILL.md mentions under references/ or templates/ exists.
- Marketplace entries and plugin.json versions agree.
- Every results.json under a plugin's starter/ matches the plugin's results schema.
"""
import json
import pathlib
import re
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors: list[str] = []


def check_skill(skill_md: pathlib.Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{skill_md}: missing YAML frontmatter")
        return
    meta = yaml.safe_load(match.group(1)) or {}
    folder = skill_md.parent.name
    if meta.get("name") != folder:
        errors.append(f"{skill_md}: name '{meta.get('name')}' should match folder '{folder}'")
    description = meta.get("description") or ""
    if not description:
        errors.append(f"{skill_md}: description is empty")
    if len(description) > 1024:
        errors.append(f"{skill_md}: description is {len(description)} characters (max 1024)")
    for ref in sorted(set(re.findall(r"`((?:references|templates)/[^`\s]+)`", text))):
        if not (skill_md.parent / ref).exists():
            errors.append(f"{skill_md}: mentions {ref}, which does not exist")


def check_plugin(plugin_dir: pathlib.Path, marketplace: dict) -> None:
    manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text())
    entry = next((p for p in marketplace["plugins"] if p["name"] == manifest["name"]), None)
    if entry is None:
        errors.append(f"{plugin_dir}: not listed in .claude-plugin/marketplace.json")
    elif entry.get("version") and entry["version"] != manifest.get("version"):
        errors.append(f"{plugin_dir}: marketplace version {entry['version']} != plugin.json {manifest.get('version')}")

    for skill_md in plugin_dir.glob("skills/*/SKILL.md"):
        check_skill(skill_md)

    schemas = list(plugin_dir.glob("skills/*/templates/results.schema.json"))
    for schema_path in schemas:
        validator = Draft202012Validator(json.loads(schema_path.read_text()))
        for results in plugin_dir.glob("starter/**/results.json"):
            for err in validator.iter_errors(json.loads(results.read_text())):
                path = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{results}: {path}: {err.message}")


def main() -> int:
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    for plugin_dir in sorted(p for p in (ROOT / "plugins").iterdir() if p.is_dir()):
        check_plugin(plugin_dir, marketplace)
    if errors:
        print("\n".join(f"✗ {e}" for e in errors))
        return 1
    print("✓ Content checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
