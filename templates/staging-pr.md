<!--
Shift-report template for the single open `staging → main` PR (the human review surface).
Used by /improve-run (Phase 6) and /improve-report. Goal: let a reviewer approve hours of
unattended work in minutes by summarizing USER VALUE, not just code. Group every change by
the persona/journey it serves, lead with a recommendation, and attach evidence.
Placeholders in <angle brackets>.
-->
# 🤖 self-improve — staging review

The **review surface** for autonomous work. The loop never merges here — **you** decide what
ships to `main`. Tick items in `.self-improve/staging-changelog.md` or reply with the ids to keep.

**This run:** <N> improvements shipped · QA gate: <green/▲> · cycles <a>–<b> · runtime <hh:mm>

## Shipped, grouped by who it serves
<!-- one subsection per persona that benefited; omit personas with no changes -->
### <emoji> <Persona> · <category(ies)> / <journey ids>
- **<SI-id> — <title>** (`<squash-sha>`)
  - *Why:* <user problem / competitive gap this closes, tied to the persona/journey>
  - *What:* <the change, 1–2 lines>
  - *Evidence:* <tests run + result; before/after screenshots for UI; cycle log link>
  - **Recommendation: <Ship | Hold | Needs-review>** — <one-line reason>

## Risk & attention
<!-- anything green-but-worth-a-look: sensitive areas, deliberate tradeoffs, near-out-of-bounds -->
- <item or "None this run.">

## Blocked / abandoned
- <SI-id — reason, or "None.">

## Backlog ahead (top)
<SI-id title · SI-id title · …>

## Competitive movement
<gaps closed / new advantages vs competitors this run, or "No net change.">

## How to decide
- **Ship everything:** merge this PR.
- **Ship selectively:** keep `<sha>`; reply with ids to drop and I'll prepare a `self-improve/ship-<date>` branch with only those.
- **Continue:** `/improve-run`. **Pause:** `/improve-stop`.
