# Features — self-improve plugin

Living catalogue of every feature (principle 5). Consulted in every evaluation so no feature is
changed or tested in isolation. Maturity: solid / rough / partial.

| feature | what it does | personas | journeys | where | maturity |
|---|---|---|---|---|---|
| One-off setup (`/self-improve:setup`) | Research personas/journeys/features/competitors, detect commands, scaffold E2E, seed backlog, write `.self-improve/` + staging branch | all | J1, J2 | `commands/setup.md` | solid |
| Autonomous loop (`/self-improve:run`) | Pick -> investigate -> implement+test -> QA gate -> auto-merge to staging -> self-schedule | Operator | J1, J3 | `commands/run.md` | solid |
| Focus modes (`/self-improve:harden`, `/self-improve:enhance`) | Steer the loop: harden (bugs/security/perf/a11y/robustness/tech-debt, no new features) vs enhance (features/competitive gaps first) vs balanced; via commands, a run argument, or `loop.focus` | Operator, Gatekeeper | J3 | `commands/harden.md`, `commands/enhance.md`, `commands/run.md` | solid |
| Report (`/self-improve:report`) | Ship/hold briefing grouped by persona/journey/feature with evidence | Reviewer | J1 | `commands/report.md` | solid |
| Status (`/self-improve:status`) | Read-only progress snapshot | Operator | J5 | `commands/status.md` | solid |
| Stop (`/self-improve:stop`) | Clean halt; kill switch; cancel re-arm | Operator | J4 | `commands/stop.md` | solid |
| Recalibrate (`/self-improve:recalibrate`) | Refresh personas/journeys/features/competitors without full re-setup | Reviewer | J2 | `commands/recalibrate.md` | solid |
| Specialist agents (9) | Persona/journey/competitor research, bug hunting, UX review, feature scouting, journey testing, QA verdict, implementation | all | J2, J3 | `agents/*.md` | solid |
| Branch & merge model | main human-gated; vetted changes squash-merged to `self-improve/staging`; one staging->main review PR | Operator, Reviewer | J1, J3 | `commands/run.md` | solid |
| Safety guardrails | Kill switch, auto-pause on failure streak, merges/hour cap, optional spend cap, out-of-bounds | Operator, Gatekeeper | J3, J4 | `commands/run.md`, `config.json` | solid |
| Operating principles | Canonical standards (no emoji, simplify, de-dup, docs current, document+test features/personas/journeys) enforced by commands, agents, and the QA gate | all | all | `PRINCIPLES.md` | solid |
| Knowledge base | `.self-improve/` personas, journeys, features, competitors, backlog, state, changelog, per-cycle logs | all | J2, J3 | `.self-improve/` | solid |
| Playbooks/knowledge | Reusable repro+verify steps captured on success and reused | Operator | J3 | `.self-improve/knowledge/` | rough |
| Competitor gap-tickets | Loop turns competitor capabilities into sourced backlog items | Reviewer | J2 | `agents/competitor-researcher.md` | rough |
| Validation / QA gate | Validates manifests, command/agent frontmatter, generated state, and emoji ban; runs in CI, `make validate`, and pre-push hook | Maintainer, Gatekeeper | J6, J7 | `scripts/validate_plugin.py`, `Makefile`, `.githooks/`, `.github/workflows/` | solid |
| Marketplace install | One-line install via plugin marketplace | all | J1 | `.claude-plugin/` | solid |
| E2E + visual gate | Playwright + visual-regression scaffold (`templates/e2e/`) tied to journeys; blocking gate for UI target repos | Operator | J3 | `templates/e2e/`, journey-tester, setup Step 6, run Phase 4 | rough |
