"""
seed_new_courses_structure.py
==============================
Learning OS — Seed Module + Lesson Structure for 25 New Stub Courses

Workflow:
  STEP 1 — Audit existing course
  STEP 2 — Generate missing Modules
  STEP 3 — Generate missing Lessons (status=pending)
  STEP 4 — Generate placeholder LessonSection stubs
  STEP 5 — Print course metadata summary
  STEP 6 — STOP (no content generated)

Usage:
  python scripts/seed_new_courses_structure.py              # all 25 courses
  python scripts/seed_new_courses_structure.py --course docker
  python scripts/seed_new_courses_structure.py --audit-only
"""
import sys, re, argparse
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection

app = create_app()

PLACEHOLDER_SECTIONS = [
    ("overview",    "Overview",              1),
    ("objectives",  "Learning Objectives",   2),
    ("concept",     "Theory / Concept",      3),
    ("syntax",      "Syntax & API",          4),
    ("example",     "Worked Example",        5),
    ("pitfall",     "Common Mistakes",       6),
    ("exercise",    "Exercise",              7),
    ("quiz",        "Quiz",                  8),
    ("summary",     "Summary & Cheat Sheet", 9),
    ("references",  "References",           10),
]


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


# =============================================================================
# CURRICULUM SPEC — 25 New Courses
# Format per module: (title, slug, [(lesson_title, est_minutes, description)])
# =============================================================================

CURRICULUM = {

    # ─── PRIORITY 1: Used by 2+ Paths ────────────────────────────────────────

    # ── DOCKER (5 paths) ─────────────────────────────────────────────────────
    "docker": {
        "title": "Docker",
        "domain": "DevOps / Containers",
        "difficulty": "Intermediate",
        "estimated_hours": 20,
        "modules": [
            ("Docker Fundamentals", "docker-fundamentals", [
                ("What Is Docker and Why Containers", 20, "Container vs VM, Docker daemon, Docker Hub."),
                ("Installing Docker", 20, "Docker Desktop on Windows/Mac, Docker Engine on Linux."),
                ("Docker Architecture", 20, "Daemon, client, registry, images, containers."),
                ("Running Your First Container", 15, "docker run hello-world, pulling images."),
                ("Docker CLI Essentials", 25, "run, ps, stop, rm, images, pull, push."),
            ]),
            ("Docker Images", "docker-images", [
                ("Dockerfile Syntax", 25, "FROM, RUN, COPY, WORKDIR, ENV, EXPOSE, CMD, ENTRYPOINT."),
                ("Building Images", 20, "docker build, tagging, layer caching."),
                ("Multi-Stage Builds", 25, "Optimizing image size with multi-stage Dockerfiles."),
                ("Pushing to Docker Hub", 15, "docker login, tag, push to registry."),
                ("Image Best Practices", 20, "Minimal base images, .dockerignore, non-root user."),
            ]),
            ("Containers", "containers", [
                ("Container Lifecycle", 20, "create, start, stop, restart, remove."),
                ("Port Mapping and Volumes", 25, "Exposing ports (-p), bind mounts, named volumes."),
                ("Environment Variables", 15, "Passing config with --env and .env files."),
                ("Container Networking", 25, "Bridge, host, none networks; container communication."),
                ("Logging and Debugging", 20, "docker logs, exec, inspect, stats."),
            ]),
            ("Docker Compose", "docker-compose", [
                ("Docker Compose Overview", 20, "YAML service definitions, why Compose."),
                ("Writing docker-compose.yml", 25, "services, ports, volumes, environment, depends_on."),
                ("Multi-Service Applications", 25, "Flask + MySQL + Nginx with Compose."),
                ("Compose Networking", 20, "Custom networks, service discovery."),
                ("Compose Commands", 15, "up, down, build, logs, exec, scale."),
            ]),
            ("Docker in Production", "docker-in-production", [
                ("Docker with CI/CD", 25, "Building and pushing images in GitHub Actions."),
                ("Docker Secrets and Configs", 20, "Secure credentials in Docker Swarm."),
                ("Health Checks", 20, "HEALTHCHECK in Dockerfile and Compose."),
                ("Resource Limits", 15, "CPU and memory constraints."),
                ("Docker Registry Setup", 20, "Running a private Docker registry."),
            ]),
        ],
    },

    # ── ADVANCED PYTHON (4 paths) ─────────────────────────────────────────────
    "advanced-python": {
        "title": "Advanced Python",
        "domain": "Python",
        "difficulty": "Intermediate",
        "estimated_hours": 30,
        "modules": [
            ("Python Internals", "python-internals", [
                ("Python Object Model", 20, "Everything is an object — id, type, value."),
                ("Memory Management and GC", 25, "Reference counting, garbage collector, memory profiling."),
                ("Python Bytecode", 20, "dis module, .pyc files, CPython internals."),
                ("Global Interpreter Lock", 20, "What GIL is, implications for concurrency."),
                ("Python Data Model", 25, "Dunder methods, operator overloading."),
            ]),
            ("Functional Programming", "functional-programming", [
                ("First-Class Functions", 20, "Functions as objects, passing and returning functions."),
                ("Closures and Nonlocal", 20, "Closure scope, nonlocal keyword."),
                ("Decorators", 30, "Function decorators, stacking decorators, decorator factories."),
                ("Generators and Yield", 25, "Generator functions, yield from, lazy evaluation."),
                ("Itertools and Functools", 20, "map, filter, reduce, partial, lru_cache."),
            ]),
            ("OOP Advanced", "oop-advanced", [
                ("Magic Methods Deep Dive", 25, "__str__, __repr__, __len__, __getitem__, __contains__."),
                ("Class Methods and Static Methods", 20, "@classmethod, @staticmethod, when to use each."),
                ("Properties and Descriptors", 25, "@property, setter, deleter, descriptor protocol."),
                ("Metaclasses", 30, "type(), __new__, __init_subclass__, metaclass use cases."),
                ("Abstract Base Classes", 20, "abc module, ABCMeta, @abstractmethod."),
            ]),
            ("Concurrency", "concurrency-python", [
                ("Threading", 25, "Thread class, daemon threads, thread safety."),
                ("Multiprocessing", 25, "Process, Pool, shared memory, IPC."),
                ("Asyncio", 30, "Event loop, coroutines, async/await, tasks."),
                ("Concurrent Futures", 20, "ThreadPoolExecutor, ProcessPoolExecutor."),
                ("Asyncio Advanced Patterns", 25, "aiohttp, asyncpg, async context managers."),
            ]),
            ("Python Packaging and Tools", "python-packaging", [
                ("Virtual Environments", 15, "venv, pipenv, poetry, pyproject.toml."),
                ("Writing Python Packages", 25, "setup.py vs pyproject.toml, package structure."),
                ("Publishing to PyPI", 20, "twine, TestPyPI, versioning."),
                ("Type Hints and Mypy", 20, "PEP 484, TypeVar, Protocol, runtime checking."),
                ("Testing with Pytest", 25, "fixtures, parametrize, markers, coverage."),
            ]),
            ("Advanced Patterns", "advanced-patterns-python", [
                ("Context Managers", 20, "__enter__, __exit__, contextlib."),
                ("Design Patterns in Python", 25, "Singleton, Factory, Observer, Strategy."),
                ("Data Classes", 20, "@dataclass, field(), frozen, slots."),
                ("Protocol and Structural Subtyping", 20, "Duck typing, Protocol class, runtime_checkable."),
                ("Python Performance Optimization", 25, "profiling, caching, slots, C extensions."),
            ]),
        ],
    },

    # ── LINUX ADMINISTRATION (2 paths) ────────────────────────────────────────
    "linux": {
        "title": "Linux Administration",
        "domain": "Linux / DevOps",
        "difficulty": "Beginner",
        "estimated_hours": 25,
        "modules": [
            ("Linux Fundamentals", "linux-fundamentals", [
                ("What Is Linux and Distributions", 20, "Kernel, shell, distributions: Ubuntu, CentOS, Debian."),
                ("File System Hierarchy", 20, "/, /home, /etc, /var, /usr, /tmp, /proc."),
                ("Basic Commands", 25, "ls, cd, pwd, mkdir, rm, cp, mv, cat, echo."),
                ("File Permissions", 25, "chmod, chown, umask, rwx notation, octal."),
                ("Users and Groups", 20, "useradd, passwd, groupadd, sudo, /etc/passwd."),
            ]),
            ("Shell and Navigation", "shell-navigation", [
                ("Shell Basics", 20, "bash, sh, zsh — prompts, history, aliases."),
                ("File Viewing and Searching", 20, "cat, less, head, tail, grep, find, locate."),
                ("Pipes and Redirection", 20, "stdout, stderr, stdin, |, >, >>, 2>, /dev/null."),
                ("Text Processing", 25, "awk, sed, cut, sort, uniq, wc, tr."),
                ("Wildcards and Globbing", 15, "*, ?, [], brace expansion, parameter expansion."),
            ]),
            ("Process Management", "process-management", [
                ("Processes and Jobs", 20, "ps, top, htop, kill, pkill, &, jobs, bg, fg."),
                ("Systemd Services", 25, "systemctl, journalctl, .service files, enable/disable."),
                ("Cron Jobs", 20, "crontab -e, cron syntax, /etc/cron.d."),
                ("Log Management", 20, "/var/log, syslog, logrotate, journalctl."),
                ("System Monitoring", 20, "df, du, free, vmstat, iostat, lsof."),
            ]),
            ("Networking", "linux-networking", [
                ("Network Basics", 20, "IP, subnet, gateway, DNS — ip addr, ifconfig."),
                ("Network Tools", 25, "ping, traceroute, netstat, ss, nmap, curl, wget."),
                ("SSH", 20, "ssh, scp, ssh-keygen, authorized_keys, config file."),
                ("Firewall with UFW/iptables", 20, "UFW allow/deny, iptables basics."),
                ("DNS and /etc/hosts", 15, "Host resolution, /etc/resolv.conf, dig, nslookup."),
            ]),
            ("Package and System Management", "package-management", [
                ("APT Package Manager", 20, "apt install, update, upgrade, remove, search."),
                ("YUM and DNF", 15, "RHEL/CentOS package management."),
                ("Environment Variables", 20, "export, .bashrc, .bash_profile, PATH, source."),
                ("Disk Management", 20, "fdisk, lsblk, mount, umount, fstab."),
                ("Linux Security Basics", 20, "SSH hardening, fail2ban, sudo policies."),
            ]),
        ],
    },

    # ── REACT.JS (2 paths) ────────────────────────────────────────────────────
    "react": {
        "title": "React.js",
        "domain": "Frontend",
        "difficulty": "Intermediate",
        "estimated_hours": 35,
        "modules": [
            ("React Fundamentals", "react-fundamentals", [
                ("What Is React and Why", 15, "Component model, virtual DOM, SPA concept."),
                ("Create React App and Vite", 20, "Scaffolding a React project."),
                ("JSX Syntax", 20, "JSX rules, expressions, fragments, comments."),
                ("Functional Components", 20, "Arrow function components, props, children."),
                ("Props and PropTypes", 20, "Passing data, default props, PropTypes validation."),
            ]),
            ("State and Events", "state-events", [
                ("useState Hook", 25, "State declaration, updating, derived state."),
                ("Event Handling", 20, "onClick, onChange, onSubmit, synthetic events."),
                ("Controlled Components", 20, "Forms with controlled inputs."),
                ("Lifting State Up", 20, "Sharing state between sibling components."),
                ("Conditional Rendering", 15, "&&, ternary, early return patterns."),
            ]),
            ("Component Patterns", "component-patterns", [
                ("Lists and Keys", 20, ".map(), unique keys, list rendering."),
                ("Component Composition", 20, "children prop, render props, compound components."),
                ("useEffect Hook", 30, "Side effects, dependencies, cleanup functions."),
                ("useRef Hook", 20, "DOM refs, storing mutable values."),
                ("Custom Hooks", 25, "Extracting reusable stateful logic."),
            ]),
            ("Advanced Hooks and Context", "hooks-context", [
                ("useContext Hook", 25, "Context API, createContext, Provider, Consumer."),
                ("useReducer Hook", 25, "Complex state logic, reducer pattern."),
                ("useMemo and useCallback", 20, "Performance optimization, memoization."),
                ("Context vs Props", 15, "When to use each pattern."),
                ("Error Boundaries", 20, "Catching rendering errors, fallback UI."),
            ]),
            ("React Router", "react-router", [
                ("React Router Setup", 20, "BrowserRouter, Routes, Route, Link."),
                ("Dynamic Routes", 20, "URL params, useParams, nested routes."),
                ("Navigation and Redirects", 15, "useNavigate, Navigate component."),
                ("Protected Routes", 25, "Auth guards, redirect to login."),
                ("Query Strings", 15, "useSearchParams, URL state."),
            ]),
            ("API Integration", "react-api-integration", [
                ("Fetch API in React", 25, "useEffect + fetch, loading/error states."),
                ("Axios in React", 20, "axios instance, interceptors, base URL."),
                ("React Query Basics", 25, "useQuery, useMutation, caching."),
                ("Forms with React Hook Form", 25, "register, handleSubmit, validation."),
                ("Full CRUD with Flask API", 30, "GET, POST, PUT, DELETE with React frontend."),
            ]),
        ],
    },

    # ── REST API DEVELOPMENT ─────────────────────────────────────────────────
    "rest-api": {
        "title": "REST API Development",
        "domain": "Backend",
        "difficulty": "Intermediate",
        "estimated_hours": 15,
        "modules": [
            ("REST Fundamentals", "rest-fundamentals", [
                ("What Is REST", 15, "REST constraints, statelessness, uniform interface."),
                ("HTTP Methods and Status Codes", 20, "GET, POST, PUT, PATCH, DELETE — 200, 201, 400, 401, 404, 500."),
                ("URL Design Best Practices", 20, "Resources, nouns, versioning (/api/v1/), query params."),
                ("Request and Response Format", 15, "JSON body, headers, Content-Type, Accept."),
                ("REST vs GraphQL vs gRPC", 15, "When to choose each API style."),
            ]),
            ("API Design", "api-design", [
                ("Resource Naming Conventions", 15, "Plural nouns, nested resources, filtering."),
                ("Pagination Patterns", 20, "Offset, cursor, page-based pagination."),
                ("Error Response Design", 20, "Consistent error schema, error codes, messages."),
                ("API Versioning Strategies", 15, "URL, header, query param versioning."),
                ("HATEOAS", 15, "Hypermedia links in API responses."),
            ]),
            ("API Documentation", "api-documentation", [
                ("OpenAPI and Swagger", 25, "openapi.yaml spec, Swagger UI, ReDoc."),
                ("FastAPI Auto Docs", 20, "Automatic /docs and /redoc in FastAPI."),
                ("Postman Collections", 20, "Documenting and sharing API with Postman."),
                ("API Changelog", 10, "Managing breaking changes and deprecation."),
                ("API Mocking", 15, "Mock servers for frontend development."),
            ]),
        ],
    },

    # ── AUTH & JWT ────────────────────────────────────────────────────────────
    "auth-jwt": {
        "title": "Authentication and JWT",
        "domain": "Backend Security",
        "difficulty": "Intermediate",
        "estimated_hours": 15,
        "modules": [
            ("Authentication Concepts", "auth-concepts", [
                ("Authentication vs Authorization", 15, "Who are you vs what can you do."),
                ("Session-Based Authentication", 20, "Server-side sessions, cookies."),
                ("Token-Based Authentication", 20, "Stateless auth, token storage."),
                ("OAuth2 Flows Overview", 20, "Authorization code, client credentials, implicit."),
                ("SSO and SAML", 15, "Enterprise single sign-on concepts."),
            ]),
            ("JWT in Depth", "jwt-in-depth", [
                ("JWT Structure", 20, "Header, payload, signature — base64url encoding."),
                ("Signing Algorithms", 20, "HS256, RS256, ES256 — when to use each."),
                ("Access and Refresh Tokens", 25, "Short-lived access, long-lived refresh, rotation."),
                ("JWT Claims", 15, "iss, sub, aud, exp, iat, nbf, custom claims."),
                ("JWT Security Pitfalls", 20, "alg:none attack, key confusion, token leakage."),
            ]),
            ("Implementation", "auth-implementation", [
                ("JWT with Flask", 25, "flask-jwt-extended, protected routes."),
                ("JWT with FastAPI", 25, "python-jose, OAuth2PasswordBearer, Depends."),
                ("Role-Based Access Control", 25, "Roles, permissions, route guards."),
                ("Password Hashing", 15, "bcrypt, Argon2, never store plaintext."),
                ("Auth Best Practices Checklist", 15, "HTTPS, secure cookies, token expiry, CORS."),
            ]),
        ],
    },

    # ─── PRIORITY 2: Java Full Stack ──────────────────────────────────────────

    # ── SERVLET & JSP ─────────────────────────────────────────────────────────
    "servlet-jsp": {
        "title": "Servlet and JSP",
        "domain": "Java Web",
        "difficulty": "Intermediate",
        "estimated_hours": 20,
        "modules": [
            ("Servlet Basics", "servlet-basics", [
                ("Web Application Architecture", 15, "Client-server, HTTP, web containers."),
                ("Servlet Lifecycle", 20, "init, service, destroy — HttpServlet."),
                ("Handling GET and POST", 20, "doGet(), doPost(), request, response."),
                ("Request and Response Objects", 20, "getParameter, getReader, setContentType."),
                ("Session Management", 25, "HttpSession, cookies, URL rewriting."),
            ]),
            ("JSP", "jsp", [
                ("JSP Basics", 20, "Scriptlets, expressions, declarations."),
                ("JSP Directives and Actions", 20, "page, include, taglib directives, jsp:include."),
                ("JSTL Core Tags", 25, "c:if, c:forEach, c:set, c:out."),
                ("EL Expression Language", 20, "EL syntax, implicit objects, beans."),
                ("MVC with Servlet and JSP", 25, "Servlet as controller, JSP as view, Model bean."),
            ]),
            ("Deployment", "servlet-deployment", [
                ("Apache Tomcat Setup", 20, "Installing, configuring, deploying WAR."),
                ("web.xml Configuration", 20, "Servlet mapping, filters, listeners."),
                ("Filters and Listeners", 20, "Pre/post-processing, application lifecycle events."),
                ("Error Handling in Servlets", 15, "Error pages, exception handling."),
                ("Servlet Best Practices", 15, "Thread safety, resource management."),
            ]),
        ],
    },

    # ── SPRING FRAMEWORK ─────────────────────────────────────────────────────
    "spring": {
        "title": "Spring Framework",
        "domain": "Java Backend",
        "difficulty": "Intermediate",
        "estimated_hours": 25,
        "modules": [
            ("Spring Core", "spring-core", [
                ("Spring Framework Overview", 15, "Spring ecosystem, modules, why Spring."),
                ("IoC and Dependency Injection", 25, "Inversion of control, DI types, benefits."),
                ("Spring Bean and ApplicationContext", 25, "Bean lifecycle, ApplicationContext vs BeanFactory."),
                ("XML vs Annotation Configuration", 20, "@Component, @Autowired, @Bean, @Configuration."),
                ("Component Scanning", 15, "@ComponentScan, stereotype annotations."),
            ]),
            ("Spring AOP", "spring-aop", [
                ("AOP Concepts", 20, "Aspect, advice, pointcut, join point, weaving."),
                ("Advice Types", 20, "@Before, @After, @Around, @AfterReturning, @AfterThrowing."),
                ("Pointcut Expressions", 20, "execution(), within(), @annotation() expressions."),
                ("Logging with AOP", 25, "Cross-cutting concern: method logging."),
                ("Transaction Management with AOP", 20, "Declarative @Transactional."),
            ]),
            ("Spring JDBC", "spring-jdbc", [
                ("JdbcTemplate", 25, "query, update, batchUpdate — eliminating boilerplate."),
                ("NamedParameterJdbcTemplate", 20, "Named params vs positional params."),
                ("RowMapper and ResultSetExtractor", 20, "Mapping result sets to objects."),
                ("Spring Transaction Management", 25, "@Transactional, propagation, isolation."),
                ("Spring Data Access Exception", 15, "Exception hierarchy, checked to unchecked."),
            ]),
        ],
    },

    # ── SPRING BOOT ──────────────────────────────────────────────────────────
    "spring-boot": {
        "title": "Spring Boot",
        "domain": "Java Backend",
        "difficulty": "Intermediate",
        "estimated_hours": 30,
        "modules": [
            ("Spring Boot Introduction", "spring-boot-intro", [
                ("What Is Spring Boot", 15, "Auto-configuration, starters, opinionated defaults."),
                ("Creating a Project with Spring Initializr", 20, "Dependencies, project structure."),
                ("Spring Boot Application Structure", 20, "Main class, application.properties, layers."),
                ("Auto-Configuration", 20, "Conditional beans, @EnableAutoConfiguration."),
                ("Spring Boot DevTools", 15, "Hot reload, LiveReload, Developer experience."),
            ]),
            ("REST API with Spring Boot", "spring-boot-rest", [
                ("@RestController and @RequestMapping", 20, "Exposing REST endpoints."),
                ("@GetMapping, @PostMapping, @PutMapping, @DeleteMapping", 20, "CRUD REST methods."),
                ("Request Body and Path Variables", 20, "@RequestBody, @PathVariable, @RequestParam."),
                ("Response Entity and HTTP Status", 20, "Returning proper status codes."),
                ("Exception Handling with @ControllerAdvice", 25, "Global error handler."),
            ]),
            ("Data Layer", "spring-boot-data", [
                ("Spring Data JPA", 25, "JpaRepository, CRUD methods, custom queries."),
                ("Entity and Repository", 25, "@Entity, @Table, @Id, @Column."),
                ("JPQL and Derived Queries", 20, "findByName, @Query annotation."),
                ("Database Configuration", 15, "application.properties for MySQL."),
                ("Hibernate and ORM", 20, "ORM concept, Hibernate as JPA provider."),
            ]),
            ("Spring Boot Advanced", "spring-boot-advanced", [
                ("Profiles and Environment", 20, "@Profile, application-dev.properties."),
                ("Actuator and Monitoring", 20, "/health, /info, /metrics endpoints."),
                ("Validation with Bean Validation", 20, "@Valid, @NotNull, @Size, @Email."),
                ("File Upload and Download", 25, "MultipartFile, storage service."),
                ("Spring Boot Deployment", 20, "Building JAR, running as service, Docker."),
            ]),
        ],
    },

    # ── SPRING MVC ───────────────────────────────────────────────────────────
    "spring-mvc": {
        "title": "Spring MVC",
        "domain": "Java Web",
        "difficulty": "Intermediate",
        "estimated_hours": 20,
        "modules": [
            ("Spring MVC Architecture", "spring-mvc-architecture", [
                ("DispatcherServlet", 20, "Front controller pattern in Spring MVC."),
                ("Handler Mapping", 15, "Resolving controllers from request."),
                ("View Resolver", 20, "InternalResourceViewResolver, Thymeleaf."),
                ("Model, View, Controller", 20, "MVC roles and data flow."),
                ("Spring MVC vs Spring Boot", 15, "When to use each."),
            ]),
            ("Controllers and Views", "controllers-views", [
                ("@Controller and @RequestMapping", 20, "Mapping URLs to controller methods."),
                ("Model and ModelAndView", 20, "Passing data to views."),
                ("Thymeleaf Integration", 25, "th:text, th:each, th:if, th:href."),
                ("Form Handling", 25, "@ModelAttribute, BindingResult, form tags."),
                ("Validation in Spring MVC", 20, "@Valid, custom validators."),
            ]),
            ("Advanced Spring MVC", "spring-mvc-advanced", [
                ("Interceptors", 20, "HandlerInterceptor, pre/postHandle."),
                ("File Upload with Spring MVC", 20, "MultipartResolver, file storage."),
                ("REST with Spring MVC", 20, "@ResponseBody, @RequestBody, JSON."),
                ("Internationalization", 15, "MessageSource, LocaleResolver, i18n."),
                ("Spring MVC Testing", 20, "MockMvc, @WebMvcTest."),
            ]),
        ],
    },

    # ── SPRING SECURITY ──────────────────────────────────────────────────────
    "spring-security": {
        "title": "Spring Security",
        "domain": "Java Security",
        "difficulty": "Advanced",
        "estimated_hours": 20,
        "modules": [
            ("Spring Security Basics", "spring-security-basics", [
                ("Spring Security Architecture", 20, "Filter chain, SecurityContext, Authentication."),
                ("Basic Authentication Setup", 20, "UserDetailsService, in-memory auth."),
                ("Password Encoding", 15, "BCryptPasswordEncoder, PasswordEncoder."),
                ("Security Configuration", 25, "SecurityFilterChain, HttpSecurity, CSRF."),
                ("Method-Level Security", 20, "@PreAuthorize, @Secured, @RolesAllowed."),
            ]),
            ("JWT with Spring Security", "spring-security-jwt", [
                ("JWT Filter Implementation", 30, "OncePerRequestFilter, token extraction."),
                ("JWT Token Service", 25, "Generating, validating, parsing tokens."),
                ("Securing REST Endpoints", 20, "Stateless session, JWT authentication."),
                ("Refresh Token Implementation", 25, "Refresh token rotation strategy."),
                ("Logout and Token Blacklisting", 20, "Invalidating tokens."),
            ]),
            ("OAuth2 and Advanced", "spring-security-oauth2", [
                ("OAuth2 Login", 25, "Google, GitHub social login with Spring Security."),
                ("OAuth2 Resource Server", 25, "JWT-based resource server configuration."),
                ("CORS Configuration", 15, "Allowing cross-origin requests."),
                ("Security Testing", 20, "@WithMockUser, SecurityMockMvcRequestPostProcessors."),
                ("Spring Security Best Practices", 15, "HTTPS, headers, content security policy."),
            ]),
        ],
    },

    # ── MAVEN ────────────────────────────────────────────────────────────────
    "maven": {
        "title": "Maven",
        "domain": "Java Build Tool",
        "difficulty": "Beginner",
        "estimated_hours": 10,
        "modules": [
            ("Maven Fundamentals", "maven-fundamentals", [
                ("What Is Maven and Why", 15, "Build automation, dependency management, project structure."),
                ("POM File Structure", 20, "groupId, artifactId, version, packaging, properties."),
                ("Maven Lifecycle", 20, "validate, compile, test, package, install, deploy."),
                ("Running Maven Commands", 15, "mvn clean install, mvn package, mvn test."),
                ("Maven vs Gradle", 15, "Comparing Java build tools."),
            ]),
            ("Dependencies and Plugins", "maven-dependencies", [
                ("Adding Dependencies", 20, "Searching Maven Central, dependency scope."),
                ("Dependency Scope", 15, "compile, test, provided, runtime, system."),
                ("Dependency Management", 20, "Transitive deps, exclusions, dependencyManagement."),
                ("Common Maven Plugins", 20, "compiler, surefire, jar, shade, spring-boot."),
                ("Multi-Module Projects", 25, "Parent POM, module inheritance, reactor build."),
            ]),
        ],
    },

    # ─── PRIORITY 3: IoT ──────────────────────────────────────────────────────

    # ── ELECTRICAL FUNDAMENTALS ───────────────────────────────────────────────
    "electrical-fundamentals": {
        "title": "Electrical Fundamentals",
        "domain": "Electronics / IoT",
        "difficulty": "Beginner",
        "estimated_hours": 20,
        "modules": [
            ("Basic Electrical Theory", "basic-electrical-theory", [
                ("Voltage Current and Resistance", 20, "Definitions, units, measurement instruments."),
                ("Ohms Law", 20, "V=IR, calculating unknown values."),
                ("Kirchhoffs Laws", 25, "KVL and KCL — series and parallel circuits."),
                ("Power and Energy", 20, "P=VI, energy calculations, watt-hour."),
                ("AC vs DC", 20, "Alternating vs direct current, frequency, amplitude."),
            ]),
            ("Circuit Components", "circuit-components", [
                ("Resistors", 20, "Color code, tolerance, power rating."),
                ("Capacitors", 20, "Charge storage, capacitance, filtering."),
                ("Inductors and Coils", 15, "Magnetic field, inductance, transformers."),
                ("Series and Parallel Circuits", 25, "Equivalent resistance and capacitance."),
                ("Voltage Dividers", 20, "Resistive voltage divider, sensor interfacing."),
            ]),
            ("Practical Electrical Skills", "practical-electrical", [
                ("Using a Multimeter", 20, "Measuring V, I, R, continuity."),
                ("Reading Circuit Diagrams", 20, "Schematic symbols, reading schematics."),
                ("Breadboard Prototyping", 25, "Breadboard layout, building circuits."),
                ("Safety and ESD", 15, "Electrical safety, anti-static precautions."),
                ("Power Supply Basics", 20, "Regulated vs unregulated, LDO regulators."),
            ]),
        ],
    },

    # ── ELECTRONICS BASICS ────────────────────────────────────────────────────
    "electronics-basics": {
        "title": "Electronics Basics",
        "domain": "Electronics / IoT",
        "difficulty": "Beginner",
        "estimated_hours": 25,
        "modules": [
            ("Semiconductor Devices", "semiconductor-devices", [
                ("Diodes", 20, "PN junction, forward/reverse bias, diode types."),
                ("Rectifiers", 20, "Half-wave, full-wave, bridge rectifier circuits."),
                ("Transistors BJT", 25, "NPN/PNP, biasing, switch and amplifier modes."),
                ("MOSFETs", 20, "N-channel, P-channel, gate drive, switching."),
                ("Zener Diodes and Voltage Regulation", 15, "Zener breakdown, simple voltage reference."),
            ]),
            ("Operational Amplifiers", "op-amps", [
                ("Op-Amp Basics", 20, "Ideal op-amp, virtual ground, open loop gain."),
                ("Inverting and Non-Inverting Amplifier", 25, "Gain formulas, feedback resistors."),
                ("Comparator", 20, "Comparing voltages, output switching."),
                ("Summing Amplifier", 15, "Weighted sum of inputs."),
                ("Op-Amp Applications in IoT", 20, "Signal conditioning for sensors."),
            ]),
            ("Digital Electronics", "digital-electronics", [
                ("Number Systems", 20, "Binary, octal, hexadecimal — conversions."),
                ("Logic Gates", 20, "AND, OR, NOT, NAND, NOR, XOR truth tables."),
                ("Combinational Circuits", 25, "Adders, multiplexers, decoders."),
                ("Sequential Circuits", 20, "Flip-flops, registers, counters."),
                ("Digital IC Families", 15, "TTL, CMOS — voltage levels, interfacing."),
            ]),
            ("Practical Electronics", "practical-electronics", [
                ("Soldering Techniques", 20, "Through-hole, SMD, desoldering."),
                ("PCB Reading and Assembly", 20, "Reading PCB silkscreen, placing components."),
                ("Signal Conditioning", 20, "Filtering, level shifting, impedance matching."),
                ("EMI and Noise Reduction", 15, "Bypass capacitors, shielding, ground planes."),
                ("Datasheets and Component Selection", 20, "Reading datasheets, absolute maximum ratings."),
            ]),
        ],
    },

    # ── STM32 ────────────────────────────────────────────────────────────────
    "stm32": {
        "title": "STM32",
        "domain": "Embedded Systems",
        "difficulty": "Advanced",
        "estimated_hours": 35,
        "modules": [
            ("STM32 Introduction", "stm32-introduction", [
                ("STM32 Family Overview", 20, "F0, F1, F4, H7 series — when to choose each."),
                ("STM32 Architecture", 20, "Cortex-M core, AHB/APB bus, clock tree."),
                ("STM32CubeIDE Setup", 25, "IDE installation, device configuration, project creation."),
                ("STM32CubeMX", 20, "Pin configuration, clock setup, code generation."),
                ("HAL Library Overview", 20, "HAL vs LL, driver abstraction, portability."),
            ]),
            ("STM32 Peripherals", "stm32-peripherals", [
                ("GPIO in STM32", 20, "HAL_GPIO_WritePin, ReadPin, Exti interrupts."),
                ("UART in STM32", 25, "HAL_UART_Transmit, Receive, interrupt mode."),
                ("SPI in STM32", 25, "HAL_SPI_Transmit, full-duplex, DMA."),
                ("I2C in STM32", 25, "HAL_I2C_Master_Transmit, memory read/write."),
                ("ADC in STM32", 20, "12-bit ADC, polling, interrupt, DMA modes."),
            ]),
            ("Timers and PWM", "stm32-timers", [
                ("Basic Timers", 20, "TIM6/7, period, prescaler, interrupt."),
                ("General Purpose Timers", 25, "Output compare, input capture."),
                ("PWM Generation", 25, "TIM in PWM mode, duty cycle, frequency."),
                ("Input Capture", 20, "Measuring pulse width and frequency."),
                ("RTC Real-Time Clock", 20, "RTC configuration, alarm, backup registers."),
            ]),
            ("DMA and Low Power", "stm32-dma-lowpower", [
                ("DMA Fundamentals", 25, "DMA channels, request mapping, circular mode."),
                ("DMA with UART and SPI", 25, "Zero-CPU peripheral transfers."),
                ("STM32 Low Power Modes", 20, "Sleep, Stop, Standby modes."),
                ("RTC Wakeup from Stop Mode", 20, "Ultra-low power data logging."),
                ("Power Profiling", 20, "Measuring current with STM32 power modes."),
            ]),
            ("FreeRTOS on STM32", "stm32-freertos", [
                ("FreeRTOS on STM32", 25, "CMSIS-RTOS2 API, task creation."),
                ("Task Communication", 20, "Queues, semaphores, event groups."),
                ("Memory Management", 20, "heap_4, stack sizing, memory pools."),
                ("STM32 RTOS Project", 35, "Multi-task sensor system with FreeRTOS."),
                ("STM32 Production Checklist", 15, "Clock security, watchdog, CRC."),
            ]),
        ],
    },

    # ── FIREBASE ────────────────────────────────────────────────────────────
    "firebase": {
        "title": "Firebase",
        "domain": "Cloud / IoT Backend",
        "difficulty": "Beginner",
        "estimated_hours": 15,
        "modules": [
            ("Firebase Introduction", "firebase-introduction", [
                ("What Is Firebase", 15, "BaaS, Firebase products, Google ecosystem."),
                ("Firebase Console Setup", 15, "Creating project, SDK config."),
                ("Firebase Authentication", 25, "Email/password, Google login, anonymous."),
                ("Firebase SDK in Python", 20, "pyrebase, firebase-admin, setup."),
                ("Firebase SDK in JavaScript", 20, "Web SDK setup, initialization."),
            ]),
            ("Firebase Database", "firebase-database", [
                ("Realtime Database", 25, "JSON tree structure, read/write rules."),
                ("Firestore", 25, "Collections, documents, queries, real-time listeners."),
                ("Realtime Database vs Firestore", 15, "Choosing the right database."),
                ("Security Rules", 20, "Read/write rules, authenticated access."),
                ("IoT Data to Firebase", 25, "ESP32 pushing sensor data to Realtime DB."),
            ]),
            ("Firebase Hosting and Functions", "firebase-hosting", [
                ("Firebase Hosting", 20, "Deploying static web apps, CLI."),
                ("Cloud Functions", 25, "Serverless functions triggered by DB events."),
                ("Firebase Storage", 20, "Uploading images and files."),
                ("Firebase Notifications", 15, "FCM push notifications."),
                ("Full IoT Dashboard with Firebase", 30, "ESP32 + Firebase + Web dashboard."),
            ]),
        ],
    },

    # ── TINYML ───────────────────────────────────────────────────────────────
    "tinyml": {
        "title": "TinyML",
        "domain": "AI / Embedded",
        "difficulty": "Advanced",
        "estimated_hours": 25,
        "modules": [
            ("TinyML Introduction", "tinyml-introduction", [
                ("What Is TinyML", 20, "ML on microcontrollers, use cases, limitations."),
                ("TinyML vs Cloud AI", 15, "Latency, privacy, connectivity trade-offs."),
                ("Hardware for TinyML", 20, "Arduino Nano 33 BLE, ESP32-S3, STM32."),
                ("TensorFlow Lite Overview", 20, "TFLite, quantization, interpreter."),
                ("Edge Impulse Platform", 20, "No-code TinyML development platform."),
            ]),
            ("Model Training and Optimization", "tinyml-training", [
                ("Training a Simple Classifier", 25, "Keras model for gesture/keyword detection."),
                ("Model Quantization", 25, "Float32 to int8, post-training quantization."),
                ("Model Pruning", 20, "Reducing model size and operations."),
                ("TFLite Model Conversion", 20, "SavedModel to .tflite file."),
                ("Evaluating Quantized Models", 20, "Accuracy vs size trade-off."),
            ]),
            ("Deployment on Microcontrollers", "tinyml-deployment", [
                ("TFLite Micro on Arduino", 30, "Deploying .tflite model on Arduino."),
                ("TFLite Micro on ESP32", 30, "ESP32 inference with TFLite Micro."),
                ("Keyword Spotting", 30, "Wake word detection on microcontroller."),
                ("Gesture Recognition", 30, "IMU-based gesture with Edge Impulse."),
                ("TinyML in Production", 20, "OTA model updates, monitoring."),
            ]),
        ],
    },

    # ─── PRIORITY 4: DevOps ───────────────────────────────────────────────────

    # ── BASH SCRIPTING ───────────────────────────────────────────────────────
    "bash": {
        "title": "Bash Scripting",
        "domain": "Linux / DevOps",
        "difficulty": "Beginner",
        "estimated_hours": 15,
        "modules": [
            ("Bash Fundamentals", "bash-fundamentals", [
                ("What Is Bash", 15, "Shell, bash vs sh, interactive vs scripting."),
                ("Writing Your First Script", 20, "Shebang, chmod +x, running scripts."),
                ("Variables and Data Types", 20, "Variable assignment, quoting, arrays."),
                ("Input and Output", 15, "echo, read, printf, stdin/stdout/stderr."),
                ("Special Variables", 15, "$0, $1, $#, $@, $?, $$, $!."),
            ]),
            ("Control Flow", "bash-control-flow", [
                ("Conditionals", 20, "if/elif/else, test command, [ ], [[ ]]."),
                ("Loops", 20, "for, while, until, break, continue."),
                ("Case Statements", 15, "case..esac, pattern matching."),
                ("Functions", 20, "Defining, calling, local variables, return."),
                ("Error Handling", 20, "set -e, set -u, set -o pipefail, trap."),
            ]),
            ("Bash Automation", "bash-automation", [
                ("Text Processing", 20, "grep, awk, sed, cut, sort, uniq, wc."),
                ("File Operations", 20, "Test operators, file manipulation scripts."),
                ("Cron Jobs", 15, "Scheduling scripts, crontab syntax."),
                ("Script Debugging", 15, "set -x, bash -n, common debugging techniques."),
                ("Practical Automation Scripts", 30, "Backup, log rotation, deploy scripts."),
            ]),
        ],
    },

    # ── GITHUB ACTIONS ───────────────────────────────────────────────────────
    "github-actions": {
        "title": "GitHub Actions",
        "domain": "CI/CD",
        "difficulty": "Intermediate",
        "estimated_hours": 15,
        "modules": [
            ("GitHub Actions Fundamentals", "gha-fundamentals", [
                ("What Is GitHub Actions", 15, "CI/CD, workflow automation, GitHub integration."),
                ("Workflow File Structure", 20, ".github/workflows/ci.yml anatomy."),
                ("Triggers and Events", 20, "on: push, pull_request, schedule, workflow_dispatch."),
                ("Jobs and Steps", 20, "jobs, steps, runs-on, uses, run."),
                ("Actions Marketplace", 15, "Using pre-built actions, versions."),
            ]),
            ("Building CI/CD Pipelines", "gha-pipelines", [
                ("Python CI Pipeline", 25, "Lint, test, coverage for Python project."),
                ("Java CI Pipeline", 25, "Maven build, test, artifact upload."),
                ("Docker Build and Push", 25, "Build image, push to Docker Hub/GHCR."),
                ("Deploy to Server", 25, "SSH deploy action, rsync, restart service."),
                ("Matrix Builds", 20, "Testing across multiple Python/Node versions."),
            ]),
            ("Advanced GitHub Actions", "gha-advanced", [
                ("Secrets and Environment Variables", 20, "GitHub secrets, env contexts."),
                ("Reusable Workflows", 20, "workflow_call, sharing workflows."),
                ("Caching Dependencies", 15, "actions/cache for pip, npm, Maven."),
                ("GitHub Actions for IoT", 20, "Build and flash firmware on commit."),
                ("Monitoring Workflow Runs", 15, "Status badges, notifications, artifacts."),
            ]),
        ],
    },

    # ── JENKINS ──────────────────────────────────────────────────────────────
    "jenkins": {
        "title": "Jenkins",
        "domain": "CI/CD",
        "difficulty": "Intermediate",
        "estimated_hours": 20,
        "modules": [
            ("Jenkins Fundamentals", "jenkins-fundamentals", [
                ("What Is Jenkins", 15, "CI/CD server, open-source, plugin ecosystem."),
                ("Jenkins Installation", 20, "Docker, WAR, Linux package install."),
                ("Jenkins UI Overview", 15, "Dashboard, jobs, builds, console output."),
                ("Freestyle Jobs", 20, "Creating build jobs, build steps, triggers."),
                ("Build Triggers", 15, "Poll SCM, webhook, manual trigger."),
            ]),
            ("Jenkins Pipeline", "jenkins-pipeline", [
                ("Declarative Pipeline", 25, "Jenkinsfile, stages, steps, agent."),
                ("Scripted Pipeline", 20, "Groovy DSL, node, stage, sh."),
                ("Pipeline Stages", 20, "Checkout, build, test, deploy stages."),
                ("Pipeline with Docker", 25, "Building Docker images in Jenkins."),
                ("Shared Libraries", 20, "Reusable Groovy functions across pipelines."),
            ]),
            ("Jenkins Integration", "jenkins-integration", [
                ("Jenkins with Git", 20, "Webhook setup, branch builds."),
                ("Jenkins with Maven", 20, "Building Java projects with Maven."),
                ("Jenkins with Docker", 25, "Docker agent, image build, push."),
                ("Notifications and Reports", 15, "Email, Slack notifications, test reports."),
                ("Jenkins Best Practices", 15, "Security, master-agent, backup."),
            ]),
        ],
    },

    # ── AWS ──────────────────────────────────────────────────────────────────
    "aws": {
        "title": "AWS",
        "domain": "Cloud",
        "difficulty": "Intermediate",
        "estimated_hours": 35,
        "modules": [
            ("AWS Fundamentals", "aws-fundamentals", [
                ("Cloud Computing and AWS Overview", 15, "IaaS, PaaS, SaaS, AWS global infrastructure."),
                ("AWS Console and CLI", 20, "Console navigation, AWS CLI setup and commands."),
                ("IAM Users Roles and Policies", 25, "IAM best practices, least privilege, MFA."),
                ("AWS Pricing and Free Tier", 15, "Cost management, free tier limits, billing alerts."),
                ("AWS Regions and AZs", 15, "Region selection, availability zones, edge locations."),
            ]),
            ("Compute", "aws-compute", [
                ("EC2 Instances", 25, "Instance types, AMI, launch, connect via SSH."),
                ("Security Groups", 20, "Inbound/outbound rules, port access."),
                ("Elastic IPs and Load Balancers", 20, "Static IPs, ALB for web apps."),
                ("Auto Scaling Groups", 20, "Scaling policies, launch templates."),
                ("AWS Lambda", 25, "Serverless functions, event triggers, layers."),
            ]),
            ("Storage and Database", "aws-storage-db", [
                ("S3 Storage", 25, "Buckets, objects, versioning, static website hosting."),
                ("S3 Policies and Permissions", 20, "Bucket policies, ACL, public access."),
                ("RDS", 25, "MySQL/Postgres on RDS, snapshots, multi-AZ."),
                ("DynamoDB Basics", 20, "NoSQL table, partition key, scan, query."),
                ("EBS Volumes", 15, "Block storage, snapshots, attaching to EC2."),
            ]),
            ("Networking and Deployment", "aws-networking", [
                ("VPC Basics", 20, "Virtual Private Cloud, subnets, route tables."),
                ("Internet Gateway and NAT", 20, "Public/private subnets, internet access."),
                ("API Gateway", 25, "REST API trigger for Lambda, rate limiting."),
                ("CloudFront CDN", 20, "Content delivery, S3 + CloudFront setup."),
                ("Route 53 DNS", 20, "Domain registration, record types, routing."),
            ]),
            ("DevOps on AWS", "aws-devops", [
                ("CodeCommit and CodePipeline", 20, "AWS CI/CD services."),
                ("Elastic Beanstalk", 25, "Deploying Flask/Spring Boot apps."),
                ("ECS and ECR", 25, "Docker containers on AWS ECS, ECR registry."),
                ("CloudWatch Monitoring", 20, "Logs, metrics, alarms, dashboards."),
                ("AWS CLI Automation", 20, "Scripting infrastructure with AWS CLI."),
            ]),
        ],
    },

    # ── KUBERNETES ───────────────────────────────────────────────────────────
    "kubernetes": {
        "title": "Kubernetes",
        "domain": "Container Orchestration",
        "difficulty": "Advanced",
        "estimated_hours": 30,
        "modules": [
            ("Kubernetes Fundamentals", "k8s-fundamentals", [
                ("What Is Kubernetes", 15, "Container orchestration, why K8s, architecture."),
                ("Cluster Architecture", 20, "Control plane, worker nodes, etcd, API server."),
                ("kubectl Setup and Commands", 20, "kubectl install, context, get, describe, apply."),
                ("Pods", 20, "Smallest unit, pod spec, running containers."),
                ("Namespaces", 15, "Logical isolation, default vs custom namespaces."),
            ]),
            ("Core Workloads", "k8s-workloads", [
                ("Deployments", 25, "ReplicaSet, rolling update, rollback."),
                ("Services", 25, "ClusterIP, NodePort, LoadBalancer, headless."),
                ("ConfigMaps and Secrets", 20, "Externalizing config, base64 secrets."),
                ("Persistent Volumes", 20, "PV, PVC, StorageClass, volume mounts."),
                ("DaemonSets and StatefulSets", 20, "Node-level pods, stateful apps."),
            ]),
            ("Networking and Ingress", "k8s-networking", [
                ("Kubernetes Networking Model", 20, "Pod-to-pod, service discovery, DNS."),
                ("Ingress Controller", 25, "NGINX ingress, routing rules, TLS."),
                ("Network Policies", 20, "Restricting pod communication."),
                ("Helm Charts", 25, "Package manager for K8s, values.yaml, templates."),
                ("Horizontal Pod Autoscaler", 20, "CPU-based scaling, metrics server."),
            ]),
            ("Production Kubernetes", "k8s-production", [
                ("Resource Requests and Limits", 15, "CPU/memory management, LimitRange."),
                ("Liveness and Readiness Probes", 20, "Health checks, restart policies."),
                ("RBAC", 20, "Role, ClusterRole, RoleBinding."),
                ("Kubernetes on AWS EKS", 25, "Managed K8s cluster on AWS."),
                ("Monitoring with Prometheus and Grafana", 25, "K8s monitoring stack."),
            ]),
        ],
    },

    # ─── PRIORITY 5: QA & Others ──────────────────────────────────────────────

    # ── MANUAL TESTING ───────────────────────────────────────────────────────
    "manual-testing": {
        "title": "Manual Testing",
        "domain": "QA",
        "difficulty": "Beginner",
        "estimated_hours": 15,
        "modules": [
            ("Testing Fundamentals", "testing-fundamentals", [
                ("Software Testing Introduction", 15, "Why test, types of bugs, cost of defects."),
                ("SDLC and STLC", 20, "Software development vs testing life cycles."),
                ("Types of Testing", 20, "Functional, non-functional, regression, smoke, sanity."),
                ("Testing Levels", 15, "Unit, integration, system, acceptance testing."),
                ("Testing Principles", 15, "7 testing principles every QA must know."),
            ]),
            ("Test Design", "test-design", [
                ("Test Planning and Strategy", 20, "Test plan document, scope, resources."),
                ("Test Case Writing", 25, "Test case template, test ID, preconditions, steps."),
                ("Test Case Design Techniques", 25, "BVA, equivalence partitioning, decision table."),
                ("Test Execution and Reporting", 20, "Bug lifecycle, severity vs priority."),
                ("Bug Report Writing", 20, "Clear bug reports, screenshots, reproduction steps."),
            ]),
            ("Tools and Process", "testing-tools-process", [
                ("JIRA for Bug Tracking", 20, "Creating issues, workflow, Kanban board."),
                ("Agile Testing", 20, "Sprint testing, story acceptance criteria."),
                ("API Testing Basics", 20, "Postman for manual API validation."),
                ("Database Testing", 15, "SQL queries for backend data validation."),
                ("Testing Best Practices", 15, "Test coverage, regression suite, exploratory testing."),
            ]),
        ],
    },

    # ── PLAYWRIGHT ───────────────────────────────────────────────────────────
    "playwright": {
        "title": "Playwright",
        "domain": "Test Automation",
        "difficulty": "Intermediate",
        "estimated_hours": 20,
        "modules": [
            ("Playwright Fundamentals", "playwright-fundamentals", [
                ("What Is Playwright", 15, "Browser automation, cross-browser, Chromium/Firefox/WebKit."),
                ("Playwright Setup", 20, "npm install, Python setup, CLI."),
                ("Browser and Page Objects", 20, "Browser, BrowserContext, Page hierarchy."),
                ("Locators and Selectors", 25, "CSS, XPath, text, role, test-id locators."),
                ("Basic Interactions", 20, "click, fill, press, hover, check, select."),
            ]),
            ("Test Writing", "playwright-tests", [
                ("Test Structure", 20, "test(), expect(), describe(), beforeEach()."),
                ("Assertions", 25, "toBeVisible, toHaveText, toHaveValue, toBeEnabled."),
                ("Page Object Model", 25, "POM design pattern, reusable page classes."),
                ("Test Fixtures", 20, "Fixtures for setup/teardown, shared context."),
                ("API Testing with Playwright", 25, "request context, GET, POST assertions."),
            ]),
            ("Advanced Playwright", "playwright-advanced", [
                ("Network Interception", 25, "Mocking API responses, route.fulfill()."),
                ("Screenshot and Video", 15, "Capturing screenshots, video recording."),
                ("Parallel Test Execution", 20, "Workers, sharding, parallel config."),
                ("CI with GitHub Actions", 20, "Running Playwright in CI pipeline."),
                ("Playwright Reports", 15, "HTML report, trace viewer, allure."),
            ]),
        ],
    },

    # ── POSTMAN ──────────────────────────────────────────────────────────────
    "postman": {
        "title": "Postman and API Testing",
        "domain": "API Testing",
        "difficulty": "Beginner",
        "estimated_hours": 15,
        "modules": [
            ("Postman Fundamentals", "postman-fundamentals", [
                ("What Is Postman", 10, "REST client, collections, team collaboration."),
                ("Sending Requests", 20, "GET, POST, PUT, DELETE, headers, body."),
                ("Environments and Variables", 20, "Env variables, global variables, base URL."),
                ("Authentication", 20, "Bearer token, API key, OAuth2 in Postman."),
                ("Request Chaining", 20, "Pre-request scripts, passing response values."),
            ]),
            ("Writing Tests", "postman-tests", [
                ("Postman Test Scripts", 25, "pm.test(), pm.expect(), pm.response."),
                ("Status Code Assertions", 15, "Testing HTTP status, response time."),
                ("Response Body Assertions", 20, "JSON path assertions, schema validation."),
                ("Collections and Test Suites", 20, "Organizing requests into collections."),
                ("Newman CLI", 20, "Running Postman collections from terminal."),
            ]),
            ("API Testing Workflow", "api-testing-workflow", [
                ("Testing REST APIs End-to-End", 25, "Full CRUD test collection."),
                ("Mock Servers in Postman", 20, "Simulating API responses for dev."),
                ("API Documentation", 15, "Publishing docs from Postman collection."),
                ("CI Integration with Newman", 20, "Newman in GitHub Actions / Jenkins."),
                ("API Testing Best Practices", 15, "Coverage, edge cases, security basics."),
            ]),
        ],
    },

    # ── DATA STRUCTURES & ALGORITHMS ─────────────────────────────────────────
    "python-dsa": {
        "title": "Data Structures and Algorithms",
        "domain": "Computer Science",
        "difficulty": "Intermediate",
        "estimated_hours": 30,
        "modules": [
            ("Complexity Analysis", "complexity-analysis", [
                ("Big O Notation", 20, "Time and space complexity, O(1), O(n), O(log n), O(n^2)."),
                ("Best Average Worst Case", 15, "Analyzing algorithms under different inputs."),
                ("Recursion", 25, "Base case, recursive case, call stack, memoization."),
                ("Recursion vs Iteration", 15, "Trade-offs, tail recursion."),
                ("Problem-Solving Framework", 20, "Understand, plan, code, test — UPCT method."),
            ]),
            ("Linear Data Structures", "linear-ds", [
                ("Arrays and Lists", 20, "Python list internals, slicing, operations."),
                ("Linked Lists", 25, "Singly, doubly, circular — node implementation."),
                ("Stacks", 20, "LIFO, push, pop, balanced parentheses."),
                ("Queues and Deques", 20, "FIFO, collections.deque, priority queue."),
                ("Hash Tables", 25, "Dict internals, collision handling, hash function."),
            ]),
            ("Non-Linear Data Structures", "nonlinear-ds", [
                ("Binary Trees", 25, "Node, traversals — inorder, preorder, postorder."),
                ("Binary Search Trees", 25, "Insert, search, delete, BST property."),
                ("Heaps", 20, "Min-heap, max-heap, heapq module."),
                ("Graphs", 25, "Adjacency list/matrix, directed/undirected, weighted."),
                ("Tries", 20, "Prefix tree, autocomplete use case."),
            ]),
            ("Searching and Sorting", "searching-sorting", [
                ("Linear and Binary Search", 20, "Sequential search, binary search on sorted array."),
                ("Bubble, Selection, Insertion Sort", 20, "O(n^2) sorts — when to use."),
                ("Merge Sort", 25, "Divide and conquer, stable sort."),
                ("Quick Sort", 25, "Pivot, partition, average O(n log n)."),
                ("Counting and Radix Sort", 20, "Linear time sorting for special inputs."),
            ]),
            ("Graph Algorithms", "graph-algorithms", [
                ("BFS Breadth-First Search", 25, "Level order traversal, shortest path."),
                ("DFS Depth-First Search", 25, "Path finding, cycle detection."),
                ("Dijkstra Shortest Path", 25, "Weighted graph, priority queue."),
                ("Dynamic Programming", 30, "Memoization, tabulation, Fibonacci, knapsack."),
                ("Greedy Algorithms", 20, "Activity selection, coin change, interval scheduling."),
            ]),
        ],
    },
}


# ─── Seeder Functions ─────────────────────────────────────────────────────────

def audit_course(course_slug: str):
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        print(f"  [NOT FOUND] {course_slug}")
        return 0, 0
    mods = course.modules.all()
    total_lessons = sum(m.lessons.filter_by(is_deleted=False).count() for m in mods)
    print(f"  Existing: {len(mods)} modules | {total_lessons} lessons")
    return len(mods), total_lessons


def seed_course(course_slug: str, spec: dict) -> dict:
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        print(f"  [ERROR] Course not found in DB: {course_slug}")
        return {}

    stats = {"modules_created": 0, "lessons_created": 0,
             "sections_created": 0, "modules_existing": 0, "lessons_existing": 0}

    for mod_idx, (mod_title, mod_slug, lessons) in enumerate(spec["modules"], start=1):
        mod = Module.query.filter_by(course_id=course.id, slug=mod_slug).first()
        if not mod:
            mod = Module(
                course_id=course.id, title=mod_title, slug=mod_slug,
                sort_order=mod_idx, is_published=True,
                description=f"Module {mod_idx}: {mod_title}",
            )
            db.session.add(mod)
            db.session.flush()
            stats["modules_created"] += 1
            print(f"  [MOD+] {mod_title}")
        else:
            stats["modules_existing"] += 1

        for lesson_idx, (lesson_title, est_minutes, lesson_desc) in enumerate(lessons, start=1):
            lesson_slug = slugify(lesson_title)
            lesson = Lesson.query.filter_by(module_id=mod.id, slug=lesson_slug).first()
            if not lesson:
                lesson = Lesson(
                    module_id=mod.id, title=lesson_title, slug=lesson_slug,
                    sort_order=lesson_idx, status='draft',
                    is_deleted=False, estimated_minutes=est_minutes,
                    summary=lesson_desc,
                )
                db.session.add(lesson)
                db.session.flush()
                stats["lessons_created"] += 1

            if LessonSection.query.filter_by(lesson_id=lesson.id).count() == 0:
                for (stype, stitle, sort_order) in PLACEHOLDER_SECTIONS:
                    db.session.add(LessonSection(
                        lesson_id=lesson.id, section_type=stype,
                        title=stitle, content_markdown="",
                        content_html="", sort_order=sort_order, is_visible=False,
                    ))
                    stats["sections_created"] += 1

    db.session.commit()
    return stats


def print_summary(course_slug: str, spec: dict):
    course = Course.query.filter_by(slug=course_slug, is_deleted=False).first()
    if not course:
        return
    mods = course.modules.all()
    total = sum(m.lessons.filter_by(is_deleted=False).count() for m in mods)
    pending = sum(m.lessons.filter_by(is_deleted=False, status='pending').count() for m in mods)
    print(f"  Status: Structure Ready | {len(mods)} modules | {total} lessons ({pending} pending)")


def run(course_filter=None, audit_only=False):
    courses = (
        {course_filter: CURRICULUM[course_filter]}
        if course_filter and course_filter in CURRICULUM
        else CURRICULUM
    )

    with app.app_context():
        print(f"\nSeeding {len(courses)} course(s)...")

        for course_slug, spec in courses.items():
            print(f"\n{'='*60}")
            print(f"COURSE: {spec['title']} ({course_slug})")
            print(f"{'='*60}")

            print("[STEP 1] Audit:")
            audit_course(course_slug)

            if audit_only:
                continue

            print("[STEPS 2-4] Seeding modules, lessons, placeholders:")
            stats = seed_course(course_slug, spec)
            print(f"  Modules: +{stats.get('modules_created', 0)} new | "
                  f"={stats.get('modules_existing', 0)} existing")
            print(f"  Lessons: +{stats.get('lessons_created', 0)} new")
            print(f"  Sections: +{stats.get('sections_created', 0)} placeholders")

            print("[STEP 5] Summary:")
            print_summary(course_slug, spec)
            print("[STEP 6] STOP — content generation is a separate step.")

        print(f"\n{'='*60}")
        print("ALL COURSES: Structure Ready. Content: Pending.")
        print(f"{'='*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed structure for 25 new courses")
    parser.add_argument("--course", help="Seed only this course slug")
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    run(course_filter=args.course, audit_only=args.audit_only)
