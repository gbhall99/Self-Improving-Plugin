---
description: One-off setup. Researches the product's personas, maps and documents user journeys, profiles competitors, detects build/test/run commands, scaffolds E2E/visual tooling, and writes the .self-improve/ knowledge base the autonomous loop depends on.
argument-hint: "[optional: short product description or focus, e.g. 'B2B invoicing SaaS, focus on onboarding']"
---

# Self-Improve · Setup (run once per repo)

You are bootstrapping the **self-improvement knowledge base** for this repository. This is a one-time, foundational pass. Everything the autonomous loop (`/self-improve:run`) does later depends on the quality of what you produce here, so be rigorous and concrete — no vague placeholders.

User-provided focus (may be empty): **$ARGUMENTS**

Apply the **operating principles** in `PRINCIPLES.md` throughout (no emojis / crisp iconography, simplify for the user, remove redundancy, keep docs current, document every feature/persona/journey, and prefer AI-centric, agentic solutions). They are the standard the loop will hold every change to. When seeding the backlog, actively look for AI-native/agentic opportunities (principle 6) for the personas, not only conventional fixes.

## Startup questions (ask the user, then proceed)

Use the `AskUserQuestion` tool to ask up to 4 concise questions. Skip any you can confidently infer from the codebase or the focus argument; never ask something the repo already answers. Prioritize:

1. **Product in one line + primary goal** — what is this app and what is the single most important outcome for its users? (Only ask if not obvious from README/code.)
2. **Top competitors / alternatives** — name 2–4, or say "you decide" and you'll research them.
3. **Cycle cadence & runtime** — how long should each unattended session run before it pauses (e.g. ~5–6h), and roughly how often to re-arm a cycle (default: continuous, ~15–20 min checkpoints).
4. **Out-of-bounds** — anything the loop must NOT touch (files, services, dependencies, design language, auth, billing, migrations, etc.).

If the user is unavailable or says "use your judgement", choose sensible defaults and record them.

## Step 1 — Understand the codebase

- Detect the stack, frameworks, package manager, and app type (web UI, API, CLI, mobile, library).
- Find and record the canonical commands for: install, **lint**, **typecheck**, **build**, **unit/integration test**, **run/dev server**, and **E2E** (if any). Prefer reading `package.json`/`Makefile`/`pyproject.toml`/CI config over guessing.
- Identify the main entry points and the surfaces real users touch (routes, screens, key CLI commands, public API endpoints).

## Step 2 — Research personas (deep)

Define **3–6 concrete personas** for this product. For each: name/archetype, goals, context of use, pain points, what "success" feels like, and technical sophistication. Ground them in the actual product — not generic marketing personas. Where useful, use web research (the `deep-research` skill or WebSearch) to validate that these personas match the real market for this kind of product. Write to `.self-improve/personas.md`.

## Step 3 — Map user journeys

For each persona, document their **critical user journeys** end-to-end: trigger → steps → expected outcome → failure/abandon points. Mark each journey's priority (P0/P1/P2) and the exact app surface it exercises (URL/route/screen/command). These journeys are what the loop will test on every cycle. Write to `.self-improve/journeys.md`.

## Step 3b — Catalogue every feature

Produce a living document of **every feature** the product has today (principle 5). For each:
name, what it does, the persona(s) and journey(s) it serves, where it lives in the code, and its
maturity (solid / rough / partial). This catalogue is consulted in every future evaluation so no
feature is changed or tested in isolation. Write to `.self-improve/features.md`.

## Step 4 — Competitive profile

Research the named (or top) competitors. For each: positioning, standout features, UX strengths, and gaps. Produce a **capability matrix** of "us vs. them" and a list of areas where we are behind or could leapfrog. Use the `deep-research` skill for depth where the topic warrants it. Write to `.self-improve/competitors.md`.

## Step 5 — Seed the backlog

Synthesize Steps 1–4 into a single prioritized **improvement backlog** at `.self-improve/backlog.md`. Each item must have: a unique id (`SI-001`…), title, category (`bug` | `ux` | `feature` | `journey` | `perf` | `a11y` | `tech-debt`), the persona/journey it serves, a crisp acceptance criterion, an effort estimate (S/M/L), and a priority score. Order by priority. Aim for 15–30 well-formed items so the loop never starves.

## Step 6 — Verification tooling

The loop must be able to prove every change works, including UI/UX.

- Confirm tests/build can run. If the project has no E2E/visual testing and is a web/UI app, **scaffold Playwright with visual regression** from `templates/e2e/` — adapt `playwright.config.example.ts` (base URL + the dev/start command as a `webServer`) and create one `tests/journeys/<journey>.spec` per P0 journey from `journey.example.spec.ts`, each walking the journey as the persona and asserting the real outcome **plus a `toHaveScreenshot` visual checkpoint**. Commit the baseline snapshots. Keep it minimal and idiomatic to the repo; do not force it on non-UI projects (libraries, CLIs, pure APIs).
- Record exactly how to run the full **QA gate** (lint → typecheck → build → unit tests → E2E/visual) in config (`commands.e2e` and `e2e` in `qaGate` for UI repos).
- If there is no obvious way to launch the app for verification, note it and prefer the `/verify` and `/run` skills at loop time.

## Step 7 — Write config & branch model

Create `.self-improve/config.json` capturing everything the loop needs:

```json
{
  "product": "<one-line description>",
  "primaryGoal": "<the single most important user outcome>",
  "commands": {
    "install": "...", "lint": "...", "typecheck": "...",
    "build": "...", "test": "...", "e2e": "...", "run": "..."
  },
  "branches": {
    "main": "main",
    "staging": "self-improve/staging",
    "cyclePrefix": "self-improve/cycle-"
  },
  "loop": {
    "sessionBudgetHours": 6,
    "checkpointMinutes": 20,
    "mergePolicy": "auto-merge-to-staging",
    "guardrails": {
      "maxConsecutiveFailures": 3,
      "maxMergesPerHour": 6,
      "maxSpendUSD": null
    }
  },
  "outOfBounds": ["..."],
  "qaGate": ["lint", "typecheck", "build", "test", "e2e"],
  "competitors": ["..."],
  "setupCompletedAt": "<ISO timestamp>"
}
```

Also create `.self-improve/state.json` with `{ "status": "ready", "cycle": 0, "lastReport": null }`, an empty `.self-improve/cycles/` directory, and an empty `.self-improve/knowledge/` directory for reusable playbooks (add a `.gitkeep` to each). Create `.self-improve/staging-changelog.md` with a header only.

## Step 8 — Establish branches & commit

- Ensure the long-running staging branch exists: branch `self-improve/staging` off the current default branch if it doesn't already exist (do NOT push anything to `main`).
- Commit the entire `.self-improve/` knowledge base (and any scaffolded E2E tooling) on the **current working branch**, and also ensure it's present on `self-improve/staging`.
- Push and, if no PR from `self-improve/staging` → `main` exists yet, leave that for the first report (don't open an empty PR).

## Finish

Print a concise summary: personas count, journeys (with P0 list), competitor gaps to attack first, top 5 backlog items, the QA gate command, and the exact command to start the autonomous loop:

> Run `/self-improve:run` to begin the autonomous self-improvement loop. Come back later and run `/self-improve:report` to review what shipped to `self-improve/staging`.

Do not begin implementing backlog items in this command — setup only.
