import asyncio
import time
from threading import Thread
import discord
from PySide6.QtCore import Signal, QObject
from lumiastream import LumiaStream
from loglevel import LogLevel

class DiscordBot(discord.Client):
    """
    Class that represents a Discord Bot
    """

    SecsBetweenResponses = 10

    def __init__(self, discord_token, discord_channel_id, msg_callback=None):
        """
        Constructs a Discord Bot object
        Parameters:
            discord_token: Discord Auth Token
            discord_channel_id: The Discord channel ID (not name) to monitor
            msg_callback: Callback function called when Discord message is received
        """
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(intents=intents)
        self.discord_token = discord_token
        self.channels = [int(discord_channel_id)]
        self.msg_callback = msg_callback
        self.last_response = 0
        self.num_responses = 0

    async def on_message(self, message):
        """Callback function when a discord message is received"""
        if message.channel.id in self.channels:
            if len(message.content) > 0 and message.content[0] == "!":
                command = message.content[1:]
                self.msg_callback(command)
                if time.time()-self.last_response > DiscordBot.SecsBetweenResponses:
                    response_str = ""
                    if self.num_responses > 0:
                        response_str = f"  - and {self.num_responses} others"
                    await message.channel.send(f"Sent to Lumia: {message.content}{response_str}")
                    self.num_responses = 0
                    self.last_response = time.time()
                else:
                    self.num_responses += 1
                    
    async def start(self):
        """Overridden function to start the Discord bot."""
        await super().start(self.discord_token)

class DiscordBotRunner(Thread):
    """
    Class to encapsulate the running of both LumiaStream connection and the Discord bot.
    It also facilitates the communication between LumiaStream and Discord.
    """

    class Signals(QObject):
        """
        Subclass to contain Qt Signals to be sent back to GUI
        """
        log = Signal(str, LogLevel)

    def __init__(self, discord_token, channel_id, lumia_token, lumia_host, lumia_port):
        """
        Constructs a DiscordBotRunner object
        Parameters:
            discord_token: Discord Auth Token
            discord_channel_id: The Discord channel ID (not name) to monitor
            lumia_token: LumiaStream API Auth Token. Found at LumiaStream > Settings > API
            lumia_host: lumiastream api hostname (e.g. localhost)
            lumia_port: LumiaStream TCP port number of the API endpoint
        """
        Thread.__init__(self)
        self.discord_token = discord_token
        self.channel_id = channel_id
        self.lumia_token = lumia_token
        self.lumia_host = lumia_host
        self.lumia_port = lumia_port
        self.lumia = None
        self.bot = None
        self.signals = DiscordBotRunner.Signals()
        self.runner = asyncio.Runner()
        self.loop = self.runner.get_loop()
        self._stopping = False
    
    def on_discord_msg(self, msg):
        """Callback Function called when a Discord message is received"""
        if self.lumia:
            self.lumia.send_chat_cmd(msg)
        self.log(f"Discord Msg: {msg}", LogLevel.DEBUG)

    def close(self):
        """Function to quit the Discord bot and close the LumiaStream connection"""
        self._stopping = True
        if self.lumia is not None:
            self.lumia.stop()
            self.lumia.join()
        if self.bot is not None:
            asyncio.run_coroutine_threadsafe(self.bot.close(), self.loop)
    
    def log(self, msg, level=LogLevel.INFO):
        """Function to send a log message back to the GUI"""
        self.signals.log.emit(msg, level)

    def discord_status(self):
        discord_alive = False
        discord_ready = False
        msg = ""
        if self.bot is not None:
            discord_alive = self.bot.user is not None
            discord_ready = self.bot.is_ready()
            msg = "Logged In"
            self.log(f"DiscordBot Status: LoggedIn[{discord_alive}] Ready[{discord_ready}]", LogLevel.DEBUG)
        else:
            msg= "Not Running"
        self.log(f"DiscordBot Status: LoggedIn[{discord_alive}] Ready[{discord_ready}]", LogLevel.DEBUG)
        return discord_alive and discord_ready, msg

    def lumia_status(self):
        msg = "Not Connected"
        connected = self.lumia.is_connected()
        if connected:
            msg = "Connected"
        self.log(f"Lumia WebSocket: Connected = {connected}", LogLevel.DEBUG)
        return connected, msg

    def lumia_callback_disconnected(self):
        self.log("Lumia Disconnected")

    def lumia_callback_connected(self):
        self.log("Lumia Connected")

    def lumia_callback_on_msg(self, msg):
        self.log(f"Lumia Msg: {msg}", LogLevel.DEBUG)

    def lumia_callback_on_error(self, msg):
        self.log(f"Lumia Error: {msg}", LogLevel.ERROR)

    def lumia_start(self):
        log_msg = f"""
            Starting LumiaStream Connection.
            Lumia: {self.lumia_host}:{self.lumia_port}
            Token: {self.lumia_token}
        """
        self.log("Connecting to LumiaStream: " )
        self.lumia = LumiaStream(self.lumia_token, self.lumia_host, self.lumia_port)
        self.lumia.signals.log.connect(self.log)
        self.lumia.signals.disconnected.connect(self.lumia_callback_disconnected)
        self.lumia.signals.connected.connect(self.lumia_callback_connected)
        self.lumia.signals.on_message.connect(self.lumia_callback_on_msg)
        self.lumia.signals.on_error.connect(self.lumia_callback_on_error)
        self.lumia.start()

    def run(self):
        """
        Overriden Function ran when Thread.start is called
        Creates and runs the LumiaStream connection and DiscordBot
        """
        self.lumia_start()
        self.bot = DiscordBot(self.discord_token, self.channel_id, self.on_discord_msg)
        self.runner.run(self.bot.start())