import os

from flask import Flask, jsonify, render_template, request, session, flash, url_for, redirect
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

channels = {'general':[]}
online_users = []
errors = {'channelExists': 'That channel already exists.', 'userExists': 'That user already exists.'}

@app.route('/')
def index():
    return render_template('index.html', messages=channels['general'])

@socketio.on('add user')
def add_user(data):
    username = data['username']
    channel = data['channel']
    general = 'general'
    error = errors['userExists']
    if username in online_users:
        join_room(channel)
        emit('errors', {'error': error}, room=channel)
    else:
        if channel in channels:
            online_users.append(username)
            join_room(channel)
            emit('announce user', {'username': username, 'channel': channel}, broadcast=True)
        else:
            online_users.append(username)
            join_room(general)
            emit('announce user', {'username': username, 'channel': general}, broadcast=True)

@socketio.on('send message')
def send_message(data):
    username = data['username']
    channel = data['channel']
    message = data['message']
    time = data['time']
    channels[channel].append([time, username, message])
    emit('announce message', {'username': username, 'channel': channel, 'message': message, 'time': time}, broadcast=True)