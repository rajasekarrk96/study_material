# Learning OS v2 — Course Classification & Architecture Audit Report

_Audit Date: 2026-08-09 (Re-Audited)_  
_Scope: Complete Inventory of `exports/` (22 Foundations + 44 Technologies + 24 Specializations + 10 Learning Paths = 100 Folders)_  
_Standard: Learning OS Architecture v2.0_

---

## 1. Executive Summary

A rigorous, first-principles audit was conducted across all 100 folders in `content_pipeline/exports/`. The audit re-evaluated the categorization of every course against the strict Learning OS v2 model:
- **Foundations:** Must be zero-prerequisite fundamental languages, systems, mathematics, or hardware baselines learnable independently. Frameworks and platforms (Docker, K8s, Jenkins, AWS, Github Actions, IoT Cloud) are reclassified as Technologies.
- **Technologies:** Standalone tools, frameworks, libraries, platforms, databases, and protocols. Multi-language tools (Selenium) are unified into one canonical course.
- **Specializations:** Domain integrations combining multiple prerequisites into end-to-end pipelines.
- **Learning Paths:** Roadmaps referencing canonical slugs with zero teaching content.

---

## 2. Complete 100-Folder Master Classification Matrix

### Category 1: Current `exports/foundations/` (22 Folders)

| # | Current Folder | Course Title | Recommended Category | Recommended Target Slug | Action Required & Pedagogical Rationale |
|---|---|---|---|---|---|
| 1 | `advanced-components` | Advanced Electronic Components | **FOUNDATION** | `foundations/advanced-components` | **KEEP**: Pure hardware component baseline (sensors, displays, relays, optocouplers). Zero framework dependencies. |
| 2 | `arduino` | Arduino Microcontroller Fundamentals | **FOUNDATION** | `foundations/arduino` | **KEEP**: Foundational microcontroller hardware baseline. |
| 3 | `aws` | AWS Cloud Computing | **TECHNOLOGY** | `technologies/aws` | **RELOCATE**: Proprietary cloud infrastructure platform requiring Linux/Networking. Belongs in Technologies. |
| 4 | `bash` | Bash Shell Scripting | **FOUNDATION** | `foundations/bash` | **KEEP**: Foundational CLI shell scripting language. |
| 5 | `basic-ml-iot` | Basic Machine Learning for IoT | **SPECIALIZATION** | `specializations/tinyml` (Merge) | **MERGE & ARCHIVE**: Requires 6 prerequisites (Python, Arduino, ESP32, Sensors). Merge unique sensor ML topics into `specializations/tinyml`. |
| 6 | `docker` | Docker & Containerization | **TECHNOLOGY** | `technologies/docker` | **RELOCATE**: Containerization platform technology requiring Linux. Belongs in Technologies. |
| 7 | `ds-math` | Data Science Mathematics | **FOUNDATION** | `foundations/ds-math` | **KEEP**: Pure mathematics baseline (Linear algebra, calculus, probability, statistics). |
| 8 | `electrical-fundamentals` | Electrical Fundamentals | **FOUNDATION** | `foundations/electrical-fundamentals` | **KEEP**: First-principles physical circuits, Ohm's law, AC/DC. |
| 9 | `electronics-basics` | Electronics Basics | **FOUNDATION** | `foundations/electronics-basics` | **KEEP**: Analog and digital semiconductor electronics baseline. |
| 10 | `esp32` | ESP32 Embedded Systems | **FOUNDATION** | `foundations/esp32` | **KEEP**: Foundational microcontroller hardware baseline. |
| 11 | `git` | Git Version Control | **FOUNDATION** | `foundations/git` | **KEEP**: Foundational version control system for all engineering paths. |
| 12 | `github-actions` | GitHub Actions CI/CD | **TECHNOLOGY** | `technologies/github-actions` | **RELOCATE**: Proprietary CI/CD workflow platform. Belongs in Technologies. |
| 13 | `iot-cloud` | IoT Cloud Computing | **TECHNOLOGY** | `technologies/iot-cloud` | **RELOCATE**: Cloud IoT platform technologies (AWS IoT, Azure IoT, ThingsBoard). Requires ESP32/REST. Belongs in Technologies. |
| 14 | `iot-hardware` | IoT Hardware Architecture | **FOUNDATION** | `foundations/iot-hardware` | **KEEP**: Hardware buses (I2C, SPI, UART), pinouts, power design. |
| 15 | `iot-projects` | IoT Projects & Systems | **SPECIALIZATION** | `specializations/iot-projects` | **RELOCATE**: 120-hour multi-service integration capstone combining Arduino, ESP32, Cloud, and REST. Belongs in Specializations. |
| 16 | `jenkins` | Jenkins CI/CD Automation | **TECHNOLOGY** | `technologies/jenkins` | **RELOCATE**: CI/CD automation server tool. Belongs in Technologies. |
| 17 | `kubernetes` | Kubernetes Container Orchestration | **TECHNOLOGY** | `technologies/kubernetes` | **RELOCATE**: Distributed container orchestration platform. Belongs in Technologies. |
| 18 | `linux` | Linux System Fundamentals | **FOUNDATION** | `foundations/linux` | **KEEP**: Foundational operating system for all engineering. |
| 19 | `python-dsa` | Python Data Structures & Algorithms | **FOUNDATION** | `foundations/python-dsa` | **KEEP**: Foundational algorithms and data structures baseline. |
| 20 | `raspberry-pi` | Raspberry Pi Single-Board Computing | **FOUNDATION** | `foundations/raspberry-pi` | **KEEP**: Single-board computer hardware baseline. |
| 21 | `sensors-actuators` | Sensors & Actuators | **FOUNDATION** | `foundations/sensors-actuators` | **KEEP**: Hardware transducers, sensors, motors, servos. |
| 22 | `simulation` | Circuit & Hardware Simulation | **FOUNDATION** | `foundations/simulation` | **KEEP**: Virtual breadboarding and simulation baseline (Wokwi, Tinkercad). |

---

### Category 2: Current `exports/technologies/` (44 Folders)

| # | Current Folder | Course Title | Recommended Category | Recommended Target Slug | Action Required & Pedagogical Rationale |
|---|---|---|---|---|---|
| 23 | `advanced-python` | Advanced Python & Professional Practices | **TECHNOLOGY** | `technologies/advanced-python` | **KEEP**: Advanced language mechanics deep dive (memory model, decorators, metaclasses, async). |
| 24 | `apache-airflow` | Apache Airflow | **TECHNOLOGY** | `technologies/apache-airflow` | **KEEP**: Workflow orchestration platform technology. |
| 25 | `apache-spark` | Apache Spark | **TECHNOLOGY** | `technologies/apache-spark` | **KEEP**: Distributed big data processing engine. |
| 26 | `auth-jwt` | Authentication, Authorization & JWT | **TECHNOLOGY** | `technologies/auth-jwt` | **KEEP**: Canonical security & authentication architectural standard. |
| 27 | `big-data-fundamentals` | Big Data Fundamentals | **TECHNOLOGY** | `technologies/big-data-fundamentals` | **KEEP**: Hadoop ecosystem and distributed data concepts. |
| 28 | `bootstrap` | Bootstrap | **TECHNOLOGY** | `technologies/bootstrap` | **KEEP**: Standalone CSS responsive UI framework. |
| 29 | `c-object-oriented-programming` | C++ Object-Oriented Programming | **FOUNDATION** | `foundations/cpp` (Merge) | **MERGE & ARCHIVE**: Redundant fragment of C++. Merge OOP classes/templates into `foundations/cpp`; archive folder. |
| 30 | `c-programming` | C Programming | **FOUNDATION** | `foundations/c-programming` | **RELOCATE**: Zero-prerequisite systems programming language. Belongs in Foundations. |
| 31 | `cloud-ai-services` | Cloud AI Services | **TECHNOLOGY** | `technologies/cloud-ai-services` | **KEEP**: Pre-trained cloud AI APIs (AWS/GCP/Azure). |
| 32 | `core-java` | Core Java Programming | **FOUNDATION** | `foundations/core-java` | **RELOCATE & MERGE**: Zero-prerequisite language. Merge unique topics from `java` into canonical `foundations/core-java`. |
| 33 | `core-python` | Core Python Programming | **FOUNDATION** | `foundations/core-python` | **RELOCATE & MERGE**: Zero-prerequisite language. Merge unique topics from `python` into canonical `foundations/core-python`. |
| 34 | `cpp` | C++ Programming | **FOUNDATION** | `foundations/cpp` | **RELOCATE**: Foundational systems language. Merge `c-object-oriented-programming` into `foundations/cpp`. |
| 35 | `css3` | CSS3 Styling | **FOUNDATION** | `foundations/css3` | **RELOCATE**: Foundational web styling language. Belongs in Foundations. |
| 36 | `data-analytics` | Data Analytics Monolith | **LEARNING_PATH** | `learning_paths/data-analytics` | **DECOMPOSE & ARCHIVE**: 7,000-line monolith bundling 11 courses. Remove syllabus; keep roadmap definition in `learning_paths/data-analytics`. |
| 37 | `data-science` | Data Science Monolith | **LEARNING_PATH** | `learning_paths/data-scientist` | **DECOMPOSE & ARCHIVE**: 10,000-line monolith bundling 18 courses. Remove syllabus; keep roadmap definition in `learning_paths/data-scientist`. |
| 38 | `data-visualization` | Data Visualization | **TECHNOLOGY** | `technologies/data-visualization` | **KEEP**: Standalone Python visualization libraries (Matplotlib, Seaborn, Plotly). |
| 39 | `data-warehousing` | Data Warehousing & dbt | **TECHNOLOGY** | `technologies/data-warehousing` | **KEEP**: Dimensional modeling, cloud DWH concepts, and dbt. |
| 40 | `embedded-c` | Embedded C Programming | **TECHNOLOGY** | `technologies/embedded-c` | **BUG FIX**: Regenerate corrupted syllabus (currently contains HTML5 canvas/video) with true register/ISR microcontroller C topics. |
| 41 | `excel-data-analysis` | Excel for Data Analysis | **TECHNOLOGY** | `technologies/excel-data-analysis` | **KEEP**: Standalone spreadsheet analytics, Power Query, and Pivot Tables. |
| 42 | `fastapi` | FastAPI | **TECHNOLOGY** | `technologies/fastapi` | **KEEP**: Standalone modern Python async API framework. |
| 43 | `feature-engineering` | Feature Engineering | **TECHNOLOGY** | `technologies/feature-engineering` | **KEEP**: Standalone applied ML data transformation and feature stores. |
| 44 | `flask` | Flask | **TECHNOLOGY** | `technologies/flask` | **KEEP**: Standalone lightweight Python web framework. |
| 45 | `hibernate` | Hibernate & JPA | **TECHNOLOGY** | `technologies/hibernate` | **KEEP**: Standalone Java ORM and persistence framework. |
| 46 | `html5` | HTML5 Web Markup | **FOUNDATION** | `foundations/html5` | **RELOCATE**: Zero-prerequisite web structure baseline. Belongs in Foundations. |
| 47 | `java` | Java Duplicate | **FOUNDATION** | `foundations/core-java` (Merge) | **MERGE & ARCHIVE**: Duplicate of `core-java`. Merge unique topics into `foundations/core-java`; archive `java`. |
| 48 | `javascript` | JavaScript Programming | **FOUNDATION** | `foundations/javascript` | **RELOCATE**: Zero-prerequisite foundational web programming language. Belongs in Foundations. |
| 49 | `jquery` | jQuery | **TECHNOLOGY** | `technologies/jquery` | **KEEP**: Standalone JavaScript DOM manipulation library. |
| 50 | `kubeflow` | Kubeflow | **TECHNOLOGY** | `technologies/kubeflow` | **KEEP**: Cloud-native ML orchestration platform on Kubernetes. |
| 51 | `maven` | Maven | **TECHNOLOGY** | `technologies/maven` | **KEEP**: Standalone Java build and dependency management tool. |
| 52 | `mlflow` | MLflow | **TECHNOLOGY** | `technologies/mlflow` | **KEEP**: Standalone ML experiment tracking and registry platform. |
| 53 | `mongodb` | MongoDB | **TECHNOLOGY** | `technologies/mongodb` | **KEEP**: Standalone NoSQL document database. |
| 54 | `mysql` | MySQL Database | **FOUNDATION** | `foundations/mysql` | **RELOCATE**: Foundational relational SQL database. Belongs in Foundations. |
| 55 | `nlp-generative-ai` | NLP & GenAI Monolith | **SPECIALIZATIONS** | Decompose to Canonical | **DECOMPOSE & ARCHIVE**: 1,890-line monolith bundling 6 courses. Decompose; individual courses already exist in Specializations. |
| 56 | `python` | Python Duplicate | **FOUNDATION** | `foundations/core-python` (Merge) | **MERGE & ARCHIVE**: Duplicate of `core-python`. Merge unique topics into `foundations/core-python`; archive `python`. |
| 57 | `python-data-science` | Python for Data Science | **TECHNOLOGY** | `technologies/python-data-science` | **KEEP**: Standalone scientific Python stack (NumPy, Pandas, Scipy). |
| 58 | `react` | React | **TECHNOLOGY** | `technologies/react` | **KEEP**: Standalone frontend UI library. |
| 59 | `rest-api` | REST API Design & Development | **TECHNOLOGY** | `technologies/rest-api` | **KEEP**: Canonical REST architectural standard. |
| 60 | `servlet-jsp` | Servlet & JSP | **TECHNOLOGY** | `technologies/servlet-jsp` | **KEEP**: Standalone traditional Java server-side web technology. |
| 61 | `snowflake` | Snowflake | **TECHNOLOGY** | `technologies/snowflake` | **KEEP**: Standalone cloud data warehouse platform. |
| 62 | `spring` | Spring Framework Core | **TECHNOLOGY** | `technologies/spring` | **KEEP**: Standalone Spring IoC/DI container framework. |
| 63 | `spring-boot` | Spring Boot | **TECHNOLOGY** | `technologies/spring-boot` | **KEEP**: Standalone opinionated enterprise backend framework. |
| 64 | `spring-mvc` | Spring MVC | **TECHNOLOGY** | `technologies/spring-mvc` | **KEEP**: Standalone Spring web MVC layer. |
| 65 | `spring-security` | Spring Security | **TECHNOLOGY** | `technologies/spring-security` | **KEEP**: Standalone enterprise Java security framework. |
| 66 | `tableau` | Tableau | **TECHNOLOGY** | `technologies/tableau` | **KEEP**: Standalone enterprise BI and data visualization platform. |

---

### Category 3: Current `exports/specializations/` (24 Folders)

| # | Current Folder | Course Title | Recommended Category | Recommended Target Slug | Action Required & Pedagogical Rationale |
|---|---|---|---|---|---|
| 67 | `ai-agents` | AI Agents and Multi-Agent Systems | **SPECIALIZATION** | `specializations/ai-agents` | **KEEP**: Integrates LLMs, memory, tools, and multi-agent graph workflows. |
| 68 | `backend-concepts-work-package` | Backend Concepts | **TECHNOLOGY** | `technologies/backend-architecture` | **NORMALIZE**: Fix folder name; replace `.gdoc` artifact with clean markdown syllabus. |
| 69 | `basic-matlab` | Basic MATLAB Programming | **TECHNOLOGY** | `technologies/matlab` | **RELOCATE**: Standalone programming tool/environment. Move to Technologies. |
| 70 | `computer-vision` | Computer Vision & Visual Intelligence | **SPECIALIZATION** | `specializations/computer-vision` | **KEEP**: Integrates classical CV algorithms, CNNs, YOLO, and segmentation. |
| 71 | `computer-vision-iot` | Computer Vision for Edge AI & IoT | **SPECIALIZATION** | `specializations/computer-vision-iot` | **KEEP**: Gold standard specialization integrating CV, ESP32-CAM, RPi, MQTT, and Flask. |
| 72 | `deep-learning` | Deep Learning | **SPECIALIZATION** | `specializations/deep-learning` | **KEEP & CLEANUP**: Integrates neural network architectures, backprop, and optimization. Remove raw notes. |
| 73 | `firebase` | Firebase Platform | **TECHNOLOGY** | `technologies/firebase` | **SPLIT & RELOCATE**: Move to Technologies; strip bundled Auth/JWT & REST API modules. |
| 74 | `generative-ai-llms` | Generative AI and LLMs | **SPECIALIZATION** | `specializations/generative-ai-llms` | **KEEP**: Integrates Transformers, scaling laws, instruction tuning, PEFT, and quantization. |
| 75 | `java-selenium` | Java Selenium | **TECHNOLOGY** | `technologies/selenium` (Merge) | **MERGE & ARCHIVE**: Consolidate Java Selenium modules into canonical `technologies/selenium`. |
| 76 | `machine-learning` | Machine Learning | **SPECIALIZATION** | `specializations/machine-learning` | **KEEP**: Integrates statistics, Scikit-Learn algorithms, and validation pipelines. |
| 77 | `manual-testing` | Manual Software Testing | **TECHNOLOGY** | `technologies/manual-testing` | **RELOCATE**: Standalone testing methodology, STLC, test design. Move to Technologies. |
| 78 | `mlops-ai-deployment` | MLOps and AI Deployment | **SPECIALIZATION** | `specializations/mlops-ai-deployment` | **KEEP**: Integrates ML models, Docker, K8s, MLflow, and CI/CD serving pipelines. |
| 79 | `mqtt` | MQTT for IoT | **TECHNOLOGY** | `technologies/mqtt` | **RELOCATE**: Standalone IoT protocol and Mosquitto broker. Move to Technologies. |
| 80 | `nlp` | Natural Language Processing | **SPECIALIZATION** | `specializations/nlp` | **KEEP**: Integrates text processing, embeddings, sequence models, and transformers. |
| 81 | `pcb` | PCB Design | **TECHNOLOGY** | `technologies/pcb-design` | **RELOCATE**: Standalone hardware design tool/skill (EDA, schematics, Gerber). Move to Technologies. |
| 82 | `playwright` | Playwright | **TECHNOLOGY** | `technologies/playwright` | **RELOCATE**: Standalone modern browser automation technology. Move to Technologies. |
| 83 | `postman` | Postman / API Testing | **TECHNOLOGY** | `technologies/postman` | **RELOCATE**: Standalone API testing tool and Newman runner. Move to Technologies. |
| 84 | `power-bi` | Power BI | **TECHNOLOGY** | `technologies/power-bi` | **RELOCATE**: Standalone BI tool (Power Query, DAX, reports). Move to Technologies. |
| 85 | `prompt-engineering` | Prompt Engineering | **TECHNOLOGY** | `technologies/prompt-engineering` | **RELOCATE**: Standalone prompting methodology and techniques. Move to Technologies. |
| 86 | `rag-engineering` | RAG Engineering | **SPECIALIZATION** | `specializations/rag-engineering` | **KEEP**: Integrates LLMs, chunking, vector search, reranking, and Ragas evaluation. |
| 87 | `selenium` | Selenium Automation | **TECHNOLOGY** | `technologies/selenium` | **RELOCATE & CONSOLIDATE**: Canonical browser automation technology with Python and Java sections. |
| 88 | `sql-server` | SQL Server Enterprise Architecture | **TECHNOLOGY** | `technologies/sql-server` | **RELOCATE**: Standalone enterprise relational database platform. Move to Technologies. |
| 89 | `stm32` | STM32 Embedded Development | **TECHNOLOGY** | `technologies/stm32` | **RELOCATE**: Standalone ARM Cortex-M hardware platform and STM32CubeIDE. Move to Technologies. |
| 90 | `tinyml` | TinyML & Edge AI | **SPECIALIZATION** | `specializations/tinyml` | **KEEP & MERGE**: Integrates model quantization/pruning with MCU hardware. Merges `basic-ml-iot`. |

---

### Category 4: Current `exports/learning_paths/` (10 Folders)

| # | Current Folder | Path Title | Recommended Action | Notes & Prerequisite Sequence |
|---|---|---|---|---|
| 91 | `ai-engineer` | AI Engineer | **KEEP & UPDATE** | Pure roadmap: Python $\rightarrow$ Math $\rightarrow$ ML $\rightarrow$ DL $\rightarrow$ NLP/CV $\rightarrow$ GenAI $\rightarrow$ RAG $\rightarrow$ Agents $\rightarrow$ MLOps. |
| 92 | `data-science-learning-path` | Legacy Data Science Path | **CONSOLIDATE & ARCHIVE** | Legacy unformatted path. Consolidate into canonical `learning_paths/data-scientist`. |
| 93 | `data-scientist` | Data Scientist | **KEEP & UPDATE** | Canonical roadmap: Python $\rightarrow$ Math $\rightarrow$ Python DS $\rightarrow$ MySQL $\rightarrow$ Power BI $\rightarrow$ ML $\rightarrow$ DL. |
| 94 | `devops-engineer` | DevOps Engineer | **KEEP & UPDATE** | Canonical roadmap: Linux $\rightarrow$ Bash $\rightarrow$ Git $\rightarrow$ Docker $\rightarrow$ K8s $\rightarrow$ Jenkins $\rightarrow$ GH Actions $\rightarrow$ AWS. |
| 95 | `frontend-development` | Frontend Development | **KEEP & UPDATE** | Canonical roadmap: HTML5 $\rightarrow$ CSS3 $\rightarrow$ JavaScript $\rightarrow$ Bootstrap $\rightarrow$ React. |
| 96 | `iot-full-stack` | IoT Full Stack Engineering | **KEEP & UPDATE** | Canonical roadmap: Electronics $\rightarrow$ Arduino $\rightarrow$ ESP32 $\rightarrow$ MQTT $\rightarrow$ Flask $\rightarrow$ CV-IoT $\rightarrow$ TinyML $\rightarrow$ IoT Projects. |
| 97 | `java-full-stack` | Java Full Stack Engineering | **KEEP & UPDATE** | Canonical roadmap: Core Java $\rightarrow$ Git $\rightarrow$ MySQL $\rightarrow$ HTML/CSS/JS $\rightarrow$ Maven $\rightarrow$ Spring $\rightarrow$ Spring Boot $\rightarrow$ React. |
| 98 | `ml-engineer` | ML Engineer | **KEEP & UPDATE** | Canonical roadmap: Python $\rightarrow$ Math $\rightarrow$ Python DS $\rightarrow$ ML $\rightarrow$ DL $\rightarrow$ PyTorch $\rightarrow$ MLOps. |
| 99 | `python-full-stack` | Python Full Stack Engineering | **KEEP & UPDATE** | Canonical roadmap: Core Python $\rightarrow$ Git $\rightarrow$ MySQL $\rightarrow$ HTML/CSS/JS $\rightarrow$ REST $\rightarrow$ Auth $\rightarrow$ FastAPI/Flask $\rightarrow$ React. |
| 100 | `qa-automation` | QA Automation Engineer | **KEEP & UPDATE** | Canonical roadmap: Manual Testing $\rightarrow$ Python/Java $\rightarrow$ Git $\rightarrow$ Postman $\rightarrow$ Selenium $\rightarrow$ Playwright $\rightarrow$ CI/CD. |
