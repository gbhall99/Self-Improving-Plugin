# Cycle 3 — SI-003

- **Item:** SI-003 — Unattended safety guardrails
- **Category / priority:** feature / 8 · **Persona/journey:** Operator, Gatekeeper / J3, J4

## Investigate (multi-angle)
- competitor lens: rivals bill per-task precisely because they don't run unbounded. Offering
  *bounded, auditable* continuous operation is what makes "run overnight" adoptable.
- Operator/Gatekeeper lens: the fear is waking up to chaos or a huge bill. Need hard caps,
  an auto-halt on repeated failure, and an explicit kill switch — not just trust.

## Implement
- `/improve-run`: added a Guardrails section enforced before/during each cycle — kill switch
  (`status=stopped`), auto-pause after `maxConsecutiveFailures`, `maxMergesPerHour` rate cap,
  optional `maxSpendUSD`, absolute out-of-bounds; sensible defaults when absent.
- `/improve-setup`: config template now writes `loop.guardrails`.
- `/improve-stop`: documents `stopped` (user) vs `paused` (loop auto-halt) semantics.
- This repo's `config.json` updated with `loop.guardrails`.

## QA gate (make validate)
- 49 checks pass, exit 0. Notably SI-006's schema check validated the new `loop.guardrails`
  shape on `config.json` — earlier cycles compounding (the plugin guarding its own changes).

## Outcome
- GO. Squash-merged to `self-improve/staging`.
