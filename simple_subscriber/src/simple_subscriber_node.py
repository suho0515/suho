#!/usr/bin/env python3
# coding: utf-8

import rospy
from std_msgs.msg import String
from rospy_message_converter import json_message_converter
# import asyncio
# import websockets

# async def hello():
#     async with websockets.connect("ws://192.168.56.11:3000") as websocket:
#         await websocket.send("Hello world!")
#         await websocket.recv()

# asyncio.run(hello())

import socket

SERVER_IP = '192.168.56.11'
SERVER_PORT = 3000
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR) 
    client_socket.send('hi'.encode()) 
    msg = client_socket.recv(SIZE) 
    print("resp from server : {}".format(msg)) 
    # rospy.sleep(1)

# def callback(data):
#     # rospy.loginfo("I heard %s",data.data)
#     json_str = json_message_converter.convert_ros_message_to_json(data)
#     # rospy.loginfo(json_str)
#     # rospy.loginfo(type(json_str))
    




# rospy.init_node('simple_subscriber_node')
# rospy.Subscriber("simple_msg", String, callback)
# # spin() simply keeps python from exiting until this node is stopped
# rospy.spin()