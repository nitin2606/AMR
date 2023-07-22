import rospy

from std_msgs.msg import String
from std_msgs.msg import Float32

def callback(data):

    rospy.loginfo("Received %s", data.data)


def subscriber_node():

    rospy.init_node('sub_node', anonymous=True)
    rospy.Subscriber('imp', String, callback=callback)
    