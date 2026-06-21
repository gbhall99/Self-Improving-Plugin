# Improvement Backlog — self-improve plugin

Categories: `bug` `ux` `feature` `journey` `perf` `a11y` `tech-debt`. Effort: S/M/L.
Priority score 1–10 (higher = sooner). Status: `todo` `in-progress` `done` `blocked`.

| id | title | cat | persona/journey | acceptance criterion | effort | pri | status |
|---|---|---|---|---|---|---|---|
| SI-006 | Validate generated `.self-improve/` state (config.json, state.json) in the QA gate | tech-debt | Maintainer / J2,J3 | Validator checks config/state schema + required fields when present; passes on valid, fails (exit 1) on bad; CI + `make validate` cover it | S | 9 | done ✓ cycle 1 |
| SI-001 | Persona/journey-grouped "shift report" PR body + report | feature | Reviewer / J1 | `/improve-run` Phase 6 & `/improve-report` group changes by persona/journey w/ evidence & rationale; template documented | M | 8 | done ✓ cycle 2 |
| SI-003 | Unattended safety guardrails (budget caps, auto-pause on N consecutive QA failures, kill switch) | feature | Operator,Gatekeeper / J3,J4 | `config.json` carries `loop.guardrails`; `/improve-run` honors caps & auto-pauses; documented | M | 8 | todo |
| SI-008 | Add `CONTRIBUTING.md` for the Maintainer persona | ux | Maintainer / J7 | Clear contribution + local-validation guide; linked from README | S | 7 | todo |
| SI-007 | README polish: CI badge, table of contents, no-egress/zero-infra guarantees | ux | Operator,Gatekeeper / J1 | Badge renders; TOC links resolve; guarantees section present | S | 7 | todo |
| SI-009 | Wire a real E2E + visual-regression gate tied to `journeys.md` | feature | Operator / J3 | journey-tester scaffolds Playwright+visual diff for UI repos and blocks staging on failure; documented | L | 7 | todo |
| SI-002 | Competitive research → queued citable gap tickets each loop | feature | Reviewer / J2 | competitor-researcher appends structured, sourced backlog items on discovery passes | M | 6 | todo |
| SI-004 | `/improve-recalibrate` to refresh personas/journeys/competitors | ux | Reviewer / J2 | New command re-runs research agents and diffs/updates the knowledge base | S | 6 | todo |
| SI-005 | Local versioned "playbooks/knowledge" of verified repros | feature | Operator / J3 | Successful fixes write repro+verify steps to `.self-improve/knowledge/`; loop reuses them | M | 5 | todo |
| SI-010 | Add a `CHANGELOG.md` + version bump convention | tech-debt | Maintainer | Keep-a-changelog file; version policy documented | S | 4 | todo |
| SI-011 | Consider renaming commands so they read `/self-improve:setup` not `:improve-setup` | ux | Operator / J1 | Decision recorded; if renamed, all refs/validator updated, no breakage | M | 4 | todo |

## Notes
- Bias order: P0 journey breakage & real bugs → high-impact UX → competitive-gap features → perf/a11y/tech-debt.
- SI-006 selected for cycle 1 (testable code, strengthens the plugin's own QA gate — on-theme self-improvement).
