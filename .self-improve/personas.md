# Personas — self-improve plugin

> The "product" here is the **self-improve Claude Code plugin** itself. These are the
> humans who install and operate it. Ranked by importance to the primary goal:
> *let an owner safely improve their product unattended and stay in control of what ships.*

## P1 — The Solo Founder / Indie Hacker ("the Operator") [primary]
- **Goals:** ship a better product faster than they can alone; make progress while asleep/away; never babysit.
- **Context:** owns one or a few product repos; works from laptop and phone; limited time, no QA team.
- **Pains:** bugs and rough UX pile up; no bandwidth for competitive research; agents that "go rogue" or rack up cost; reviewing a huge unexplained diff.
- **Success feels like:** start it, walk away 5–6h, come back to a clean staging branch + a report, tick what to ship.
- **Tech level:** high. **Cares most about:** unattended autonomy, safety/cost guardrails, a fast-to-review report.

## P2 — The Eng Lead / PM on a small team ("the Reviewer")
- **Goals:** keep the product ahead of competitors; tie work to real users; approve hours of agent output in minutes.
- **Context:** reviews PRs; owns roadmap; answerable for quality and direction.
- **Pains:** generic agent changes not tied to user value; competitive catch-up is manual; trust in autonomous merges.
- **Success feels like:** a `staging → main` PR grouped by persona/journey with evidence; cherry-pick what ships.
- **Tech level:** high. **Cares most about:** human-gated merge model, persona/journey rationale, competitive coverage.

## P3 — The Regulated / Security-conscious Engineer ("the Gatekeeper")
- **Goals:** improvement without code leaving the org; no new infra/vendors; auditable changes.
- **Context:** enterprise/regulated; can't send code to hosted "AI engineer" VMs; strict CI budgets.
- **Pains:** competitors run on their own cloud; surprise CI/Actions spend; opaque automation.
- **Success feels like:** runs entirely inside their existing Claude Code install; no egress; validation works even at zero Actions credit.
- **Tech level:** high. **Cares most about:** no code egress, zero extra infra, full audit trail, out-of-bounds controls.

## P4 — The Plugin Contributor ("the Maintainer")
- **Goals:** extend the plugin (new agents/commands) without breaking it.
- **Context:** edits `commands/`, `agents/`, `scripts/`; opens PRs to this repo.
- **Pains:** silent breakage of manifest/frontmatter; no fast local feedback.
- **Success feels like:** `make validate` and the pre-push hook catch mistakes instantly; clear contribution path.
- **Tech level:** high. **Cares most about:** validation tooling, clear structure/docs, fast local gate.

## Under-served today (→ backlog seeds)
- P2 has no persona/journey-grouped PR report yet (only a generic body) → **SI-001**.
- P1/P3 have no explicit budget/failure guardrails for unattended runs → **SI-003**.
- P4 has no `CONTRIBUTING.md` and the validator doesn't cover generated state → **SI-006, SI-008**.
