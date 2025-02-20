#!/usr/bin/env python3
import rclpy
import struct
from rclpy.node import Node
from delta_robot_msgs.msg import DeltaRobotCmd, DeltaMotorCmd

DEVICE_PATH = "/dev/delta_robot"

class DeltaRobotCommNode(Node):
    def __init__(self):
        super().__init__('delta_robot_comm_node')
        self.subscription = self.create_subscription(
            DeltaRobotCmd,
            '/delta_robot/cmd',
            self.cmd_callback,
            10
        )
        self.get_logger().info('DeltaRobotCommNode has started.')

    def send_to_kernel(self, commands):
        """Sends all motor commands in a single write operation."""
        try:
            with open(DEVICE_PATH, "wb") as dev_file:
                # Pack data: each command is (motor_id, pulses, direction)
                cmd_data = b''.join(struct.pack("iii", cmd.motor_id, cmd.pulses, cmd.direction) for cmd in commands)

                dev_file.write(cmd_data)
                self.get_logger().info(f"Sent {len(commands)} commands to kernel in a single write.")
                return True
        except OSError as e:
            self.get_logger().error(f"Failed to write to {DEVICE_PATH}: {e}")
            return False

    def cmd_callback(self, msg):
        """Handles incoming DeltaRobotCmd messages."""
        if len(msg.commands) > 3:
            self.get_logger().error(f"Too many motor commands received ({len(msg.commands)}). Max is 3.")
            return

        self.get_logger().info(f"Processing {len(msg.commands)} motor command(s).")
        success = self.send_to_kernel(msg.commands)
        
        if not success:
            self.get_logger().error("Failed to send motor commands to kernel.")

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
