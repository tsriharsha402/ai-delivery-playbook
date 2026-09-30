# Monitoring plan: `<feature name>`

> **Purpose:** know within hours, not weeks, when quality, cost or safety drifts. AI
> features rarely fail with errors; they fail by quietly getting worse. Required for
> Tier 2+; implemented before **Gate 3**.

| | |
|---|---|
| **Owner** | `<name>` |
| **Dashboard** | `<link>` |
| **Alert destination** | `<channel / pager>` |

## 1. What to measure

| Signal | Metric | Alert when | Severity |
|---|---|---|---|
| **Availability** | Error rate, provider timeouts | `<> 2% over 15 min>` | Page |
| **Latency** | p50 / p95 end to end | `<p95 > 10 s over 15 min>` | Ticket |
| **Cost** | Spend per hour and per day; cost per request | `<daily spend > 2× 7-day average>` | Page |
| **Quality proxy** | Abstention rate, refusal rate, answer length | `<abstention rate ±50% vs 7-day baseline>` | Ticket |
| **User signal** | Thumbs-down rate, escalations to humans | `<thumbs-down > 20% over a day>` | Ticket |
| **Safety** | Flagged outputs, policy violations, injection attempts | `<any confirmed case>` | Page |
| **Usage** | Requests, unique users, cache hit rate | Informational | None |

> Abstention and refusal rates are cheap, early warnings: a sudden change usually means
> the model, the prompt or the source data changed underneath you.

## 2. Ongoing quality checks

- **Scheduled evaluation:** run the evaluation suite against production configuration
  `<weekly>`, and on every model or prompt change.
- **Production sampling:** review `<n>` random real interactions per `<week>`, labeled
  by `<who>`. Add interesting failures to the evaluation set.
- **Feedback loop:** every thumbs-down with a comment is triaged within `<x days>`.

## 3. Logging

Per request: request ID, timestamp, user or client ID (pseudonymous), model and version,
prompt version, retrieval results (IDs and scores), token counts, cost, latency, outcome
flags (abstained, refused, cached). Retention: `<x days>`. Exclude or redact `<fields>`.

## 4. Review cadence

| Cadence | Review | Attendees |
|---|---|---|
| Weekly | Dashboard, alerts fired, sampled failures | Feature owner, tech lead |
| Monthly | Quality trend, cost per task, user feedback themes, roadmap | + Engineering manager, product |
| Quarterly | Model landscape: is there a better or cheaper option? Re-run model selection | + Stakeholders |
