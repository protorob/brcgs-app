from flask import Blueprint, render_template, flash, \
                redirect, url_for, request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


reception_bp = Blueprint('reception_bp', __name__)

@reception_bp.route("/reception", methods=("GET", "POST"))
@login_required
def reception():
    reception = []
    return render_template("reception.html", reception=reception)
