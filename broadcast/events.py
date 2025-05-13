from flask import request
from flask_socketio import emit
from aStar import reverse_astar

from .extensions import socketio
import random
import time
import json
import os

users = {}

@socketio.on("connect")
def handle_connect(auth):
    evId = auth.get("evID") if auth else None
    if evId:
        print(f"Client: {evId}")
    else:
        print("Client unauthorized")

@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined!")
    users[username] = request.sid
    emit("update_users", list(users.keys()), broadcast=True)

# @socketio.on("disconnect")
# def handle_disconnect():
#     username = None
#     for user, sid in list(users.items()):
#         if sid == request.sid:
#             username = user
#             del users[user]
#             break
#     print(f"User {username} disconnected!")
#     emit("update_users", list(users.keys()), broadcast=True)

@socketio.on("rnd_message")
def handle_new_message():
    msg_list = [
                "North road closure notice",
                "Hazard in 100 meters",
                "Traffic due to an accident in less than a mile",
                "South road closure due to a parade",
            ]
    message = random.choice(msg_list)
    
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)
    print(username)
         
              
@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)
    print(username)
       
@socketio.on("private_message")
def handle_private_message(data):
    recipient_sid = users.get(data["recipient"])
    print(f"New message: {data["message"]}")
    
    emit("private_chat", {"message": data["message"], "username": data["sender"]}, broadcast=True)
    
@socketio.on("chargeReq")
def chargeReqHandle(value): 
    emit("ChargeReqAlert", value, broadcast=True)
    

@socketio.on("AutoCS")
def handleAutoCS(data):
    ev_pos = tuple(data.get("position", ()))
    grid_size = (20, 20)

    if not ev_pos:
        emit("route_result", {"error": "Missing EV position"})
        return

    json_path = os.path.join("broadcast", "static", "data", "CSList.json")

    with open(json_path) as f:
        stations = json.load(f)

    available_stations = [tuple(st["position"]) for st in stations if st["status"] == "Available"]

    if not available_stations:
        emit("route_result", {"error": "No available stations"})
        return

    blocked_cells = [
        (1,1), (1,2), (1,3), (3,5), (7,8), (12,12), (14,6), (8,14)
    ]

    closestCS, path = reverse_astar(ev_pos, available_stations, blocked_cells, grid_size)

    station = next((s for s in stations if tuple(s["position"]) == closestCS), None)
    CSports = []
    for port in station["ports"]:
        CSports.append(port)

    if not path or station is None:
        emit("route_result", {"error": "No path found"})
    else:
        emit("route_result", {
            "station_id": station["id"],
            "station_name": station["name"],
            "station_distance": station["distance_km"],
            "path": path,
            "ports": CSports
        })