"""
Learning OS — API Controller Routes.
Exposes JSON endpoints for JWT JWKS metadata, key rotations, and manually trigger entitlements syncing.
"""
from flask import Blueprint, jsonify, request, abort
from flask_login import login_required
from app.core.decorators import require_min_role
from app.services.sso_handshake_service import SSOHandshakeService

api_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_bp.route("/sso/jwks", methods=["GET"])
def get_sso_jwks():
    """Retrieve JWKS public metadata parameters for validating JWT tokens."""
    jwks = SSOHandshakeService.get_jwks()
    return jsonify(jwks)


@api_bp.route("/sso/rotate", methods=["POST"])
@login_required
@require_min_role("admin")
def rotate_sso_keys():
    """Rotate JWT signing key configurations (Admin-only authorization)."""
    new_jwks = SSOHandshakeService.rotate_keys()
    return jsonify({
        "status": "success",
        "message": "SSO keys rotated successfully.",
        "jwks": new_jwks
    })


@api_bp.route("/sso/sync-entitlements", methods=["POST"])
@login_required
def sync_sso_entitlements():
    """Synchronize course enrollment permissions using external JSON payload data."""
    data = request.get_json() or {}
    user_id = data.get("user_id") or request.form.get("user_id", type=int)
    courses = data.get("courses", [])

    if not user_id:
        return jsonify({"status": "error", "message": "user_id is required."}), 400

    from flask_login import current_user
    # Ensure current user is admin, or syncing their own entitlements
    if current_user.role.name not in ["admin", "super_admin"] and current_user.id != int(user_id):
        abort(403, "Access Denied: You cannot sync entitlements for other users.")

    synced = SSOHandshakeService.sync_external_entitlements(int(user_id), courses)
    return jsonify({
        "status": "success",
        "message": f"Successfully synchronized {synced} course entitlements."
    })
