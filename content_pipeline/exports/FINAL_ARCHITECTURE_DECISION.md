# Final Architecture Decision & Inventory Freeze (`FINAL_ARCHITECTURE_DECISION.md`)

_Decision Date: 2026-08-09_  
_Status: ARCHITECTURAL DECISION RECORD (ADR) — Frozen Baseline_  
_Scope: Authoritative Freeze of Course Inventory in `content_pipeline/exports/`_

---

## 1. Executive Answers to the 10 Core Architectural Questions

### Question 1: What is the final number of Foundations?
- **Answer:** Exactly **22 Canonical Foundations**.
- **Verification:** Every course satisfies the zero-prerequisite, zero-framework constraint. Permissible Foundation-to-Foundation prerequisites (`python-dsa` $\rightarrow$ `core-python`; `css3` $\rightarrow$ `html5`) are verified.

### Question 2: What is the final number of Technologies?
- **Answer:** Exactly **55 Canonical Technologies**.
- **Verification:** Every course teaches one standalone tool, framework, platform, database, or protocol. Multi-language bindings (`selenium`) are unified.

### Question 3: What is the final number of Specializations?
- **Answer:** Exactly **12 Canonical Specializations**.
- **Verification:** Every course integrates multiple prerequisite Foundations and Technologies into professional domain workflows without reteaching baseline syntax.

### Question 4: What is the final number of Learning Paths?
- **Answer:** Exactly **9 Active Canonical Roadmaps** (with 1 planned optional roadmap: `data-analytics`).
- **Verification:** Every path is strictly a sequence roadmap with zero embedded teaching content.

### Question 5: Which courses were investigated as questionable, and what is the ruling?
1. **`prompt-engineering`:**
   - *Ruling:* **REMAIN IN TECHNOLOGIES (`technologies/prompt-engineering`).**
   - *Rationale:* Prompt engineering is a standalone toolset (prompt construction, DSPy, structured outputs) applicable across frontend, backend, QA, and AI engineering tracks. Classifying it as a Technology allows it to be reused as a dependency across `generative-ai-llms`, `rag-engineering`, and `ai-agents` without DAG inversion.
2. **`backend-concepts`:**
   - *Ruling:* **REMAIN IN TECHNOLOGIES (`technologies/backend-concepts`).**
   - *Rationale:* Teaches universal backend principles (HTTP wire level, routing engines, DTO serialization, connection pooling, graceful shutdown). It is a standalone core discipline course.
3. **`basic-matlab`:**
   - *Ruling:* **REMAIN IN TECHNOLOGIES (`technologies/basic-matlab`).**
   - *Rationale:* Standalone technical computing tool for engineers.
4. **`iot-projects`:**
   - *Ruling:* **REMAIN IN SPECIALIZATIONS (`specializations/iot-projects`).**
   - *Rationale:* 120-hour multi-service capstone integrating hardware, cloud, database, web dashboard, and security.

### Question 6: Which courses are duplicates, and where are they?
- **Confirmed Duplicates (Safely Archived in `exports/archive/duplicate_courses/`):**
  1. `python` $\rightarrow$ Merged into canonical `foundations/core-python`.
  2. `java` $\rightarrow$ Merged into canonical `foundations/core-java`.
  3. `c-object-oriented-programming` $\rightarrow$ Merged into canonical `foundations/cpp`.
  4. `java-selenium` $\rightarrow$ Consolidated into canonical `technologies/selenium`.
  5. `data-science-learning-path` $\rightarrow$ Unified into canonical `learning_paths/data-scientist`.

### Question 7: Which courses should remain separate?
1. **`basic-ml-iot` and `tinyml`:**
   - *Decision:* **REMAIN SEPARATE.**
   - *Rationale:* `basic-ml-iot` (60 hours) is an applied sensor ML & anomaly detection specialization for IoT developers using Scikit-Learn pipelines. `tinyml` (10–20 hours) is a bare-metal deep learning model compression specialization (quantization, pruning, memory arenas) for ultra-low-power microcontrollers.
2. **`computer-vision` and `computer-vision-iot`:**
   - *Decision:* **REMAIN SEPARATE.**
   - *Rationale:* `computer-vision` covers algorithmic CNNs, YOLO, and segmentation on server/cloud GPU environments. `computer-vision-iot` covers edge deployment, RTSP camera feeds on Raspberry Pi/ESP32-CAM, and MQTT alerting.
3. **`machine-learning` and `deep-learning`:**
   - *Decision:* **REMAIN SEPARATE.**
   - *Rationale:* Distinct mathematical and algorithmic domains (classical statistical learning vs gradient-based neural representations).

### Question 8: Which courses should eventually merge?
- **Decision:** None in the active canonical set. All necessary merges (`python` into `core-python`, `java` into `core-java`, `c-oop` into `cpp`, `java-selenium` into `selenium`) have been completed and verified.

### Question 9: Which Learning Paths are missing or recommended?
- **`data-analytics`:** Currently, `learning_paths/data-scientist` covers full-stack data science including deep learning and Python algorithms. A dedicated `learning_paths/data-analytics` path (focusing on Excel, SQL, Tableau, Power BI, Python DS, and Feature Engineering without Deep Learning/MLOps) can be created as a pure roadmap when desired.

### Question 10: Which documentation files must be updated to align with the final frozen numbers?
- Update `ARCHITECTURE_V2.md`, `COURSE_CLASSIFICATION_REPORT.md`, and `MIGRATION_PLAN.md` to reflect the authoritative frozen counts: **22 Foundations, 55 Technologies, 12 Specializations, 9 Learning Paths**.

---

## 2. Frozen Authoritative Course Inventory (89 Canonical Courses + 9 Learning Paths)

```
┌─────────────────────────────────────────────────────────────────────────┐
│              LEARNING OS v2 — AUTHORITATIVE FROZEN INVENTORY            │
├─────────────────────────────────────────────────────────────────────────┤
│ Tier 1: Foundations (22 Courses)                                        │
│  1. advanced-components        12. esp32                                │
│  2. arduino                    13. git                                  │
│  3. bash                       14. html5                                │
│  4. c-programming              15. iot-hardware                         │
│  5. core-java                  16. javascript                           │
│  6. core-python                17. linux                                │
│  7. cpp                        18. mysql                                │
│  8. css3                       19. python-dsa                           │
│  9. ds-math                    20. raspberry-pi                         │
│ 10. electrical-fundamentals    21. sensors-actuators                    │
│ 11. electronics-basics         22. simulation                           │
├─────────────────────────────────────────────────────────────────────────┤
│ Tier 2: Technologies (55 Courses)                                       │
│  1. advanced-python            29. maven                                │
│  2. apache-airflow             30. mlflow                               │
│  3. apache-spark               31. mongodb                              │
│  4. auth-jwt                   32. mqtt                                 │
│  5. aws                        33. opencv                               │
│  6. backend-concepts           34. pcb                                  │
│  7. basic-matlab               35. playwright                           │
│  8. big-data-fundamentals      36. postman                              │
│  9. bootstrap                  37. power-bi                             │
│ 10. cloud-ai-services          38. prompt-engineering                   │
│ 11. data-visualization         39. pytest                               │
│ 12. data-warehousing           40. python-data-science                  │
│ 13. django                     41. pytorch                              │
│ 14. docker                     42. react                                │
│ 15. embedded-c                 43. rest-api                             │
│ 16. excel-data-analysis        44. selenium                             │
│ 17. fastapi                    45. servlet-jsp                          │
│ 18. feature-engineering        46. snowflake                            │
│ 19. firebase                   47. spring                               │
│ 20. flask                      48. spring-boot                          │
│ 21. github-actions             49. spring-mvc                           │
│ 22. hibernate                  50. spring-security                      │
│ 23. iot-cloud                  51. sql-server                           │
│ 24. jenkins                    52. stm32                                │
│ 25. jquery                     53. tableau                              │
│ 26. kubeflow                   54. tensorflow                           │
│ 27. kubernetes                 55. vector-databases                     │
│ 28. manual-testing                                                      │
├─────────────────────────────────────────────────────────────────────────┤
│ Tier 3: Specializations (12 Courses)                                    │
│  1. ai-agents                   7. iot-projects                         │
│  2. basic-ml-iot                8. machine-learning                     │
│  3. computer-vision             9. mlops-ai-deployment                  │
│  4. computer-vision-iot        10. nlp                                  │
│  5. deep-learning              11. rag-engineering                     │
│  6. generative-ai-llms         12. tinyml                               │
├─────────────────────────────────────────────────────────────────────────┤
│ Tier 4: Learning Paths (9 Career Roadmaps)                              │
│  1. ai-engineer                 6. java-full-stack                      │
│  2. data-scientist              7. ml-engineer                          │
│  3. devops-engineer             8. python-full-stack                    │
│  4. frontend-development        9. qa-automation                        │
│  5. iot-full-stack                                                      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Next Operational Phase: Authorization Gate

With this reconciliation and DAG audit complete:
1. **The physical course hierarchy in `content_pipeline/exports/` is 100% frozen.**
2. **The inventory is ready for note generation according to canonical syllabuses.**
3. **No further structural file moves are required.**
