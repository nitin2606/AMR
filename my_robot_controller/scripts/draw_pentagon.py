#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move_square():
    rospy.init_node('square_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    vel_msg = Twist()

    # Move forward
    vel_msg.linear.x = 1.0  # linear velocity in x-direction
    vel_msg.angular.z = 0.0  # angular velocity in z-direction (turning)
    duration = rospy.Duration(2)  # duration to move forward
    start_time = rospy.Time.now()
    while (rospy.Time.now() - start_time) < duration:
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    # Stop moving
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)
    rospy.sleep(1)

    # Turn 90 degrees
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 1.0  # angular velocity for turning
    duration = rospy.Duration(2)  # duration to turn
    start_time = rospy.Time.now()
    while (rospy.Time.now() - start_time) < duration:
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    # Stop turning
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)
    rospy.sleep(1)

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
