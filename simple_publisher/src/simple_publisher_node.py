#!/usr/bin/env python3
# coding: utf-8

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('simple_msg', String, queue_size=10)
rospy.init_node('simple_publisher_node')
r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
   pub.publish("hello world")
   r.sleep()

   