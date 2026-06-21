# Cycle 13 — SI-014

- **Item:** SI-014 — Fix plugin manifest so it installs (bug, found by smoke test)
- **Category / priority:** bug / 10 · **Persona/journey:** all / J1 (install)

## Investigate
- Smoke test: `claude plugin validate .` failed -> `plugins[0] plugin.json -> agents: Invalid input`.
  `commands`/`agents` were string paths; the official schema auto-discovers those dirs and rejects
  the string form. Our own validator had only checked dir existence, missing the type error.

## Implement
- Removed `commands`/`agents` from plugin.json (auto-discovery).
- validate_plugin.py: require array form for commands/agents if present (so CI catches it).
- Makefile: also run `claude plugin validate .` when the CLI is available (best-effort; not on CI).
- Docs: CONTRIBUTING + CHANGELOG.

## QA gate
- python validator 70 checks PASS; official `claude plugin validate` PASS; install succeeds;
  6 commands + 9 agents load (verified via `claude plugin details`).

## Outcome
- GO. Squash-merged to staging.
