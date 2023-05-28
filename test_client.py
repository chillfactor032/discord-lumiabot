import time
from discordbot import DiscordBotRunner

discord_token = "MTExMDUzMTI2NDg0MDIxNjYwNg.G5dgBH.FqNppQ65FymM7pzqr15oOmIN7gcXuGaF6LlDHU"
channel = 1110899285635125248
lumia_token = "gyzetm2pbek5jggjygj9"
lumia_host = "localhost"
lumia_port = 39231

try:
    runner = DiscordBotRunner(discord_token, channel, lumia_token, lumia_host, lumia_port)
    runner.start()
    print("Running DiscordBotRunner...")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt as e:
    print("Keyboard Interrupt. Closing Bot.")
    runner.close()
print("Done")
