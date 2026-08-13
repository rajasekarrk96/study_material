# Django & Django REST Framework — Master Syllabus

**Target Role:** Python Backend Engineer / Full Stack Python Developer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 25 Hours  
**Prerequisites:** foundations/core-python, foundations/mysql, foundations/html5, foundations/css3  
**Required Courses:** foundations/core-python, foundations/mysql  
**Optional Courses:** technologies/docker, technologies/auth-jwt  

---

## Study Flow

### Module 1 — Django MTV Architecture & Setup
1. **Django Architecture & Project Lifecycle** (Model-Template-View pattern, `django-admin`, `manage.py`, project configuration in `settings.py`)
2. **Django Apps & Modular Project Structure** (Creating modular apps with `startapp`, app registry, routing in `urls.py`)
3. **HTTP Request & Response Handling** (`HttpRequest`, `HttpResponse`, `JsonResponse`, `render`, `redirect`)

### Module 2 — Django ORM & Database Modeling
1. **Model Definitions & Field Types** (CharFields, IntegerFields, DateFields, ForeignKey, ManyToManyField, OneToOneField)
2. **Migrations Workflow** (`makemigrations`, `migrate`, `sqlmigrate`, rolling back migrations, data migrations)
3. **QuerySets & Filtering Mechanics** (`filter()`, `exclude()`, `get()`, lookups `__exact`, `__icontains`, `Q` objects, `F` expressions)
4. **Performance & Query Optimization** (`select_related` vs `prefetch_related`, aggregate and annotate functions, indexing)

### Module 3 — Views, Templates & Forms
1. **Class-Based Views (CBVs)** (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, Mixins)
2. **Django Template Engine (DTL)** (Template inheritance `{% extends %}`, tags, filters, static files management)
3. **Django Forms & ModelForms** (Form rendering, CSRF token security, field validation, custom clean methods)

### Module 4 — Django Authentication & Admin Interface
1. **Built-in User Authentication** (User model, login, logout, password hashing, `@login_required`, permission decorators)
2. **Customizing the User Model** (`AbstractUser` vs `AbstractBaseUser`, custom user managers)
3. **Django Admin Customization** (`ModelAdmin`, custom list displays, filters, search fields, inline models)

### Module 5 — Django REST Framework (DRF) & API Development
1. **DRF Serializers & ModelSerializers** (Validation, field-level validators, nested serializers)
2. **APIViews, Generic Views & ViewSets** (`APIView`, `ListCreateAPIView`, `ModelViewSet`, DRF Routers)
3. **DRF Authentication & Permissions** (SessionAuth, TokenAuth, JWT with `djangorestframework-simplejwt`, `IsAuthenticated`, custom permissions)

### Module 6 — Production Deployment & Security
1. **Django Security Best Practices** (SQL injection protection, XSS prevention, CSRF protection, secure cookies, Clickjacking)
2. **Production Configuration & Caching** (Database connection pooling, Redis caching, Whitenoise static serving)
3. **WSGI/ASGI Production Deployment** (Gunicorn, Uvicorn, Nginx, Docker containerization)
