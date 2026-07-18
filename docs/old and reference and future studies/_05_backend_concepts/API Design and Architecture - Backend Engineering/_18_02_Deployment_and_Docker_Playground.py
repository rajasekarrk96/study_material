# %% [markdown]
# # Topic 18: Deployment & Docker Playground
# In this playground, we won't run Python code. Instead, this script will programmatically
# generate a production-grade **Dockerfile** and a **docker-compose.yml** file in your workspace.
#
# It also provides a complete Cheat Sheet of the Docker commands you need to know
# to build, run, and orchestrate your API.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above the code block to generate the files.

# %%
import os

# Define paths
base_dir = r"c:\Users\rajas\OneDrive\_00_a_study\_05_backend_concepts\API Design and Architecture - Backend Engineering"
dockerfile_path = os.path.join(base_dir, "Dockerfile")
docker_compose_path = os.path.join(base_dir, "docker-compose.yml")

# 1. Define the Dockerfile content
dockerfile_content = """# --- STAGE 1: Build dependencies ---
FROM python:3.11-slim as builder

WORKDIR /app

# Install compilation tools (required for some Python packages like psycopg2 or cryptography)
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential

# We mock a requirements file for now
RUN echo "fastapi\\nuvicorn\\npydantic\\nemail-validator\\npython-jose[cryptography]\\npasslib[bcrypt]\\nredis\\nsqlalchemy" > requirements.txt

# Install dependencies to a local directory
RUN pip install --user --no-cache-dir -r requirements.txt

# --- STAGE 2: Run the application ---
FROM python:3.11-slim as runner

WORKDIR /app

# Copy installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
# Copy the application folder (when you build your app, make sure it's in the same directory)
# COPY ./app ./app

# Add local bin to path so we can run uvicorn
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Run as a secure, non-root user
RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Start Uvicorn. In production, we use multiple worker processes.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# 2. Define the docker-compose.yml content
docker_compose_content = """version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      # Mounts your local 'app' directory into the container.
      # This enables "Hot Reloading" - when you edit code locally, the container updates instantly!
      - ./app:/app/app
    environment:
      - DATABASE_URL=postgresql://postgres:postgres123@db:5432/ecommerce
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    container_name: postgres_db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres123
      - POSTGRES_DB=ecommerce
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    container_name: redis_cache
    ports:
      - "6379:6379"

volumes:
  postgres_data:
"""

# Write the files
with open(dockerfile_path, "w") as f:
    f.write(dockerfile_content)

with open(docker_compose_path, "w") as f:
    f.write(docker_compose_content)

print("Successfully generated:")
print(f"1. {dockerfile_path}")
print(f"2. {docker_compose_path}")

# %% [markdown]
# ## Docker Command Cheat Sheet
#
# Open your terminal in the directory containing these files and run the following commands:
#
# ### 1. Build the Docker Image
# Builds your Dockerfile and tags it as `ecommerce-api:latest`.
# ```bash
# docker build -t ecommerce-api:latest .
# ```
#
# ### 2. Run a Single Container
# Runs the built image, mapping port 8000 of your machine to port 8000 of the container.
# ```bash
# docker run -d -p 8000:8000 --name my-running-api ecommerce-api:latest
# ```
#
# ### 3. Orchestrate the Entire Stack (FastAPI + Postgres + Redis)
# Builds the API image and spins up all three services in the background.
# ```bash
# docker compose up -d
# ```
#
# ### 4. Check Logs of the Stack
# Follows the logs of all running containers in real-time.
# ```bash
# docker compose logs -f
# ```
#
# ### 5. Stop the Stack
# Stops and removes all containers, keeping database data safe in the volume.
# ```bash
# docker compose down
# ```
