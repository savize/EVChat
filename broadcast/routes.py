from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/chat")
def chat():
    return render_template("chat.html")

@main.route("/public")
def public():
    return render_template("public.html")

@main.route("/CSs")
def CSList():
    return render_template("stations.html")

@main.route("/parking")
def parkingSlots():
    return render_template("parkings.html")

@main.route("/CSs/<int:cs_id>")
def closestCS(cs_id):
    return render_template("chat.html", cs_id=cs_id)

@main.route("/CSs/<port_type>")
def portType(port_type):
    return render_template("chat.html", port=port_type)

@main.route("/CSReq/<ev_id>")
def CSRequest(ev_id):
    return render_template("chargeReq.html")