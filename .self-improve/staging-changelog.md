# Staging Changelog — self-improve plugin

Each entry is one improvement squash-merged onto `self-improve/staging`, awaiting a ship
decision on the `staging → main` PR. Tick `Ship?` to mark what to keep.

<!-- entries appended newest-last by the loop -->

## Cycle 1 — SI-006 · Validate generated `.self-improve/` state in the QA gate
- **Category:** tech-debt · **Persona/journey:** Maintainer / J2, J3
- **Impact:** the plugin's QA gate now also validates the knowledge base the loop itself
  generates (`config.json`, `state.json`) — malformed generated state can no longer
  silently break a run.
- **Evidence:** `make validate` → 49 checks pass; negative tests (bad `status`, missing
  `cycle`, empty `qaGate`, missing `loop.*`) correctly fail with exit 1.
- **Commit:** `737905a`
- **Ship?** [ ] yes [ ] hold

## Cycle 2 — SI-001 · Persona/journey-grouped "shift report" PR + report
- **Category:** feature · **Persona/journey:** Reviewer / J1
- **Impact:** the `staging → main` PR and `/improve-report` now group every change by the
  persona/journey it serves with a Ship/Hold recommendation + evidence — a reviewer can
  approve hours of unattended work in minutes by reading user value, not raw code. Closes
  the top competitive gap (no rival summarizes user value).
- **Evidence:** `make validate` → 49 checks pass; new `templates/staging-pr.md` wired into
  `/improve-run` Phase 6 and `/improve-report`. (This very PR body is rendered from it.)
- **Commit:** `<pending>`
- **Ship?** [ ] yes [ ] hold
