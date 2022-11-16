#!/usr/bin/env python3
# coding: utf-8

import rospy
from json_to_str_cvt import JSON_TO_STR_CVT

if __name__ == '__main__':
    try:
        json_to_str_cvt = JSON_TO_STR_CVT()
    except rospy.ROSInterruptException:
        pass