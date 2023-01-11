FROM osrf/ros:foxy-desktop

WORKDIR /root
RUN mkdir -p foxy_ws/src/

RUN apt update &&\
    apt install ros-foxy-navigation2 ros-foxy-nav2-bringup ros-foxy-turtlebot3* -y

VOLUME [ "/root/foxy_ws/src/" ]

SHELL [ "/bin/bash" , "-c"]
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> .bashrc
WORKDIR /root/foxy_ws/src