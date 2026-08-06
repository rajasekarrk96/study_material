"""
Learning OS — Application Factory
"""
import os
import logging
from flask import Flask, request, redirect, url_for
from flask_login import current_user

from app.core.config import config
from app.core.extensions import db, login_manager, csrf, limiter

logger = logging.getLogger("learning_os")


def create_app() -> Flask:
    """Application factory for Learning OS."""
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # ── Configuration ──────────────────────────────────────────────────────
    app.config["SECRET_KEY"] = config.secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = config.db.database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = _get_engine_options()
    app.config["RATELIMIT_STORAGE_URI"] = os.environ.get("REDIS_URL", "memory://")

    # ── Extensions ─────────────────────────────────────────────────────────
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    # ── Flask-Login user loader ─────────────────────────────────────────────
    from app.domains.auth.models import User

    @login_manager.user_loader
    def load_user(user_id: str):
        return db.session.get(User, int(user_id))

    # ── JWT SSO Request Interceptor ─────────────────────────────────────────
    @app.before_request
    def handle_jwt_sso():
        if request.path.startswith("/static/"):
            return
        if request.endpoint == "auth.logout":
            return

        # If already authenticated, skip unless a fresh JWT token query parameter is explicitly provided
        has_new_jwt_param = bool(request.args.get("jwt"))
        if not current_user.is_authenticated or has_new_jwt_param:
            token = request.args.get("jwt") or request.cookies.get("jwt") or request.cookies.get("token")
            if not token:
                auth_header = request.headers.get("Authorization")
                if auth_header and auth_header.startswith("Bearer "):
                    token = auth_header[7:]
            
            if token:
                from app.domains.auth.providers import ExternalAuthProvider
                provider = ExternalAuthProvider()
                user = provider.authenticate(token)
                if user:
                    from flask_login import login_user
                    from flask import session
                    login_user(user)
                    session["auth_source"] = "jwt"

    # ── Create tables & seed defaults ──────────────────────────────────────
    with app.app_context():
        _import_all_models()
        db.create_all()
        _seed_defaults()

    # ── Register blueprints ────────────────────────────────────────────────
    _register_blueprints(app)

    # ── Context processors ─────────────────────────────────────────────────
    from app.services.navigation import get_nav_catalog_tree
    @app.context_processor
    def inject_globals():
        nav_catalog_tree = []
        try:
            nav_catalog_tree = get_nav_catalog_tree()
        except Exception:
            pass
        return {
            "platform_name": "Bytes and Boards Solutions",
            "current_user": current_user,
            "nav_catalog_tree": nav_catalog_tree,
        }

    # ── Jinja Template Filters ─────────────────────────────────────────────
    import markdown as md_converter
    from app.core.markdown_utils import insert_blank_lines_before_lists, render_mermaid_blocks

    @app.template_filter("markdown")
    def render_markdown(text):
        if not text:
            return ""
        text = render_mermaid_blocks(text)
        text = insert_blank_lines_before_lists(text)
        return md_converter.markdown(text, extensions=["extra", "codehilite", "toc"])

    logger.info("Learning OS application ready.")
    return app


def _get_engine_options() -> dict:
    """Returns SQLAlchemy engine options, adds SSL for TiDB."""
    opts: dict = {"pool_pre_ping": True}
    if config.db.database_type == "tidb" and config.db.tidb_ssl_ca:
        opts["connect_args"] = {
            "ssl": {"ca": config.db.tidb_ssl_ca}
        }
    return opts


def _import_all_models() -> None:
    """Import all models so SQLAlchemy registers them before db.create_all()."""
    import app.domains.auth.models           # noqa: F401
    import app.domains.content.models        # noqa: F401
    import app.domains.assessment.models     # noqa: F401
    import app.domains.sandbox.models        # noqa: F401
    import app.domains.gamification.models   # noqa: F401
    import app.domains.learning_path.models  # noqa: F401
    import app.domains.srs.models            # noqa: F401
    import app.domains.study.models          # noqa: F401
    import app.domains.knowledge.models      # noqa: F401
    import app.domains.workflow.models       # noqa: F401
    import app.domains.tutor.models          # noqa: F401






def _seed_defaults() -> None:
    """Seed essential default data on first run (roles, admin user)."""
    from app.domains.auth.models import Role
    from app.core.constants import UserRole

    default_roles = [
        (UserRole.SUPER_ADMIN, "Super Admin", 7),
        (UserRole.ADMIN,       "Admin",       6),
        (UserRole.EDITOR,      "Editor",      5),
        (UserRole.REVIEWER,    "Reviewer",    4),
        (UserRole.AUTHOR,      "Author",      3),
        (UserRole.MODERATOR,   "Moderator",   2),
        (UserRole.STUDENT,     "Student",     1),
    ]

    for role_name, display_name, level in default_roles:
        existing = Role.query.filter_by(name=role_name.value).first()
        if not existing:
            role = Role(name=role_name.value, display_name=display_name, level=level)
            db.session.add(role)

    db.session.commit()

    # Seed Admin User
    from app.domains.auth.models import User
    from werkzeug.security import generate_password_hash

    admin_role = Role.query.filter_by(name=UserRole.ADMIN.value).first()
    if admin_role:
        existing_admin = User.query.filter_by(email="rajasekar.rk96@gmail.com").first()
        if not existing_admin:
            admin_user = User(
                email="rajasekar.rk96@gmail.com",
                username="rajasekar",
                display_name="Rajasekar",
                password_hash=generate_password_hash("rajasekarRSK96#"),
                role_id=admin_role.id,
                is_active=True,
                is_verified=True
            )
            db.session.add(admin_user)
            db.session.commit()

    # Seed default permissions in PermissionMatrix
    from app.domains.auth.models import PermissionMatrix
    matrix_seeds = [
        ("student", "view_notes", True),
        ("student", "edit_draft", False),
        ("student", "create_proposal", False),
        ("student", "review_proposal", False),
        ("student", "merge_proposal", False),
        
        ("author", "view_notes", True),
        ("author", "edit_draft", True),
        ("author", "create_proposal", True),
        ("author", "review_proposal", False),
        ("author", "merge_proposal", False),
        
        ("reviewer", "view_notes", True),
        ("reviewer", "edit_draft", True),
        ("reviewer", "create_proposal", True),
        ("reviewer", "review_proposal", True),
        ("reviewer", "merge_proposal", False),
        
        ("editor", "view_notes", True),
        ("editor", "edit_draft", True),
        ("editor", "create_proposal", True),
        ("editor", "review_proposal", True),
        ("editor", "merge_proposal", False),
    ]
    for r_name, p_code, granted in matrix_seeds:
        role = Role.query.filter_by(name=r_name).first()
        if role:
            entry = PermissionMatrix.query.filter_by(role_id=role.id, permission_code=p_code).first()
            if not entry:
                entry = PermissionMatrix(role_id=role.id, permission_code=p_code, is_granted=granted)
                db.session.add(entry)
    db.session.commit()

    # Seed default certificates for existing courses
    # Wrapped in try/except to handle the migration window where new columns
    # (course_type, is_standalone, subtitle) may not yet exist in the DB.
    try:
        from app.domains.content.models import Course, Certificate
        courses = Course.query.all()
        for course in courses:
            existing_cert = Certificate.query.filter_by(course_id=course.id).first()
            if not existing_cert:
                new_cert = Certificate(
                    course_id=course.id,
                    title=f"{course.title} Certification",
                    description=f"Demonstrates mastery of the concepts and practices in {course.title}."
                )
                db.session.add(new_cert)
        db.session.commit()
    except Exception:
        # Schema migration pending — skip certificate seed until DB is up to date.
        db.session.rollback()

    if not os.environ.get("SKIP_SEARCH_REBUILD"):
        from app.services.search_service import SearchIndexService
        try:
            SearchIndexService.rebuild_search_index()
        except Exception:
            pass


def _register_blueprints(app: Flask) -> None:
    """Register all Flask blueprints."""
    from app.blueprints.public.routes import public_bp
    from app.blueprints.auth.routes import auth_bp
    from app.blueprints.learn.routes import learn_bp
    from app.blueprints.assessment.routes import assessment_bp
    from app.blueprints.sandbox.routes import sandbox_bp
    from app.blueprints.srs.routes import srs_bp
    from app.blueprints.study.routes import study_bp
    from app.blueprints.ai.routes import ai_bp
    from app.blueprints.admin.routes import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(learn_bp, url_prefix="/learn")
    app.register_blueprint(assessment_bp)
    app.register_blueprint(sandbox_bp)
    app.register_blueprint(srs_bp)
    app.register_blueprint(study_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(admin_bp)





