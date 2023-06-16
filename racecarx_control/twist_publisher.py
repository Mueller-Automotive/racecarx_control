import rclpy
import time

from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwistPublisher(Node):

    def __init__(self):
        super().__init__('twist_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        time.sleep(5)

        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.3

        self.publish_callback(msg)

        time.sleep(5)

        msg.linear.x = 0.0
        msg.angular.z = 0.0

        self.publish_callback(msg)
        

    def publish_callback(self, msg):
        time.sleep(5)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing twist data!')


def main(args=None):
    rclpy.init(args=args)

    twist_publisher = TwistPublisher()

    rclpy.spin(twist_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    twist_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()