from flask import Blueprint, render_template, flash, \
                redirect, url_for, request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


inprocess_bp = Blueprint('inprocess_bp', __name__)

@inprocess_bp.route("/inprocess", methods=("GET", "POST"))
@login_required
def inprocess():
    inprocess = []
    return render_template("inprocess.html", inprocess=inprocess)
