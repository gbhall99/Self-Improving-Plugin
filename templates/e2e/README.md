# E2E + visual-regression scaffold

These are the templates `/self-improve:setup` copies into a **UI target repo** that lacks
end-to-end / visual testing (Step 6, Verification tooling). They give the loop a real way to
prove user journeys work and that the UI did not regress visually -- not just that unit tests pass.

Skip for non-UI projects (libraries, CLIs, pure APIs).

## What gets scaffolded
- `playwright.config.*` -- adapted from `playwright.config.example.ts` (base URL, the dev/start
  command as a `webServer`, and screenshot/visual settings).
- `tests/journeys/<journey>.spec.*` -- one spec per P0 journey in `journeys.md`, adapted from
  `journey.example.spec.ts`. Each walks the journey as the persona and asserts the real outcome
  plus a visual snapshot at key steps.

## How it plugs into the QA gate
- Setup records the commands in `.self-improve/config.json` (`commands.e2e`, and `e2e` in `qaGate`).
- `/self-improve:run` Phase 4 runs them as a **blocking** part of the gate: a failed assertion
  OR an unreviewed visual diff is a NO-GO. The qa-verifier confirms it independently.
- Baselines live in the repo; an intended visual change updates the baseline in the same cycle
  (principle 4) with the before/after shown in the staging PR.

Keep the scaffold idiomatic to the target repo (its framework, package manager, test layout) and
stable -- no arbitrary sleeps; wait on real conditions.
