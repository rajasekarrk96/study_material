```yaml
schema_version: "2.0"
metadata:
  lesson_id: "HTML5-MOD07-LES02"
  course_slug: "course-01-html5"
  course_title: "Course 1: HTML5"
  module_slug: "mod-07-advanced-apis-storage"
  module_title: "Module 7 - HTML5 Advanced APIs & Storage Mechanisms"
  lesson_slug: "geolocation-and-device-apis"
  lesson_title: "Lesson 7.2 Geolocation & Device APIs"
  sort_order: 702

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 60

prerequisites:
  required_lesson_ids:
    - "HTML5-MOD07-LES01"
  required_skills:
    - "JavaScript Async Callbacks & Browser Permissions"

skills_acquired:
  - "Geolocation API Implementation (`getCurrentPosition`, `watchPosition`)"
  - "Coordinates Object Inspection (Latitude, Longitude, Accuracy)"
  - "Handling Geolocation Permissions & Error Codes"
  - "Device Orientation & Motion APIs (`DeviceOrientationEvent`)"

dependencies:
  software:
    - "VS Code"
  hardware: []

seo_and_social:
  meta_title: "HTML5 Geolocation API & Device Sensors (Orientation & Motion)"
  meta_description: "Master HTML5 Geolocation API: getCurrentPosition, watchPosition, GPS coordinates, permission handling, and Device Orientation sensors."
  keywords: ["Geolocation API", "navigator.geolocation", "getCurrentPosition", "watchPosition", "GPS Coordinates", "DeviceOrientation"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 7.2 Geolocation & Device APIs

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 7.1 Web Storage](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_01_html5/_01_17_web_storage_and_indexeddb.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Retrieve physical device coordinates using `navigator.geolocation.getCurrentPosition()`.
2. Track real-time position updates using `watchPosition()` and `clearWatch()`.
3. Handle permission models and error codes (`PERMISSION_DENIED`, `POSITION_UNAVAILABLE`, `TIMEOUT`).
4. Read accelerometer and gyroscope sensors via `DeviceOrientationEvent`.

---

## 2. Environment & Prerequisites [id: prerequisites]

Geolocation requires an **HTTPS** connection (or `localhost` for development).

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Geolocation API
Exposed via `navigator.geolocation`:

```javascript
navigator.geolocation.getCurrentPosition(
  (position) => {
    console.log(`Lat: ${position.coords.latitude}, Lng: ${position.coords.longitude}`);
    console.log(`Accuracy: ${position.coords.accuracy} meters`);
  },
  (error) => console.error(`Error Code: ${error.code}`),
  { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 }
);
```

### 3.2 Position & Error Objects
- **Coordinates**: `latitude`, `longitude`, `accuracy`, `altitude`, `speed`, `heading`.
- **Error Codes**:
  - `1`: `PERMISSION_DENIED`
  - `2`: `POSITION_UNAVAILABLE`
  - `3`: `TIMEOUT`

---

## 4. Architecture & Diagram Visualizations [id: diagram]

### Geolocation Permission Loop
```mermaid
flowchart TD
    App[App Calls getCurrentPosition] --> Check{HTTPS Context?}
    Check -->|No| Fail[Block Access]
    Check -->|Yes| Prompt[Prompt User for Location Permission]
    Prompt -->|Granted| ReturnCoords[Return GPS Coordinates]
    Prompt -->|Denied| ReturnError[Return PERMISSION_DENIED Error]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Geolocation Test</title>
</head>
<body>
  <button id="loc-btn">Get GPS Location</button>
  <p id="output"></p>

  <script>
    document.getElementById('loc-btn').addEventListener('click', () => {
      if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition((pos) => {
          document.getElementById('output').textContent = 
            `Latitude: ${pos.coords.latitude}, Longitude: ${pos.coords.longitude}`;
        });
      }
    });
  </script>
</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Fleet Management & Asset Tracking**: Uses `watchPosition()` to monitor vehicle location in real time.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Open code in Chrome $\rightarrow$ Click **Get GPS Location** $\rightarrow$ Allow browser permission.

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Geolocation Fails** | Origin is unencrypted HTTP. | Geolocation requires HTTPS in production. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Set `enableHighAccuracy: true`**: Recommended for hardware tracking apps.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why does Geolocation require HTTPS?
**Answer**: To protect user privacy and prevent MitM attackers from intercepting physical location data.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 7.2 Geolocation Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which method tracks continuous real-time location updates?",
      "options": ["getCurrentPosition()", "watchPosition()", "trackPosition()", "getPosition()"],
      "correct_answer_index": 1,
      "explanation": "watchPosition() continuously monitors location changes."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a real-time GPS tracking dashboard with Leaflet.js maps.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What method stops a continuous `watchPosition()` tracker?
**Back**: `navigator.geolocation.clearWatch(watchId)`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
navigator.geolocation.getCurrentPosition((pos) => console.log(pos.coords));
```
