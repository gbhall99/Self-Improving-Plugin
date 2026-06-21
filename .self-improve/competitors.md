# Competitive Profile — autonomous / agentic SWE tools (mid-2026)

## Landscape
Three camps: **hosted "AI engineers"** (Devin/Cognition, Cursor Cloud/Background Agents) —
ticket-in/PR-out on their own VMs, newest ones self-test via computer-use + recorded video;
**platform-native** (GitHub Copilot coding agent, successor to the sunset Copilot Workspace) —
runs in GitHub Actions, issue→draft PR, agentic review can auto-fix; **open/local toolkits**
(OpenHands ~72% SWE-bench, Aider terminal pair-programmer, SWE-agent research) — control and no
lock-in but single-task. Adjacent: self-healing test tools (Applitools/Virtuoso/Testsigma) and
self-evolving-agent research validate the *concept* but are point solutions.

**Key finding:** every major competitor is **task-triggered**, most run on **their own infra**,
and **none** takes personas, user-journeys, or competitive research as input. That whitespace —
continuous, self-directed, persona/journey/competitor-driven improvement running zero-infra
inside the user's own repo — is where self-improve wins. The one area where Devin/Cursor have
genuinely pulled ahead and we are only at parity: **E2E + visual QA via computer-use**.

## Capability matrix (Better / Parity / Worse / Missing vs self-improve)
| Capability | self-improve | Devin | Copilot agent | Cursor Agents | OpenHands | Aider |
|---|---|---|---|---|---|---|
| Continuous unattended, picks own work | Better | Worse | Worse | Worse | Worse | Missing |
| Persona/journey-driven improvement | Better | Missing | Missing | Missing | Missing | Missing |
| Competitive research built-in | Better | Missing | Missing | Missing | Missing | Missing |
| Full QA gate incl. E2E + visual | Better* | Parity | Worse | Parity | Worse | Worse |
| Human-gated merge (staging→main) | Parity | Parity | Parity | Parity | Parity | Parity |
| Runs in user's own repo (no egress) | Better | Worse | Worse | Worse | Parity | Better |
| Zero extra infra (no VM/CI/seats) | Better | Worse | Worse | Worse | Worse | Parity |

\*intended design; today closer to parity until the E2E/visual gate is fully wired (→ SI-009).

## Attack-first opportunities (→ backlog)
1. Persona/journey/competitor brief as durable, versioned, self-updating context → **SI-001, SI-004**
2. Competitive research → queued, citable gap tickets each loop → **SI-002**
3. Real E2E + visual-regression gate tied to `journeys.md`, blocking staging → **SI-009**
4. Rich "shift report" `staging→main` PR grouped by persona/journey w/ screenshots → **SI-001**
5. Local, versioned "playbooks/knowledge" of verified repros (match Devin, keep local) → **SI-005**
6. Lean into zero-infra / no-egress story; `dry-run` + guarantees doc → **SI-007**
7. Self-scheduling with budget/failure guardrails + kill switch (safe "run overnight") → **SI-003**
8. Marketplace-native one-line install (lowest-friction adoption) → already shipped ✓

## Sources
Devin (devin.ai, docs.devin.ai/release-notes/2026, cognition.ai blog) · OpenHands
(openhands.dev, github.com/OpenHands) · Aider (aider.chat) · SWE-agent (princeton / SWE-bench
leaderboard) · Cursor (cursor.com/blog/scaling-agents) · GitHub Copilot coding agent
(docs.github.com/copilot, github.blog) · Claude Code subagents & plugin ecosystem
(code.claude.com/docs). Full links captured in the cycle research log.
