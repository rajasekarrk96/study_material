# Path Migration — Content Conflict Findings

_Generated: 2026-08-08 — Learning OS Export Pipeline standardization_

> ⚠️ **These findings change the migration plan.** Several learning-path courses that were
> assumed to be *duplicates* of a canonical course actually contain **richer or unique
> content** than the canonical. Per the rule *"do NOT merge automatically unless they are
> TRUE duplicates,"* these must **not** be auto-deleted. No content has been deleted.

## A. `frontend-development` — path curriculum is REAL content; canonical is scaffold

| Course | Path curriculum | Canonical (`technologies/`) curriculum | Verdict |
|---|---|---|---|
| html5 (sampled) | **182 lines, 0 TODO** (authored notes) | 58 lines, 15 TODO (scaffold only) | **Path is richer** — do NOT delete |

The 6 `frontend-development` syllabi (html5, css3, javascript, react, bootstrap, jquery) map to
canonical `technologies/` courses, **but** the learning-path CURRICULUM already contains authored
lesson notes, whereas the canonical `technologies/` CURRICULUM is only `> TODO` placeholders
(generated earlier this session). Deleting the path curriculum would destroy real content.

**Recommendation:** promote the `frontend-development` authored notes **into** the canonical
`technologies/<course>/CURRICULUM` (they become the canonical content), then reference from the
path. This is a *merge*, not a delete — needs approval.

## B. `data-science-learning-path` — 6 "overlap" courses vs existing canonical

Lesson-file counts (module.md/desktop.ini excluded):

| Course (in path) | Path lessons | Existing canonical | Canonical lessons | Which is richer? |
|---|---|---|---|---|
| computer-vision | 72 | specializations/computer-vision | 144 | canonical |
| deep-learning | 94 | specializations/deep-learning | 189 | canonical |
| machine-learning | 107 | specializations/machine-learning | 214 | canonical |
| power-bi | 65 | specializations/power-bi | 70 | ~equal (verify) |
| nlp-generative-ai | 72 | specializations/nlp | 13 | **path much richer** |
| mlops-engineering | 59 | specializations/mlops-ai-deployment | 118 | canonical |

- Where **canonical is richer** (CV, DL, ML, MLOps): safe to reference canonical and retire the
  path copy — **after** a spot content check.
- Where **path is richer** (nlp-generative-ai): the path version should likely become (or merge
  into) the canonical `nlp` / `generative-ai-llms` course. Needs a merge decision.
- Where **~equal** (power-bi): compare and pick one canonical.

## C. `data-science-learning-path` — 14 orphan courses (NO canonical home) → SAFE to promote

These exist **only** in the learning path, so moving them to `technologies/` is a pure relocation
with zero data-loss risk:

`data-analytics`, `data-science`, `tableau`, `excel-data-analysis`, `cloud-ai-services`,
`big-data-fundamentals`, `apache-spark`, `apache-airflow`, `mlflow`, `kubeflow`,
`data-warehousing`, `snowflake`, `feature-engineering`, `data-visualization`.

> Note: `data-science` (1075 lesson files) and `data-analytics`/`mlops-engineering` have very large
> syllabi in an older note-dump format; relocation preserves them but a later quality pass is advised.

## Recommended safe execution order

1. **Promote the 14 orphans** (Section C) to `technologies/` — non-destructive, do now on approval.
2. **Merge, don't delete** the frontend-development authored notes into canonical `technologies/`
   (Section A).
3. **Per-course decision** for the 6 overlaps (Section B) — keep the richer side as canonical.
4. Only after 1–3, remove the emptied `SYLLABUS/`/`CURRICULUM/` from both learning paths and add
   `referenced_courses.md`.

**No files have been moved or deleted yet.**
