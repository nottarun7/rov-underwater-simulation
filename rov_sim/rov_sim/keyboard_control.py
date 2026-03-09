import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, termios, tty

class KeyboardControl(Node):

    def __init__(self):
        super().__init__('keyboard_control')
        self.pub = self.create_publisher(Twist, '/babyrov/cmd_vel', 10)

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def run(self):
        twist = Twist()

        while True:
            key = self.get_key()

            if key == 'w':
                twist.linear.x = 1.0
            elif key == 's':
                twist.linear.x = -1.0
            elif key == 'a':
                twist.linear.y = 1.0
            elif key == 'd':
                twist.linear.y = -1.0
            elif key == 'q':
                twist.angular.z = 1.0
            elif key == 'e':
                twist.angular.z = -1.0
            else:
                twist = Twist()

            self.pub.publish(twist)

settings = termios.tcgetattr(sys.stdin)

def main():
    rclpy.init()
    node = KeyboardControl()
    node.run()

if __name__ == '__main__':
    main()