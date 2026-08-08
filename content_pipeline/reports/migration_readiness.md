# Migration Readiness Report

_Generated: 2026-08-08 — Learning OS Export Pipeline standardization_

## Migration Ready: **NO** (close — architecture is clean; content-format polish remains)

### ✅ Resolved this session
- **Learning-path architecture compliant:** neither `frontend-development` nor
  `data-science-learning-path` owns any SYLLABUS/CURRICULUM. Both now have
  `referenced_courses.md` (+ roadmap) pointing to canonical courses. **LP violations: 0.**
- **14 orphan courses promoted** to `technologies/` (canonical single location) with metadata + README.
- **frontend-development authored notes merged** into canonical `technologies/` (html5, css3,
  javascript, react, bootstrap, jquery) — replaced empty scaffolds; no content lost.
- **`nlp-generative-ai` promoted** to `technologies/` (richer/unique than `specializations/nlp`).
- **5 overlap copies removed** (computer-vision, deep-learning, machine-learning, power-bi,
  mlops-engineering) — verified **strict subsets** of their specializations canonical (0 unique files),
  now referenced.
- **Missing assets: 0.** Generated CURRICULUM structure for the 7 courses that lacked it
  (github-actions, computer-vision-iot, firebase, java-selenium, playwright, postman, selenium).
- **Decision recorded:** ML/DL/NLP/CV/Power BI **stay in `specializations/`** (owner's call).

### Remaining before **YES**
1. **~29 courses below 90/100 health** — architecture is correct, but their **syllabi are still in the
   older (non-Foundation) format** and/or their **curriculum is flat** (no `module.md`, not modularized).
   This covers: the 14 promoted data-science courses (flat curriculum), the 7 newly-scaffolded courses,
   and the remaining non-Foundation specialization syllabi (selenium, playwright, postman, java-selenium,
   firebase, computer-vision-iot, sql-server, backend-concepts).
   **Fix:** convert these syllabi to Foundation format (preserving content) and modularize curriculum —
   same process already applied to all 29 `technologies` courses.
2. **1 intentional overlap:** `technologies/nlp-generative-ai` vs `specializations/nlp` +
   `specializations/generative-ai-llms` — reconcile canonical scope (kept for now to avoid content loss).
3. **`data-science` quality:** oversized flat curriculum (1075 files, note-dump format) needs a
   restructure/dedup pass.

### Recommended next sequence
1. Convert the remaining non-Foundation syllabi to Foundation format (batch, content-preserving).
2. Modularize the flat promoted curricula (add `module.md`, group lessons into modules).
3. Reconcile the `nlp-generative-ai` scope decision.
4. Re-run the audit until Migration Ready = YES.

_All originals are git-tracked and recoverable. No Learning OS / imports / completed content was touched._
