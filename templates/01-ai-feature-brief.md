# AI feature brief: `<feature name>`

> **Purpose:** decide whether this is worth building, and whether it needs AI at all.
> One to two pages. Written by the proposing PM or engineer; approved at **Gate 1** by
> product and engineering leads.

| | |
|---|---|
| **Owner** | `<name>`, accountable for quality, cost and incidents after launch |
| **Status** | Draft / In review / Approved / Rejected |
| **Risk tier** | 1 / 2 / 3 (see [risk tiers](../README.md#right-size-the-process-risk-tiers)), with one sentence on why |
| **Gate 1 sign-off** | `<link to approval>` |

## 1. Problem

Who has the problem, how often, and what it costs them today. Use numbers where you have
them (time spent, tickets, error rate, revenue at risk).

## 2. Why AI, and why now

- What does AI do here that a rules-based or search-based solution can't?
- What is the simplest non-AI alternative, and why is it not enough?
- What has changed (model capability, cost, data availability) that makes this viable now?

> If a non-AI solution gets 80% of the value at 20% of the risk, write that down and
> consider shipping it first.

## 3. Users and use

| | |
|---|---|
| Primary users | `<who>` |
| How they use the output | e.g. read and act on it / edit before sending / fully automated |
| Human in the loop? | Where a person reviews, approves or can override |
| Volume | Expected requests per day at launch and in 12 months |

## 4. What "good" looks like

| Metric | Type | Target | How measured |
|---|---|---|---|
| `<e.g. answers correct and cited>` | Quality | `<e.g. ≥ 90% on eval set>` | Evaluation suite |
| `<e.g. says "I don't know" when it should>` | Safety | `<e.g. ≥ 90%>` | Evaluation suite |
| `<e.g. time to answer a policy question>` | Outcome | `<e.g. 10 min → 1 min>` | User study / telemetry |
| `<e.g. adoption>` | Outcome | `<e.g. 40% of team weekly>` | Telemetry |
| Cost per task | Cost | `<e.g. ≤ $0.02>` | Token usage × price |
| p95 latency | Experience | `<e.g. ≤ 10 s>` | Service metrics |

## 5. Failure modes

What does a wrong answer cost, and to whom? List the three worst plausible failures and
who would notice. The [risk assessment](03-risk-assessment.md) goes deeper for Tier 2+.

## 6. Scope

- **In scope:** `<…>`
- **Non-goals:** `<…>` (as important as the goals; prevents scope creep)

## 7. Data

What data the feature reads and writes, where it lives, who can see it, and whether any
of it is personal, confidential or regulated. Note any data that must not leave the
company or be sent to a model provider.

## 8. Cost estimate

| | |
|---|---|
| Tokens per request (input / output) | `<estimate>` |
| Price per million tokens | `<model, input / output>` |
| Cost per request | `<…>` |
| Monthly cost at expected volume | `<…>` |
| Build effort | `<people × weeks>` |

## 9. Rollout and exit

How it will be released (internal pilot, % rollout) and **the conditions under which
we would roll it back or shut it down**.

## 10. Open questions

`<…>`
