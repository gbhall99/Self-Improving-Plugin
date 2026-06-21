# User Journeys — self-improve plugin

Surfaces this product exposes: the 5 slash commands (`commands/*.md`), the 9 subagents
(`agents/*.md`), the validation tooling (`scripts/validate_plugin.py`, `Makefile`,
`.githooks/pre-push`, `.github/workflows/validate.yml`), and the docs (`README.md`).

## P0 — core journeys

### J1 · First run, end to end (Operator)
`/plugin marketplace add …` → `/plugin install self-improve` → `/improve-setup` (answer
startup questions) → `/improve-run` → walk away → `/improve-report` → ship.
- **Outcome:** vetted improvements on `self-improve/staging`, one report, ship decision made.
- **Friction/abandon points:** unclear startup questions; setup produces vague personas;
  loop doesn't actually re-arm; report too long to act on.
- **Verify:** structure validates; commands carry clear `argument-hint`s; setup writes a complete `.self-improve/`.

### J2 · Setup research quality (Operator/Reviewer)
`/improve-setup` produces concrete personas, prioritized testable journeys, a real
competitor matrix, detected commands, and a 15–30 item backlog.
- **Outcome:** a complete, committed `.self-improve/` knowledge base + `self-improve/staging`.
- **Friction:** generic personas; journeys with no test mapping; empty/over-long backlog.
- **Verify:** all `.self-improve/*` files present and well-formed; `config.json`/`state.json` valid (→ SI-006).

### J3 · A loop cycle lands a vetted change (Operator)
Pick → investigate (subagents) → implement + tests → **full QA gate** → squash-merge to
staging → changelog entry → fresh `staging → main` PR.
- **Outcome:** one clean, revertible improvement on staging; nothing red ever merged.
- **Friction:** QA gate not actually run; merge while red; scope creep per cycle.
- **Verify:** `make validate` green before any land; one item per cycle; changelog updated.

## P1 — important journeys

### J4 · Stop cleanly (Operator)
`/improve-stop` → status `stopped`, re-arm cancelled, no half-done work on staging.
- **Verify:** in-flight cycle finished-or-reverted; scheduled re-arm cancelled.

### J5 · Mid-run status (Operator, often on phone)
`/improve-status` → fast read-only snapshot: status, current item, cycles done, backlog, PR link.
- **Verify:** no mutations; concise output.

### J6 · Validation with zero Actions credit (Gatekeeper/Maintainer)
`make validate` and the pre-push hook run the same check locally; CI is a bonus, not a dependency.
- **Verify:** `python3 scripts/validate_plugin.py` exits 0/1 correctly; hook blocks bad pushes.

## P2 — secondary

### J7 · Contributor extends the plugin (Maintainer)
Add an agent/command → `make validate` catches missing frontmatter/name mismatch → PR.
- **Friction:** no `CONTRIBUTING.md`; validator gaps. **Verify:** validator covers new file.

## Journeys lacking automated coverage (→ backlog seeds)
- J2/J3 generated state (`config.json`, `state.json`) is unvalidated → **SI-006**.
- J1 PR review surface is generic, not persona/journey-grouped → **SI-001**.
- J7 has no contributor guide → **SI-008**.
