---
description: Start the autonomous loop in HARDEN focus — only bugs, security, performance, accessibility, robustness, test coverage, and tech-debt. No new features. A shortcut for `/self-improve:run harden`.
argument-hint: "[optional: max cycles this run, or 'until <time>']"
---

# Self-Improve · Harden

Run the autonomous self-improvement loop in **harden** focus: strengthen what already exists —
fix bugs, close security and robustness gaps, improve performance and accessibility, raise test
coverage, and pay down tech-debt. **Do not build new features** in this mode.

This is a thin shortcut: set the focus to `harden` (persist it as `loop.focus` in
`.self-improve/config.json`) and then execute `/self-improve:run` exactly as documented, passing
through any `$ARGUMENTS` (cycle/time limits). All guardrails, the full QA gate, and the operating
principles apply unchanged — only the selection of work narrows to hardening.

Prefer the `/security-review` skill during investigation, and bias the QA gate toward regression
and edge-case coverage. When done, summarise with `/self-improve:report`.
