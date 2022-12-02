from flask import Flask
from threading import Thread
import asyncio

app = Flask("/")
grroms_id = 567680071628881921

channel = None
loop = None


@app.route("/")
def home():
    ping_grrom()
    return "Hello Annie here!"


def ping_grrom():
    # print("ping grrom")
    # theloop = asyncio.new_event_loop().create_task(channel.send(
    #     f"<@{grroms_id}> UptimeBot just pinged me!"))

    asyncio.run_coroutine_threadsafe(
        channel.send(
            f"<@{grroms_id}> UptimeBot just pinged me!"), loop)

    # await channel.send(f"<@{grroms_id}> Annie is online!")


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive(theChannel, theLoop):
    global channel
    global loop
    channel = theChannel
    loop = theLoop

    t = Thread(target=run)
    t.start()