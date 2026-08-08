# Duplicate / Overlapping Courses Report

_Generated: 2026-08-08 — Learning OS Content Pipeline audit_

Courses that appear under multiple categories or overlap heavily. Per rules, duplicates are REPORTED (with recommendations) — not auto-merged unless a true duplicate.

## Exact-name matches across categories

| Normalized Name | Occurrences | Recommendation |
|---|---|---|
| bootstrap | technologies/bootstrap, learning_paths/bootstrap | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| computervision | specializations/computer-vision, learning_paths/computer-vision | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| css3 | technologies/css3, learning_paths/css3 | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| deep | specializations/deep-learning, learning_paths/deep-learning | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| html5 | technologies/html5, learning_paths/html5 | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| javascript | technologies/javascript, learning_paths/javascript | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| jquery | technologies/jquery, learning_paths/jquery | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| machine | specializations/machine-learning, learning_paths/machine-learning | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| powerbi | specializations/power-bi, learning_paths/power-bi | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |
| react | technologies/react, learning_paths/react | Likely intentional (learning-path bundle re-uses the technology). Keep canonical in `technologies`, reference from paths. |

## Conceptual overlaps to review (manual judgement)

| Overlap | Note |
|---|---|
| linux vs bash | Linux includes a Bash automation module; Bash is a standalone course — verify no duplicated lessons. |
| arduino vs esp32 | Both cover GPIO/communication basics — ensure ESP32 focuses on WiFi/BLE, Arduino on fundamentals. |
| iot-hardware vs advanced-components | Overlap on sensors/actuators/power — keep component depth in advanced-components. |
| sensors-actuators vs electronics-basics | Sensor interfacing overlap — electronics-basics stays at component theory. |
| machine-learning (spec) vs basic-ml-iot (found) | Different depth/audience — keep both, cross-link prerequisites. |
| computer-vision (spec) vs computer-vision-iot (spec) | CV-IoT is edge-deployment focused — verify divergence. |
| html5/css3/javascript/react | Present in technologies AND learning_paths/frontend-development — path bundles reference tech canon. |
