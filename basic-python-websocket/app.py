import socketio

server_io = socketio.AsyncServer(async_mode='asgi', logger=True)
app = socketio.ASGIApp(server_io, static_files={
    '/': './client/index.html',
    '/index.js': './client/index.js'
})

# a Python dictionary comprised of some heroes and their names
hero_names = {
  "ironMan": "Tony Stark",
  "hulk": "Bruce Banner",
  "wonderWoman": "Diana",
  "batMan": "Bruce Wayne",
  "blackPanther": "T'Challa"
}

# Triggered when a client connects to our socket. 
@server_io.event
def connect(sid, socket):    
    print(sid, 'connected')

# Triggered when a client disconnects from our socket
@server_io.event
def disconnect(sid):
    print(sid, 'disconnected')

@server_io.event
async def get_name(sid, data):
    """Takes a hero, grabs corresponding “real” name, and sends it back to the client

    Key arguments:
    sid - the session_id, which is unique to each client
    data - payload sent from the client
    """

    print(data["hero"])

    await server_io.emit("name", {'hero_name': hero_names[data["hero"]]}, to=sid)
