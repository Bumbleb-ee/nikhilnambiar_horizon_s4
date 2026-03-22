#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher=self.create_publisher(String,'/distance',10)
        self.timer=self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        
        distance=random.randint(1,100)
        msg=String()
        msg.data=str(distance)
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing distance: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = DistancePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()