---
description: Quick glance at the autonomous loop — current status, the item in progress, cycles completed, backlog depth, and the staging PR. Lightweight; no changes made.
---

# Self-Improve · Status

Give a fast, read-only snapshot. Do not modify anything.

Read `.self-improve/state.json`, `config.json`, `staging-changelog.md`, and `backlog.md`; check the open `staging → main` PR.

Report, in a few lines:
- **Status** — `state.json.status` (ready / running / scheduled / stopped) and whether a next cycle is scheduled.
- **Now** — the item currently in progress, if any.
- **Progress** — cycles completed, improvements landed on staging since last report, last activity time.
- **Backlog** — count of actionable / blocked items and the next 3 up.
- **Review surface** — link to the `staging → main` PR and count of items awaiting a ship decision.

If `.self-improve/config.json` is missing, tell the user to run `/improve-setup`.
