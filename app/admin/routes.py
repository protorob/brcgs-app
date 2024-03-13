from flask import Blueprint, render_template, flash, \
                redirect, url_for, request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.permissions import admin_only


admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/usermanager", methods=("GET", "POST"))
@admin_only
def usermanager():
    users = []
    return render_template("usermanager.html", users=users)
