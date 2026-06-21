# Changelog

All notable changes to the **self-improve** plugin are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning is [SemVer](https://semver.org/) and tracks `.claude-plugin/plugin.json`.

## [Unreleased]

### Added
- One-off setup command (`/improve-setup`) — persona/journey/competitor research, command
  detection, E2E scaffolding, backlog seeding.
- Autonomous self-scheduling loop (`/improve-run`) with full QA gate and auto-merge to
  `self-improve/staging`.
- Review/operations commands: `/improve-report`, `/improve-status`, `/improve-stop`,
  `/improve-recalibrate`.
- Nine specialist agents (persona-researcher, journey-mapper, competitor-researcher,
  bug-hunter, ux-reviewer, feature-scout, journey-tester, qa-verifier, implementer).
- Plugin + marketplace manifests for one-line install.
- Validation tooling (`scripts/validate_plugin.py`) wired into CI, `make validate`, and a
  pre-push hook so it works at zero GitHub Actions credit.
- Validation of generated `.self-improve/` state (config/state schemas).
- Persona/journey-grouped "shift report" PR template (`templates/staging-pr.md`).
- Unattended safety guardrails (`loop.guardrails`): auto-pause, rate cap, spend cap, kill switch.
- `CONTRIBUTING.md` and README polish (CI badge, table of contents, zero-infra/no-egress guarantees).

## [0.1.0] — 2026-06-21

### Added
- Initial release of the self-improve plugin.

[Unreleased]: https://github.com/gbhall99/Self-Improving-Plugin/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/gbhall99/Self-Improving-Plugin/releases/tag/v0.1.0
