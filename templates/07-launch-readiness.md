# Launch readiness: `<feature name>`

> **Purpose:** the go/no-go checklist at **Gate 3**. Every unchecked item needs either a
> date or a named person accepting the risk. Run through it in a 30-minute review with
> the feature owner, engineering manager, and (Tier 2+) the risk reviewer.

| | |
|---|---|
| **Launch date** | `<YYYY-MM-DD>` |
| **Rollout** | `<e.g. internal pilot → 10% → 50% → 100%>` |
| **Decision** | Go / No-go / Go with conditions |
| **Decided by** | `<name>` |

## Quality

- [ ] Evaluation suite passes every blocking threshold in the [evaluation plan](02-evaluation-plan.md), on the exact configuration being launched
- [ ] Evaluation runs automatically on every model, prompt or retrieval change
- [ ] A sample of real or realistic outputs has been reviewed by a domain expert

## Safety and risk

- [ ] All risks scoring 6+ in the [risk assessment](03-risk-assessment.md) are mitigated or accepted by a named person (Tier 2+)
- [ ] The system says "I don't know" rather than guessing when it lacks information
- [ ] Users can verify outputs (citations, sources, reasoning shown)
- [ ] AI-generated content is labeled where users see it

## Reliability

- [ ] Timeouts, retries and a user-facing message when the model provider is unavailable
- [ ] Rate limits per user and a total spend limit
- [ ] Load tested at `<x>`× expected peak traffic
- [ ] Rollback tested: `<method>` takes `<minutes>`

## Observability

- [ ] [Monitoring plan](08-monitoring-plan.md) implemented: dashboards and alerts live
- [ ] Every request is traceable (request ID, model, prompt version, tokens, cost, latency)
- [ ] User feedback captured (e.g. thumbs up/down with an optional comment)

## Cost

- [ ] Cost per request measured on the launch configuration: `<$x>`
- [ ] Monthly forecast at expected volume: `<$x>`, within budget of `<$y>`
- [ ] Alert when daily spend exceeds `<$z>`

## People

- [ ] Named owner and on-call path for AI-specific incidents
- [ ] Support team briefed: known limitations and how to escalate
- [ ] Users told what the feature is for, what it isn't, and how to report problems

## Conditions for rollback

Written before launch: `<e.g. abstention rate doubles, negative feedback > 20%, any Tier 3 harm incident, daily cost > 3× forecast>`.
