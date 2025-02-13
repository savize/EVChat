from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/chat/<username>")
def chat(username):
    return render_template("chat.html", username=username)
