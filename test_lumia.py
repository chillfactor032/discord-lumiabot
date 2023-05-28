from lumiastream import LumiaStream
import time

lumia = LumiaStream("localhost:39231", "gyzetm2pbek5jggjygj9")
lumia.start()
time.sleep(5)
lumia.send_chat_cmd("!police")
time.sleep(3)
lumia.stop()
lumia.join()
