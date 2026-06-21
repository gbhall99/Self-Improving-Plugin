# self-improve

An **autonomous, continuous, self-improving engineering loop** as a Claude Code plugin.

Point it at a repo, answer a few startup questions once, and it runs unattended for
hours — relentlessly hunting bugs, fixing them, improving UI/UX, walking and testing
real user journeys, researching competitors, and shipping vetted improvements. Come
back later, read one report, and decide what to ship.

It is built around a simple promise: **every change it lands is bug-free, fully
working, tested, and a genuine improvement — verified from multiple angles — and you
always stay in control of what reaches `main`.**

---

## What it does

1. **One-off setup** (`/improve-setup`) — researches your **personas**, maps the
   **user journeys**, profiles your **competitors**, detects your build/test/run
   commands, scaffolds **E2E/visual testing** (Playwright) if missing, and writes a
   `.self-improve/` knowledge base plus a prioritized backlog.
2. **Autonomous loop** (`/improve-run`) — works one improvement per cycle:
   pick → investigate from multiple angles → implement with tests → **full QA gate
   (lint, typecheck, build, unit tests, E2E/visual)** → auto-merge onto a staging
   branch → re-arm itself and keep going.
3. **Review on your schedule** (`/improve-report`) — a ship/hold briefing of
   everything that landed, with evidence, so you choose what merges to `main`.

You never have to touch the session in between. Walk away, come back in 5–6 hours,
read the report, and merge what you like.

---

## Workflow

```
/improve-setup     # once per repo — personas, journeys, competitors, config, backlog
/improve-run       # start the autonomous loop (self-schedules to keep running)
   …hours pass, you're away…
/improve-status    # (optional) quick glance at progress
/improve-report    # summary + ship/hold decisions when you return
/improve-stop      # stop cleanly anytime
```

---

## Branch & merge model (you stay in control)

```
main                  ← protected. The loop NEVER pushes or merges here. You do.
  ▲  (one aggregate PR you review)
self-improve/staging  ← long-running. Each vetted improvement is squash-merged here,
  ▲                     one clean, independently-revertible commit at a time.
self-improve/cycle-*  ← short-lived per-improvement branch. QA gate must be green
                        before it's auto-merged into staging, then deleted.
```

- Every improvement reaches `staging` **only after a fully green QA gate** (independently
  re-checked by the `qa-verifier` agent).
- There is always exactly one open **`staging → main` PR** — your review surface. The
  loop keeps its body updated with a ship/hold checklist. **You** merge it (everything),
  or cherry-pick the commits you want (selective). `/improve-report` gives you the exact
  commands.

---

## How "continuous & unattended" works

The loop is **self-scheduling**. After each batch of cycles it re-arms the next run of
`/improve-run` (via the session's scheduler, e.g. `send_later`, or the `/loop` skill)
and ends its turn — no busy-waiting. It keeps going until the session budget is reached,
the backlog is exhausted, or you run `/improve-stop`. Configure cadence and runtime in
`.self-improve/config.json` (`loop.sessionBudgetHours`, `loop.checkpointMinutes`).

> Tip: for a fully hands-off run you can also wrap it yourself: `/loop 20m /improve-run`.

---

## The `.self-improve/` knowledge base

Setup writes (and the loop maintains) a committed knowledge base so runs are resumable:

| File | Purpose |
|---|---|
| `config.json` | product, primary goal, commands, branch model, loop settings, QA gate, out-of-bounds |
| `personas.md` | concrete, evidence-grounded personas |
| `journeys.md` | prioritized, testable end-to-end user journeys (P0/P1/P2) |
| `competitors.md` | competitive matrix + gaps to attack first |
| `backlog.md` | prioritized improvement items (`SI-001`…) with acceptance criteria |
| `staging-changelog.md` | every landed improvement + ship/hold checkbox + commit SHA |
| `state.json` | loop status, current cycle/item, last report |
| `cycles/cycle-N.md` | per-cycle audit log |

---

## The specialist agents

The loop looks at the product from many angles by dispatching purpose-built subagents:

- **persona-researcher** — who the product is really for
- **journey-mapper** — how each persona moves through the product
- **competitor-researcher** — keep the product ahead of the market
- **bug-hunter** — find and prove real bugs (no guesses)
- **ux-reviewer** — hold the bar for world-class UI/UX & accessibility
- **feature-scout** — the right features, not feature bloat
- **journey-tester** — E2E/visual proof that journeys work
- **qa-verifier** — independent GO/NO-GO gate before anything lands
- **implementer** — high-quality, tested, focused changes

---

## Safety

- **Never** pushes or merges to `main` — that decision is always yours.
- **Never** merges a red QA gate; an independent verifier must say GO.
- Respects an **out-of-bounds** list (files/services/concerns it must not touch).
- One small, independently-revertible change per cycle, with a full audit trail.

---

## Installation

This repository is itself a Claude Code plugin marketplace.

```text
/plugin marketplace add gbhall99/Self-Improving-Plugin
/plugin install self-improve
```

Then, in the repo you want to improve:

```text
/improve-setup
/improve-run
```

(You can also point `/plugin marketplace add` at a local clone path.)

---

## Commands

| Command | What it does |
|---|---|
| `/improve-setup` | One-off: research personas & journeys, profile competitors, detect commands, scaffold E2E, seed backlog |
| `/improve-run` | Start/continue the autonomous, self-scheduling improvement loop |
| `/improve-status` | Quick read-only progress snapshot |
| `/improve-report` | Summary + ship/hold review of what landed on staging |
| `/improve-stop` | Stop the loop cleanly and cancel any scheduled re-arm |

---

## Validation & CI

A single script — `scripts/validate_plugin.py` (pure stdlib, no installs) — checks the
plugin/marketplace manifests and the frontmatter of every command and agent. The **same
script** runs in three places, so quality stays gated even if you run out of GitHub
Actions credit:

| Where | How | Needs Actions credit? |
|---|---|---|
| GitHub Actions | `.github/workflows/validate.yml` on push/PR | yes |
| Locally, on demand | `make validate` | no |
| Locally, on every push | git pre-push hook (`make install-hooks`) | no |

**If you run out of Actions minutes:** nothing breaks. Run `make install-hooks` once per
clone and the pre-push hook validates locally on every `git push` (bypass with
`git push --no-verify`). You can also run `make validate` anytime. The workflow is also
kept deliberately cheap — a `paths` filter so it only runs when plugin files change,
`concurrency` to cancel superseded runs, and a single ~10s step with no install steps —
so it sips minutes when it does run.

## Requirements

- Claude Code with plugin support.
- A git repo with a GitHub remote (for the staging → main PR review surface).
- Best results on projects with runnable tests/build; for UI apps the setup step can
  scaffold Playwright if you don't already have E2E/visual testing.
