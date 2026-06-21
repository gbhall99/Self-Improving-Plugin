---
description: Refresh the knowledge base without redoing full setup. Re-runs the research agents to update personas, user journeys, and the competitive profile, diffs against the current files, and re-prioritizes the backlog so the loop keeps aiming at what matters now.
argument-hint: "[optional: what to refresh — 'personas' | 'journeys' | 'features' | 'competitors' | 'all' (default all)]"
---

# Self-Improve · Recalibrate

Markets, products, and users drift. This refreshes the `.self-improve/` knowledge base so the
autonomous loop keeps optimizing for what's true *now* — without the full one-off `/improve-setup`.

**If `.self-improve/config.json` is missing, STOP and tell the user to run `/improve-setup` first.**
Read the existing `.self-improve/` files first. Respect `$ARGUMENTS` to scope the refresh (default: all).

## Steps

1. **Re-research** the requested areas by dispatching the specialist agents:
   - `persona-researcher` → updated personas
   - `journey-mapper` → updated journeys (re-grounded in the current codebase surfaces)
   - re-scan the codebase to refresh `features.md` so every current feature is documented (principle 5)
   - `competitor-researcher` → refreshed competitive profile + new gaps
2. **Diff, don't clobber.** For each file, show what changed (new/removed/changed personas,
   journeys, competitor moves). Preserve anything still accurate; only update what drifted.
   Keep stable ids so history stays meaningful.
3. **Re-prioritize the backlog.** Fold newly discovered gaps in as well-formed items
   (id, title, category, persona/journey, acceptance criterion, effort, priority). Re-score
   existing `todo` items against the refreshed context; never silently drop user-added items.
4. **Record it.** Write a short `recalibrated` note (date + summary of what changed) to the top
   of the affected files, and commit the refreshed knowledge base on the current branch / staging.

## Finish
Print a concise diff summary: what changed in personas/journeys/competitors, new backlog items
added, items re-prioritized, and the top 5 items the loop will tackle next. Do not implement
backlog items here — recalibration only. Resume improving with `/improve-run`.
