# Cycle 6 — SI-004

- **Item:** SI-004 — /improve-recalibrate command
- **Category / priority:** ux / 6 · **Persona/journey:** Reviewer / J2

## Investigate
- Reviewer lens: setup is one-off, but personas/journeys/competitors drift. Without a refresh
  path the loop slowly optimizes for stale context. competitor-researcher already emits gaps;
  needed a command to re-run research and fold results back in without clobbering.

## Implement
- Added commands/improve-recalibrate.md: re-runs research agents, diffs (stable ids preserved),
  re-prioritizes backlog, records a recalibrated note. Scoped via args (personas/journeys/competitors/all).

## QA gate
- make validate -> 50 checks pass (command count grew by one; frontmatter valid).

## Outcome
- GO. Squash-merged to staging.
