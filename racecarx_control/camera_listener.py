import rclpy
import cv2 
from rclpy.node import Node
from cv_bridge import CvBridge

from sensor_msgs.msg import Image

class CameraSubscriber(Node):

    def __init__(self):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(Image, "camera", self.img_callback, 10)
        self.subscription

        self.br = CvBridge()

    def img_callback(self, data):
        #self.get_logger().info('Receiving image frame')

        # Convert the message from ROS 2 Image format to a more usable OpenCV format
        current_frame = self.br.imgmsg_to_cv2(data)
        cv2.imshow("camera", current_frame)   
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    camera_subscriber = CameraSubscriber()

    rclpy.spin(camera_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    camera_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()