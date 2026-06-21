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
- **Commit:** `ae3a6a0`
- **Ship?** [ ] yes [ ] hold

## Cycle 3 — SI-003 · Unattended safety guardrails
- **Category:** feature · **Persona/journey:** Operator, Gatekeeper / J3, J4
- **Impact:** makes "leave it running for hours" actually safe — kill switch, auto-pause
  after a failure streak (default 3), merges/hour rate cap (default 6), optional spend cap,
  and absolute out-of-bounds, all honored by `/improve-run`. This is the precondition rivals
  avoid by billing per-task; we offer bounded, auditable continuous operation.
- **Evidence:** `make validate` → 49 checks pass (incl. SI-006's config/state schema check
  on the new `loop.guardrails`); `/improve-setup` writes guardrails; `/improve-stop` documents
  stopped vs paused.
- **Commit:** `9e483c4`
- **Ship?** [ ] yes [ ] hold

## Cycle 4 — SI-008 · CONTRIBUTING.md for the Maintainer persona
- **Category:** ux · **Persona/journey:** Maintainer / J7
- **Impact:** contributors now have a clear path — project layout, the local validation gate,
  and how to add commands/agents with correct frontmatter — lowering the barrier to extend the plugin.
- **Evidence:** `make validate` → 49 checks pass; `CONTRIBUTING.md` added and linked from README.
- **Commit:** `bc4b328`
- **Ship?** [ ] yes [ ] hold


## Cycle 5 — SI-007 · README polish (badge, TOC, guarantees)
- **Category:** ux · **Persona/journey:** Operator, Gatekeeper / J1
- **Impact:** the front door now surfaces the differentiators — CI status badge, a navigable
  table of contents, and an explicit "Zero-infra, no-egress" + bounded-autonomy guarantees
  section that the Operator and (especially) Gatekeeper personas evaluate on.
- **Evidence:** `make validate` → 49 checks pass; badge points at the validate workflow; TOC anchors resolve.
- **Commit:** `29d513f`
- **Ship?** [ ] yes [ ] hold
