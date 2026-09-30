# Risk assessment: Handbook Assistant

| | |
|---|---|
| **Owner** | Sriharsha T |
| **Risk tier** | 1 (internal, assistive) |

## 1. Risk register

Likelihood (L) and impact (I) from 1 to 3. Scores of 6+ must be mitigated or accepted
before launch.

| # | Risk | L | I | Score | Mitigation | Residual | Status |
|---|---|---|---|---|---|---|---|
| R1 | Confidently wrong answer | 2 | 3 | **6** | Answers only from retrieved text; every claim cited with a verbatim quote; fixed abstention sentence; abstain without calling the model when retrieval finds nothing | Low | ✅ Mitigated; verify with Claude eval results |
| R2 | Answer from an outdated policy | 2 | 2 | 4 | Cache key includes a hash of all documents, so any edit invalidates cached answers | Low | ✅ Mitigated |
| R3 | Prompt injection through handbook content | 1 | 2 | 2 | Handbook edits are reviewed; the model has no tools and can't take actions | Low | ✅ Accepted |
| R4 | Personal details typed into questions reach the provider or logs | 2 | 2 | 4 | Logs record metadata only (IDs, tokens, cost, latency), not question text | Medium | ⚠️ Open: review the provider's data terms; add a notice in the UI |
| R5 | Over-reliance: people skip the source | 2 | 2 | 4 | Source quote shown under every answer | Medium | ⚠️ Open: state in the UI that the handbook is authoritative |
| R7 | Cost runaway | 2 | 2 | 4 | Answer cache; per-client rate limit (30/min) | Medium | ⚠️ Open: no total daily spend cap |
| R8 | Model provider outage | 2 | 1 | 2 | SDK retries; 503 with a clear message; users fall back to the handbook | Low | ✅ Accepted |
| R9 | Behavior change after a model or prompt update | 2 | 2 | 4 | Model pinned by ID; changes require the [AI change review](../../templates/06-ai-change-review.md) with eval results | Low | ✅ Mitigated |
| R11 | Anyone on the network can call the API | 3 | 2 | **6** | Put the service behind company SSO before launch | High until fixed | ⛔ **Blocking** |
| R12 | False-positive safety refusal blocks a legitimate question | 1 | 1 | 1 | Server-side refusal fallback enabled; refusals are never cached | Low | ✅ Mitigated |

R6 (uneven quality across groups) and R10 (harmful content) were reviewed and judged not
applicable: English-only internal policy content with no user-generated text in the corpus.

## 2. Decision

| | |
|---|---|
| Blocking | R11 (no authentication) |
| Open, must close before launch | R4 (data terms review, privacy notice), R5 (UI wording), R7 (spend cap) |
| Re-review | On any model change, and before expanding beyond the handbook |
