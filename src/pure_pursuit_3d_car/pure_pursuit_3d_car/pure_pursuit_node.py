import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math

class PurePursuit3D(Node):

    def __init__(self):
        super().__init__('pure_pursuit_3d_node')

        self.declare_parameter('target_x', 5.0)
        self.declare_parameter('target_y', 5.0)

        self.target_x = self.get_parameter('target_x').value
        self.target_y = self.get_parameter('target_y').value

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        dx = self.target_x - x
        dy = self.target_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        angle = math.atan2(dy, dx)

        cmd = Twist()
        cmd.linear.x = min(1.0, distance)
        cmd.angular.z = angle  # Simplified — will refine this

        self.publisher_.publish(cmd)
        self.get_logger().info(f"Tracking to ({self.target_x}, {self.target_y}) | Current: ({x:.2f}, {y:.2f})")

def main(args=None):
    rclpy.init(args=args)
    node = PurePursuit3D()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
