# 07 — Folder Structure Report

**Generated:** 2026-08-04

---

## Canonical Folder Hierarchy

```
docs/
├── syllabus/          ← 33 master track files (_01_ to _33_)
├── curriculum/        ← 55 canonical subject folders (01- to 55-)
├── learning_paths/    ← Learning path definitions
├── archive/           ← Archived duplicate/legacy content
│   └── curriculum_duplicates/
└── reports/           ← All audit reports (this directory)
```

---

## Curriculum Folder Inventory

| # | Folder | Notes | Status |
| :---: | :--- | :---: | :---: |
| 1 | `01-c-programming` | 36 | 🟢 Rich |
| 2 | `02-cpp-programming` | 32 | 🟢 Rich |
| 3 | `03-git-version-control` | 57 | 🟢 Rich |
| 4 | `04-html5-essentials` | 95 | 🟢 Rich |
| 5 | `05-css3-styling` | 76 | 🟢 Rich |
| 6 | `06-bootstrap-framework` | 36 | 🟢 Rich |
| 7 | `07-jquery-library` | 24 | 🟡 Growing |
| 8 | `08-javascript-core` | 167 | 🟢 Rich |
| 9 | `09-python-core` | 118 | 🟢 Rich |
| 10 | `10-advanced-python` | 60 | 🟢 Rich |
| 11 | `11-java-core` | 212 | 🟢 Rich |
| 12 | `12-spring-boot` | 20 | 🟡 Growing |
| 13 | `13-mysql-database` | 65 | 🟢 Rich |
| 14 | `14-sql-server` | 74 | 🟢 Rich |
| 15 | `15-mongodb-nosql` | 26 | 🟡 Growing |
| 16 | `16-flask-backend` | 78 | 🟢 Rich |
| 17 | `17-fastapi-backend` | 75 | 🟢 Rich |
| 18 | `18-rest-api-design` | 30 | 🟢 Rich |
| 19 | `19-auth-jwt-security` | 30 | 🟢 Rich |
| 20 | `20-react-frontend` | 60 | 🟢 Rich |
| 21 | `21-selenium-automation` | 84 | 🟢 Rich |
| 22 | `22-linux-administration` | 50 | 🟢 Rich |
| 23 | `23-docker-containers` | 50 | 🟢 Rich |
| 24 | `24-electrical-fundamentals` | 15 | 🟡 Growing |
| 25 | `25-electronics-basics` | 20 | 🟡 Growing |
| 26 | `26-pcb-design` | 56 | 🟢 Rich |
| 27 | `27-embedded-c` | 60 | 🟢 Rich |
| 28 | `28-arduino-platform` | 50 | 🟢 Rich |
| 29 | `29-esp32-microcontroller` | 62 | 🟢 Rich |
| 30 | `30-raspberry-pi` | 15 | 🟡 Growing |
| 31 | `31-sensors-actuators` | 35 | 🟢 Rich |
| 32 | `32-mqtt-protocol` | 30 | 🟢 Rich |
| 33 | `33-stm32-firmware` | 25 | 🟡 Growing |
| 34 | `34-firebase-cloud` | 15 | 🟡 Growing |
| 35 | `35-tinyml-edge-ai` | 15 | 🟡 Growing |
| 36 | `36-iot-hardware` | 137 | 🟢 Rich |
| 37 | `37-iot-projects` | 24 | 🟡 Growing |
| 38 | `38-ds-math-statistics` | 24 | 🟡 Growing |
| 39 | `39-python-data-science` | 10 | 🟡 Growing |
| 40 | `40-power-bi` | 70 | 🟢 Rich |
| 41 | `41-machine-learning` | 214 | 🟢 Rich |
| 42 | `42-deep-learning` | 189 | 🟢 Rich |
| 43 | `43-computer-vision` | 144 | 🟢 Rich |
| 44 | `44-nlp-systems` | 144 | 🟢 Rich |
| 45 | `45-generative-ai-llms` | 142 | 🟢 Rich |
| 46 | `46-rag-engineering` | 117 | 🟢 Rich |
| 47 | `47-ai-agents` | 116 | 🟢 Rich |
| 48 | `48-mlops-ai-deployment` | 118 | 🟢 Rich |
| 49 | `49-prompt-engineering` | 79 | 🟢 Rich |
| 50 | `50-python-dsa` | 50 | 🟢 Rich |
| 51 | `51-dotnet-full-stack` | 0 | 🔴 Empty |
| 52 | `52-matlab-simulation` | 0 | 🔴 Empty |
| 53 | `53-cloud-computing` | 0 | 🔴 Empty |
| 54 | `54-software-testing` | 0 | 🔴 Empty |
| 55 | `55-database-technologies` | 0 | 🔴 Empty |

---

## Folder Structure Compliance

| Check | Result |
| :--- | :---: |
| All folders use kebab-case naming | ✅ Pass |
| All folders have sequential numbering | ✅ Pass |
| No gaps in folder numbering (01-55) | ✅ Pass |
| No duplicate subject folders | ⚠️ Issues found |
| All folders contain .md files | ⚠️ 5 empty folders |
| Archive directory exists | ✅ Pass |

---

## Folders Requiring Attention

### Empty Folders (5)
- `51-dotnet-full-stack` — needs content generation
- `52-matlab-simulation` — needs content generation
- `53-cloud-computing` — needs content generation
- `54-software-testing` — needs content generation
- `55-database-technologies` — needs content generation

### Duplicate Subject Folders (1)
- **python:** `09-python-core`, `10-advanced-python`, `39-python-data-science`, `50-python-dsa`
