cmake_minimum_required(VERSION 3.5)
project(delta_robot_comm)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(delta_robot_msgs REQUIRED)  # Dependency on your interface package

ament_python_install_package(${PROJECT_NAME})
ament_package()
