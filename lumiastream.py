"""
Create LumiaStream WebSocket Connection Objects

Classes:
    LumiaStream
"""
import json
from threading import Thread
import websocket
from PySide6.QtCore import Signal, QObject
from loglevel import LogLevel

class LumiaStream(Thread):
    """
    A class to represent a connection to LumiaStream Websocket API. 
    Host and Port information is in LumiaStream > Settings > API.

    Attributes:
        token: The auth token for LumiaStream API
        host: The host of the LumiaStream API
            e.g. "localhost"
        port: The port number running the LumiaStream API
        socket: The Websocket App object
    """

    class Signals(QObject):
        """
        Subclass to contain Qt Signals to be sent back to GUI
        """
        log = Signal(str, LogLevel)
        disconnected = Signal()
        connected = Signal()
        on_message = Signal(str)
        on_error = Signal(str)

    def __init__(self, token, host, port):
        """
        Constructs a LumiaStream object
        Parameters:
            token: LumiaStream API Auth Token. Found at LumiaStream > Settings > API
            host: lumiastream api hostname (e.g. localhost)
            port: LumiaStream TCP port number of the API endpoint
        """
        Thread.__init__(self)
        self.token = token
        self.host = host
        self.port = port
        self._url = f"ws://{host}:{port}/api?token={self.token}"
        self._connected = False
        self.socket = None
        self.signals = LumiaStream.Signals()

    def send_chat_cmd(self, cmd):
        """Fucntion to send a chat command to LumiaStream"""
        msg = {
            "type": "chat-command",    
            "params": {        
                "value": cmd   
            }
        }
        self.socket.send(json.dumps(msg))

    def is_connected(self):
        """Function to return the websocket connection state"""
        return self._connected
    
    def on_message(self, ws_app, message):
        """Call-back function when a websocket message is received."""
        self.signals.on_message.emit(message)

    def on_error(self, ws_app, error):
        """Call-back function when a websocket error occurs."""
        self.signals.on_error.emit(error)

    def on_close(self, ws_app, close_status_code, close_msg):
        """Call-back function when a websocket connection is closed."""
        self._connected = False
        self.signals.disconnected.emit()

    def on_open(self, ws_app):
        """Call-back function when a websocket connection is opened."""
        self._connected = True
        self.signals.connected.emit()

    def stop(self):
        """Function that closes the websocket connection"""
        self.socket.close()

    def log(self, msg, level=LogLevel.INFO):
        self.signals.log.emit(msg, level)

    def run(self):
        """Overridden from Thread. This function runs when Thread.start is called."""
        self.socket = websocket.WebSocketApp(self._url,
                              on_open=self.on_open,
                              on_message=self.on_message,
                              on_error=self.on_error,
                              on_close=self.on_close)
        self._connected = True
        self.socket.run_forever(skip_utf8_validation=False)
            