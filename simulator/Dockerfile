FROM osrf/ros:foxy-desktop

RUN apt-get update

# Install Gazebo
RUN apt-get install -y ros-foxy-gazebo-*

# Install Cartographer Package
RUN apt install -y ros-foxy-cartographer
RUN apt install -y ros-foxy-cartographer-ros

# Install Navigation Package
RUN apt install -y ros-foxy-navigation2
RUN apt install -y ros-foxy-nav2-bringup

# Install Package to create URDF
RUN apt install -y ros-foxy-joint-state-publisher-gui
RUN apt install -y ros-foxy-xacro

RUN apt-get install -y nano