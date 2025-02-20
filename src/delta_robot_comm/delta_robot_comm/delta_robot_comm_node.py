#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from delta_robot_msgs.msg import DeltaRobotCmd, DeltaMotorCmd

class DeltaRobotCommNode(Node):
    def __init__(self):
        super().__init__('delta_robot_comm_node')
        # Subscribe to the /delta_robot/cmd topic using our custom message
        self.subscription = self.create_subscription(
            DeltaRobotCmd,
            '/delta_robot/cmd',
            self.cmd_callback,
            10
        )
        self.get_logger().info('DeltaRobotCommNode has started.')

    def cmd_callback(self, msg):
        # Log the received command
        for i, motor_cmd in enumerate(msg.commands):
            self.get_logger().info(f"Command {i}: motor_id={motor_cmd.motor_id}, pulses={motor_cmd.pulses}, direction={motor_cmd.direction}")

def main(args=None):
    rclpy.init(args=args)
    node = DeltaRobotCommNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
