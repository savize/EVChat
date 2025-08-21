from flask import Blueprint, render_template
from flask import *
import subprocess
import threading
import os
from .services import *

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/map")
def mapTest():
    return render_template("map.html") 

# @main.route("/chat")
# def chat():
#     return render_template("chat.html")

# @main.route("/public")
# def public():
#     return render_template("public.html")

@main.route("/CSs")
def CSList():
    return render_template("stations.html", CSList = CSList)

@main.route("/api/CS")
def sendCS():
    stations = readCS()
    data = [{"id": s.id, "name": s.name, "location": s.location, "lat": s.lat, "lng": s.lng, "status": s.status} for s in stations]
    return jsonify(data)


@main.route("/parking")
def parking():
    return render_template("parkings.html")

@main.route("/CSs/<port_type>")
def portType(port_type):
    return render_template("chat.html", port=port_type)

@main.route("/CSReq")
def CSRequest():
    return render_template("chargeReq.html")

ocpp_started = False

def run_ocpp_server():
    subprocess.Popen(
        ["python3", os.path.join(os.path.dirname(__file__), "server.py")],
        stdout=None, stderr=None
    )

def run_ocpp_client():
    subprocess.Popen(
        ["python3", os.path.join(os.path.dirname(__file__), "client.py")],
        stdout=None, stderr=None
    )

@main.route("/charging")
def charging():
    global ocpp_started
    port = request.args.get("port")

    if not ocpp_started:
        threading.Thread(target=run_ocpp_server, daemon=True).start()
        threading.Thread(target=run_ocpp_client, daemon=True).start()
        ocpp_started = True

    return render_template("charging.html", port=port)