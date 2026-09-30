# AI incident postmortem: `<short title>`

> **Purpose:** learn from an AI-specific failure (wrong or harmful outputs, prompt
> injection, quality regression, cost spike) without blame. Due within 5 business days of
> resolution. Focus on systems and decisions, not individuals.

| | |
|---|---|
| **Severity** | `<SEV1 / SEV2 / SEV3>` |
| **Detected** | `<date time>`, by `<monitoring alert / user report / eval run>` |
| **Resolved** | `<date time>` |
| **Duration of user impact** | `<…>` |
| **Author / reviewers** | `<names>` |

## Summary

Two or three sentences a non-engineer can follow: what users experienced, how many, for
how long, and what fixed it.

## Impact

- Users or requests affected: `<n>`
- Nature of harm: `<wrong information / exposed data / offensive output / cost / downtime>`
- Downstream effects: `<decisions made on wrong answers, customer escalations, spend>`

## Timeline

| Time | Event |
|---|---|
| | Change deployed / trigger occurred |
| | First signal (and whether anyone noticed it) |
| | Detected |
| | Mitigated |
| | Resolved |

## Root cause

What went wrong in the system. For AI incidents, check each:

- [ ] **Model change:** provider update, new version, changed settings
- [ ] **Prompt change:** instructions weakened, conflicting, or untested
- [ ] **Data change:** stale, missing, incorrect or poisoned source content
- [ ] **Retrieval failure:** the right context wasn't found, or wrong context was
- [ ] **Adversarial input:** prompt injection or jailbreak
- [ ] **Evaluation gap:** the evaluation suite didn't cover this case
- [ ] **Monitoring gap:** signals existed but no alert fired

## Why the safeguards didn't catch it

The most important section. Which layer should have caught this: evaluation,
review, monitoring, rate limits, human oversight? Why didn't it?

## Action items

Each has one owner and a due date, and is tracked in `<issue tracker>`.

| Action | Type | Owner | Due |
|---|---|---|---|
| Add the failing cases to the evaluation set | Prevent | | |
| `<…>` | Detect | | |
| `<…>` | Mitigate | | |

## What went well

Detection, communication or tooling that worked and should be kept.
