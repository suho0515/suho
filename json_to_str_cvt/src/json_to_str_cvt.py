#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function
import time
import json
import roslibpy

import asyncio
import websockets

class JSON_TO_STR_CVT:
    def __init__(self):
        self.websocket_msg = ""
        self.ros_msgs = []

        self.client = roslibpy.Ros(host='192.168.56.3', port=9090)
        self.client.run()

        self.simple_msg_listener = roslibpy.Topic(self.client, '/simple_msg', 'std_msgs/String')
        self.simple_msg_listener.subscribe(self.simple_msg_subscriber)

        asyncio.run(self.websocket_server())

        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.client.terminate()

    def simple_msg_subscriber(self, msg):
        msg["name"] = "simple_msg"
        msg["type"] = "std_msgs/String"
        print(json.dumps(msg))
        self.ros_msgs.append(json.dumps(msg))
        # header = Header(msg['seq'], msg['stamp'], msg['frame_id'])
        # age = time.time() - header['stamp'].to_sec()
        # fmt = 'Age of message (sequence #%d): %6.3f seconds'
        # log.info(fmt, msg['seq'], age)
        # Simulate a very slow consumer
        # time.sleep(.5)

    async def websocket_server(self):
        async with websockets.serve(self.echo, "192.168.56.11", 3000):
            await asyncio.Future()  # run forever

    async def echo(self, websocket):
        async for message in websocket:
            print(message)
            # if message != "request":
            #     self.websocket_msg = message
            # elif message == "request":
            #     await websocket.send(self.websocket_msg)

            if message == "request":
                while(len(self.ros_msgs) != 0):
                    await websocket.send(self.ros_msgs[0])
                    del self.ros_msgs[0]
                    







