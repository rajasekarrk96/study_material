"""
phase2_upgrade.py
─────────────────────────────────────────────────────────────────
Phase 2 — Complete near-done courses + fix ML structure:
  1. Fix _23_machine_learning supervised_learning nested dirs
  2. Fix ML module folder prefixes (still show _10_ inside _23_)
  3. Flask — fill 6 remaining stubs with content
  4. FastAPI — fill 13 remaining stubs with content
  5. MySQL — fill 12 remaining stubs with content
  6. Python — add 39 proper stubs with detailed topic lists
"""
import os, shutil

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'

# ══════════════════════════════════════════════════════════════════
# FIX 1: Flatten ML supervised_learning nested sub-dirs
# ══════════════════════════════════════════════════════════════════
print("=" * 60)
print("FIX 1: Flatten _23_machine_learning supervised_learning")
print("=" * 60)

ml_path = os.path.join(BASE, "_23_machine_learning")
sup_path = os.path.join(ml_path, "_10_06_supervised_learning")

if os.path.exists(sup_path):
    for subdir in os.listdir(sup_path):
        sdp = os.path.join(sup_path, subdir)
        if os.path.isdir(sdp):
            for fn in os.listdir(sdp):
                src = os.path.join(sdp, fn)
                dst = os.path.join(sup_path, fn)
                if fn.endswith('.md') and not os.path.exists(dst):
                    shutil.move(src, dst)
                    print(f"  [MOVE] {subdir}/{fn} -> {fn}")
            remaining = [f for f in os.listdir(sdp)]
            if not remaining:
                os.rmdir(sdp)
                print(f"  [RMDIR] {subdir}")
    print("  Done.")
else:
    print("  Path not found:", sup_path)

# ══════════════════════════════════════════════════════════════════
# FIX 2: Rename ML module folders from _10_XX to _23_XX
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 2: Rename ML module folder prefixes _10_ -> _23_")
print("=" * 60)

ML_MODULE_RENAMES = {
    "_10_01_foundations":               "_23_01_foundations",
    "_10_02_mathematics_for_ml":        "_23_02_mathematics_for_ml",
    "_10_03_data_preparation":          "_23_03_data_preparation",
    "_10_04_feature_engineering":       "_23_04_feature_engineering",
    "_10_05_model_evaluation":          "_23_05_model_evaluation",
    "_10_06_supervised_learning":       "_23_06_supervised_learning",
    "_10_07_unsupervised_learning":     "_23_07_unsupervised_learning",
    "_10_08_semi_supervised_learning":  "_23_08_semi_supervised_learning",
    "_10_09_reinforcement_learning":    "_23_09_reinforcement_learning",
    "_10_10_ensemble_learning":         "_23_10_ensemble_learning",
    "_10_11_explainable_ai":            "_23_11_explainable_ai",
    "_10_12_automl":                    "_23_12_automl",
    "_10_13_mlops_for_ml":              "_23_13_mlops_for_ml",
    "_10_14_industry_projects":         "_23_14_industry_projects",
}

TEMP = "_TEMP_ML_"
# Phase A: temp
for old, new in ML_MODULE_RENAMES.items():
    op = os.path.join(ml_path, old)
    tp = os.path.join(ml_path, TEMP + old)
    if os.path.exists(op):
        os.rename(op, tp)

# Phase B: final
for old, new in ML_MODULE_RENAMES.items():
    tp = os.path.join(ml_path, TEMP + old)
    np = os.path.join(ml_path, new)
    if os.path.exists(tp):
        if not os.path.exists(np):
            os.rename(tp, np)
            print(f"  [RENAME] {old} -> {new}")
        else:
            print(f"  [SKIP]   {new} already exists")

print("  Done.")


# ══════════════════════════════════════════════════════════════════
# HELPER: Write a file with full content (not just stub)
# ══════════════════════════════════════════════════════════════════
written = 0

def write_lesson(path, content):
    global written
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [WRITE] {os.path.basename(path)}")
    written += 1

def frontmatter(lid, title, course, mod, mod_title, les, diff, tags, duration=60):
    tag_str = ", ".join(f'"{t}"' for t in tags)
    return f"""---
id: "{lid}"
title: "{title}"
course: "{course}"
module: {mod}
module_title: "{mod_title}"
lesson: {les}
version: "2.0"
difficulty: "{diff}"
duration_minutes: {duration}
tags: [{tag_str}]
prerequisites: []
lab_required: true
---

"""

# ══════════════════════════════════════════════════════════════════
# FIX 3: Flask — fill 6 remaining stubs
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 3: Flask — filling 6 remaining stubs")
print("=" * 60)

FK = os.path.join(BASE, "_14_flask")

write_lesson(os.path.join(FK, "_04_29_flask_response_objects_and_streaming.md"),
frontmatter("04_29","Flask Response Objects and Streaming","Flask",4,"Advanced Flask Patterns",29,"advanced",["Response","make-response","headers","mimetype","stream-with-context","stream_template","chunked","SSE","server-sent-events"]) + """
# Flask Response Objects and Streaming

## Topics Covered

### 1. Response Object Basics
- `make_response()` — creating custom response objects
- Setting headers: `response.headers['X-Custom'] = 'value'`
- Setting cookies: `response.set_cookie('key', 'val', httponly=True)`
- Status codes and MIME types
- `Response(content, status, headers, mimetype)`

### 2. Streaming Responses
```python
from flask import Response, stream_with_context
import time

def generate():
    for i in range(10):
        yield f"data: Line {i}\\n\\n"
        time.sleep(0.5)

@app.route('/stream')
def stream():
    return Response(stream_with_context(generate()),
                    mimetype='text/event-stream')
```

### 3. Server-Sent Events (SSE)
```python
@app.route('/events')
def events():
    def event_stream():
        while True:
            data = get_new_data()
            yield f"data: {json.dumps(data)}\\n\\n"
            time.sleep(1)
    return Response(event_stream(), mimetype='text/event-stream',
                    headers={'Cache-Control': 'no-cache',
                             'X-Accel-Buffering': 'no'})
```

### 4. File Streaming
```python
from flask import send_file, send_from_directory

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

# Stream large files
@app.route('/large-file')
def large():
    def generate_chunks():
        with open('large.bin', 'rb') as f:
            while chunk := f.read(8192):
                yield chunk
    return Response(generate_chunks(), mimetype='application/octet-stream')
```

### 5. JSON Responses
```python
from flask import jsonify
# Flask auto-serializes dicts in return
@app.route('/api/data')
def data():
    return {"key": "value"}, 200  # shorthand
    # OR
    return jsonify({"key": "value"})
```

## Lab Exercise
Build a live log streaming endpoint using SSE that tails a log file and pushes new lines to a browser client using `EventSource`.
""")

write_lesson(os.path.join(FK, "_04_30_advanced_form_validation_and_file_uploads.md"),
frontmatter("04_30","Advanced Form Validation and File Uploads","Flask",4,"Advanced Flask Patterns",30,"advanced",["WTForms","FileField","validators","secure-filename","werkzeug","file-size","MIME-check","multipart","save"]) + """
# Advanced Form Validation and File Uploads

## Topics Covered

### 1. WTForms File Field
```python
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, validators

class UploadForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=2, max=50)])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
    ])
```

### 2. Secure File Handling
```python
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
MAX_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'error': 'No file'}, 400
    file = request.files['file']
    if file.filename == '':
        return {'error': 'Empty filename'}, 400
    if not allowed_file(file.filename):
        return {'error': 'File type not allowed'}, 415
    # Check file size
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    if size > MAX_SIZE:
        return {'error': 'File too large'}, 413
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return {'filename': filename}, 201
```

### 3. MIME Type Validation
```python
import magic  # python-magic

def validate_mime(file_stream):
    header = file_stream.read(2048)
    file_stream.seek(0)
    mime = magic.from_buffer(header, mime=True)
    return mime in ['image/jpeg', 'image/png', 'application/pdf']
```

### 4. Multiple File Uploads
```python
@app.route('/multi-upload', methods=['POST'])
def multi_upload():
    files = request.files.getlist('files[]')
    saved = []
    for file in files:
        if file and allowed_file(file.filename):
            fn = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, fn))
            saved.append(fn)
    return jsonify({'uploaded': saved})
```

### 5. Custom Validators
```python
from wtforms import ValidationError

def validate_image_size(form, field):
    if field.data:
        field.data.seek(0, 2)
        size = field.data.tell()
        field.data.seek(0)
        if size > 2 * 1024 * 1024:
            raise ValidationError('Image must be under 2MB')
```

## Lab Exercise
Build a profile photo upload system with: file type restriction, 5MB size limit, MIME validation, UUID-based filenames, and thumbnail generation with Pillow.
""")

write_lesson(os.path.join(FK, "_04_31_sqlalchemy_relationship_types_and_lazy_loading.md"),
frontmatter("04_31","SQLAlchemy Relationship Types and Lazy Loading","Flask",4,"Advanced Flask Patterns",31,"advanced",["relationship","backref","back-populates","lazy","joined","subquery","dynamic","many-to-many","secondary","cascade"]) + """
# SQLAlchemy Relationship Types and Lazy Loading

## Topics Covered

### 1. One-to-Many Relationship
```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    books = db.relationship('Book', back_populates='author',
                            lazy='dynamic', cascade='all, delete-orphan')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', back_populates='books')
```

### 2. Many-to-Many with Association Table
```python
# Association table (no model needed for simple junction)
student_course = db.Table('student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model):
    courses = db.relationship('Course', secondary=student_course,
                              back_populates='students')
```

### 3. Lazy Loading Strategies
| Strategy | SQL | When |
|---|---|---|
| `lazy='select'` | Separate SELECT on access | Default, small sets |
| `lazy='joined'` | JOIN in same query | Always needed |
| `lazy='subquery'` | Subquery per collection | Medium sets |
| `lazy='dynamic'` | Returns Query object | Large collections |
| `lazy='raise'` | Raises error if accessed | Detect N+1 |

```python
# Eager loading to avoid N+1
authors = Author.query.options(
    db.joinedload(Author.books)
).all()

# Using selectin for collections
authors = Author.query.options(
    db.selectinload(Author.books)
).all()
```

### 4. Association Object Pattern (with extra fields)
```python
class Enrollment(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id  = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Float)
    student = db.relationship('Student', back_populates='enrollments')
    course  = db.relationship('Course',  back_populates='enrollments')
```

## Lab Exercise
Build a Blog API with Authors → Posts (one-to-many) and Posts ↔ Tags (many-to-many). Use `selectinload` to return all posts with their tags in a single efficient query.
""")

write_lesson(os.path.join(FK, "_04_32_access_control_and_role_authorization.md"),
frontmatter("04_32","Access Control and Role Authorization","Flask",4,"Advanced Flask Patterns",32,"advanced",["RBAC","roles","permissions","Flask-Principal","current-user","login-required","role-required","decorators","admin-panel"]) + """
# Access Control and Role Authorization

## Topics Covered

### 1. Role-Based Access Control (RBAC) Pattern
```python
from enum import Enum
from functools import wraps
from flask_login import current_user
from flask import abort

class Role(str, Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'

# User model with role field
class User(db.Model, UserMixin):
    role = db.Column(db.Enum(Role), default=Role.VIEWER)

    def has_role(self, *roles):
        return self.role in roles
```

### 2. Role-Required Decorator
```python
def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if not current_user.has_role(*roles):
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/admin/dashboard')
@login_required
@role_required(Role.ADMIN)
def admin_dashboard():
    return render_template('admin.html')
```

### 3. Permission-Based Access (Fine-Grained)
```python
PERMISSIONS = {
    Role.ADMIN:  {'read', 'write', 'delete', 'manage'},
    Role.EDITOR: {'read', 'write'},
    Role.VIEWER: {'read'},
}

def can(permission):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user_perms = PERMISSIONS.get(current_user.role, set())
            if permission not in user_perms:
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/posts/<int:id>', methods=['DELETE'])
@login_required
@can('delete')
def delete_post(id):
    ...
```

### 4. Flask-Principal Integration
```python
from flask_principal import Principal, Permission, RoleNeed
principal = Principal(app)

admin_permission = Permission(RoleNeed('admin'))

@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin():
    return 'Admin only'
```

## Lab Exercise
Build a content management system with three roles (Admin/Editor/Viewer), role-required decorators, a permission matrix, and 403/401 error pages.
""")

write_lesson(os.path.join(FK, "_04_33_reverse_proxy_nginx_configuration.md"),
frontmatter("04_33","Reverse Proxy and Nginx Configuration","Flask",5,"Production Deployment",33,"advanced",["nginx","reverse-proxy","proxy-pass","gunicorn","uwsgi","ssl","https","location","upstream","X-Forwarded-For"]) + """
# Reverse Proxy and Nginx Configuration

## Topics Covered

### 1. Nginx as Reverse Proxy for Flask
```nginx
# /etc/nginx/sites-available/myapp
upstream flask_app {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name myapp.com www.myapp.com;

    location / {
        proxy_pass http://flask_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /var/www/myapp/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    client_max_body_size 16M;
}
```

### 2. Gunicorn Configuration
```bash
# Install
pip install gunicorn

# Run
gunicorn -w 4 -b 127.0.0.1:8000 "app:create_app()"

# gunicorn.conf.py
workers = 4
worker_class = "gthread"
threads = 2
bind = "127.0.0.1:8000"
timeout = 120
keepalive = 5
accesslog = "/var/log/gunicorn/access.log"
errorlog  = "/var/log/gunicorn/error.log"
```

### 3. SSL/HTTPS with Let's Encrypt
```bash
# Certbot
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d myapp.com -d www.myapp.com
```

```nginx
server {
    listen 443 ssl http2;
    ssl_certificate     /etc/letsencrypt/live/myapp.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myapp.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```

### 4. Flask ProxyFix Middleware
```python
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app,
    x_for=1, x_proto=1, x_host=1, x_prefix=1)
```

### 5. Systemd Service
```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/var/www/myapp/venv/bin/gunicorn --config gunicorn.conf.py "app:create_app()"
Restart=always

[Install]
WantedBy=multi-user.target
```

## Lab Exercise
Deploy a Flask app with Nginx + Gunicorn + HTTPS on a Ubuntu VPS. Configure static file serving, SSL, and verify headers with `curl -I`.
""")

write_lesson(os.path.join(FK, "_04_34_containerization_with_docker.md"),
frontmatter("04_34","Containerization with Docker","Flask",5,"Production Deployment",34,"advanced",["docker","dockerfile","docker-compose","image","container","volumes","networks","env-file","multi-stage","docker-hub"]) + """
# Containerization with Docker

## Topics Covered

### 1. Flask Dockerfile
```dockerfile
# Multi-stage build
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

# Non-root user
RUN adduser --disabled-password --gecos '' appuser
USER appuser

EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:create_app()"]
```

### 2. Docker Compose (Flask + MySQL + Redis)
```yaml
# docker-compose.yml
version: '3.9'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./uploads:/app/uploads
    networks:
      - app_network

  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app_network

  redis:
    image: redis:7-alpine
    networks:
      - app_network

volumes:
  mysql_data:

networks:
  app_network:
```

### 3. Environment Management
```bash
# .env file (never commit!)
FLASK_ENV=production
SECRET_KEY=your-secret-key
DB_URL=mysql+pymysql://user:pass@db/dbname
REDIS_URL=redis://redis:6379/0
```

### 4. Build and Run Commands
```bash
docker build -t myapp:latest .
docker compose up -d
docker compose logs -f web
docker compose exec web flask db upgrade
docker compose down --volumes  # remove volumes too
```

### 5. Health Check and Restart Policy
```yaml
web:
  restart: unless-stopped
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    interval: 30s
    timeout: 10s
    retries: 3
```

## Lab Exercise
Containerize a Flask + SQLAlchemy app with Docker Compose. Include Nginx as a separate service, environment variables via `.env`, and a `/health` endpoint. Run migrations on startup using `entrypoint.sh`.
""")

print(f"  Flask stubs filled: {written}")
w0 = written


# ══════════════════════════════════════════════════════════════════
# FIX 4: FastAPI — fill 13 remaining stubs with content
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 4: FastAPI — filling 13 remaining stubs")
print("=" * 60)

FA = os.path.join(BASE, "_15_fastapi")

lessons = {
    "_05_21_api_metadata_and_documentation_enrichment.md": (
        "21","API Metadata and Documentation Enrichment","FastAPI",3,"Advanced Features",21,"intermediate",
        ["openapi","tags","summary","description","response-description","deprecated","metadata","redoc","swagger-ui"],
        """
## Topics Covered

### 1. App-Level Metadata
```python
app = FastAPI(
    title="My API",
    description="# My API\\n\\nFull **markdown** description.",
    version="2.1.0",
    terms_of_service="https://example.com/terms",
    contact={"name": "Dev Team", "email": "api@example.com"},
    license_info={"name": "MIT"},
    openapi_tags=[
        {"name": "users", "description": "Operations with users"},
        {"name": "items", "description": "Manage items"},
    ]
)
```

### 2. Route-Level Metadata
```python
@app.get(
    "/users/{id}",
    tags=["users"],
    summary="Get a user by ID",
    description="Returns full user details. Requires auth.",
    response_description="The user object",
    responses={
        404: {"description": "User not found"},
        200: {"content": {"application/json": {"example": {"id": 1, "name": "Raja"}}}},
    },
    deprecated=False,
    operation_id="get_user_by_id",
)
async def get_user(id: int):
    ...
```

### 3. Hiding Routes from Docs
```python
@app.get("/internal", include_in_schema=False)
async def internal():
    ...
```

### 4. Customising Docs URLs
```python
app = FastAPI(docs_url="/swagger", redoc_url="/docs", openapi_url="/openapi.json")
```

## Lab
Build an API with rich metadata for three resources, custom tag descriptions, example responses, and disable the default `/docs` URL, replacing it with `/api/docs`.
"""),

    "_05_22_query_parameters_and_validation.md": (
        "22","Query Parameters and Validation","FastAPI",3,"Advanced Features",22,"intermediate",
        ["Query","optional","required","alias","title","description","min-length","max-length","regex","ge","le"],
        """
## Topics Covered

### 1. Basic Query Parameters
```python
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10, q: str | None = None):
    return {"skip": skip, "limit": limit, "q": q}
```

### 2. Annotated with Query()
```python
from fastapi import Query
from typing import Annotated

@app.get("/search")
async def search(
    q: Annotated[str, Query(
        min_length=3,
        max_length=50,
        title="Search Query",
        description="Search string, 3-50 chars",
        alias="search",            # URL uses ?search=
        example="python fastapi",
    )],
    page: Annotated[int, Query(ge=1, le=1000)] = 1,
    size: Annotated[int, Query(ge=5, le=100)] = 20,
):
    ...
```

### 3. List Query Parameters
```python
@app.get("/filter")
async def filter_items(
    tags: Annotated[list[str], Query()] = []
):
    # /filter?tags=a&tags=b&tags=c
    return {"tags": tags}
```

### 4. Regex Validation
```python
from fastapi import Query
@app.get("/validate")
async def validate(
    code: Annotated[str, Query(pattern=r"^[A-Z]{3}-\\d{3}$")]
):
    return {"code": code}
```

## Lab
Build a product search endpoint with: keyword (min 2 chars), category list, price range (ge/le), sort field (enum), page/size pagination — all validated with `Query()`.
"""),

    "_05_23_multi_source_parameter_declarations.md": (
        "23","Multi-Source Parameter Declarations","FastAPI",3,"Advanced Features",23,"intermediate",
        ["Path","Query","Body","Header","Cookie","multiple-params","mixed","Annotated","Field"],
        """
## Topics Covered

### 1. Mixing Path, Query, Body
```python
from fastapi import Path, Query, Body

@app.put("/users/{user_id}/items/{item_id}")
async def update_item(
    user_id: Annotated[int, Path(title="User ID", ge=1)],
    item_id: Annotated[int, Path(ge=1)],
    q: Annotated[str | None, Query(max_length=50)] = None,
    item: Item | None = None,
    importance: Annotated[int, Body(ge=1, le=5)] = 1,
):
    return {"user_id": user_id, "item_id": item_id, "q": q, "importance": importance}
```

### 2. Multiple Body Parameters
```python
@app.post("/composite")
async def composite(
    user: User,
    item: Item,
    note: Annotated[str, Body(embed=True)] = ""
):
    # JSON body: {"user": {...}, "item": {...}, "note": "..."}
    ...
```

### 3. Body with `embed=True`
```python
@app.post("/single-embed")
async def single(
    item: Annotated[Item, Body(embed=True)]
    # JSON: {"item": {"name": "..."}} instead of {"name": "..."}
):
    ...
```

### 4. Header and Cookie
```python
from fastapi import Header, Cookie

@app.get("/headers")
async def read_headers(
    x_token: Annotated[str, Header()],   # X-Token header
    user_agent: Annotated[str | None, Header()] = None,
    session: Annotated[str | None, Cookie()] = None,
):
    return {"token": x_token, "ua": user_agent, "session": session}
```

## Lab
Create an API endpoint that accepts: path ID, query filter, JSON body, auth header, and session cookie — all in one function with proper validation.
"""),

    "_05_24_form_submissions_and_file_handling.md": (
        "24","Form Submissions and File Handling","FastAPI",3,"Advanced Features",24,"intermediate",
        ["Form","File","UploadFile","multipart","form-data","python-multipart","size-limit","multiple-files"],
        """
## Topics Covered

### 1. Form Data
```python
from fastapi import Form
# pip install python-multipart

@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    return {"username": username}
```

### 2. File Upload
```python
from fastapi import File, UploadFile

@app.post("/upload")
async def upload(file: UploadFile):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents),
            "content_type": file.content_type}
```

### 3. File + Form Together
```python
@app.post("/profile")
async def update_profile(
    username: Annotated[str, Form()],
    avatar: UploadFile,
):
    return {"username": username, "avatar": avatar.filename}
```

### 4. Multiple Files
```python
@app.post("/multi-upload")
async def multi(files: list[UploadFile]):
    return [{"name": f.filename, "type": f.content_type} for f in files]
```

### 5. File Size Limit
```python
@app.post("/safe-upload")
async def safe_upload(file: UploadFile):
    MAX = 5 * 1024 * 1024  # 5MB
    content = await file.read(MAX + 1)
    if len(content) > MAX:
        raise HTTPException(413, "File too large")
    # Save
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(content)
    return {"saved": file.filename}
```

## Lab
Build a document upload endpoint that accepts: title (form), description (form), file (≤10MB, PDF/DOCX only). Save with UUID filename, return download URL.
"""),

    "_05_25_headers_cookies_and_request_info.md": (
        "25","Headers Cookies and Request Info","FastAPI",3,"Advanced Features",25,"intermediate",
        ["Header","Cookie","Request","client","url","method","response-headers","set-cookie","response"],
        """
## Topics Covered

### 1. Reading Headers
```python
from fastapi import Header

@app.get("/auth")
async def auth(
    authorization: Annotated[str, Header()],
    x_api_version: Annotated[str | None, Header()] = None,
):
    return {"auth": authorization, "version": x_api_version}
```

### 2. Reading Cookies
```python
from fastapi import Cookie

@app.get("/session")
async def session(session_id: Annotated[str | None, Cookie()] = None):
    return {"session": session_id}
```

### 3. Setting Response Headers and Cookies
```python
from fastapi import Response

@app.post("/login")
async def login(response: Response, username: str = Form(...)):
    token = create_token(username)
    response.set_cookie(key="session", value=token, httponly=True,
                        samesite="lax", max_age=3600)
    response.headers["X-Auth-Token"] = token
    return {"status": "logged in"}
```

### 4. Raw Request Object
```python
from fastapi import Request

@app.get("/info")
async def info(request: Request):
    return {
        "method":  request.method,
        "url":     str(request.url),
        "headers": dict(request.headers),
        "client":  request.client.host,
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }
```

## Lab
Build a middleware-free rate limiter using client IP from `request.client.host`, stored in Redis, enforced via a dependency injection.
"""),

    "_05_26_response_models_and_status_codes.md": (
        "26","Response Models and Status Codes","FastAPI",3,"Advanced Features",26,"intermediate",
        ["response_model","status_code","exclude_unset","response_model_include","response_model_exclude","JSONResponse","201","422","404"],
        """
## Topics Covered

### 1. Response Model
```python
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

@app.post("/users", response_model=UserOut, status_code=201)
async def create_user(user: UserIn):
    db_user = User(username=user.username, hashed=hash(user.password))
    db.add(db_user); db.commit(); db.refresh(db_user)
    return db_user  # password field auto-stripped
```

### 2. Partial Response Filtering
```python
@app.get("/items/{id}", response_model=Item,
         response_model_include={"name", "price"},
         response_model_exclude_unset=True)
async def get_item(id: int):
    ...
```

### 3. Multiple Response Types
```python
from typing import Union

@app.get("/items/{id}", response_model=Union[ItemFull, ItemBasic])
async def get_item(id: int, full: bool = False):
    item = get_from_db(id)
    return item if full else ItemBasic(**item.dict())
```

### 4. Common Status Codes
```python
from fastapi import status

@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id: int):
    delete_from_db(id)
    # Returns no body
```

## Lab
Design a User API with separate request/response models (hide password), 201 on create, 404 on not found, 204 on delete — all documented in OpenAPI.
"""),

    "_05_27_advanced_response_classes.md": (
        "27","Advanced Response Classes","FastAPI",3,"Advanced Features",27,"advanced",
        ["JSONResponse","HTMLResponse","PlainTextResponse","RedirectResponse","FileResponse","StreamingResponse","ORJSONResponse"],
        """
## Topics Covered

### 1. Response Class Variants
```python
from fastapi.responses import (
    JSONResponse, HTMLResponse, PlainTextResponse,
    RedirectResponse, FileResponse, StreamingResponse
)

@app.get("/html", response_class=HTMLResponse)
async def html():
    return "<h1>Hello</h1>"

@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello, plain world"

@app.get("/redirect")
async def redirect():
    return RedirectResponse(url="/new-location", status_code=302)

@app.get("/file")
async def file():
    return FileResponse("report.pdf", media_type="application/pdf",
                        filename="download.pdf")
```

### 2. Streaming Response
```python
import asyncio

async def generate():
    for i in range(100):
        yield f"chunk {i}\\n".encode()
        await asyncio.sleep(0.01)

@app.get("/stream")
async def stream():
    return StreamingResponse(generate(), media_type="text/plain")
```

### 3. ORJSONResponse (faster)
```python
from fastapi.responses import ORJSONResponse
# pip install orjson

@app.get("/fast", response_class=ORJSONResponse)
async def fast():
    return {"data": list(range(1000))}
```

### 4. Custom Headers in Response
```python
@app.get("/custom-headers")
async def custom():
    content = {"message": "ok"}
    headers = {"X-Custom-Header": "value", "Cache-Control": "no-cache"}
    return JSONResponse(content=content, headers=headers)
```

## Lab
Build an export endpoint that: returns CSV for `?format=csv`, JSON for `?format=json`, triggers file download for `?format=excel` — all from the same data source.
"""),

    "_05_28_schema_evolution_with_alembic.md": (
        "28","Schema Evolution with Alembic","FastAPI",4,"Database Integration",28,"advanced",
        ["alembic","migration","revision","upgrade","downgrade","autogenerate","env.py","alembic.ini","async-alembic"],
        """
## Topics Covered

### 1. Alembic Setup
```bash
pip install alembic
alembic init alembic
```

```python
# alembic/env.py
from app.models import Base
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(...)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()
```

### 2. Creating Migrations
```bash
alembic revision --autogenerate -m "add users table"
alembic upgrade head
alembic downgrade -1
alembic history --verbose
alembic current
```

### 3. Migration File
```python
# alembic/versions/001_add_users.py
def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_users_email', 'users', ['email'])

def downgrade():
    op.drop_index('ix_users_email')
    op.drop_table('users')
```

### 4. Async Alembic
```python
# For SQLAlchemy async engine
from sqlalchemy.ext.asyncio import AsyncConnection

async def run_async_migrations():
    async with engine.begin() as conn:
        await conn.run_sync(do_run_migrations)
```

## Lab
Add `created_at` and `updated_at` columns to an existing `products` table via Alembic migration. Then add an index, run forward/backward migrations, and verify with `alembic history`.
"""),

    "_05_29_scope_based_fine_grained_authorization.md": (
        "29","Scope-Based Fine-Grained Authorization","FastAPI",4,"Database Integration",29,"advanced",
        ["scopes","SecurityScopes","OAuth2","JWT-scopes","role-scope-mapping","permission","HTTPBearer"],
        """
## Topics Covered

### 1. JWT with Scopes
```python
SCOPES = {
    "items:read": "Read items",
    "items:write": "Create/update items",
    "users:admin": "Manage users",
}

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes=SCOPES
)
```

### 2. Scope Validation Dependency
```python
from fastapi.security import SecurityScopes

async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
    )
    payload = decode_jwt(token)
    token_scopes = payload.get("scopes", [])
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(403, f"Missing scope: {scope}")
    return payload
```

### 3. Protecting Routes with Scopes
```python
from fastapi import Security

@app.get("/items", dependencies=[Security(get_current_user, scopes=["items:read"])])
async def list_items():
    ...

@app.post("/items", dependencies=[Security(get_current_user, scopes=["items:write"])])
async def create_item(item: ItemIn):
    ...
```

## Lab
Build a multi-tenant API where admins get all scopes, editors get write, viewers get read. Return 403 with `missing_scope` detail when unauthorized.
"""),

    "_05_30_custom_exception_handling.md": (
        "30","Custom Exception Handling","FastAPI",3,"Advanced Features",30,"intermediate",
        ["HTTPException","exception-handler","RequestValidationError","422","custom-error","middleware","error-schema"],
        """
## Topics Covered

### 1. HTTPException
```python
from fastapi import HTTPException

@app.get("/items/{id}")
async def get_item(id: int):
    item = db.get(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {id} not found",
                            headers={"X-Error": "not-found"})
    return item
```

### 2. Custom Exception Classes
```python
class DomainError(Exception):
    def __init__(self, code: str, message: str, status: int = 400):
        self.code = code
        self.message = message
        self.status = status

@app.exception_handler(DomainError)
async def domain_error_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=exc.status,
        content={"error": exc.code, "message": exc.message}
    )

# Usage
raise DomainError("INVALID_EMAIL", "Email format invalid")
```

### 3. Override Validation Error Format
```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = [{"field": e["loc"][-1], "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"errors": errors})
```

### 4. Global Error Catch-All
```python
@app.exception_handler(Exception)
async def generic_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error: %s", exc)
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
```

## Lab
Build a standardised error response system with: custom exception base class, field-level validation errors, 404/403/500 handlers, and error logging middleware.
"""),

    "_05_31_websocket_architecture.md": (
        "31","WebSocket Architecture","FastAPI",3,"Advanced Features",31,"advanced",
        ["WebSocket","WebSocketDisconnect","ws-connect","ws-send","ws-receive","broadcast","rooms","connection-manager"],
        """
## Topics Covered

### 1. Basic WebSocket Endpoint
```python
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo [{client_id}]: {data}")
    except WebSocketDisconnect:
        print(f"Client {client_id} disconnected")
```

### 2. Connection Manager (Broadcast)
```python
class ConnectionManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active.remove(ws)

    async def broadcast(self, message: str):
        for connection in self.active:
            await connection.send_text(message)

    async def send_to(self, ws: WebSocket, message: str):
        await ws.send_text(message)

manager = ConnectionManager()

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            msg = await websocket.receive_text()
            await manager.broadcast(f"[broadcast] {msg}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A user left")
```

### 3. Sending JSON
```python
await websocket.send_json({"type": "message", "data": "hello"})
data = await websocket.receive_json()
```

### 4. WebSocket Authentication
```python
@app.websocket("/ws-auth")
async def ws_auth(websocket: WebSocket, token: str = Query(...)):
    user = verify_token(token)
    if not user:
        await websocket.close(code=1008)
        return
    await websocket.accept()
    ...
```

## Lab
Build a real-time chat application with rooms: users join by room name, messages broadcast only within rooms, user join/leave notifications, and token-based auth.
"""),

    "_05_32_openapi_standard_and_interactive_ui.md": (
        "32","OpenAPI Standard and Interactive UI","FastAPI",3,"Advanced Features",32,"intermediate",
        ["openapi","swagger-ui","redoc","schema","examples","openapi-extra","custom-openapi","openapi-json"],
        """
## Topics Covered

### 1. Auto-Generated OpenAPI Schema
```python
# Access at:
# /openapi.json  — raw JSON schema
# /docs          — Swagger UI
# /redoc         — ReDoc UI
```

### 2. Request/Response Examples
```python
class Item(BaseModel):
    name: str
    price: float

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"name": "Widget", "price": 9.99}]
        }
    )
```

### 3. Field-Level Examples
```python
from pydantic import Field

class Product(BaseModel):
    name: str = Field(..., examples=["Laptop", "Phone"])
    price: float = Field(..., ge=0, examples=[999.99])
```

### 4. Custom OpenAPI Function
```python
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title="Custom API",
        version="3.0.0",
        description="Custom docs",
        routes=app.routes,
    )
    schema["info"]["x-logo"] = {"url": "https://example.com/logo.png"}
    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi
```

## Lab
Add rich examples to a 3-resource API, configure a custom OpenAPI schema with logo and contact info, hide internal endpoints from the schema, and serve custom Swagger UI with a CDN.
"""),

    "_05_33_application_setup_and_environment.md": (
        "33","Application Setup and Environment Configuration","FastAPI",5,"Production FastAPI",33,"intermediate",
        ["settings","pydantic-settings","BaseSettings","env-file","dotenv","config","environment","lifespan","startup","shutdown"],
        """
## Topics Covered

### 1. Settings with pydantic-settings
```python
# pip install pydantic-settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    debug: bool = False
    database_url: str
    secret_key: str
    allowed_origins: list[str] = ["http://localhost:3000"]
    redis_url: str = "redis://localhost:6379"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
```

### 2. Dependency-Cached Settings
```python
from functools import lru_cache
from fastapi import Depends

@lru_cache
def get_settings():
    return Settings()

@app.get("/info")
async def info(s: Settings = Depends(get_settings)):
    return {"name": s.app_name, "debug": s.debug}
```

### 3. Lifespan Events (startup/shutdown)
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await db.connect()
    redis = await aioredis.from_url(settings.redis_url)
    app.state.redis = redis
    print("App started")
    yield
    # Shutdown
    await db.disconnect()
    await redis.close()
    print("App stopped")

app = FastAPI(lifespan=lifespan)
```

### 4. Environment-Specific Configuration
```python
# .env.development
DEBUG=true
DATABASE_URL=sqlite+aiosqlite:///./test.db

# .env.production
DEBUG=false
DATABASE_URL=postgresql+asyncpg://user:pass@host/db
```

```python
import os
env = os.getenv("ENVIRONMENT", "development")
Settings(_env_file=f".env.{env}")
```

## Lab
Configure a FastAPI app with environment-specific settings (dev/staging/prod), lifespan DB pool startup/shutdown, settings cached with `lru_cache`, and validated using pydantic-settings.
"""),
}

for fname, args in lessons.items():
    lid, title, course, mod, mod_title, les, diff, tags, body = args
    path = os.path.join(FA, fname)
    if "Status**: Stub" in open(path, encoding="utf-8", errors="ignore").read() if os.path.exists(path) else True:
        fm = frontmatter(lid, title, course, mod, mod_title, les, diff, tags)
        write_lesson(path, fm + body.strip() + "\n")

print(f"  FastAPI stubs filled: {written - w0}")
w1 = written


# ══════════════════════════════════════════════════════════════════
# FIX 5: MySQL — fill 12 remaining stubs with topic plans
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 5: MySQL — upgrading 12 stub topic plans")
print("=" * 60)

MY = os.path.join(BASE, "_11_mysql")

mysql_lessons = {
    "_05_01_database_architecture_and_relational_concepts.md": ("Already real — SKIP",),

    "_05_02_database_design_er_modeling_normalization.md": (
        "05_02","Database Design ER Modeling and Normalization","MySQL",1,"MySQL Foundations",2,"intermediate",
        ["er-diagram","entity","relationship","cardinality","1NF","2NF","3NF","BCNF","denormalization","crow-foot"],
"""
## Topics Covered

### 1. Entity-Relationship Modeling
- **Entities** vs **Attributes** vs **Relationships**
- Cardinality: 1:1, 1:N, M:N
- Crow's foot notation
- Identifying vs non-identifying relationships
- Weak entities and partial keys

### 2. ER to Schema Mapping
```
Student(id PK, name, email)
Course(id PK, title, credits)
Enrollment(student_id FK, course_id FK, grade)  -- M:N resolved
```

### 3. Normal Forms
| Form | Rule | Fix |
|---|---|---|
| 1NF | No repeating groups; atomic values | Split multi-value cols |
| 2NF | No partial dependencies on composite PK | Move partial deps to new table |
| 3NF | No transitive dependencies | Remove transitive cols |
| BCNF | Every determinant is a candidate key | Decompose further |

### 4. Normalization Example
```sql
-- Unnormalized
Orders(order_id, customer_name, customer_city, product1, product2)

-- After 1NF
OrderItems(order_id, line, product)
Orders(order_id, customer_name, customer_city)

-- After 3NF
Customers(customer_id, name, city)
Orders(order_id, customer_id FK)
OrderItems(order_id FK, line, product_id FK)
```

## Lab
Design an ER diagram for a Library Management System (Books, Authors, Members, Loans) and implement it in MySQL with proper FK constraints.
"""),

    "_05_03_ddl_and_integrity_constraints.md": (
        "05_03","DDL and Integrity Constraints","MySQL",2,"SQL Fundamentals",3,"beginner",
        ["CREATE-TABLE","ALTER-TABLE","DROP","TRUNCATE","PRIMARY-KEY","FOREIGN-KEY","UNIQUE","CHECK","DEFAULT","NOT-NULL","AUTO-INCREMENT"],
"""
## Topics Covered

### 1. CREATE TABLE
```sql
CREATE TABLE employees (
    emp_id      INT AUTO_INCREMENT PRIMARY KEY,
    first_name  VARCHAR(50)     NOT NULL,
    last_name   VARCHAR(50)     NOT NULL,
    email       VARCHAR(100)    NOT NULL UNIQUE,
    salary      DECIMAL(10,2)   DEFAULT 50000.00,
    dept_id     INT,
    hire_date   DATE            DEFAULT (CURRENT_DATE),
    is_active   TINYINT(1)      DEFAULT 1,
    CONSTRAINT fk_dept FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT chk_salary CHECK (salary > 0)
);
```

### 2. ALTER TABLE
```sql
ALTER TABLE employees
    ADD COLUMN phone VARCHAR(20),
    MODIFY COLUMN first_name VARCHAR(100) NOT NULL,
    DROP COLUMN is_active,
    ADD CONSTRAINT uq_phone UNIQUE (phone);
```

### 3. ON DELETE / ON UPDATE Actions
| Action | Behavior |
|---|---|
| CASCADE | Delete/update child when parent changes |
| SET NULL | Set FK to NULL |
| RESTRICT | Prevent parent delete if children exist |
| NO ACTION | Same as RESTRICT in MySQL |

### 4. Indexes Created Automatically
- PRIMARY KEY → clustered index
- UNIQUE → unique index
- FOREIGN KEY → non-clustered index on FK column

## Lab
Create a complete schema for an e-commerce system with products, categories, customers, orders, and order_items — all constraints enforced.
"""),

    "_05_04_dml_and_basic_retrieval.md": (
        "05_04","DML and Basic Retrieval","MySQL",2,"SQL Fundamentals",4,"beginner",
        ["INSERT","UPDATE","DELETE","SELECT","WHERE","ORDER-BY","LIMIT","OFFSET","DISTINCT","aliases","LIKE","BETWEEN","IN","IS-NULL"],
"""
## Topics Covered

### 1. INSERT
```sql
-- Single row
INSERT INTO products (name, price, category_id) VALUES ('Widget', 9.99, 1);

-- Multiple rows
INSERT INTO products (name, price) VALUES
    ('Gadget', 29.99), ('Doohickey', 4.99), ('Thingamajig', 49.99);

-- INSERT from SELECT
INSERT INTO archive_orders SELECT * FROM orders WHERE created_at < '2024-01-01';
```

### 2. UPDATE
```sql
UPDATE products SET price = price * 1.1 WHERE category_id = 2;
UPDATE employees SET salary = 60000, dept_id = 3 WHERE emp_id = 42;
```

### 3. DELETE
```sql
DELETE FROM cart_items WHERE session_expired = 1;
TRUNCATE TABLE temp_log;          -- Fast, non-logged, no WHERE
DELETE FROM orders WHERE id = 5;  -- Logged, triggers fire
```

### 4. SELECT with Filtering
```sql
SELECT p.name, p.price, c.name AS category
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE p.price BETWEEN 10 AND 50
  AND c.name IN ('Electronics', 'Books')
  AND p.name LIKE '%pro%'
  AND p.deleted_at IS NULL
ORDER BY p.price DESC
LIMIT 20 OFFSET 40;
```

## Lab
Write DML statements to: insert 10 products, update prices by category, delete expired records, and build a paginated search query.
"""),

    "_05_05_aggregation_grouping_and_functions.md": (
        "05_05","Aggregation Grouping and Functions","MySQL",2,"SQL Fundamentals",5,"intermediate",
        ["COUNT","SUM","AVG","MIN","MAX","GROUP-BY","HAVING","ROLLUP","string-functions","date-functions","COALESCE","NULLIF","CASE"],
"""
## Topics Covered

### 1. Aggregate Functions
```sql
SELECT
    dept_id,
    COUNT(*)           AS total_employees,
    COUNT(DISTINCT job) AS unique_jobs,
    AVG(salary)        AS avg_salary,
    MIN(salary)        AS min_salary,
    MAX(salary)        AS max_salary,
    SUM(salary)        AS total_payroll
FROM employees
WHERE is_active = 1
GROUP BY dept_id
HAVING avg_salary > 50000
ORDER BY total_payroll DESC;
```

### 2. WITH ROLLUP
```sql
SELECT dept_id, job, SUM(salary)
FROM employees
GROUP BY dept_id, job WITH ROLLUP;
-- Adds subtotal rows per dept and grand total
```

### 3. String Functions
```sql
CONCAT(first_name, ' ', last_name)
SUBSTRING(email, 1, LOCATE('@', email) - 1)  -- username
UPPER(country), LOWER(email)
TRIM(LEADING '0' FROM phone)
LENGTH(description)
REPLACE(text, 'old', 'new')
FORMAT(salary, 2)                             -- 55,000.00
```

### 4. Date Functions
```sql
NOW(), CURDATE(), CURTIME()
DATE_FORMAT(hire_date, '%d %M %Y')           -- 15 July 2023
DATEDIFF(CURDATE(), hire_date)               -- days since hire
DATE_ADD(order_date, INTERVAL 30 DAY)        -- due date
YEAR(hire_date), MONTH(hire_date), DAY(hire_date)
```

### 5. CASE Expression
```sql
SELECT name, salary,
    CASE
        WHEN salary < 30000 THEN 'Junior'
        WHEN salary < 60000 THEN 'Mid'
        ELSE 'Senior'
    END AS grade
FROM employees;
```

## Lab
Write queries to: monthly sales totals with ROLLUP, format customer names, calculate age from DOB, grade products by price bracket.
"""),

    "_05_06_relational_joins_and_set_operations.md": (
        "05_06","Relational Joins and Set Operations","MySQL",2,"SQL Fundamentals",6,"intermediate",
        ["INNER-JOIN","LEFT-JOIN","RIGHT-JOIN","FULL-OUTER","SELF-JOIN","CROSS-JOIN","UNION","INTERSECT","EXCEPT","join-conditions"],
"""
## Topics Covered

### 1. JOIN Types
```sql
-- INNER JOIN — only matching rows
SELECT o.id, c.name FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;

-- LEFT JOIN — all orders, including those without a customer
SELECT o.id, c.name FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id;

-- SELF JOIN — employee manager hierarchy
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- CROSS JOIN — all combinations (use carefully!)
SELECT s.size, c.color FROM sizes s CROSS JOIN colors c;
```

### 2. Multi-Table Join
```sql
SELECT o.id, c.name, p.name AS product, oi.quantity
FROM orders o
JOIN customers c     ON o.customer_id = c.id
JOIN order_items oi  ON oi.order_id = o.id
JOIN products p      ON oi.product_id = p.id
WHERE o.status = 'shipped';
```

### 3. Set Operations
```sql
-- UNION (removes duplicates)
SELECT email FROM customers
UNION
SELECT email FROM newsletter_subscribers;

-- UNION ALL (keeps duplicates — faster)
SELECT product_id FROM sales_2023
UNION ALL
SELECT product_id FROM sales_2024;
```

> **Note**: MySQL does not natively support INTERSECT/EXCEPT before 8.0.31.  
> Use `INNER JOIN` for intersection, `LEFT JOIN ... WHERE IS NULL` for difference.

## Lab
Write queries for: all customers with their orders (including those with no orders), product sales with category rollup, employee org chart via self-join.
"""),

    "_05_07_subqueries_ctes_and_window_functions.md": (
        "05_07","Subqueries CTEs and Window Functions","MySQL",3,"Advanced SQL",7,"intermediate",
        ["subquery","correlated","EXISTS","CTE","WITH","recursive-CTE","ROW_NUMBER","RANK","DENSE_RANK","LAG","LEAD","PARTITION-BY"],
"""
## Topics Covered

### 1. Subqueries
```sql
-- Scalar subquery
SELECT name, price,
    (SELECT AVG(price) FROM products) AS avg_price
FROM products;

-- IN subquery
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE total > 1000);

-- Correlated subquery (runs once per outer row)
SELECT name, salary FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.dept_id = e1.dept_id);

-- EXISTS
SELECT * FROM products p
WHERE EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.id);
```

### 2. Common Table Expressions (CTEs)
```sql
WITH monthly_sales AS (
    SELECT MONTH(order_date) AS month, SUM(total) AS revenue
    FROM orders WHERE YEAR(order_date) = 2024
    GROUP BY month
),
ranked AS (
    SELECT *, RANK() OVER (ORDER BY revenue DESC) AS rnk
    FROM monthly_sales
)
SELECT * FROM ranked WHERE rnk <= 3;
```

### 3. Recursive CTE — Org Chart
```sql
WITH RECURSIVE org AS (
    SELECT id, name, manager_id, 0 AS depth
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, o.depth + 1
    FROM employees e JOIN org o ON e.manager_id = o.id
)
SELECT * FROM org ORDER BY depth, name;
```

### 4. Window Functions
```sql
SELECT name, dept_id, salary,
    ROW_NUMBER()   OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn,
    RANK()         OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk,
    DENSE_RANK()   OVER (PARTITION BY dept_id ORDER BY salary DESC) AS drnk,
    LAG(salary, 1) OVER (PARTITION BY dept_id ORDER BY salary)     AS prev_salary,
    LEAD(salary,1) OVER (PARTITION BY dept_id ORDER BY salary)     AS next_salary,
    SUM(salary)    OVER (PARTITION BY dept_id)                     AS dept_total
FROM employees;
```

## Lab
Find: top 3 products per category (using ROW_NUMBER), month-over-month growth (using LAG), full org hierarchy (recursive CTE), customers who never ordered (EXISTS NOT).
"""),

    "_05_08_views_indexes_and_query_optimization.md": (
        "05_08","Views Indexes and Query Optimization","MySQL",3,"Advanced SQL",8,"advanced",
        ["CREATE-VIEW","updatable-view","INDEX","EXPLAIN","query-plan","covering-index","composite-index","ANALYZE","slow-query-log","optimizer-hints"],
"""
## Topics Covered

### 1. Views
```sql
-- Simple view
CREATE OR REPLACE VIEW active_customers AS
SELECT id, name, email, total_orders
FROM customers WHERE is_active = 1;

-- View with JOIN
CREATE VIEW product_inventory AS
SELECT p.id, p.name, p.price, c.name AS category, i.quantity
FROM products p JOIN categories c ON p.category_id = c.id
JOIN inventory i ON i.product_id = p.id;

-- Updatable view (no GROUP BY, DISTINCT, subqueries)
UPDATE active_customers SET email = 'new@mail.com' WHERE id = 5;
```

### 2. Indexes
```sql
-- Single column
CREATE INDEX idx_email ON customers(email);

-- Composite (order matters — most selective first)
CREATE INDEX idx_dept_salary ON employees(dept_id, salary);

-- Covering index (query served entirely from index)
CREATE INDEX idx_cover ON orders(customer_id, status, created_at);

-- Full-text
CREATE FULLTEXT INDEX idx_ft_name ON products(name, description);
SELECT * FROM products WHERE MATCH(name, description) AGAINST ('wireless headphones');

-- Drop index
DROP INDEX idx_email ON customers;
```

### 3. EXPLAIN and Query Analysis
```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 5 AND status = 'shipped';
-- Look for: type (range > ref > all), key, rows, Extra
EXPLAIN ANALYZE SELECT ...;  -- MySQL 8.0.18+: actual execution stats
```

### 4. Slow Query Log
```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- log queries > 1 second
SHOW STATUS LIKE 'Slow_queries';
```

## Lab
Add indexes to a 1M-row orders table. Use EXPLAIN ANALYZE to compare before/after query plans. Build a covering index for the most common API query pattern.
"""),

    "_05_09_stored_procedures_functions_triggers_events.md": (
        "05_09","Stored Procedures Functions Triggers and Events","MySQL",4,"Programmability",9,"advanced",
        ["STORED-PROCEDURE","FUNCTION","TRIGGER","EVENT","IN-OUT-INOUT","DELIMITER","DECLARE","IF","LOOP","CALL","BEFORE-AFTER"],
"""
## Topics Covered

### 1. Stored Procedures
```sql
DELIMITER //
CREATE PROCEDURE get_dept_summary(IN dept_id INT, OUT total DECIMAL(15,2))
BEGIN
    SELECT SUM(salary) INTO total
    FROM employees WHERE dept_id = dept_id AND is_active = 1;
END //
DELIMITER ;

CALL get_dept_summary(3, @total);
SELECT @total;
```

### 2. User-Defined Functions
```sql
DELIMITER //
CREATE FUNCTION full_name(first VARCHAR(50), last VARCHAR(50))
RETURNS VARCHAR(101) DETERMINISTIC
BEGIN
    RETURN CONCAT(first, ' ', last);
END //
DELIMITER ;

SELECT full_name(first_name, last_name) FROM employees;
```

### 3. Triggers
```sql
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customers SET total_orders = total_orders + 1
    WHERE id = NEW.customer_id;

    INSERT INTO audit_log(action, entity, entity_id, ts)
    VALUES ('INSERT', 'orders', NEW.id, NOW());
END //
DELIMITER ;
```

### 4. Events (Scheduled Jobs)
```sql
SET GLOBAL event_scheduler = ON;

CREATE EVENT cleanup_sessions
ON SCHEDULE EVERY 1 HOUR
DO
    DELETE FROM sessions WHERE expires_at < NOW();
```

## Lab
Build a complete order processing system using: stored procedure (create order + update inventory), trigger (audit log + customer stats), event (nightly cleanup of expired carts).
"""),

    "_05_10_transactions_concurrency_and_locking.md": (
        "05_10","Transactions Concurrency and Locking","MySQL",4,"Programmability",10,"advanced",
        ["BEGIN","COMMIT","ROLLBACK","SAVEPOINT","ACID","isolation-level","READ-COMMITTED","REPEATABLE-READ","SERIALIZABLE","deadlock","row-lock","gap-lock"],
"""
## Topics Covered

### 1. Transactions
```sql
START TRANSACTION;
    UPDATE accounts SET balance = balance - 500 WHERE id = 1;
    UPDATE accounts SET balance = balance + 500 WHERE id = 2;
    -- Check both succeeded
    IF (SELECT balance FROM accounts WHERE id = 1) < 0 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;

-- SAVEPOINT
START TRANSACTION;
    INSERT INTO orders VALUES (...);
    SAVEPOINT after_order;
    INSERT INTO payments VALUES (...);
    -- If payment fails:
    ROLLBACK TO after_order;
    COMMIT;
```

### 2. ACID Properties
| Property | Meaning |
|---|---|
| **A**tomicity | All or nothing |
| **C**onsistency | DB stays valid |
| **I**solation | Concurrent txns don't interfere |
| **D**urability | Committed data survives crashes |

### 3. Isolation Levels
```sql
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- READ UNCOMMITTED → dirty reads
-- READ COMMITTED   → no dirty reads, phantom reads possible
-- REPEATABLE READ  → MySQL default; no dirty/non-repeatable
-- SERIALIZABLE     → strictest; full locking
```

### 4. Lock Types
```sql
-- Shared lock (read)
SELECT * FROM products WHERE id = 5 LOCK IN SHARE MODE;

-- Exclusive lock (write)
SELECT * FROM products WHERE id = 5 FOR UPDATE;

-- Show active locks
SELECT * FROM performance_schema.data_locks;
```

## Lab
Simulate a bank transfer with ACID guarantee, test deadlock scenario (two sessions updating rows in opposite order), verify isolation levels with dirty read experiment.
"""),

    "_05_11_database_security_administration_replication.md": (
        "05_11","Database Security Administration and Replication","MySQL",5,"Administration",11,"advanced",
        ["CREATE-USER","GRANT","REVOKE","privileges","SSL","roles","backup","mysqldump","mysqlpump","binary-log","replication","master-slave"],
"""
## Topics Covered

### 1. User Management
```sql
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongPass123!';
CREATE USER 'read_only'@'192.168.1.%' IDENTIFIED WITH caching_sha2_password BY 'Pass!';

GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_user'@'%';
GRANT SELECT ON mydb.* TO 'read_only'@'%';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';

REVOKE INSERT ON mydb.orders FROM 'app_user'@'%';
DROP USER 'old_user'@'%';
FLUSH PRIVILEGES;
```

### 2. MySQL Roles (8.0+)
```sql
CREATE ROLE 'app_read', 'app_write', 'admin';
GRANT SELECT ON mydb.* TO 'app_read';
GRANT INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
GRANT ALL ON *.* TO 'admin';

GRANT 'app_read', 'app_write' TO 'dev_user'@'%';
SET DEFAULT ROLE ALL TO 'dev_user'@'%';
```

### 3. Backup and Restore
```bash
# Full dump
mysqldump -u root -p --all-databases --single-transaction > backup.sql

# Restore
mysql -u root -p < backup.sql

# Binary log backup (point-in-time recovery)
mysqlbinlog /var/log/mysql/mysql-bin.000001 | mysql -u root -p
```

### 4. Replication Overview
```
Primary (writes) → binary log → Replica (reads)
```
```sql
-- On primary
CREATE USER 'repl'@'%' IDENTIFIED BY 'ReplPass!';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

-- On replica
CHANGE MASTER TO MASTER_HOST='primary_ip', MASTER_USER='repl', ...;
START SLAVE;
SHOW SLAVE STATUS\\G;
```

## Lab
Set up a read-only reporting user with table-level restrictions, back up a database, simulate point-in-time recovery using binary logs.
"""),

    "_05_12_mysql_integration_with_python.md": (
        "05_12","MySQL Integration with Python","MySQL",5,"Administration",12,"intermediate",
        ["mysql-connector-python","PyMySQL","SQLAlchemy","connection-pool","cursor","execute","fetchone","fetchall","parameterized-query","ORM","transaction"],
"""
## Topics Covered

### 1. mysql-connector-python
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306,
    user="app_user", password="pass",
    database="mydb"
)
cursor = conn.cursor(dictionary=True)

# Parameterized query (prevents SQL injection)
cursor.execute("SELECT * FROM products WHERE category_id = %s AND price > %s", (2, 10.0))
rows = cursor.fetchall()

# Insert
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Widget", 9.99))
conn.commit()
product_id = cursor.lastrowid

cursor.close()
conn.close()
```

### 2. Connection Pooling
```python
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="mypool", pool_size=5,
    host="localhost", user="user", password="pass", database="mydb"
)

conn = pool.get_connection()
cursor = conn.cursor()
...
conn.close()  # Returns to pool
```

### 3. SQLAlchemy ORM (MySQL)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("mysql+pymysql://user:pass@localhost/mydb", pool_size=10)

class Base(DeclarativeBase): pass

class Product(Base):
    __tablename__ = "products"
    id    = mapped_column(Integer, primary_key=True)
    name  = mapped_column(String(200))
    price = mapped_column(Numeric(10, 2))

with Session(engine) as session:
    product = session.get(Product, 1)
    products = session.scalars(select(Product).where(Product.price > 10)).all()
    session.add(Product(name="New", price=9.99))
    session.commit()
```

### 4. Async MySQL (aiomysql)
```python
import aiomysql, asyncio

async def main():
    pool = await aiomysql.create_pool(host='localhost', user='u', password='p', db='mydb')
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM products LIMIT 10")
            rows = await cur.fetchall()
    pool.close()
    await pool.wait_closed()
```

## Lab
Build a Python product catalog CLI using: raw mysql-connector for CRUD, connection pooling, and SQLAlchemy ORM for complex queries. Include transaction handling for bulk inserts.
"""),
}

for fname, data in mysql_lessons.items():
    if data[0] == "Already real — SKIP":
        print(f"  [SKIP]   {fname}")
        continue
    lid, title, course, mod, mod_title, les, diff, tags, body = data
    path = os.path.join(MY, fname)
    fm = frontmatter(lid, title, course, mod, mod_title, les, diff, tags)
    write_lesson(path, fm + body.strip() + "\n")

print(f"  MySQL stubs filled: {written - w1}")


# ══════════════════════════════════════════════════════════════════
# FINAL REPORT
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("PHASE 2 UPGRADE COMPLETE")
print(f"  Total lessons written/updated: {written}")
print("=" * 60)
