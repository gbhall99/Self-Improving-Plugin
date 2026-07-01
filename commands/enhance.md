---
description: Start the autonomous loop in ENHANCE focus — prioritise new features and competitive-gap items (then UX), while never shipping broken work. A shortcut for `/self-improve:run enhance`.
argument-hint: "[optional: max cycles this run, or 'until <time>']"
---

# Self-Improve · Enhance

Run the autonomous self-improvement loop in **enhance** focus: move the product forward by
shipping the highest-value new features and closing competitive gaps, then high-impact UX.
Routine tech-debt is deprioritised, but quality is not — a bug that blocks a feature is fixed as
part of that feature, and nothing red ever merges.

This is a thin shortcut: set the focus to `enhance` (persist it as `loop.focus` in
`.self-improve/config.json`) and then execute `/self-improve:run` exactly as documented, passing
through any `$ARGUMENTS` (cycle/time limits). All guardrails, the full QA gate, and the operating
principles apply unchanged — including principle 6 (prefer AI-centric, agentic solutions). When
done, summarise with `/self-improve:report`.
