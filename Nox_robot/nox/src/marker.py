import rospy
from visualization_msgs.msg import Marker

def publish_marker(x, y):

    rospy.init_node('marker_publisher')
    marker_publisher = rospy.Publisher('/visualization_marker', Marker, queue_size=1)
    rospy.sleep(1)

    marker_msg = Marker()
    marker_msg.header.frame_id = "map"
    marker_msg.type = Marker.SPHERE
    marker_msg.action = Marker.ADD
    marker_msg.pose.position.x = x
    marker_msg.pose.position.y = y
    marker_msg.pose.orientation.w = 1.0  # Assuming no rotation
    marker_msg.scale.x = 0.2
    marker_msg.scale.y = 0.2
    marker_msg.scale.z = 0.2
    marker_msg.color.r = 1.0
    marker_msg.color.g = 0.0
    marker_msg.color.b = 0.0
    marker_msg.color.a = 1.0

    marker_publisher.publish(marker_msg)
    rospy.loginfo("Marker publisher")
    rospy.spin()

if __name__=='__main__':
    publish_marker(-0.51, -0.51)