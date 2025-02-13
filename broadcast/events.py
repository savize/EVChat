from flask import request
from flask_socketio import emit

from .extensions import socketio

users = {}

@socketio.on("connect")
def handle_connect():
    print("EV connected!")

@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined!")
    users[username] = request.sid
    emit("update_users", list(users.keys()), broadcast=True)

# @socketio.on("disconnect")
# def handle_disconnect():
#     # Find the username of the disconnected user
#     username = None
#     for user, sid in list(users.items()):
#         if sid == request.sid:
#             username = user
#             del users[user]
#             break
#     print(f"User {username} disconnected!")
#     emit("update_users", list(users.keys()), broadcast=True)

@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)
    
       
@socketio.on("private_message")
def handle_private_message(data):
    recipient_sid = users.get(data["recipient"])
    print(f"New message: {data["message"]}")
    
    emit("private_chat", {"message": data["message"], "username": data["recipient"]}, broadcast=True)
    