import os

from flask import Flask, render_template, request, session
from flask_session import Session
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
socketio = SocketIO(app)

channels = {'General':[]}
online_users = []

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

@app.route('/')
def index():
    return render_template('index.html', currentChannel='General', messages=channels['General'], channels=channels, users=online_users)

@app.route('/<channel>', methods=['POST'])
def channel(channel):
    return render_template('index.html', currentChannel=channel, messages=channels[channel], channels=channels, users=online_users)

@socketio.on('add user')
def add_user(data):
    username = data['username']
    channel = data['channel']
    if username not in online_users:
        online_users.append(username)
    join_room(channel)
    emit('announce user', {'username': username, 'channel': channel}, broadcast=True)

@socketio.on('add channel')
def add_channel(data):
    channel = data['channel']
    channels[channel] = []
    emit('announce channel', {'channel': channel}, broadcast=True)

@socketio.on('send message')
def send_message(data):
    username = data['username']
    channel = data['channel']
    message = data['message']
    time = data['time']
    channels[channel].append([time, username, message])
    emit('announce message', {'username': username, 'channel': channel, 'message': message, 'time': time}, room=channel)

@socketio.on('join channel')
def join_channel(data):
    channel = data['channel']
    current_channel = data['currentChannel']
    leave_room(current_channel)
    join_room(channel)
    emit('change channel', {'channel': channel})

@socketio.on('logout')
def logout(data):
    user = data['user']
    channel = data['channel']
    online_users.remove(user)
    leave_room(channel)
