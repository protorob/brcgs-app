from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/inprocess", methods=("GET", "POST"))
def inprocess():
    inprocess = []
    return render_template("inprocess.html", inprocess=inprocess)

@bp.route("/reception", methods=("GET", "POST"))
def reception():
    reception = []
    return render_template("reception.html", reception=reception)

@bp.route("/usermanager", methods=("GET", "POST"))
def usermanager():
    users = []
    return render_template("usermanager.html", users=users)