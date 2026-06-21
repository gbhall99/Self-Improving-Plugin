# Cycle 2 — SI-001

- **Item:** SI-001 — Persona/journey-grouped "shift report" PR + report
- **Category / priority:** feature / 8 · **Persona/journey:** Reviewer / J1

## Investigate (multi-angle)
- competitor lens: the #1 attack-first opportunity — Devin/Copilot/Cursor summarize *code*
  in PRs; none summarizes *user value*. The human gate is the real bottleneck of unattended
  operation, so a fast, trustworthy review surface is high leverage.
- ux-reviewer lens (Reviewer persona): a flat list of commits forces the reviewer to
  reconstruct "who does this help?". Grouping by persona/journey answers that up front.

## Implement
- Added `templates/staging-pr.md`: a shift-report template that groups shipped changes by
  persona, leads each with a Ship/Hold/Needs-review recommendation, and attaches evidence.
- Wired it into `/improve-run` Phase 6 and `/improve-report` so both render from the same
  template and stay in sync with `staging-changelog.md`.

## QA gate (make validate)
- 49 checks pass, exit 0. (Template + command-doc changes; no validator-relevant structure changed.)

## Outcome
- GO. Squash-merged to `self-improve/staging`. PR #2 body updated to use the new format.
