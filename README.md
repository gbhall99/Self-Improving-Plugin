# self-improve

[![validate-plugin](https://github.com/gbhall99/Self-Improving-Plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/gbhall99/Self-Improving-Plugin/actions/workflows/validate.yml)

An **autonomous, continuous, self-improving engineering loop** as a Claude Code plugin.

Point it at a repo, answer a few startup questions once, and it runs unattended for
hours — relentlessly hunting bugs, fixing them, improving UI/UX, walking and testing
real user journeys, researching competitors, and shipping vetted improvements. Come
back later, read one report, and decide what to ship.

It is built around a simple promise: **every change it lands is bug-free, fully
working, tested, and a genuine improvement — verified from multiple angles — and you
always stay in control of what reaches `main`.**

## Contents

- [What it does](#what-it-does)
- [Workflow](#workflow)
- [Branch & merge model](#branch--merge-model-you-stay-in-control)
- [How "continuous & unattended" works](#how-continuous--unattended-works)
- [Operating principles](#operating-principles)
- [The `.self-improve/` knowledge base](#the-self-improve-knowledge-base)
- [The specialist agents](#the-specialist-agents)
- [Safety & guarantees](#safety--guarantees)
- [Installation](#installation)
- [Commands](#commands)
- [Validation & CI](#validation--ci)
- [Contributing](#contributing)

---

## What it does

1. **One-off setup** (`/self-improve:setup`) — researches your **personas**, maps the
   **user journeys**, profiles your **competitors**, detects your build/test/run
   commands, scaffolds **E2E/visual testing** (Playwright) if missing, and writes a
   `.self-improve/` knowledge base plus a prioritized backlog.
2. **Autonomous loop** (`/self-improve:run`) — works one improvement per cycle:
   pick → investigate from multiple angles → implement with tests → **full QA gate
   (lint, typecheck, build, unit tests, E2E/visual)** → auto-merge onto a staging
   branch → re-arm itself and keep going.
3. **Review on your schedule** (`/self-improve:report`) — a ship/hold briefing of
   everything that landed, with evidence, so you choose what merges to `main`.

You never have to touch the session in between. Walk away, come back in 5–6 hours,
read the report, and merge what you like.

---

## Workflow

```
/self-improve:setup     # once per repo — personas, journeys, competitors, config, backlog
/self-improve:run       # start the autonomous loop (self-schedules to keep running)
   …hours pass, you're away…
/self-improve:status    # (optional) quick glance at progress
/self-improve:report    # summary + ship/hold decisions when you return
/self-improve:stop      # stop cleanly anytime
```

### Focus modes (harden vs. enhance)

Steer what the loop works on without touching the quality bar:

- `/self-improve:harden` — only bugs, security, performance, accessibility, robustness, test
  coverage, and tech-debt. No new features.
- `/self-improve:enhance` — prioritise new features and competitive gaps, then UX.
- `/self-improve:run` — uses the saved focus (`loop.focus` in config, default `balanced`); you
  can also pass it inline: `/self-improve:run harden`. A passed focus becomes the new default.

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
  or cherry-pick the commits you want (selective). `/self-improve:report` gives you the exact
  commands.

---

## How "continuous & unattended" works

The loop is **self-scheduling**. After each batch of cycles it re-arms the next run of
`/self-improve:run` (via the session's scheduler, e.g. `send_later`, or the `/loop` skill)
and ends its turn — no busy-waiting. It keeps going until the session budget is reached,
the backlog is exhausted, or you run `/self-improve:stop`. Configure cadence and runtime in
`.self-improve/config.json` (`loop.sessionBudgetHours`, `loop.checkpointMinutes`).

> Tip: for a fully hands-off run you can also wrap it yourself: `/loop 20m /self-improve:run`.

---

## Operating principles

Every change the loop proposes must satisfy these standards (see [PRINCIPLES.md](PRINCIPLES.md)) —
they are part of the definition of done and the QA gate enforces what it can:

1. **No emojis** — crisp iconography only (icon set / SVG in product UI; plain text symbols in docs).
2. **Simplify for the user** — the simplest solution that fully solves the problem.
3. **Remove redundancy** — delete duplicated/dead code and overlapping features; consolidate before adding.
4. **Keep documentation current** — docs are updated in the same change; stale docs block GO.
5. **Document & test against features/personas/journeys** — `features.md`, `personas.md`, and
   `journeys.md` are always maintained, and every evaluation considers all three.
6. **Prefer AI-centric, agentic solutions** — default to AI-native, agentic designs where they
   genuinely serve the user better, with the latest capable models and a reliable fallback.

## The `.self-improve/` knowledge base

Setup writes (and the loop maintains) a committed knowledge base so runs are resumable:

| File | Purpose |
|---|---|
| `config.json` | product, primary goal, commands, branch model, loop settings, QA gate, out-of-bounds |
| `personas.md` | concrete, evidence-grounded personas |
| `journeys.md` | prioritized, testable end-to-end user journeys (P0/P1/P2) |
| `features.md` | living catalogue of every feature, mapped to personas/journeys |
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

## Safety & guarantees

- **Never** pushes or merges to `main` — that decision is always yours.
- **Never** merges a red QA gate; an independent verifier must say GO.
- Respects an **out-of-bounds** list (files/services/concerns it must not touch).
- **Bounded autonomy:** configurable guardrails (`loop.guardrails`) — auto-pause after a
  failure streak, a merges-per-hour rate cap, an optional spend cap, and a kill switch
  (`/self-improve:stop`). "Run overnight" without waking up to chaos or a surprise bill.
- One small, independently-revertible change per cycle, with a full audit trail in `.self-improve/`.

### Zero-infra, no-egress

Unlike hosted "AI engineer" services, self-improve runs **entirely inside your existing
Claude Code install**:

- **No code egress** — your repo never leaves your machine/session for a third-party VM.
- **No extra infrastructure** — no new VMs, accounts, or seats to provision.
- **No CI dependency** — validation runs locally too, so it works even at zero GitHub
  Actions credit (see [Validation & CI](#validation--ci)).

---

## Installation

This repository is itself a Claude Code plugin marketplace.

```text
/plugin marketplace add gbhall99/Self-Improving-Plugin
/plugin install self-improve
```

Then, in the repo you want to improve:

```text
/self-improve:setup
/self-improve:run
```

(You can also point `/plugin marketplace add` at a local clone path.)

---

## Commands

| Command | What it does |
|---|---|
| `/self-improve:setup` | One-off: research personas & journeys, profile competitors, detect commands, scaffold E2E, seed backlog |
| `/self-improve:run` | Start/continue the autonomous, self-scheduling improvement loop (accepts a focus: `harden` \| `enhance` \| `balanced`) |
| `/self-improve:harden` | Start the loop in HARDEN focus — bugs, security, perf, a11y, robustness, tech-debt; no new features |
| `/self-improve:enhance` | Start the loop in ENHANCE focus — new features and competitive gaps first |
| `/self-improve:status` | Quick read-only progress snapshot |
| `/self-improve:report` | Summary + ship/hold review of what landed on staging |
| `/self-improve:recalibrate` | Refresh personas/journeys/features/competitors without a full re-setup |
| `/self-improve:stop` | Stop the loop cleanly and cancel any scheduled re-arm |

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for project layout, how to add a command or agent,
and the local validation gate. The short version: run `make validate` before every push
(and `make install-hooks` once to gate pushes locally).

## Requirements

- Claude Code with plugin support.
- A git repo with a GitHub remote (for the staging → main PR review surface).
- Best results on projects with runnable tests/build; for UI apps the setup step can
  scaffold Playwright if you don't already have E2E/visual testing.
