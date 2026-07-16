"""Learning OS — Auth Blueprint: Login, Register, Logout."""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.core.extensions import db
from app.domains.auth.models import User, Role

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("public.home"))
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email, is_active=True).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=request.form.get("remember") == "on")
            return redirect(url_for("public.home"))
        flash("Invalid email or password.", "danger")
    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("public.home"))
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
        flash("Account created! Welcome to EduSphere.", "success")
        return redirect(url_for("public.home"))
    return render_template("auth/register.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
