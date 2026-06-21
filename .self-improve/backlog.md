# Improvement Backlog — self-improve plugin

Categories: `bug` `ux` `feature` `journey` `perf` `a11y` `tech-debt`. Effort: S/M/L.
Priority score 1–10 (higher = sooner). Status: `todo` `in-progress` `done` `blocked`.

| id | title | cat | persona/journey | acceptance criterion | effort | pri | status |
|---|---|---|---|---|---|---|---|
| SI-006 | Validate generated `.self-improve/` state (config.json, state.json) in the QA gate | tech-debt | Maintainer / J2,J3 | Validator checks config/state schema + required fields when present; passes on valid, fails (exit 1) on bad; CI + `make validate` cover it | S | 9 | done ✓ cycle 1 |
| SI-001 | Persona/journey-grouped "shift report" PR body + report | feature | Reviewer / J1 | `/self-improve:run` Phase 6 & `/self-improve:report` group changes by persona/journey w/ evidence & rationale; template documented | M | 8 | done ✓ cycle 2 |
| SI-003 | Unattended safety guardrails (budget caps, auto-pause on N consecutive QA failures, kill switch) | feature | Operator,Gatekeeper / J3,J4 | `config.json` carries `loop.guardrails`; `/self-improve:run` honors caps & auto-pauses; documented | M | 8 | done ✓ cycle 3 |
| SI-008 | Add `CONTRIBUTING.md` for the Maintainer persona | ux | Maintainer / J7 | Clear contribution + local-validation guide; linked from README | S | 7 | done ✓ cycle 4 |
| SI-007 | README polish: CI badge, table of contents, no-egress/zero-infra guarantees | ux | Operator,Gatekeeper / J1 | Badge renders; TOC links resolve; guarantees section present | S | 7 | done ✓ cycle 5 |
| SI-009 | Wire a real E2E + visual-regression gate tied to `journeys.md` | feature | Operator / J3 | journey-tester scaffolds Playwright+visual diff for UI repos and blocks staging on failure; documented | L | 7 | todo |
| SI-002 | Competitive research → queued citable gap tickets each loop | feature | Reviewer / J2 | competitor-researcher appends structured, sourced backlog items on discovery passes | M | 6 | done ✓ cycle 8 |
| SI-004 | `/self-improve:recalibrate` to refresh personas/journeys/competitors | ux | Reviewer / J2 | New command re-runs research agents and diffs/updates the knowledge base | S | 6 | done ✓ cycle 6 |
| SI-005 | Local versioned "playbooks/knowledge" of verified repros | feature | Operator / J3 | Successful fixes write repro+verify steps to `.self-improve/knowledge/`; loop reuses them | M | 5 | done ✓ cycle 9 |
| SI-010 | Add a `CHANGELOG.md` + version bump convention | tech-debt | Maintainer | Keep-a-changelog file; version policy documented | S | 4 | done ✓ cycle 7 |
| SI-011 | Rename commands to `/self-improve:*` (BREAKING, v1.0.0) | ux | Operator / J1 | Files renamed; all refs updated; version bumped; CHANGELOG records breaking change | M | 4 | done ✓ cycle 11 |

| SI-012 | Bake in operating principles (no emoji/crisp icons, simplify, de-dup, docs current, document+test features/personas/journeys) + features.md + emoji QA check | feature | all / all | PRINCIPLES.md wired into commands+agents; features.md produced; validator rejects emojis; docs current | M | 9 | done ✓ cycle 10 |

| SI-013 | Principle 6: prefer AI-centric, agentic solutions | feature | all / all | PRINCIPLES.md gains principle 6; wired into run/setup standards + feature-scout + implementer; docs current | S | 8 | done ✓ cycle 12 |

| SI-014 | Fix plugin.json so it passes official `claude plugin validate` and installs | bug | all / J1 | Manifest validates and installs; local validator rejects non-array commands/agents; make validate runs official validator when available | S | 10 | done ✓ cycle 13 |

## Notes
- Bias order: P0 journey breakage & real bugs → high-impact UX → competitive-gap features → perf/a11y/tech-debt.
- SI-006 selected for cycle 1 (testable code, strengthens the plugin's own QA gate — on-theme self-improvement).
