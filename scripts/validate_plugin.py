#!/usr/bin/env python3
"""Validate the self-improve Claude Code plugin.

Checks plugin/marketplace manifests and the frontmatter of every command and
agent. Pure stdlib (no pip install) so it runs identically in CI, in a local
`make validate`, and from a git pre-push hook.

Exit code 0 = all good, 1 = one or more problems found.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors: list[str] = []
checks = 0


def err(msg: str) -> None:
    errors.append(msg)


def ok(_msg: str) -> None:
    global checks
    checks += 1


def load_json(rel: str) -> dict | None:
    path = ROOT / rel
    if not path.is_file():
        err(f"{rel}: file is missing")
        return None
    try:
        data = json.loads(path.read_text())
        ok(f"{rel}: valid JSON")
        return data
    except json.JSONDecodeError as exc:
        err(f"{rel}: invalid JSON ({exc})")
        return None


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    """Minimal YAML-frontmatter reader for our flat `key: value` blocks."""
    text = path.read_text()
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    # No closing delimiter found.
    return None


def require_fields(data: dict, fields: list[str], where: str) -> None:
    for field in fields:
        if field not in data or data[field] in (None, "", []):
            err(f"{where}: missing required field '{field}'")
        else:
            ok(f"{where}: has '{field}'")


def validate_plugin_manifest() -> None:
    data = load_json(".claude-plugin/plugin.json")
    if data is None:
        return
    require_fields(data, ["name", "version", "description"], "plugin.json")
    # If commands/agents dirs are declared, they must exist.
    for key in ("commands", "agents"):
        val = data.get(key)
        if isinstance(val, str) and not (ROOT / val).is_dir():
            err(f"plugin.json: '{key}' points to missing dir '{val}'")


def validate_marketplace_manifest() -> None:
    data = load_json(".claude-plugin/marketplace.json")
    if data is None:
        return
    require_fields(data, ["name", "owner", "plugins"], "marketplace.json")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        err("marketplace.json: 'plugins' must be a non-empty array")
        return
    for i, plugin in enumerate(plugins):
        where = f"marketplace.json plugins[{i}]"
        if not isinstance(plugin, dict):
            err(f"{where}: must be an object")
            continue
        require_fields(plugin, ["name", "source", "description"], where)
        source = plugin.get("source")
        if isinstance(source, str) and not (ROOT / source).exists():
            err(f"{where}: source path '{source}' does not exist")


def validate_markdown_dir(dirname: str, required: list[str]) -> None:
    directory = ROOT / dirname
    if not directory.is_dir():
        err(f"{dirname}/: directory is missing")
        return
    md_files = sorted(directory.glob("*.md"))
    if not md_files:
        err(f"{dirname}/: contains no .md files")
        return
    for path in md_files:
        rel = path.relative_to(ROOT)
        fm = parse_frontmatter(path)
        if fm is None:
            err(f"{rel}: missing or unterminated YAML frontmatter (--- ... ---)")
            continue
        require_fields(fm, required, str(rel))
        # An agent's declared name should match its filename for discoverability.
        if "name" in required and fm.get("name") and fm["name"] != path.stem:
            err(f"{rel}: agent name '{fm['name']}' should match filename '{path.stem}'")


def main() -> int:
    validate_plugin_manifest()
    validate_marketplace_manifest()
    validate_markdown_dir("commands", ["description"])
    validate_markdown_dir("agents", ["name", "description"])

    print(f"self-improve plugin validation: {checks} checks passed.")
    if errors:
        print(f"\n{len(errors)} problem(s) found:")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print("All good ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
