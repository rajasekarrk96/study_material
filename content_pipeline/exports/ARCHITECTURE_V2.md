# Learning OS v2 Architecture Specification

_Standardized Architecture & Curriculum Hierarchy_  
**Version:** 2.0.0  
**Status:** Frozen Authoritative Standard  

---

## 1. Executive Summary & Core Philosophy

The **Learning OS** is a modular, component-driven educational knowledge graph designed to scale technical education across computer science, artificial intelligence, data engineering, IoT, and software development.

### Core Axiom: "Teach Once. Reuse Everywhere."

Traditional curriculum design suffers from massive redundancy: every course attempts to teach its prerequisites from scratch (e.g., teaching Python in Data Science, teaching Python in Machine Learning, teaching Python in Web Development, and teaching Python in IoT). This creates:
1. **Maintenance Drift:** Inconsistent explanations, outdated syntax, and divergent best practices across courses.
2. **Cognitive Fatigue:** Students waste time re-learning setup, syntax, and foundational primitives.
3. **Bloated Repositories:** Redundant notes, duplicated exercises, and conflicting syllabus structures.

**Learning OS v2 enforces a strictly decoupled Directed Acyclic Graph (DAG)** of courses. Every concept, tool, language, and framework is authored **once** as an authoritative canonical course and referenced everywhere as a dependency.

```mermaid
graph TD
    subgraph Tier 1: Foundations (22 Courses)
        F1[Core Python]
        F2[C / C++]
        F3[Core Java]
        F4[HTML5 / CSS3 / JavaScript]
        F5[Linux / Bash / Git]
        F6[SQL / MySQL]
        F7[Electronics / ESP32 / Arduino]
        F8[DS Math / Python DSA]
    end

    subgraph Tier 2: Technologies (55 Courses)
        T1[Flask / FastAPI / Django]
        T2[React / Bootstrap / jQuery]
        T3[Spring Boot / Hibernate]
        T4[Docker / Kubernetes / Jenkins / AWS]
        T5[PyTorch / TensorFlow / OpenCV]
        T6[MQTT / Firebase / STM32]
        T7[Postman / Playwright / Selenium]
        T8[REST API / Auth & JWT / Backend Concepts]
        T9[MongoDB / SQL Server / Snowflake]
        T10[Power BI / Tableau / Excel]
    end

    subgraph Tier 3: Specializations (12 Courses)
        S1[Computer Vision for Edge AI & IoT]
        S2[Generative AI & LLM Systems]
        S3[RAG Engineering & AI Agents]
        S4[MLOps & AI Deployment]
        S5[Machine Learning & Deep Learning]
        S6[TinyML & Basic ML for IoT]
        S7[IoT Projects & Full Stack Systems]
    end

    subgraph Tier 4: Learning Paths (10 Paths)
        LP1[AI Engineer Path]
        LP2[IoT Full Stack Path]
        LP3[Java Full Stack Path]
        LP4[Data Scientist Path]
        LP5[Python Full Stack Path]
        LP6[Data Analytics Path]
    end

    F1 --> T1 & T5
    F4 --> T2
    F3 --> T3
    F5 --> T4
    F6 --> T8 & T9
    F7 --> T6
    F8 --> S5

    T1 & T5 & T6 & F7 --> S1
    T5 & T1 & T8 --> S2
    S2 & T8 --> S3
    T4 & T5 & T1 --> S4
    T5 & F8 --> S5
    T6 & S5 --> S6
    T6 & T1 & F7 --> S7

    S1 & S2 & S3 & S4 --> LP1
    S1 & S6 & S7 & T6 --> LP2
    T3 & T8 & F4 --> LP3
    S5 & T9 & T10 --> LP4
    T1 & T8 & F4 --> LP5
    T9 & T10 & F1 --> LP6
```

---

## 2. Four-Tier Architecture Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                    TIER 4: LEARNING PATHS                   │
│   (Zero Teaching Content — Sequence & Milestone Maps Only)  │
│   Total: 10 Career Roadmaps                                 │
└──────────────────────────────┬──────────────────────────────┘
                               │ references
┌──────────────────────────────▼──────────────────────────────┐
│                  TIER 3: SPECIALIZATIONS                    │
│    (Integration Only — Integrates Multiple Prerequisites)   │
│    Total: 12 Domain Integrations & Capstones                │
└──────────────────────────────┬──────────────────────────────┘
                               │ depends on
┌──────────────────────────────▼──────────────────────────────┐
│                    TIER 2: TECHNOLOGIES                     │
│   (Single Tool/Framework Deep Dive — 1 Technology Canonical)│
│   Total: 55 Standalone Tools, Frameworks & Protocols        │
└──────────────────────────────┬──────────────────────────────┘
                               │ depends on
┌──────────────────────────────▼──────────────────────────────┐
│                    TIER 1: FOUNDATIONS                      │
│      (Zero Prerequisites — First-Principles Fundamentals)   │
│      Total: 22 Baseline Languages, Systems & Electronics    │
└─────────────────────────────────────────────────────────────┘
```

---

### Tier 1: Foundations (`exports/foundations/` — 22 Courses)

#### Purpose
Foundations teach first-principles programming languages, systems fundamentals, mathematics, and hardware baselines. They assume **zero prerequisite knowledge** and can be learned independently without any framework or tool dependency.

#### Cardinal Rules
1. **Zero Prior Knowledge:** A student can open any Foundation course on Day 1 and start immediately.
2. **No Upstream Dependencies:** A Foundation must NOT depend on any Technology or Specialization. It may depend only on another Foundation where pedagogically necessary (e.g. `python-dsa` depends on `core-python`; `css3` depends on `html5`).
3. **No Framework Contamination:** Does not teach frameworks, cloud providers, or proprietary tools.

#### Canonical Foundations (22 Courses)
- **Languages:** `core-python`, `c-programming`, `core-java`, `cpp`, `html5`, `css3`, `javascript`
- **Systems & Baselines:** `linux`, `bash`, `git`
- **Databases:** `mysql`
- **Mathematics & Data Structures:** `ds-math`, `python-dsa`
- **Hardware & Physical Baselines:** `electrical-fundamentals`, `electronics-basics`, `arduino`, `esp32`, `raspberry-pi`, `sensors-actuators`, `simulation`, `iot-hardware`, `advanced-components`

---

### Tier 2: Technologies (`exports/technologies/` — 55 Courses)

#### Purpose
Technologies provide comprehensive, standalone mastery of a **single** framework, tool, library, database platform, protocol, or engineering technology.

#### Cardinal Rules
1. **One Technology per Course:** Teaches ONE technology completely from installation to production patterns.
2. **Multi-Language Parity:** Multi-language tools (e.g. `selenium`) unify Python and Java bindings under one course.
3. **Canonical Singularity:** Each technology exists exactly once across the repository.
4. **No Monolithic Bundling:** Does not bundle multiple distinct technologies into one file.

#### Canonical Technologies (55 Courses)
- **Web Frontend:** `react`, `bootstrap`, `jquery`
- **Web Backend:** `flask`, `fastapi`, `django`, `servlet-jsp`, `spring`, `spring-boot`, `spring-mvc`, `spring-security`
- **Architecture & Security:** `rest-api`, `auth-jwt`, `backend-concepts`
- **Data & Distributed Engines:** `python-data-science`, `data-visualization`, `feature-engineering`, `data-warehousing`, `apache-spark`, `apache-airflow`, `snowflake`, `big-data-fundamentals`
- **Databases & BI Tools:** `mongodb`, `sql-server`, `tableau`, `power-bi`, `excel-data-analysis`
- **Infrastructure, DevOps & Cloud:** `docker`, `kubernetes`, `jenkins`, `aws`, `github-actions`, `iot-cloud`
- **AI/ML Core Libraries:** `pytorch`, `tensorflow`, `opencv`, `vector-databases`, `mlflow`, `kubeflow`, `cloud-ai-services`
- **Testing & QA Tools:** `manual-testing`, `selenium`, `playwright`, `postman`, `pytest`
- **Embedded & Hardware Technologies:** `embedded-c`, `stm32`, `mqtt`, `firebase`, `pcb`
- **Language Deep-Dives & Build Tools:** `advanced-python`, `basic-matlab`, `maven`, `prompt-engineering`

---

### Tier 3: Specializations (`exports/specializations/` — 12 Courses)

#### Purpose
Specializations combine multiple prerequisite Foundations and Technologies into an integrated, professional domain capability. They teach **system integration, architecture, cross-technology pipelines, and production engineering trade-offs**.

#### Canonical Specializations (12 Courses)
- `machine-learning` (Prereq: `core-python`, `python-data-science`, `ds-math`)
- `deep-learning` (Prereq: `machine-learning`, `pytorch` / `tensorflow`, `ds-math`)
- `computer-vision` (Prereq: `deep-learning`, `opencv`, `pytorch`)
- `computer-vision-iot` (Prereq: `computer-vision`, `raspberry-pi`, `esp32`, `mqtt`, `flask`)
- `nlp` (Prereq: `deep-learning`, `pytorch`)
- `generative-ai-llms` (Prereq: `deep-learning`, `nlp`, `pytorch`)
- `rag-engineering` (Prereq: `generative-ai-llms`, `core-python`, `vector-databases`)
- `ai-agents` (Prereq: `generative-ai-llms`, `rag-engineering`, `rest-api`)
- `mlops-ai-deployment` (Prereq: `machine-learning`, `docker`, `kubernetes`, `mlflow`, `fastapi`)
- `tinyml` (Prereq: `machine-learning`, `embedded-c`, `esp32`)
- `basic-ml-iot` (Prereq: `core-python`, `esp32`, `sensors-actuators`, `ds-math`)
- `iot-projects` (Prereq: `arduino`, `esp32`, `iot-cloud`, `mqtt`, `rest-api`, `core-python`)

---

### Tier 4: Learning Paths (`exports/learning_paths/` — 10 Paths)

#### Purpose
Learning Paths define end-to-end career roadmaps. They assemble Foundations, Technologies, and Specializations into linear, milestone-driven progressions.

#### Canonical Learning Paths (10 Paths)
1. `ai-engineer`
2. `data-analytics`
3. `data-scientist`
4. `devops-engineer`
5. `frontend-development`
6. `iot-full-stack`
7. `java-full-stack`
8. `ml-engineer`
9. `python-full-stack`
10. `qa-automation`
