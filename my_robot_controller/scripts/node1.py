import rospy

from std_msgs.msg import String
from std_msgs.msg import Float32

def publisher_node():

    rospy.init_node("pub_node", anonymous=True)
    pub = rospy.Publisher('imp', String, queue_size=10)

    rate = rospy.Rate(1)


    while not rospy.is_shutdown():

        data = "Hello ROS!"
        rospy.loginfo("Publishing : %s", data)
        pub.publish(data)
        rate.sleep()


if __name__=='__main__':

    try:
        publisher_node()
    
    except rospy.ROSInterruptException:
        pass