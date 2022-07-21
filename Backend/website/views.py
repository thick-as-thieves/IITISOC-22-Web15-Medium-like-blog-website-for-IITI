from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/perspective")
@login_required
def home():
    return render_template("perspective.html")

@views.route("/homefeed")
def homefeed():
    return render_template("homefeed.html")

@views.route("/second.html")
@views.route("perspective/second")
def second():
    return render_template("second.html")

@views.route("/login")
def login():
    return render_template("login.html")   
