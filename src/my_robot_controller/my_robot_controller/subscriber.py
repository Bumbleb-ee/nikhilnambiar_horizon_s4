#!/usr/bin/env python3
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')

        self.subscription = self.create_subscription(
            String,
            '/distance',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
      
        self.get_logger().info(f'Received distance: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()