# Cycle 14 — SI-009

- **Item:** SI-009 — E2E + visual-regression gate for UI target repos
- **Category / priority:** feature / 7 (L) · **Persona/journey:** Operator / J3

## Investigate
- Competitive research flagged E2E/visual as the one area rivals (Devin/Cursor computer-use +
  recorded demos) had pulled ahead. The plugin promised it but only scaffolded a smoke test.
- This repo has no UI, so the deliverable is the plugin's capability to do this well on UI targets.

## Implement
- templates/e2e/: playwright.config.example.ts (webServer + toHaveScreenshot defaults),
  journey.example.spec.ts (walk journey as persona + visual checkpoint), README.
- setup Step 6: scaffold from the templates for UI repos; record e2e in qaGate.
- run Phase 4: visual regression is blocking; intended changes update baseline same-cycle.
- journey-tester: author visual checks; treat diffs as failures.

## QA gate
- make validate -> 70 checks pass; official claude plugin validate PASS.

## Outcome
- GO. Squash-merged to staging. Backlog of real items now fully drained.
