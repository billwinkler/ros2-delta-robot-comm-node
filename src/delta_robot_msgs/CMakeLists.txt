cmake_minimum_required(VERSION 3.5)
project(delta_robot_msgs)

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
# Uncomment if your messages use other packages (e.g., std_msgs)
# find_package(std_msgs REQUIRED)

# Generate interfaces (messages)
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/DeltaMotorCmd.msg"
  "msg/DeltaRobotCmd.msg"
  # Uncomment the DEPENDENCIES line if your messages use types from other packages
  # DEPENDENCIES std_msgs
)

# Export dependencies for runtime (needed for Python interfaces, etc.)
ament_export_dependencies(rosidl_default_runtime)

ament_package()
