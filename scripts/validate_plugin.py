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
    # `commands`/`agents` are auto-discovered from their directories. If declared
    # explicitly they must be an ARRAY of paths (a bare string fails the official
    # `claude plugin validate` schema), and each path must exist.
    for key in ("commands", "agents"):
        if key not in data:
            continue
        val = data[key]
        if not isinstance(val, list):
            err(f"plugin.json: '{key}' must be an array of paths (or omitted for auto-discovery)")
            continue
        for entry in val:
            if not isinstance(entry, str) or not (ROOT / entry).exists():
                err(f"plugin.json: '{key}' entry '{entry}' does not exist")


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


VALID_STATES = {"ready", "running", "scheduled", "stopped", "paused"}


def validate_self_improve_state() -> None:
    """Validate the generated .self-improve/ knowledge base, if present.

    These files only exist after `/improve-setup` has run, so absence is fine
    (a fresh target repo, or this plugin before its own setup). When they do
    exist, a malformed config/state would silently break the loop — so the QA
    gate covers them too.
    """
    base = ROOT / ".self-improve"
    if not base.is_dir():
        return  # not set up yet — nothing to validate

    config = base / "config.json"
    if config.is_file():
        data = load_json(".self-improve/config.json")
        if data is not None:
            require_fields(
                data, ["product", "primaryGoal", "branches", "loop", "qaGate"],
                ".self-improve/config.json",
            )
            branches = data.get("branches")
            if isinstance(branches, dict):
                require_fields(
                    branches, ["main", "staging", "cyclePrefix"],
                    ".self-improve/config.json branches",
                )
            elif branches is not None:
                err(".self-improve/config.json: 'branches' must be an object")
            loop = data.get("loop")
            if isinstance(loop, dict):
                require_fields(
                    loop, ["sessionBudgetHours", "checkpointMinutes", "mergePolicy"],
                    ".self-improve/config.json loop",
                )
                focus = loop.get("focus")
                if focus is not None and focus not in ("harden", "enhance", "balanced"):
                    err(
                        ".self-improve/config.json: loop.focus must be one of "
                        "['balanced', 'enhance', 'harden']"
                    )
            elif loop is not None:
                err(".self-improve/config.json: 'loop' must be an object")
            qa = data.get("qaGate")
            if qa is not None and (not isinstance(qa, list) or not qa):
                err(".self-improve/config.json: 'qaGate' must be a non-empty array")

    state = base / "state.json"
    if state.is_file():
        data = load_json(".self-improve/state.json")
        if data is not None:
            require_fields(data, ["status", "cycle"], ".self-improve/state.json")
            status = data.get("status")
            if status is not None and status not in VALID_STATES:
                err(
                    f".self-improve/state.json: status '{status}' must be one of "
                    f"{sorted(VALID_STATES)}"
                )
            if "cycle" in data and not isinstance(data["cycle"], int):
                err(".self-improve/state.json: 'cycle' must be an integer")


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


# Codepoints treated as emoji (principle 1). Astral pictographs plus a few BMP
# emoji-presentation symbols. Plain text-style icons like ✓ ✗ → • are allowed.
_EMOJI_BLOCKLIST = {
    0x2B50, 0x2B55, 0x2705, 0x274C, 0x2728, 0x26A0, 0x2757, 0x2753, 0x2B1B, 0x2B1C,
}


def _has_emoji(ch: str) -> bool:
    cp = ord(ch)
    return cp >= 0x1F000 or cp in _EMOJI_BLOCKLIST


def validate_no_emojis() -> None:
    """Principle 1: no emojis in the plugin's own markdown — crisp iconography only."""
    targets: list[Path] = []
    for dirname in ("commands", "agents", "templates"):
        d = ROOT / dirname
        if d.is_dir():
            # recursive so nested docs (e.g. templates/e2e/README.md) are covered too
            targets += sorted(d.rglob("*.md"))
    for name in ("README.md", "CONTRIBUTING.md", "PRINCIPLES.md", "CHANGELOG.md"):
        p = ROOT / name
        if p.is_file():
            targets.append(p)
    for path in targets:
        rel = path.relative_to(ROOT)
        bad = sorted({ch for ch in path.read_text() if _has_emoji(ch)})
        if bad:
            chars = " ".join(f"U+{ord(c):04X}" for c in bad)
            err(f"{rel}: contains emoji ({chars}) — principle 1 forbids emojis (use crisp iconography)")
        else:
            ok(f"{rel}: no emojis")


def main() -> int:
    validate_plugin_manifest()
    validate_marketplace_manifest()
    validate_markdown_dir("commands", ["description"])
    validate_markdown_dir("agents", ["name", "description"])
    validate_self_improve_state()
    validate_no_emojis()

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
