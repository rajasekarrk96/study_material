# 19 — Security Architecture

> The Security Architecture safeguards student data, limits system load, and secures application keys.

---

## 19.1 Authentication & Session Architecture

Authentication features session-based controls for local access, alongside bearer tokens (JWT) to authenticate the REST API.

```
       ┌────────────────────────┐
       │   Authentication Flow  │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐ ┌──────────────────┐
│  Local Session   │ │ API Bearer Token │
├──────────────────┤ ├──────────────────┤
│ CSRF protection, │ │ PyJWT token tags,│
│ secure cookies   │ │ key validation   │
└──────────────────┘ └──────────────────┘
```

---

## 19.2 Rate Limiting Policies

To mitigate DDoS attacks and brute-force attempts, the platform implements rate limiting decorators using memory-backed caching (Redis):

- `POST /api/v1/auth/login`: Maximum 5 attempts per minute.
- `POST /api/v1/auth/register`: Maximum 3 attempts per IP per hour.
- `POST /api/v1/exercises/*/submit`: Maximum 10 runs per minute per user.
- General API routes: Maximum 60 requests per minute per IP.

---

## 19.3 Data Protection & Secret Key Cryptography

Secret tokens (such as password credentials, email tokens, or Judge0 sandbox API keys) are stored encrypted.

```python
# app/core/security.py

from cryptography.fernet import Fernet
import os

class CryptographyManager:
    def __init__(self, key: str = None):
        # Fallback to loading key from environment variable
        self.key = key or os.environ.get("ENCRYPTION_KEY")
        if not self.key:
            raise ValueError("No Encryption Key provided.")
        self.fernet = Fernet(self.key.encode())

    def encrypt_secret(self, raw_secret: str) -> str:
        """
        Encrypts key string to safe base64 bytes.
        """
        return self.fernet.encrypt(raw_secret.encode()).decode()

    def decrypt_secret(self, encrypted_secret: str) -> str:
        """
        Decrypts base64 bytes string back to plain string.
        """
        return self.fernet.decrypt(encrypted_secret.encode()).decode()
```

---

## 19.4 SQL Injection & XSS Guardrails
- **SQL Injection**: SQLAlchemy ORM queries parameters using parameterized attributes. Raw execution is prohibited.
- **XSS**: Jinja2 templates auto-escape output. Sections containing markdown content are rendered using structured HTML processors (such as Python's `markdown` library) combined with bleach sanitization libraries:

```python
import bleach
import markdown

def render_safe_markdown(raw_markdown: str) -> str:
    """
    Renders raw markdown content into sanitized HTML.
    """
    html = markdown.markdown(raw_markdown, extensions=['fenced_code', 'tables'])
    allowed_tags = bleach.sanitizer.ALLOWED_TAGS + [
        'pre', 'code', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'h1', 'h2', 'h3', 'p', 'span'
    ]
    allowed_attrs = {
        'code': ['class'],
        'span': ['class'],
        **bleach.sanitizer.ALLOWED_ATTRIBUTES
    }
    return bleach.clean(html, tags=allowed_tags, attributes=allowed_attrs)
```
