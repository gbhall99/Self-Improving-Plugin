---
description: Stop the autonomous self-improvement loop cleanly. Cancels any scheduled re-arm, finishes safely, and leaves staging in a reviewable state.
---

# Self-Improve · Stop

Halt the autonomous loop without leaving a mess.

1. Set `.self-improve/state.json` `status` to `"stopped"` so any in-flight `/improve-run` re-arm aborts. (This is the kill switch the loop's guardrails check before every cycle. Note: `"paused"` is the loop's own auto-halt after a failure streak — it resumes only when the user runs `/improve-run`; `"stopped"` is the deliberate user stop.)
2. If a cycle is mid-implementation: either finish it through the QA gate if it's nearly done and green, or revert its cycle branch so nothing half-done lingers. Never leave a red or half-merged change on `staging`.
3. Cancel any scheduled self check-ins: unschedule via `send_later` / stop the `/loop` if one is running (`TaskStop` if applicable). Tell the user exactly what you cancelled.
4. Push the latest clean `staging` and make sure the `staging → main` PR is up to date.
5. Confirm the loop is stopped and remind the user they can review with `/improve-report` and restart anytime with `/improve-run`.
