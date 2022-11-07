#!/usr/bin/env python3
# coding: utf-8

import rospy
from std_msgs.msg import String
from rospy_message_converter import json_message_converter
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://192.168.56.11:3000") as websocket:
        await websocket.send("Hello world! Test, awdsjkfwoe")
        await websocket.recv()

asyncio.run(hello())


# def callback(data):
#     # rospy.loginfo("I heard %s",data.data)
#     json_str = json_message_converter.convert_ros_message_to_json(data)
#     # rospy.loginfo(json_str)
#     # rospy.loginfo(type(json_str))
    




# rospy.init_node('simple_subscriber_node')
# rospy.Subscriber("simple_msg", String, callback)
# # spin() simply keeps python from exiting until this node is stopped
# rospy.spin()