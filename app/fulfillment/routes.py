from flask import Blueprint, render_template, flash, \
                redirect, url_for, request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


fulfillment_bp = Blueprint('fulfillment_bp', __name__)


@fulfillment_bp.route("/fulfillment", methods=("GET", "POST"))
def fulfillment():
    fulfillment = []
    return render_template("fulfillment.html", reception=fulfillment)