"""
generate_pfs_batch_direct.py
=============================
Direct sub-second batch content generator for Python Full Stack Remaining Batch:
- docker (25 lessons)
- linux (25 lessons)
- react (30 lessons)
- advanced-python (30 lessons)
- python-dsa (25 lessons)
- rest-api (15 lessons)
- auth-jwt (15 lessons)

Seeds missing modules/lessons and populates section notes with bulk collection.
"""
import sys
from datetime import datetime
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

SECTION_TYPES = ["overview", "concept", "syntax", "example", "pitfall", "qa"]

PFS_COURSES = [
    {
        "slug": "docker",
        "title": "Docker & Containerization",
        "hours": 15,
        "modules": [
            {
                "title": "Module 1: Docker Fundamentals",
                "lessons": [
                    "Introduction to Containerization vs VMs",
                    "Installing Docker Engine & Desktop",
                    "Docker Architecture & Daemon",
                    "Working with Docker CLI Commands",
                    "Understanding Docker Images & Registries"
                ]
            },
            {
                "title": "Module 2: Dockerfiles & Custom Images",
                "lessons": [
                    "Writing your First Dockerfile",
                    "FROM, RUN, CMD, and ENTRYPOINT Directives",
                    "Managing Image Layers & Caching",
                    "Multi-Stage Docker Builds",
                    "Optimizing Dockerfile Size & Security"
                ]
            },
            {
                "title": "Module 3: Docker Networking & Storage",
                "lessons": [
                    "Docker Volumes & Bind Mounts",
                    "Persisting Database Data in Docker",
                    "Docker Bridge, Host, and Overlay Networks",
                    "Container Port Mapping & Communication",
                    "Container Inspection & Logging"
                ]
            },
            {
                "title": "Module 4: Multi-Container Apps with Docker Compose",
                "lessons": [
                    "Introduction to docker-compose.yml",
                    "Defining Services, Networks, and Volumes",
                    "Environment Variables & Configuration",
                    "Orchestrating Python Web App + Database",
                    "Docker Compose Commands & Lifecycle"
                ]
            },
            {
                "title": "Module 5: Production Deployment & Best Practices",
                "lessons": [
                    "Docker Security & Non-Root Users",
                    "Container Health Checks & Restart Policies",
                    "Pushing Images to Docker Hub & AWS ECR",
                    "Docker Cleanup & Pruning System Resources",
                    "Building a Complete Python Flask App Container Stack"
                ]
            }
        ]
    },
    {
        "slug": "linux",
        "title": "Linux Systems & Administration",
        "hours": 15,
        "modules": [
            {
                "title": "Module 1: Linux Basics & Navigation",
                "lessons": [
                    "Linux Operating System Architecture & Shell",
                    "Navigating Filesystem (ls, cd, pwd, tree)",
                    "File Operations (cp, mv, rm, mkdir, touch)",
                    "Reading Files (cat, less, head, tail)",
                    "File Searching (find, locate, grep)"
                ]
            },
            {
                "title": "Module 2: Permissions, Users & Groups",
                "lessons": [
                    "Understanding Linux File Permissions (chmod)",
                    "File Ownership & Group Management (chown, chgrp)",
                    "User Administration (useradd, usermod, passwd)",
                    "Sudo Access & Privileged Execution",
                    "File System Hierarchy Standard (FHS)"
                ]
            },
            {
                "title": "Module 3: Process & Resource Management",
                "lessons": [
                    "Viewing Processes (ps, top, htop)",
                    "Managing Process Signal Handling (kill, pkill)",
                    "Background & Foreground Jobs (bg, fg, &)",
                    "Memory & Disk Space Auditing (free, df, du)",
                    "System Monitoring & Log Inspection (journalctl)"
                ]
            },
            {
                "title": "Module 4: Networking & Systemd Services",
                "lessons": [
                    "Network Interfaces & Troubleshooting (ip, ping, netstat, ss)",
                    "Downloading & Transferring Files (curl, wget, scp)",
                    "SSH Remote Access & Key Authentication",
                    "Writing Custom Systemd Service Files",
                    "Managing System Services (systemctl start, stop, enable)"
                ]
            },
            {
                "title": "Module 5: Shell Scripting & Automation",
                "lessons": [
                    "Introduction to Bash Shell Scripting",
                    "Variables, Arguments, and Input",
                    "Control Flow (if, case, loops)",
                    "Scheduling Tasks with Cron & Crontab",
                    "Automating Server Maintenance Scripts"
                ]
            }
        ]
    },
    {
        "slug": "react",
        "title": "React.js Modern Frontend Development",
        "hours": 18,
        "modules": [
            {
                "title": "Module 1: React Fundamentals & JSX",
                "lessons": [
                    "Introduction to Modern Single Page Applications",
                    "Setting up React with Vite",
                    "JSX Syntax & Virtual DOM Mechanics",
                    "Functional Components & Props",
                    "Rendering Lists & Conditional Logic"
                ]
            },
            {
                "title": "Module 2: State Management & Hooks",
                "lessons": [
                    "useState Hook for Local Component State",
                    "Handling Form Inputs & Synthetic Events",
                    "useEffect Hook for Side Effects & Lifecycle",
                    "Custom Hooks Reusability",
                    "useRef Hook for DOM References"
                ]
            },
            {
                "title": "Module 3: Component Communication & Context API",
                "lessons": [
                    "Lifting State Up in Component Trees",
                    "Prop Drilling & Clean Component Hierarchy",
                    "React Context API for Global State",
                    "useContext Hook Pattern",
                    "useReducer for Complex State Management"
                ]
            },
            {
                "title": "Module 4: Routing & API Integration",
                "lessons": [
                    "Client-Side Routing with React Router v6",
                    "Dynamic Route Parameters & Navigation",
                    "Fetching Data with Axios & Fetch API",
                    "Handling Loading, Error, and Success UI States",
                    "React Query / TanStack Query Overview"
                ]
            },
            {
                "title": "Module 5: Advanced Patterns & Optimization",
                "lessons": [
                    "Performance Optimization (useMemo, useCallback)",
                    "React.memo for Component Memoization",
                    "Code Splitting & Lazy Loading (React.lazy, Suspense)",
                    "Form Validation with React Hook Form & Zod",
                    "Building a Complete Full Stack Python-React App UI"
                ]
            },
            {
                "title": "Module 6: Testing & Production Deployment",
                "lessons": [
                    "Component Testing with Vitest & React Testing Library",
                    "Building Production Distribution Bundles",
                    "Deploying React App to Nginx & Vercel",
                    "Handling Environment Variables in Frontend",
                    "Frontend Security & XSS Prevention Best Practices"
                ]
            }
        ]
    },
    {
        "slug": "advanced-python",
        "title": "Advanced Python & Professional Practices",
        "hours": 15,
        "modules": [
            {
                "title": "Module 1: Advanced Object-Oriented Python",
                "lessons": [
                    "Python Data Model & Special Dunder Methods",
                    "Multiple Inheritance & Method Resolution Order (MRO)",
                    "Abstract Base Classes (abc module)",
                    "Properties, Getters, and Setters",
                    "Dataclasses & Pydantic Data Validation"
                ]
            },
            {
                "title": "Module 2: Functional Programming & Metaprogramming",
                "lessons": [
                    "First-Class Functions, Closures, and Higher-Order Functions",
                    "Function & Class Decorators",
                    "Decorators with Arguments & Wraps",
                    "Generators, Yield, and Generator Expressions",
                    "Iterators, Iterables, and Custom Iterators"
                ]
            },
            {
                "title": "Module 3: Memory Management & Context Managers",
                "lessons": [
                    "Python Memory Management & Garbage Collection",
                    "Context Managers & the with Statement",
                    "Creating Context Managers via contextlib",
                    "Weak References & Memory Optimization",
                    "Python Metaclasses & Dynamic Code Execution"
                ]
            },
            {
                "title": "Module 4: Concurrency & Async Programming",
                "lessons": [
                    "Threading vs Multiprocessing in Python",
                    "Global Interpreter Lock (GIL) Deep Dive",
                    "ThreadPoolExecutor & ProcessPoolExecutor",
                    "Asyncio Event Loop, Async/Await Syntax",
                    "Gathering Tasks & Asynchronous I/O Performance"
                ]
            },
            {
                "title": "Module 5: Packaging & Testing Frameworks",
                "lessons": [
                    "Unit Testing with Pytest & Fixtures",
                    "Mocking Dependencies with unittest.mock",
                    "Code Coverage Analysis & Linting (Ruff, Black, Flake8)",
                    "Type Hinting & Static Analysis with Mypy",
                    "Building & Publishing Python Packages to PyPI"
                ]
            },
            {
                "title": "Module 6: Design Patterns in Python",
                "lessons": [
                    "Creational Patterns (Singleton, Factory, Builder)",
                    "Structural Patterns (Adapter, Decorator, Facade)",
                    "Behavioral Patterns (Observer, Strategy, State)",
                    "Clean Architecture & Dependency Injection",
                    "Refactoring Legacy Python Codebases"
                ]
            }
        ]
    },
    {
        "slug": "python-dsa",
        "title": "Data Structures & Algorithms in Python",
        "hours": 16,
        "modules": [
            {
                "title": "Module 1: Algorithm Analysis & Basics",
                "lessons": [
                    "Big O Notation: Time & Space Complexity Analysis",
                    "Array & List Manipulation in Python",
                    "Two-Pointer Technique & Applications",
                    "Sliding Window Algorithm Pattern",
                    "Prefix Sum Arrays & Range Queries"
                ]
            },
            {
                "title": "Module 2: Linear Data Structures",
                "lessons": [
                    "Singly & Doubly Linked List Implementations",
                    "Linked List Fast & Slow Pointer Patterns",
                    "Stack Implementation & Monotonic Stack",
                    "Queue, Deque, and Circular Queue",
                    "Valid Parentheses & Expression Evaluation"
                ]
            },
            {
                "title": "Module 3: Sorting & Searching",
                "lessons": [
                    "Binary Search Algorithm & Variational Problems",
                    "Bubble, Selection, and Insertion Sort",
                    "Merge Sort & Divide and Conquer Strategy",
                    "Quick Sort & Partition Schemes",
                    "Custom Comparators & Python sorting"
                ]
            },
            {
                "title": "Module 4: Non-Linear Data Structures",
                "lessons": [
                    "Binary Trees & Tree Traversals (Inorder, Preorder, Postorder)",
                    "Binary Search Trees (BST) Insertion & Deletion",
                    "Breadth-First Search (BFS) & Depth-First Search (DFS) on Trees",
                    "Heap / Priority Queue & heapq Module",
                    "Hash Tables & Collision Resolution Strategies"
                ]
            },
            {
                "title": "Module 5: Graphs & Dynamic Programming",
                "lessons": [
                    "Graph Representation (Adjacency Matrix & List)",
                    "Graph Traversals (BFS & DFS) and Cycle Detection",
                    "Dijkstra Shortest Path Algorithm",
                    "Introduction to Dynamic Programming (Memoization vs Tabulation)",
                    "Classic DP Problems (Knapsack, Longest Common Subsequence)"
                ]
            }
        ]
    },
    {
        "slug": "rest-api",
        "title": "RESTful API Architecture & Design",
        "hours": 8,
        "modules": [
            {
                "title": "Module 1: REST Principles & Standards",
                "lessons": [
                    "HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)",
                    "REST Architectural Constraints & Statelessness",
                    "Resource Naming Conventions & URL Design",
                    "HTTP Status Codes (2xx, 3xx, 4xx, 5xx)",
                    "API Versioning Strategies (URI, Header, Query)"
                ]
            },
            {
                "title": "Module 2: Request & Response Engineering",
                "lessons": [
                    "Designing Consistent JSON Payload Schemas",
                    "Pagination, Sorting, and Filtering Patterns",
                    "Global Error Handling & RFC 7807 Problem Details",
                    "Handling File Uploads & Multipart Requests",
                    "API Rate Limiting & Throttling Strategies"
                ]
            },
            {
                "title": "Module 3: Documentation & Testing",
                "lessons": [
                    "OpenAPI / Swagger Specification Standard",
                    "Contract-First vs Code-First API Design",
                    "API Integration Testing with Postman & Pytest",
                    "CORS (Cross-Origin Resource Sharing) Configuration",
                    "Building a Production REST API with Python"
                ]
            }
        ]
    },
    {
        "slug": "auth-jwt",
        "title": "Authentication, Authorization & JWT",
        "hours": 8,
        "modules": [
            {
                "title": "Module 1: Authentication Fundamentals",
                "lessons": [
                    "Session-Based vs Token-Based Authentication",
                    "Password Hashing Standards (Bcrypt, Argon2)",
                    "Secure Storage of Credentials in Databases",
                    "OAuth 2.0 & OpenID Connect Fundamentals",
                    "Multi-Factor Authentication (MFA/TOTP) Mechanics"
                ]
            },
            {
                "title": "Module 2: JSON Web Tokens (JWT) Deep Dive",
                "lessons": [
                    "JWT Structure: Header, Payload, and Signature",
                    "Signing Algorithms (HS256 vs RS256)",
                    "Access Tokens vs Refresh Tokens Strategy",
                    "Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)",
                    "Token Revocation & Blacklisting Strategies"
                ]
            },
            {
                "title": "Module 3: Authorization & Security Best Practices",
                "lessons": [
                    "Role-Based Access Control (RBAC) Architecture",
                    "Attribute-Based Access Control (ABAC) Fundamentals",
                    "Securing REST Endpoints & Middleware Interceptors",
                    "CSRF Protection & Security Headers (CSP, HSTS)",
                    "Building a Complete Python Security Auth Microservice"
                ]
            }
        ]
    }
]

def generate_pfs_batch():
    with app.app_context():
        # Pre-fetch all existing section pairs to avoid N+1 queries
        existing_section_pairs = set(
            db.session.query(LessonSection.lesson_id, LessonSection.section_type).all()
        )

        total_lessons_published = 0
        sections_to_insert = []

        for cdata in PFS_COURSES:
            slug = cdata["slug"]
            course = Course.query.filter_by(slug=slug, is_deleted=False).first()
            if not course:
                course = Course(
                    slug=slug,
                    title=cdata["title"],
                    summary=f"Comprehensive master course on {cdata['title']}.",
                    status="published",
                    estimated_hours=cdata["hours"],
                    created_by=1
                )
                db.session.add(course)
                db.session.commit()

            course.title = cdata["title"]
            course.status = "published"
            course.estimated_hours = cdata["hours"]
            db.session.commit()

            existing_modules = {m.title: m for m in course.modules.all()}

            for m_idx, mdata in enumerate(cdata["modules"], start=1):
                mod_title = mdata["title"]
                module = existing_modules.get(mod_title)
                if not module:
                    module = Module(
                        course_id=course.id,
                        title=mod_title,
                        slug=mod_title.lower().replace(":", "").replace("&", "and").replace(" ", "-"),
                        sort_order=m_idx
                    )
                    db.session.add(module)
                    db.session.commit()

                existing_lessons = {l.title: l for l in module.lessons.filter_by(is_deleted=False).all()}

                for l_idx, ltitle in enumerate(mdata["lessons"], start=1):
                    lesson = existing_lessons.get(ltitle)
                    l_slug = ltitle.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(",", "").replace("/", "-").replace("&", "and")

                    if not lesson:
                        lesson = Lesson(
                            module_id=module.id,
                            title=ltitle,
                            slug=l_slug,
                            summary=f"Technical lesson covering {ltitle} in {course.title}.",
                            status="published",
                            sort_order=l_idx,
                            estimated_minutes=20,
                            difficulty_level="intermediate",
                            created_by=1
                        )
                        db.session.add(lesson)
                        db.session.commit()

                    lesson.status = "published"
                    total_lessons_published += 1

                    for s_idx, stype in enumerate(SECTION_TYPES, start=1):
                        if (lesson.id, stype) in existing_section_pairs:
                            continue

                        stitle = stype.capitalize()
                        if stype == "qa": stitle = "Q & A"
                        elif stype == "concept": stitle = "Core Concept"

                        md = f"### {stitle}: {lesson.title}\n\nComprehensive technical guide, implementation patterns, and industry best practices for {lesson.title} in {course.title}."
                        if stype == "syntax":
                            if "python" in slug or "advanced-python" in slug or "dsa" in slug:
                                md += f"\n\n```python\n# Code syntax for {lesson.title}\ndef solve_{lesson.slug.replace('-', '_')}(data: list) -> dict:\n    \"\"\"Implementation logic for {lesson.title}.\"\"\"\n    return {{\n        'status': 'success',\n        'processed': len(data)\n    }}\n```"
                            elif "react" in slug:
                                md += f"\n\n```jsx\n// React component snippet for {lesson.title}\nimport React, {{ useState }} from 'react';\n\nexport const {lesson.title.replace(' ', '')}Component = () => {{\n  const [state, setState] = useState(null);\n  return <div className=\"p-4 bg-slate-900 text-white\">{lesson.title} Ready</div>;\n}};\n```"
                            elif "docker" in slug:
                                md += f"\n\n```dockerfile\n# Docker configuration snippet for {lesson.title}\nFROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD [\"python\", \"app.py\"]\n```"
                            elif "linux" in slug:
                                md += f"\n\n```bash\n#!/bin/bash\n# Linux shell command reference for {lesson.title}\necho \"Executing {lesson.title}...\"\nsudo systemctl status nginx\n```"
                            else:
                                md += f"\n\n```json\n{{\n  \"endpoint\": \"/api/v1/{lesson.slug}\",\n  \"status\": 200,\n  \"message\": \"{lesson.title} operation successful\"\n}}\n```"
                        elif stype == "example":
                            md += f"\n\n```python\n# Practical test example for {lesson.title}\nif __name__ == '__main__':\n    print('Validating {lesson.title} execution...')\n```"
                        elif stype == "pitfall":
                            md += f"\n\n1. Inadequate error handling & unhandled exception propagation.\n2. Overlooking memory footprint and resource leak possibilities.\n3. Missing automated unit/integration test assertions."
                        elif stype == "qa":
                            md += f"\n\n**Q1: What is the primary objective of {lesson.title}?**\nA: Provides robust, scalable, and maintainable implementation of {lesson.title} in production software environments."

                        sec = LessonSection(
                            lesson_id=lesson.id,
                            section_type=stype,
                            title=stitle,
                            content_markdown=md,
                            content_html="",
                            sort_order=s_idx,
                            is_visible=True,
                            created_at=datetime.utcnow(),
                            updated_at=datetime.utcnow()
                        )
                        sections_to_insert.append(sec)

            db.session.commit()
            print(f"  [COMPLETED] {course.title}: Modules & lessons checked/seeded.")

        if sections_to_insert:
            print(f"Bulk saving {len(sections_to_insert)} LessonSection objects to DB...")
            db.session.bulk_save_objects(sections_to_insert)
            db.session.commit()

        print(f"\n===================================================================================")
        print(f"  BATCH COMPLETED: Published {total_lessons_published} lessons across {len(PFS_COURSES)} courses!")
        print(f"  Total Section Notes Created/Updated: {len(sections_to_insert)}")
        print(f"===================================================================================")

if __name__ == "__main__":
    generate_pfs_batch()
