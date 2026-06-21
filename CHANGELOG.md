# Changelog

All notable changes to the **self-improve** plugin are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning is [SemVer](https://semver.org/) and tracks `.claude-plugin/plugin.json`.

## [Unreleased]

### Added
- Operating principle 6: prefer AI-centric, agentic solutions — wired into `/self-improve:run`,
  `/self-improve:setup`, and the feature-scout and implementer agents.
- `make validate` also runs the official `claude plugin validate` when the CLI is present.
- E2E + visual-regression scaffold (`templates/e2e/`): Playwright config + per-journey spec with
  `toHaveScreenshot` checkpoints; setup scaffolds it for UI repos and the loop treats visual
  diffs as a blocking gate failure.

### Fixed
- Plugin failed `claude plugin validate` / install because `plugin.json` declared `commands`
  and `agents` as string paths. Removed them (the directories auto-discover); the local
  validator now rejects the non-array form so CI catches it too.

## [1.0.0] — 2026-06-21

### Changed
- **BREAKING:** commands renamed from `/improve-*` to the namespaced `/self-improve:*`
  (e.g. `/improve-setup` is now `/self-improve:setup`). Update any saved invocations.

### Added
- One-off setup command (`/self-improve:setup`) — persona/journey/competitor research, command
  detection, E2E scaffolding, backlog seeding.
- Autonomous self-scheduling loop (`/self-improve:run`) with full QA gate and auto-merge to
  `self-improve/staging`.
- Review/operations commands: `/self-improve:report`, `/self-improve:status`, `/self-improve:stop`,
  `/self-improve:recalibrate`.
- Nine specialist agents (persona-researcher, journey-mapper, competitor-researcher,
  bug-hunter, ux-reviewer, feature-scout, journey-tester, qa-verifier, implementer).
- Plugin + marketplace manifests for one-line install.
- Validation tooling (`scripts/validate_plugin.py`) wired into CI, `make validate`, and a
  pre-push hook so it works at zero GitHub Actions credit.
- Validation of generated `.self-improve/` state (config/state schemas).
- Persona/journey-grouped "shift report" PR template (`templates/staging-pr.md`).
- Unattended safety guardrails (`loop.guardrails`): auto-pause, rate cap, spend cap, kill switch.
- `CONTRIBUTING.md` and README polish (CI badge, table of contents, zero-infra/no-egress guarantees).
- Competitor research files queued, citable gap tickets into the backlog on discovery passes.
- Local versioned playbooks/knowledge (`.self-improve/knowledge/`) captured on success and reused.
- Canonical operating principles (`PRINCIPLES.md`) enforced by commands, agents, and the QA gate:
  no emojis (crisp iconography), simplify for the user, remove redundancy, keep docs current,
  and document/test against features, personas, and journeys.
- Feature catalogue (`features.md`) produced by setup and maintained by the loop.
- QA gate now rejects emojis in the plugin's markdown/docs.

## [0.1.0] — 2026-06-21

### Added
- Initial release of the self-improve plugin.

[Unreleased]: https://github.com/gbhall99/Self-Improving-Plugin/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/gbhall99/Self-Improving-Plugin/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/gbhall99/Self-Improving-Plugin/releases/tag/v0.1.0
