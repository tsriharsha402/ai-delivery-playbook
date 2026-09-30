# Evaluation plan: Handbook Assistant

| | |
|---|---|
| **Owner** | Sriharsha T |
| **Implementation** | [`evals/`](https://github.com/tsriharsha402/production-rag-service/tree/main/evals) in production-rag-service |

## 1. What we are evaluating

The full pipeline: section-aware chunking, BM25 retrieval (top 4, minimum score 1.0),
and `claude-opus-5-5` at `effort=medium` with search-result citations. The same suite
also runs against a deterministic offline baseline, so CI needs no API key.

## 2. Test set

46 questions about the handbook: 33 direct, 8 deliberately paraphrased, and 5 the
handbook cannot answer. Each answerable question records the document that must be cited
and the facts the answer must contain.

**Known gap:** 46 cases is enough to catch regressions, not to tell close configurations
apart. Goal: 200+ questions, drawn from real (anonymized) pilot traffic.

## 3. Grading

Deterministic: required facts present (keyword match), expected document cited, and the
fixed abstention sentence for unanswerable questions. An LLM-graded rubric is on the
roadmap for tone and completeness.

## 4. Metrics and thresholds

| Metric | Launch threshold (Claude) | CI gate (offline baseline) | Offline baseline, measured |
|---|---|---|---|
| Retrieval hit@k | n/a (same retrieval) | ≥ 90% | 95.1% |
| Answer keyword recall | ≥ 90% | ≥ 55% | 61.0% |
| Citation accuracy | ≥ 90% | n/a | 78.0% |
| Abstention accuracy | ≥ 80% | ≥ 60% | 80.0% |
| Overall pass rate | ≥ 90% | n/a | 63.0% |

The CI gate protects retrieval and chunking on every commit; the launch thresholds apply
to the Claude configuration. **Claude results are not published yet**, which is the first
open item in [launch readiness](04-launch-readiness.md).

## 5. Comparing options

Model and effort choices are made in
[llm-model-selection](https://github.com/tsriharsha402/llm-model-selection): 95%
bootstrap intervals, paired non-inferiority margin of 5 points, cheapest eligible
candidate wins. The rule was [committed before any results](https://github.com/tsriharsha402/llm-model-selection/blob/main/docs/evaluation-plan.md).

## 6. When the evaluation runs

- [x] Every push and pull request (offline baseline, CI gate)
- [ ] Every model, prompt or retrieval change against Claude (`make eval-live`), results attached to the PR
- [ ] Weekly against production configuration, after launch

## 7. Budget

About $1 per full run against Claude; up to about $5 for a full model-selection run
across five configurations.
