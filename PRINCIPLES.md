# Operating principles

Non-negotiable standards for **every** change the self-improve loop proposes, on any repo.
They are part of the definition of done: a change that violates one of these is not "done",
no matter how green the tests are. Commands and agents reference this file; the QA gate
enforces what can be enforced automatically.

## 1. No emojis — crisp iconography only
Never use emoji in product UI, docs, commit messages, PR bodies, reports, or generated state.
Use crisp iconography instead: a proper icon set / inline SVG in product UI, and plain
text-style symbols (`->`, `*`, `-`, `[x]`, `OK`, `FAIL`) or clear labels in text. The QA gate
fails on emoji characters in the plugin's own markdown and docs.

## 2. Simplify for the user
Prefer the simplest solution that fully solves the user's problem. Fewer steps, fewer options,
fewer concepts. Reduce cognitive load and time-to-value. If a change adds surface area, it must
remove at least as much friction as it introduces. "Could this be simpler for the user?" is a
required question in every UX review and acceptance check.

## 3. Remove redundancy in code and solution
Leave the codebase smaller or cleaner where you can. No duplicated logic, dead code, copy-paste
blocks, redundant config, or overlapping features. Consolidate before adding. Every cycle should
actively look for redundancy to delete, not only behavior to add.

## 4. Keep documentation current
Documentation is part of the change, not a follow-up. Any change that alters behavior, commands,
configuration, features, personas, or journeys MUST update the affected docs in the same change.
Stale docs are treated as a defect and block the QA gate's GO.

## 5. Document every feature, persona, and journey — and test against them
The knowledge base must contain a living document of every **feature** (`features.md`), every
**persona** (`personas.md`), and every **user journey** (`journeys.md`). Setup creates them; the
loop keeps them current (principle 4). Every evaluation, test, and review explicitly considers all
three: does this change serve a persona, complete or improve a journey, and is the affected
feature documented and exercised? Nothing is evaluated in isolation from them.

## 6. Prefer AI-centric, agentic solutions
Default to AI-native and agentic approaches when they genuinely serve the persona better than a
conventional one. For every problem, feature, and journey, ask first: *could an LLM or an agent
do this better?* Favour designs where the product understands intent in natural language, adapts
to the user, automates multi-step work, and uses tools/agents to act on the user's behalf —
rather than static forms, manual steps, and rigid rules. Where AI is involved, use the latest,
most capable models and sound agentic patterns (clear tool definitions, verification, graceful
fallback). This is a strong default, **not** a mandate to bolt AI onto everything: reject AI that
adds latency, cost, or unpredictability without a real user win, and always keep a reliable
fallback. When two solutions are comparable, prefer the more AI-centric, agentic one.
