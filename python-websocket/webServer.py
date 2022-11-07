# #!/usr/bin/env python3

import asyncio
import websockets
import threading

msg = ""
async def echo(websocket):
    global msg
    async for message in websocket:
        # print(message)
        if message != "test4":
            msg = message
        elif message == "test4":
            await websocket.send(msg)


async def main():
    async with websockets.serve(echo, "192.168.56.11", 3000):
        await asyncio.Future()  # run forever

asyncio.run(main())

