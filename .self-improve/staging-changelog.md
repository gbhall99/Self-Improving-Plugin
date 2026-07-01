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

## Cycle 6 — SI-004 · /improve-recalibrate command
- **Category:** ux · **Persona/journey:** Reviewer / J2
- **Impact:** the knowledge base can now be refreshed mid-life (personas/journeys/competitors
  drift) without a full re-setup; diffs rather than clobbers and re-prioritizes the backlog so
  the loop keeps targeting what's true now.
- **Evidence:** `make validate` -> 50 checks pass (new command picked up + frontmatter valid).
- **Commit:** `1c92256`
- **Ship?** [ ] yes [ ] hold

## Cycle 7 — SI-010 · CHANGELOG.md + SemVer release policy
- **Category:** tech-debt · **Persona/journey:** Maintainer
- **Impact:** releases are now trackable and predictable — a keep-a-changelog file and a
  documented version-bump/tag procedure.
- **Evidence:** `make validate` -> 50 checks pass; CHANGELOG.md added, CONTRIBUTING release steps updated.
- **Commit:** `c06e6fa`
- **Ship?** [ ] yes [ ] hold

## Cycle 8 — SI-002 · Competitor research → queued citable gap tickets
- **Category:** feature · **Persona/journey:** Reviewer / J2
- **Impact:** competitive catch-up becomes continuous and automatic — the loop turns the
  market into queued, sourced backlog items, closing the gap rivals leave open (none ingests
  the market as input).
- **Evidence:** `make validate` -> 50 checks pass; competitor-researcher gains a gap-ticket
  spec (dedup, cap, sourced), wired into /improve-run Phase 0.
- **Commit:** `a6ffcf4`
- **Ship?** [ ] yes [ ] hold

## Cycle 9 — SI-005 · Local versioned playbooks/knowledge
- **Category:** feature · **Persona/journey:** Operator / J3
- **Impact:** the loop now gets smarter about *your* repo over time — verified repro/verify
  steps are saved to `.self-improve/knowledge/` and reused, matching Devin's compounding
  knowledge advantage but kept local and version-controlled (no vendor knowledge silo).
- **Evidence:** `make validate` -> 50 checks pass; `/improve-run` consults knowledge (Phase 2)
  and captures playbooks (Phase 5); `/improve-setup` creates the dir; seeded a real qa-gate playbook.
- **Commit:** `128974c` (landed directly on staging — single clean commit)
- **Ship?** [ ] yes [ ] hold

## Cycle 10 — SI-012 · Bake in operating principles + features doc
- **Category:** feature, tech-debt, ux · **Persona/journey:** all / all
- **Impact:** the five standing standards are now enforced everywhere: no emojis (crisp
  iconography, now a hard QA-gate check), simplify for the user, remove redundancy, keep docs
  current, and document/test against features+personas+journeys. Adds PRINCIPLES.md and a
  features.md catalogue; scrubs existing emojis; brings README/CONTRIBUTING/CHANGELOG current.
- **Evidence:** `make validate` -> 70 checks pass; negative test: an injected emoji fails exit 1.
- **Commit:** `a2e2ab0`
- **Ship?** [ ] yes [ ] hold

## Cycle 11 — SI-011 · Rename commands to /self-improve:* (BREAKING) + v1.0.0
- **Category:** ux · **Persona/journey:** Operator / J1
- **Impact:** cleaner, namespaced command surface (`/self-improve:setup` etc.) instead of the
  redundant `/self-improve:improve-setup`. All refs updated; plugin bumped to 1.0.0 with the
  breaking change recorded in CHANGELOG.
- **Evidence:** `make validate` -> 70 checks pass; no stale `/improve-*` refs remain in current docs.
- **Commit:** `a9ef637`
- **Ship?** [ ] yes [ ] hold

## Cycle 12 — SI-013 · Principle 6: prefer AI-centric, agentic solutions
- **Category:** feature · **Persona/journey:** all / all
- **Impact:** the loop now defaults to AI-native, agentic solutions where they genuinely serve
  the user better (NL intent, adaptive behaviour, automated multi-step work, tool/agent use,
  latest capable models), with a reliable fallback and no gimmicky AI.
- **Evidence:** `make validate` -> 70 checks pass; principle 6 wired into run/setup standards,
  README, feature-scout, implementer; CHANGELOG updated.
- **Commit:** `a29879c`
- **Ship?** [ ] yes [ ] hold

## Cycle 13 — SI-014 · Fix plugin manifest so it installs (bug)
- **Category:** bug · **Persona/journey:** all / J1 (install)
- **Impact:** the plugin now passes the official `claude plugin validate` and installs cleanly;
  previously `commands`/`agents` string paths failed the schema. Found by smoke-testing install.
- **Evidence:** `claude plugin validate .` PASS; `claude plugin install` succeeds; all 6 commands
  + 9 agents load. Local validator now rejects the bad form (CI-guarded); `make validate` runs
  the official validator when the CLI is present.
- **Commit:** `012711a`
- **Ship?** [ ] yes [ ] hold

## Cycle 14 — SI-009 · E2E + visual-regression gate for UI target repos
- **Category:** feature · **Persona/journey:** Operator / J3
- **Impact:** the loop can now prove user journeys work AND that the UI did not regress visually
  on real UI products -- Playwright + visual-diff scaffold tied to journeys.md, blocking the
  staging gate on unreviewed diffs. Closes the one area where Devin/Cursor had pulled ahead.
- **Evidence:** `make validate` -> 70 checks pass + official `claude plugin validate` PASS;
  templates/e2e/ added; wired into setup Step 6, run Phase 4, journey-tester.
- **Commit:** `e7de596`
- **Ship?** [ ] yes [ ] hold

## Cycle 15 — SI-015 · Emoji gate scans template subdirectories
- **Category:** bug · **Persona/journey:** Maintainer / J6
- **Impact:** principle-1 enforcement no longer has a blind spot -- nested docs (e.g.
  templates/e2e/README.md) are now scanned for emojis.
- **Evidence:** gap reproduced (subdir emoji passed before); after fix it fails exit 1;
  `make validate` -> 71 checks pass + official validate PASS.
- **Commit:** `b7aa8a0`
- **Ship?** [ ] yes [ ] hold

## Cycle 16 — SI-016 · Focus modes (harden / enhance / balanced)
- **Category:** feature (+ doc bug fix) · **Persona/journey:** Operator, Gatekeeper / J1, J3
- **Impact:** you can now steer the loop -- `/self-improve:harden` (bugs/security/perf/a11y/
  robustness/tech-debt, no new features), `/self-improve:enhance` (features/competitive gaps
  first), or a focus arg on run, with a persistent `loop.focus` default. Quality bar unchanged in
  every mode. Also fixed command paths in features.md corrupted by the v1.0.0 rename sed.
- **Evidence:** `make validate` -> 75 checks + official `claude plugin validate` PASS; reinstall
  shows 8 commands load (enhance, harden, + the original six).
- **Commit:** `d8368bb`
- **Ship?** [ ] yes [ ] hold
