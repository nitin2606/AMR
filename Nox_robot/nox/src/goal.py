import rospy
from geometry_msgs.msg import PoseStamped


def send_goal(x, y, theta):

    rospy.init_node('goal_sender')
    goal_publisher = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    rospy.sleep(1)

    goal_msg = PoseStamped()
    goal_msg.header.frame_id = "map"
    goal_msg.pose.position.x = x
    goal_msg.pose.position.y = y
    goal_msg.pose.orientation.w = 1.0

    goal_publisher.publish(goal_msg)
    rospy.loginfo("Goal sent!") 


if __name__=='__main__':

    send_goal(-0.55, -0.55, 0.0)
