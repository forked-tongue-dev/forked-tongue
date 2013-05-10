from socketio import socketio_manage
from socketio.namespace import BaseNamespace

# Example Socket.IO service

class ChatNamespace(BaseNamespace):
    def on_chat(self, msg):
        self.emit('chat', msg)

def socketio_service(request):
    socketio_manage(request.environ, {'/chat': ChatNamespace},
                    request)
    return "out"