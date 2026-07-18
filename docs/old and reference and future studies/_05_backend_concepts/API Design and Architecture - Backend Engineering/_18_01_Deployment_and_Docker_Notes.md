# Module 10: Deployment
## Topic 18: Containerization with Docker & Production Best Practices

---

### 1. The Big Picture

#### What is Docker & Containerization?
**Containerization** is the packaging of software code with just the operating system (OS) libraries and dependencies required to run it, into a single lightweight executable called a **Container**.

**Docker** is the industry-standard platform used to create, deploy, and run containers.

#### Why Companies Use Docker
1. **Consistency:** "Works on my machine" is solved. The container runs the exact same way on a developer's laptop, a staging environment, and a production Kubernetes cluster in the cloud.
2. **Isolation:** Multiple applications running on the same server are kept completely isolated. They cannot interfere with each other's files, memory, or ports.
3. **Efficiency:** Containers share the host OS kernel, making them much faster to start and consuming far less RAM/CPU compared to traditional Virtual Machines (VMs).

```
    VIRTUAL MACHINES (VMs)                      DOCKER CONTAINERS

 ┌──────────────┐ ┌──────────────┐             ┌──────────────┐ ┌──────────────┐
 │    App A     │ │    App B     │             │    App A     │ │    App B     │
 ├──────────────┼───────────────┤             ├──────────────┼───────────────┤
 │  Libs/Bins   │ │  Libs/Bins   │             │  Libs/Bins   │ │  Libs/Bins   │
 ├──────────────┼───────────────┤             ├──────────────┴───────────────┤
 │   Guest OS   │ │   Guest OS   │             │        Docker Engine         │
 ├──────────────┼───────────────┤             ├──────────────────────────────┤
 │  Hypervisor  │  Hypervisor   │             │           Host OS            │
 ├──────────────┴───────────────┤             ├──────────────────────────────┤
 │          Host Hardware       │             │        Host Hardware         │
 └──────────────────────────────┘             └──────────────────────────────┘
```

---

### 2. Core Docker Concepts
* **Dockerfile:** A text file containing a list of instructions on how to build a Docker Image.
* **Image:** A read-only template with instructions for creating a Docker container. Think of it as the compiled "class" file.
* **Container:** A runnable instance of an image. Think of it as the "object" instantiated from the class.
* **Docker Compose:** A tool for defining and running multi-container Docker applications (e.g., spinning up your API, database, and Redis cache together using a single YAML file).

---

### 3. Production-Grade Dockerfile for FastAPI
A production Dockerfile should use a **Multi-Stage Build** to keep the final image size as small as possible (improving deployment speed and reducing security attack surfaces).

```dockerfile
# --- STAGE 1: Builder ---
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies if needed (e.g., gcc)
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential

COPY requirements.txt .

# Install wheels to a local directory
RUN pip install --user --no-cache-dir -r requirements.txt

# --- STAGE 2: Final Production Image ---
FROM python:3.11-slim as runner

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /root/.local /root/.local
COPY ./app ./app

ENV PATH=/root/.local/bin:$PATH

# Run as non-root user for security!
RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Start Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

---

### 4. Docker Compose for Local Development
A `docker-compose.yml` file allows you to spin up your entire stack with a single command: `docker compose up`.

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres123@db:5432/shop
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres123
      - POSTGRES_DB=shop
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - 6379:6379

volumes:
  postgres_data:
```

---

### 5. Hands-on Workout & Assessment

#### Part A: Deployment Challenge (Docker Security)
A junior developer writes a Dockerfile using `FROM python:3.11` (which is a full Debian image of ~1GB) and runs the container as `root`.
- Identify two issues with this approach.
- Explain how you would fix them using best practices (image size and security).

#### Part B: Quiz
1. What is the difference between a Docker Image and a Docker Container?
   A. An image is a running instance of a container.
   B. An image is a read-only blueprint; a container is a live, running instance of that blueprint.
   C. Images are only for databases; containers are only for code.
   D. There is no difference.
2. Why do we use volumes in Docker Compose for databases (e.g. `- postgres_data:/var/lib/postgresql/data`)?
   A. To make the database run faster.
   B. To ensure data is persisted on the host machine and not lost when the database container is stopped or deleted.
   C. To encrypt the database files.
   D. To allow multiple databases to share the same port.
3. What is a multi-stage build in a Dockerfile?
   A. A build that runs on multiple servers.
   B. A technique to write multiple Dockerfiles.
   C. A method to use multiple `FROM` statements in a single Dockerfile to separate the build environment from the final runtime environment, reducing the final image size.
   D. A deployment strategy.

---

### 6. Progress Tracker

* **Module 10: Deployment:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---
