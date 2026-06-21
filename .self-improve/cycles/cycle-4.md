# Cycle 4 — SI-008

- **Item:** SI-008 — CONTRIBUTING.md for the Maintainer persona
- **Category / priority:** ux / 7 · **Persona/journey:** Maintainer / J7

## Investigate
- Maintainer lens: J7 (contributor extends the plugin) had no guide; the validator rules
  (frontmatter, agent name==filename) were undocumented, so a first PR could fail opaquely.

## Implement
- Added `CONTRIBUTING.md` (layout, local gate, how to add command/agent) and linked it from README.

## QA gate
- `make validate` → 49 checks pass.

## Outcome
- GO. Squash-merged to staging.
