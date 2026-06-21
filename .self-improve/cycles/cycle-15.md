# Cycle 15 — SI-015

- **Item:** SI-015 — Emoji gate scans template subdirectories
- **Category / priority:** bug / 6 · **Persona/journey:** Maintainer / J6

## Investigate
- Self-review after SI-009 added templates/e2e/README.md (a subdir). The emoji check used
  glob('*.md') (top-level only), so subdir docs were unchecked -- a blind spot in principle 1.

## Implement
- validate_plugin.py: rglob('*.md') over commands/agents/templates so the scan is recursive.

## QA gate
- Reproduced the gap (subdir emoji passed); after fix it fails exit 1. make validate -> 71 PASS;
  official claude plugin validate PASS.

## Outcome
- GO. Squash-merged to staging.
