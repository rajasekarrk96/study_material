"""Learning OS — Auth Blueprint: Login, Register, Logout."""
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from app.core.extensions import db
from app.domains.auth.models import User, Role

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.home"))

    auth_mode = os.environ.get("AUTH_MODE", "LOCAL").upper()
    if auth_mode == "JWT":
        sso_url = os.environ.get("EXTERNAL_SSO_LOGIN_URL", "http://bytesandboards.in/login")
        return redirect(sso_url)

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        from app.domains.auth.providers import LocalAuthProvider
        provider = LocalAuthProvider()
        user = provider.authenticate(email, password)
        if user:
            login_user(user, remember=request.form.get("remember") == "on")
            return redirect(url_for("public.home"))
        flash("Invalid email or password.", "danger")
    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("public.home"))

    auth_mode = os.environ.get("AUTH_MODE", "LOCAL").upper()
    if auth_mode == "JWT":
        sso_register_url = os.environ.get("EXTERNAL_SSO_REGISTER_URL", "http://bytesandboards.in/register")
        return redirect(sso_register_url)

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "danger")
            return render_template("auth/register.html")

        student_role = Role.query.filter_by(name="student").first()
        user = User(
            email=email,
            username=username,
            display_name=username,
            password_hash=generate_password_hash(password),
            role_id=student_role.id if student_role else None,
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Account created! Welcome to Bytes & Boards Solutions.", "success")
        return redirect(url_for("public.home"))
    return render_template("auth/register.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
