# Cycle 16 — SI-016

- **Item:** SI-016 — Focus modes (harden / enhance / balanced)
- **Category / priority:** feature / 9 (user-requested) · **Persona/journey:** Operator, Gatekeeper / J1, J3

## Investigate
- User asked how to steer harden vs feature-enhance; there was no toggle (fixed priority order,
  run only took cycle/time args). Chosen design: commands + run arg + persistent config default.

## Implement
- commands/harden.md, commands/enhance.md (thin shortcuts that set focus then run).
- run.md: Focus mode section (arg > loop.focus > balanced; persist a passed focus); Phase 0
  discovery and Phase 1 selection honor focus; quality bar unchanged.
- setup.md config template + this repo config.json: loop.focus = "balanced".
- validate_plugin.py: loop.focus must be harden|enhance|balanced.
- README focus-modes section + commands table; CHANGELOG; features.md row.
- Bug fix: features.md command paths were corrupted by the v1.0.0 rename sed
  (commands/self-improve:X.md); corrected to commands/X.md.

## QA gate
- make validate -> 75 checks + official claude plugin validate PASS; reinstall shows 8 commands load.

## Outcome
- GO. Squash-merged to staging.
