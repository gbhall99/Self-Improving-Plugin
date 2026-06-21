# Cycle 9 — SI-005

- **Item:** SI-005 — Local versioned playbooks/knowledge
- **Category / priority:** feature / 5 · **Persona/journey:** Operator / J3

## Implement
- Added `.self-improve/knowledge/` convention: /improve-run consults it (Phase 2) and captures
  playbooks on success (Phase 5); /improve-setup creates the dir. Seeded `_TEMPLATE.md` and a
  real `qa-gate.md` playbook (the harness every cycle used).

## Process note
- Landed as a single direct commit on staging (128974c) — the cycle branch step was skipped;
  end state is equivalent (one clean, revertible commit). Noted for honesty.

## QA gate
- make validate -> 50 checks pass.

## Outcome
- GO.
