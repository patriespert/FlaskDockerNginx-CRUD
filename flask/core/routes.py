from flask import Flask, render_template, request, session, escape, redirect, url_for, flash, Blueprint
from .models import Users,db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return "Welcome to our shop!"

@main.route("/search")
def search():
    nickname = request.args.get("nickname")

    user = Users.query.filter_by(username=nickname).first()

    if user:
        return user.username

    return "The user doesn't exist."

@main.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["password"], method="sha256")
        new_user = Users(username=request.form["username"], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("You've registered successfully.", "success")

        return redirect(url_for("main.login"))

    return render_template("signup.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return "You are logged in"
        flash("Your credentials are invalid, check and try again.", "error")

    return render_template("login.html")

@main.route("/home")
def home():
    if "username" in session:
        return "You are %s" % escape(session["username"])

    return "You must log in first."

@main.route("/logout")
def logout():
    session.pop("username", None)

    return "You are logged out."