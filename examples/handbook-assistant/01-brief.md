# AI feature brief: Handbook Assistant

| | |
|---|---|
| **Owner** | Sriharsha T |
| **Status** | Approved by the owner (solo portfolio project, so gates are self-reviewed) |
| **Risk tier** | **1: internal, assistive.** Employees read answers and act on them, but every answer cites its source and the handbook remains the authority. No customer data, no automated decisions |
| **Code** | [production-rag-service](https://github.com/tsriharsha402/production-rag-service) |

## 1. Problem

Employees ask the same policy questions (on-call rules, expenses, deploy windows,
security procedures) in chat channels, and team leads and HR answer them by hand.
Answers are inconsistent and slow, and people often act on outdated memory of a policy.

## 2. Why AI, and why now

- Keyword search over the handbook finds documents, not answers: people still read
  several pages to find one rule.
- Retrieval plus a language model can answer the specific question in a sentence and
  point to the exact source text, so answers are both fast and verifiable.
- **Simplest non-AI alternative:** better search and an FAQ page. It helps with common
  questions but can't handle phrasing it hasn't seen. The assistant uses search
  (BM25) as its first step anyway, so it builds on that alternative rather than replacing it.

## 3. Users and use

| | |
|---|---|
| Primary users | All employees; heaviest use expected from new hires and on-call engineers |
| How they use the output | Read the answer, check the cited source, act on it |
| Human in the loop | The employee; the source quote is shown with every answer |
| Volume | ~1,000 questions/day at full rollout (estimate) |

## 4. What "good" looks like

| Metric | Type | Target | How measured |
|---|---|---|---|
| Answers correct, complete and cited | Quality | ≥ 90% pass rate | [Evaluation plan](02-evaluation-plan.md) |
| Says "I don't know" when the handbook doesn't cover it | Safety | ≥ 80% | Evaluation plan |
| Cites the right document | Quality | ≥ 90% | Evaluation plan |
| Cost per uncached question | Cost | ≤ $0.02 | Token usage × price |
| p95 latency | Experience | ≤ 10 s | `/v1/metrics` |
| Policy questions in team chat channels | Outcome | −50% after 3 months | Channel analytics |

## 5. Failure modes

1. **A confident wrong answer** about a rule someone then breaks (e.g. deploying during
   the change freeze). Mitigated by mandatory citations and abstention.
2. **An answer from an outdated document.** Mitigated by the cache being keyed on a hash
   of the documents, so edits invalidate old answers.
3. **Cost growth** from heavy use or abuse. Mitigated by caching and per-client rate limits.

## 6. Scope

- **In scope:** single questions about the handbook, answered with citations.
- **Non-goals:** conversations and follow-ups, answering from outside the handbook,
  personal HR cases, taking actions (booking time off, filing expenses).

## 7. Data

The handbook (internal, not confidential). Questions are sent to the model provider along
with the retrieved handbook excerpts. Questions may contain personal details that
employees type in; see risk R4.

## 8. Cost estimate

| | |
|---|---|
| Tokens per request | ~450 input / ~500 output (including reasoning) |
| Price | `claude-opus-5-5`: $4 / $20 per million tokens |
| Cost per uncached request | ~$0.012 |
| Monthly at 1,000/day with 30% cache hits | ~$250 |
| Build effort (estimate) | 1 engineer × 3 weeks to launch readiness |

Estimate only: [llm-model-selection](https://github.com/tsriharsha402/llm-model-selection)
will replace it with measured numbers and test cheaper models.

## 9. Rollout and exit

Internal pilot with two teams, then company-wide. Roll back if the thumbs-down rate
exceeds 20% for a week, or on any incident where an answer contradicted its own cited
source.
