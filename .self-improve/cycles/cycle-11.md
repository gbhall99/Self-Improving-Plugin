# Cycle 11 — SI-011

- **Item:** SI-011 — Rename commands to /self-improve:* (BREAKING)
- **Category / priority:** ux / 4 (user-requested) · **Persona/journey:** Operator / J1

## Investigate
- User authorized the rename + a major version bump. Command files were `improve-*.md`, which
  under the `self-improve` plugin namespace read as `/self-improve:improve-setup` (redundant).

## Implement
- git mv the 6 command files to bare names (setup/run/report/status/stop/recalibrate).
- sed-updated all `/improve-*` refs to `/self-improve:*` across commands, agents, templates,
  README, CONTRIBUTING, PRINCIPLES, features.md, journeys.md, personas.md, backlog.md.
- Left historical staging-changelog and cycle logs untouched (accurate to their time).
- Bumped plugin.json + marketplace.json to 1.0.0; CHANGELOG [1.0.0] notes the BREAKING rename.

## QA gate
- make validate -> 70 checks pass; no stale refs in current docs.

## Outcome
- GO. Squash-merged to staging.
