cmake_minimum_required(VERSION 3.0.2)
project(simple_publisher)

find_package(catkin REQUIRED COMPONENTS
  rospy
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES simple_publisher
#  CATKIN_DEPENDS rospy
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS src/simple_publisher_node.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})