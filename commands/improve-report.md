---
description: Summarize everything the autonomous loop has done since you were last here. Produces a ship/hold review of each improvement on the staging branch, with evidence, so you can decide what to merge to main.
argument-hint: "[optional: 'since <date>' or a cycle range, default: since last report]"
---

# Self-Improve · Report

Produce the briefing the user reads when they come back hours later. Be honest, concise, and decision-oriented — they will use this to choose what ships.

Read `.self-improve/config.json`, `state.json`, `staging-changelog.md`, `backlog.md`, and the per-cycle logs in `.self-improve/cycles/`. Look at the actual `staging` branch and the open `staging → main` PR. Respect any range in **$ARGUMENTS** (default: everything since `state.lastReport`).

## Output (in this order)

1. **Headline** — one line: what was accomplished this run (e.g. "11 improvements shipped to staging: 4 bug fixes, 3 UX, 2 features, 2 a11y; all green").
2. **Loop status** — current `state.json.status`, cycles completed, runtime, whether it's still scheduled to continue, and the link to the `staging → main` PR.
3. **Ship / hold review** — the core of the report. **Group the landed improvements by the persona/journey they serve** (mirroring the `staging → main` PR body rendered from `templates/staging-pr.md`), then within each group give a table/line per item: id, title, category, impact, test/visual evidence, commit SHA, and a recommendation (Ship / Hold / Needs-review) with a one-line reason. Summarize user value, not just code.
4. **Risk & attention** — anything that needs human judgement: items touching sensitive areas, changes that are technically green but worth a second look, anything that came close to `outOfBounds`.
5. **Blocked / abandoned** — items the loop tried but parked, with reasons (so the user can unblock or de-scope).
6. **Backlog ahead** — top remaining items and how long they'd likely take.
7. **Competitive movement** — net change vs. competitors this run (closed gaps / new advantages), if any.

## How to decide what to ship

End with clear, copy-pasteable instructions for the user:
- To ship **everything**: merge the `staging → main` PR.
- To ship **selected** items only: list the squash commit SHAs and give the exact `git cherry-pick`/revert sequence (or instruct the user to reply with the ids to keep and offer to prepare a `self-improve/ship-<date>` branch containing only those).
- To **continue** improving: `/improve-run`. To **pause**: `/improve-stop`.

After producing the report, update `state.json.lastReport` to now. Do not merge anything to `main` yourself.
