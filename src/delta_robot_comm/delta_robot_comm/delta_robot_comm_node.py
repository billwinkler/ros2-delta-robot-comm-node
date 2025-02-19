#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class DeltaRobotCommNode(Node):
    def __init__(self):
        super().__init__('delta_robot_comm_node')
        # Subscribe to the /delta_robot/cmd topic
        self.subscription = self.create_subscription(
            Int32MultiArray,
            '/delta_robot/cmd',
            self.cmd_callback,
            10
        )
        self.get_logger().info('DeltaRobotCommNode has started.')

    def cmd_callback(self, msg):
        # Log the received message
        self.get_logger().info(f"Received command: {msg.data}")

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
