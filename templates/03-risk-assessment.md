# Risk assessment: `<feature name>`

> **Purpose:** find what can go wrong before users do, and decide which risks are
> mitigated, accepted or blocking. Required for Tier 2 and 3; recommended for Tier 1.
> Reviewed at **Gate 2** by the engineering lead and a risk reviewer (security, privacy
> or legal, depending on the feature).

| | |
|---|---|
| **Owner** | `<name>` |
| **Risk reviewer(s)** | `<names, functions>` |
| **Risk tier** | `<1 / 2 / 3>` |

## 1. Risk register

Score likelihood and impact from 1 (low) to 3 (high). Anything scoring 6 or more needs a
mitigation, or an explicit acceptance by a named person, before launch.

| # | Risk | Likelihood | Impact | Score | Mitigation | Residual risk | Owner |
|---|---|---|---|---|---|---|---|
| R1 | Confidently wrong answers (hallucination) | | | | | | |
| R2 | Answers from stale or superseded source data | | | | | | |
| R3 | Prompt injection via user input or retrieved content | | | | | | |
| R4 | Sensitive or personal data exposed in outputs or logs | | | | | | |
| R5 | Users over-rely on the output without checking | | | | | | |
| R6 | Uneven quality across user groups or languages | | | | | | |
| R7 | Cost runaway (traffic spikes, abuse, long outputs) | | | | | | |
| R8 | Model provider outage or deprecation | | | | | | |
| R9 | Behavior change after a model or prompt update | | | | | | |
| R10 | Harmful or off-policy content | | | | | | |

Remove rows that don't apply and add feature-specific ones.

## 2. Data and privacy

- [ ] Data sent to the model provider is listed, and allowed under our data policy and the provider's terms
- [ ] Personal data is minimized, and excluded from prompts where it isn't needed
- [ ] Retention: how long prompts, outputs and logs are kept, and who can access them
- [ ] Users are told when they are interacting with AI-generated content

## 3. Security

- [ ] Untrusted text (user input, retrieved documents, web pages, tool results) cannot trigger privileged actions
- [ ] Tools the model can call follow least privilege; destructive actions require human confirmation
- [ ] Secrets never appear in prompts, outputs or logs
- [ ] Rate limits and spend limits per user and in total

## 4. Human oversight

Where a person can review, correct or override the output, and what happens when the
system is uncertain. For Tier 3: the named human decision-maker and how their review is
recorded.

## 5. Decision

| | |
|---|---|
| Blocking risks remaining | `<none / list>` |
| Accepted risks and who accepted them | `<…>` |
| Review date | `<YYYY-MM-DD>` (re-review on any major model or scope change) |
