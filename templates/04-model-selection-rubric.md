# Model selection rubric: `<feature name>`

> **Purpose:** choose a model (and its settings) with evidence, not preference. Pair it
> with the [evaluation plan](02-evaluation-plan.md): the rubric says what matters, the
> evaluation measures it. A worked, runnable version is
> [llm-model-selection](https://github.com/tsriharsha402/llm-model-selection).

## 1. Candidates

| Candidate | Model | Settings (e.g. effort, temperature, context) | Why it's a candidate |
|---|---|---|---|
| A (baseline) | | | What we run today, or the obvious default |
| B | | | |
| C | | | |

Include at least one cheaper and one more capable option than the baseline, so the
result says which direction to move.

## 2. Hard requirements (pass/fail)

A candidate failing any of these is out, whatever it scores elsewhere.

- [ ] Meets the blocking quality thresholds in the evaluation plan
- [ ] p95 latency ≤ `<x s>`
- [ ] Available in the regions / platforms we need (data residency)
- [ ] Allowed by our data policy and the provider's terms for this data
- [ ] Supports required features (e.g. citations, tool use, structured output, context length)

## 3. Tradeoffs among eligible candidates

| Criterion | Weight | How measured |
|---|---|---|
| Quality (pass rate, with confidence interval) | `<e.g. 50%>` | Evaluation suite |
| Cost per 1,000 tasks | `<e.g. 25%>` | Measured token usage × price |
| Latency (p50 / p95) | `<e.g. 15%>` | Evaluation run |
| Operational fit (rate limits, support, vendor risk) | `<e.g. 10%>` | Review |

Or, simpler and harder to game: **pick the cheapest candidate whose quality is
statistically non-inferior to the best** (e.g. the 95% interval of the gap stays within
5 points). Choose one approach before seeing results.

## 4. Build vs. buy vs. fine-tune

| Option | When it's right |
|---|---|
| Hosted model + prompting + retrieval | Default. Fastest to ship, easiest to upgrade |
| Fine-tuned or smaller self-hosted model | Very high volume, strict latency or data constraints, and an evaluation suite that proves quality holds |
| Buy a vendor product | The capability isn't a differentiator and a vendor meets the hard requirements |

## 5. Result

| | |
|---|---|
| Chosen | `<candidate>` |
| Evidence | `<link to evaluation results>` |
| Versus baseline | Quality `<±x pts>`, cost `<±x%>`, latency `<±x s>` |
| Re-evaluate when | New model release, price change, or quality regression in monitoring |
