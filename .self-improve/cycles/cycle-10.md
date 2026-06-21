# Cycle 10 — SI-012

- **Item:** SI-012 — Operating principles + features doc + emoji enforcement
- **Category / priority:** feature,tech-debt,ux / 9 · **Persona/journey:** all / all

## Investigate
- User set five standing standards. These are cross-cutting policy, so they belong in the plugin
  itself (apply to any target repo), not just generated state. Principle 1 is mechanically
  checkable -> enforce in the QA gate. Principle 5 needs a features.md alongside personas/journeys.

## Implement
- PRINCIPLES.md canonical; referenced from /improve-run, /improve-setup, /improve-report,
  /improve-recalibrate and 5 agents.
- features.md catalogue + setup step + loop read.
- validate_plugin.py: emoji ban over commands/agents/templates + root docs.
- Scrubbed existing emojis (personas star -> [primary]; template robot removed; de-emoji template).
- Docs current: README (principles, features row, recalibrate, TOC), CONTRIBUTING, CHANGELOG.

## QA gate
- make validate -> 70 checks pass; injected emoji -> exit 1 (rule fires).

## Outcome
- GO. Squash-merged to staging.
