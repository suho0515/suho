# #!/usr/bin/env python3

import asyncio
import websockets
import threading

msgs = []

async def echo(websocket):
    print(websocket.remote_address)
    async for message in websocket:
        await websocket.send(message)
        await websocket.send("test")
        # print(message)
    #     msgs.append(message)
    #     print(msgs)
    # print(websocket)
    # for i in range(len(msgs)):
    #     await websocket.send(msgs[i])
    #     # msgs.pop()
    # print("send msgs")

async def main():
    async with websockets.serve(echo, "192.168.56.11", 3000):
        await asyncio.Future()  # run forever

asyncio.run(main())

