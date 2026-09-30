# Evaluation plan: `<feature name>`

> **Purpose:** define how quality is measured and what "good enough" means, **before**
> any results exist. Approved at **Gate 2**. Changes after the first results go in a
> separate, explained revision, never alongside new numbers.

| | |
|---|---|
| **Owner** | `<name>` |
| **Linked brief** | `<link>` |
| **Version / date** | `<v1, YYYY-MM-DD>` |

## 1. What we are evaluating

The exact system under test: model, settings, prompt version, retrieval configuration,
tools. Evaluate what production will actually run, not a playground approximation.

## 2. Test set

| | |
|---|---|
| Size | `<n cases>` (at least 50 for directional results; 200+ to detect differences of a few points) |
| Source | Real user requests (anonymized) / expert-written / synthetic, with proportions |
| Coverage | Common cases, hard cases, edge cases, and cases the system **should refuse or abstain on** |
| Owner of the labels | `<who decides what "correct" is>` |
| Storage | `<path in repo>`, versioned with the code |

> A test set with no "should say I don't know" cases cannot catch hallucination.

## 3. Grading

| Method | Use for | Notes |
|---|---|---|
| Deterministic checks | Required facts, format, citations, refusals | Cheap, reproducible; can miss correct paraphrases |
| LLM-graded rubric | Tone, completeness, reasoning | Validate the grader against human labels on a sample first |
| Human review | Final check, ambiguous cases | Budget time for it: `<n cases per release>` |

Pass criteria per case: `<e.g. contains every required fact AND cites the right source AND does not abstain>`.

## 4. Metrics and thresholds

| Metric | Threshold | Blocking? |
|---|---|---|
| Overall pass rate | `<≥ x%>` | Yes |
| Abstention accuracy (should-abstain cases) | `<≥ x%>` | Yes |
| Citation / grounding accuracy | `<≥ x%>` | Yes |
| Refusal + error rate | `<≤ x%>` | Yes |
| p95 latency | `<≤ x s>` | Yes |
| Cost per 1,000 requests | `<≤ $x>` | Advisory |

## 5. Comparing options

If this evaluation chooses between configurations (models, prompts, retrieval), define
the rule now:

- How uncertainty is reported (e.g. 95% bootstrap intervals).
- When two options count as equivalent (e.g. paired non-inferiority margin of 5 points).
- The tie-breaker (e.g. cheapest, then fastest).

## 6. When the evaluation runs

- [ ] On every pull request that changes the model, prompt, retrieval or data (CI gate)
- [ ] Before each release
- [ ] On a schedule against production samples (drift check): `<frequency>`

## 7. Budget

Estimated cost per full run: `<$x>`. Approval needed above: `<$y>`.

## 8. Known limitations

What this evaluation cannot tell you (sample size, single language, synthetic data,
grader bias), written down so nobody over-reads the numbers.
