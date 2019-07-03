from websocket import create_connection
import requests
import re
import socketio
host_url='http://47.91.245.176:6001/'
sio = socketio.Client()
@sio.event
def message(data):
    print('I received a message!')


@sio.on('my message')
def on_message(obj, data):
    #data=re.findall("'content': '(.*?)',",str(data))[0]
    print(obj, data)
    print('I received a message!')

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.event
def my_event(sid, data):
    print(data)
    return "OK", 123

sio.connect(host_url)
sio.on('connect', connect)
sio.emit('subscribe', {"channel": "private-Session.1", "auth": {"headers": {"Authorization": "Bearer hOn8H0Xi8mTxqDT2wuS1RxzoMfnNBFcQnIrgBcpjoNxCJgh6ZlijkP0gUC5B"}}})
sio.on('App\\Events\\ChatMessage', on_message)

sio.emit('干你大爷')
