#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class DecisionNode(Node):
    def __init__(self):
        super().__init__('decision_node')
        
        self.subscription = self.create_subscription(
            String,
            '/distance',
            self.listener_callback,
            10
        )
        
        self.publisher_ = self.create_publisher(
            String,
            '/rover_command',
            10
        )
    def listener_callback(self, msg):
        distance = int(msg.data)
        
        if distance < 30:
            command = "STOP"
        else:
            command = "MOVE_FORWARD"
        
        cmd_msg = String()
        cmd_msg.data = command
        
        self.publisher_.publish(cmd_msg)
        
        self.get_logger().info(
            f'Received distance: {distance} -> Command: {command}'
        )
def main(args=None):
    rclpy.init(args=args)
    node = DecisionNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()