# Worked example: Handbook Assistant

The playbook applied to [production-rag-service](https://github.com/tsriharsha402/production-rag-service),
an internal assistant that answers employee questions from company policy documents,
with citations. The company, Northwind Labs, and its handbook are fictional; the
software, evaluation results and cost figures are real.

| Phase | Document | Status |
|---|---|---|
| Discover | [AI feature brief](01-brief.md) | ✅ Approved (Tier 1) |
| Design | [Evaluation plan](02-evaluation-plan.md) | ✅ Implemented, runs in CI |
| Design | [Risk assessment](03-risk-assessment.md) | ✅ Reviewed; 1 blocking and 2 open risks |
| Design | Model selection | 🔧 [Benchmark built](https://github.com/tsriharsha402/llm-model-selection), first run pending |
| Build | Decision records | ✅ [4 records](https://github.com/tsriharsha402/production-rag-service/tree/main/docs/decisions) |
| Launch | [Launch readiness](04-launch-readiness.md) | ⛔ **No-go** until open items close |
| Operate | Monitoring plan | ⬜ After launch readiness items |

The launch readiness review ending in "no-go" is deliberate: the checklist exists to
surface what's missing, and it did.
