# Launch readiness: Handbook Assistant

| | |
|---|---|
| **Rollout** | Pilot with two teams → company-wide |
| **Decision** | ⛔ **No-go**: open items below, including 1 blocking risk |

## Quality

- [x] Evaluation suite runs automatically on every change (CI quality gate)
- [ ] **Claude configuration meets the launch thresholds.** First live run: 84.8% pass rate against a 90% threshold, with every failure caused by retrieval. Retrieval was changed to send 8 chunks (context recall 82.9% → 92.7%); re-run pending
- [x] Model choice evaluated by [llm-model-selection](https://github.com/tsriharsha402/llm-model-selection): recommends `claude-sonnet-5-5` at low effort (same pass rate as Opus 5.5 on its test set, 56% cheaper). Rollout behind a flag still to do
- [ ] A domain expert (HR / people ops) reviews a sample of 30 answers

## Safety and risk

- [x] Abstains instead of guessing, including without a model call when retrieval finds nothing
- [x] Every answer shows its source quote
- [ ] **R11: authentication via company SSO** (blocking)
- [ ] R4: provider data terms reviewed; privacy notice in the UI
- [ ] R5: UI states that the handbook is authoritative

## Reliability

- [x] Retries, timeouts, and a clear 503 when the provider is unavailable
- [x] Per-client rate limiting
- [ ] Load test at 3× expected peak
- [ ] Rollback tested (plan: configuration change or redeploy of the previous image)

## Observability

- [x] Request IDs, structured logs with model, tokens, cost and latency
- [x] Metrics endpoint: latency percentiles, cache hit rate, spend, abstentions, errors
- [ ] Dashboards and alerts (monitoring plan)
- [ ] User feedback capture (thumbs up/down)

## Cost

- [x] Cost tracked per request
- [ ] Measured cost per request on the launch configuration ($0.0093 measured on Opus 5.5 with 4 chunks; re-measure on the chosen model with 8 chunks)
- [x] R7: total daily spend cap with an 80% warning

## People

- [x] Named owner
- [ ] Pilot teams briefed on scope and limitations

## Conditions for rollback

Thumbs-down rate above 20% for a week; any answer that contradicts its own cited source;
daily cost above 3× forecast.
