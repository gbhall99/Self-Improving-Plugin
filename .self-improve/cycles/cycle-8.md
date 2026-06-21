# Cycle 8 — SI-002

- **Item:** SI-002 — Competitor research files queued, citable gap tickets
- **Category / priority:** feature / 6 · **Persona/journey:** Reviewer / J2

## Investigate
- competitor lens: the research is currently a one-off setup artifact; markets move. The
  differentiator is *continuous* ingestion of the market into the backlog — no rival does this.

## Implement
- competitor-researcher: added a "gap ticket" spec — append structured, sourced, de-duplicated,
  capped backlog rows on discovery passes; never invent features.
- /improve-run Phase 0: dispatch competitor-researcher to file gap tickets during discovery.

## QA gate
- make validate -> 50 checks pass.

## Outcome
- GO. Squash-merged to staging.
