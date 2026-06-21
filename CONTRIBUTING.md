# Contributing to self-improve

Thanks for helping improve the plugin. This guide is for the **Maintainer** persona —
people editing the commands, agents, validation, or docs.

## Project layout

```
.claude-plugin/        plugin.json (manifest) + marketplace.json (installable marketplace)
commands/              one slash command per .md file (frontmatter: description)
agents/                one subagent per .md file (frontmatter: name + description)
templates/             reusable output templates (e.g. the staging-PR shift report)
scripts/               validate_plugin.py — the QA gate
.githooks/             pre-push hook that runs the QA gate locally
.github/workflows/     validate-plugin CI (mirrors the local gate)
.self-improve/         knowledge base the loop generates/maintains in a target repo
```

## The golden rule: validation must pass

The same check runs in CI, locally, and on pre-push — so it never depends on GitHub Actions
credit. Run it before every push:

```bash
make validate          # or: python3 scripts/validate_plugin.py
make install-hooks      # once per clone: gate every push locally (bypass: git push --no-verify)
```

`make validate` checks:
- `plugin.json` / `marketplace.json` — valid JSON, required fields, referenced paths exist
- every `commands/*.md` has frontmatter with a `description`
- every `agents/*.md` has frontmatter with `name` + `description`, and `name` matches the filename
- the generated `.self-improve/` state (`config.json`, `state.json`), when present

## Adding a command

1. Create `commands/<name>.md` with frontmatter:
   ```markdown
   ---
   description: One clear line shown in the command list.
   argument-hint: "[optional: what args do]"
   ---
   # Command body — the prompt the agent executes.
   ```
2. Keep it action-oriented and unambiguous; reference shared state in `.self-improve/`.
3. `make validate`, then open a PR.

## Adding an agent

1. Create `agents/<name>.md` where `name` in the frontmatter **equals the filename stem**:
   ```markdown
   ---
   name: <name>
   description: When to use this agent and what it returns.
   tools: Read, Grep, Glob   # optional; omit to inherit all
   ---
   # Agent body — its method and what it reports back.
   ```
2. `make validate`, then open a PR.

## Pull requests

- Keep changes focused and independently revertible.
- Make sure CI (`validate-plugin`) is green.
- Describe the user value, not just the code (the plugin's own ethos).

## Releasing

1. Move the relevant `[Unreleased]` notes in [CHANGELOG.md](CHANGELOG.md) under a new version heading.
2. Bump `version` in `.claude-plugin/plugin.json` (and `marketplace.json` metadata) using
   [SemVer](https://semver.org/) — patch for fixes, minor for new commands/agents, major for
   breaking changes (e.g. renaming or removing a command).
3. Tag the release `vX.Y.Z`.
