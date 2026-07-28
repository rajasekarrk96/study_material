```yaml
schema_version: "2.0"
metadata:
  lesson_id: "FLK-MOD10-LES03"
  course_slug: "course-04-flask"
  course_title: "Course 4: Flask Backend & Microservices"
  module_slug: "mod-10-advanced-extensions-celery"
  module_title: "Module 10 - Advanced Flask Extensions & Background Tasks"
  lesson_slug: "email-delivery-with-flask-mail"
  lesson_title: "Lesson 10.3 Email Delivery with Flask-Mail"
  sort_order: 1003

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "FLK-MOD10-LES02"
  required_skills:
    - "Flask Application Factory & Celery Background Tasks"

skills_acquired:
  - "Integrating Flask-Mail Extension (`Mail(app)`)"
  - "Configuring SMTP Server Settings (`MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`)"
  - "Constructing HTML & Plaintext Messages (`Message()`)"
  - "Asynchronous Email Delivery via Celery Tasks"

dependencies:
  software:
    - "VS Code"
    - "Python 3.12+"
    - "Flask-Mail"
  hardware: []

seo_and_social:
  meta_title: "Flask Email Delivery: Flask-Mail, SMTP Config & Asynchronous Celery Emails"
  meta_description: "Master Email Delivery in Flask: Flask-Mail extension, SMTP server configuration, constructing HTML Message objects, and sending emails asynchronously with Celery."
  keywords: ["Flask-Mail", "Flask Email", "SMTP Config", "Message Object", "Asynchronous Email", "Flask Celery Email", "Python Email"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 10.3 Email Delivery with Flask-Mail

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 10.2 Celery Tasks](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_04_flask/_04_23_asynchronous_background_tasks_with_celery.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Integrate the **Flask-Mail** extension.
2. Configure SMTP server credentials securely via environment variables.
3. Construct plain-text and HTML emails using `Message()`.
4. Send emails asynchronously using **Celery** background tasks to prevent request blocking.

---

## 2. Environment & Prerequisites [id: prerequisites]

Install `Flask-Mail`:

```bash
pip install Flask-Mail
```

---

## 3. Theoretical Foundations [id: theory]

### 3.1 SMTP Protocol & Synchronous vs Async Delivery
The **Simple Mail Transfer Protocol (SMTP)** is the standard protocol for sending emails. Connecting to an external SMTP server (SendGrid, Mailgun, AWS SES, Gmail) involves network handshakes and TLS encryption, taking anywhere from 1 to 3 seconds per email.

Synchronous email delivery during an HTTP request blocks the user experience. Combining **Flask-Mail** with **Celery** background tasks ensures instant HTTP responses while emails send in the background:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ASYNCHRONOUS EMAIL DELIVERY FLOW                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ HTTP Request ──► `send_async_email.delay(to, subject, body)`               │
│              ──► Immediate 200 OK to User!                                  │
│                                                                             │
│ Celery Worker ──► Opens SMTP Socket ──► Sends `Message` via Flask-Mail      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    User[User Registers] --> App[Flask App View]
    App -->|send_email.delay| Celery[Celery Background Task]
    App -->|Redirects to Dashboard| User
    Celery -->|Opens TLS Socket| SMTP[External SMTP Server: SendGrid / SES]
    SMTP --> Inbox[Delivers HTML Email to User Inbox]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```python
# Flask-Mail & Asynchronous Celery Email Delivery (mail_demo.py)
import os
from flask import Flask, jsonify, render_template
from flask_mail import Mail, Message
from celery import shared_task

app = Flask(__name__)

# 1. SMTP Server Configuration
app.config.update(
    MAIL_SERVER=os.environ.get("MAIL_SERVER", "smtp.gmail.com"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT", 587)),
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=os.environ.get("MAIL_DEFAULT_SENDER", "noreply@telemetry.io")
)

mail = Mail(app)

# 2. Celery Asynchronous Email Task
@shared_task(ignore_result=True)
def send_async_email(to_email, subject, html_body):
    # Note: Requires app context binding!
    msg = Message(
        subject=subject,
        recipients=[to_email],
        html=html_body
    )
    mail.send(msg)
    print(f"[Async Email Sent]: Delivered to {to_email}")

# 3. View Function triggering Async Email
@app.route("/api/v1/alert-email", methods=["POST"])
def trigger_alert_email():
    user_email = "operator@factory.com"
    subject = "HIGH TEMPERATURE ALERT: ESP32-A1"
    html_content = "<h1>Critical Alert</h1><p>Sensor ESP32-A1 exceeded 80.0°C!</p>"

    # Dispatch to Celery worker (Non-blocking!)
    send_async_email.delay(user_email, subject, html_content)

    return jsonify({"message": "Alert email queued for background delivery"}), 200
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **User Password Resets & Alarm Notifications**: Web applications dispatch password reset tokens and IoT critical threshold alert emails asynchronously to guarantee instantaneous user interface feedback.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `mail_demo.py`.
2. Set environment variables `MAIL_USERNAME` and `MAIL_PASSWORD`.
3. Trigger `/api/v1/alert-email` endpoint $\to$ Inspect background email delivery log!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`SMTPServerDisconnected`** | Incorrect SMTP port or TLS configuration (e.g., using TLS on port 465 instead of SSL). | Use Port 587 for TLS (`MAIL_USE_TLS=True`) or Port 465 for SSL (`MAIL_USE_SSL=True`). |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Never Hardcode SMTP Credentials**: Load passwords securely from environment variables using `os.environ.get()`.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why is it crucial to send emails asynchronously in web applications?
**Answer**: Connecting to external SMTP mail servers introduces unpredictable network latency (1–5 seconds per email). Sending emails synchronously inside a web view function blocks the web server worker thread, creating laggy user interfaces and risking browser timeout errors. Offloading email delivery to asynchronous background workers (like Celery) keeps HTTP request-response cycles instantaneous.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 10.3 Flask-Mail Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which standard SMTP port is commonly used for TLS-encrypted email connections?",
      "options": ["25", "80", "587", "443"],
      "correct_answer_index": 2,
      "explanation": "Port 587 is the standard port for TLS SMTP connections."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an automated welcome email task dispatched upon user registration.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What class in Flask-Mail constructs plain-text or HTML email objects?
**Back**: `flask_mail.Message()`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```python
msg = Message("Subject", recipients=["a@b.com"], html="<b>Hi</b>")
mail.send(msg)
```
