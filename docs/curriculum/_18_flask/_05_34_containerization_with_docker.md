# Containerization with Docker

> **Course**: Flask | **Module**: Production Deployment | **Difficulty**: advanced

---

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

---

Containerize a Flask + SQLAlchemy app with Docker Compose. Include Nginx as a separate service, environment variables via `.env`, and a `/health` endpoint. Run migrations on startup using `entrypoint.sh`.

---
