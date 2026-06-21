# Cycle 1 — SI-006

- **Item:** SI-006 — Validate generated `.self-improve/` state in the QA gate
- **Category / priority:** tech-debt / 9
- **Persona/journey:** Maintainer / J2, J3

## Investigate (multi-angle)
- bug-hunter lens: the loop writes `config.json`/`state.json`, but nothing validated them;
  a malformed `loop` block or bad `status` would surface only at runtime, mid-run.
- ux-reviewer lens (Maintainer): contributors editing state by hand get no fast feedback.
- Conclusion: extend the existing structural validator — cheapest, on-theme, and it
  strengthens the plugin's own QA gate (the plugin improving its own quality bar).

## Implement
- Added `validate_self_improve_state()` to `scripts/validate_plugin.py`:
  - `config.json`: requires `product`, `primaryGoal`, `branches{main,staging,cyclePrefix}`,
    `loop{sessionBudgetHours,checkpointMinutes,mergePolicy}`, non-empty `qaGate`.
  - `state.json`: requires `status` ∈ {ready,running,scheduled,stopped,paused}, integer `cycle`.
  - Absent `.self-improve/` is skipped, so fresh target repos still validate cleanly.

## QA gate (make validate)
- Positive: 49 checks pass, exit 0.
- Negative: bad `status`, missing `cycle`, empty `qaGate`, missing `loop.*` → exit 1 with
  precise messages. Restored → exit 0.

## Decision: do NOT add `.self-improve/**` to the CI `paths` filter
- The new check runs on every existing CI trigger and on every `make validate`. Adding
  `.self-improve/**` would fire CI on every loop commit, burning Actions minutes against
  the plugin's frugality goal. Local gate + existing CI coverage is sufficient.

## Outcome
- GO. Squash-merged to `self-improve/staging`. One clean, revertible commit.
