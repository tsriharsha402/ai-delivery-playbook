# AI change review

> **Purpose:** a model, prompt, retrieval or data change can shift behavior across every
> request at once, without a single line of "logic" changing. Use this as the pull
> request description for any such change. Copy it into
> `.github/pull_request_template.md` or link it from there.

## What changed

- [ ] Model or model settings (e.g. version, effort, temperature, max tokens)
- [ ] Prompt (system prompt, instructions, examples)
- [ ] Retrieval (chunking, ranking, number of results, filters)
- [ ] Source data (documents added, removed or updated)
- [ ] Tools available to the model
- [ ] Grading or evaluation set

Summary: `<one paragraph>`

## Why

The problem this fixes or the improvement expected, with a link to the issue or incident.

## Evaluation results

Attach before/after results from the evaluation suite on the same test set.

| Metric | Before | After | Threshold |
|---|---|---|---|
| Pass rate | | | |
| Abstention accuracy | | | |
| Citation accuracy | | | |
| p95 latency | | | |
| Cost per 1,000 requests | | | |

- [ ] No blocking metric crossed its threshold
- [ ] Failed cases reviewed by hand; new failures explained below
- [ ] If the evaluation set itself changed, results for both old and new sets are included

## Rollout

- [ ] Behind a flag / staged rollout: `<plan>`
- [ ] Monitoring to watch after release: `<metrics>`
- [ ] Rollback: `<how, and how fast>`

## Reviewer checklist

- [ ] The change does what the description says, and nothing else
- [ ] Prompt changes don't weaken safety instructions (abstention, refusals, grounding)
- [ ] Cost impact is understood and acceptable
