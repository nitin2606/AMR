#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

def publish_markers():
    rospy.init_node('marker_publisher', anonymous=True)
    marker_publisher = rospy.Publisher('visualization_marker', Marker, queue_size=10)

    # Create a marker
    marker = Marker()
    marker.header.frame_id = "map"  # The frame in which the marker is defined
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.scale.x = 0.2  # Point size
    marker.scale.y = 0.2
    marker.color.a = 1.0  # Alpha channel (fully opaque)
    marker.color.r = 1.0  # Red color
    marker.color.g = 0.0
    marker.color.b = 0.0

    # Add points and labels to the marker
    points = [(-0.51, -0.51, 0.0)]  # Example points
    for i, (x, y, z) in enumerate(points):
        point = Point()
        point.x = x
        point.y = y
        point.z = z
        marker.points.append(point)

        # Add labels for each point
        label = "Point {}".format(i)
        marker_text = Marker()
        marker_text.header.frame_id = "map"
        marker_text.type = Marker.TEXT_VIEW_FACING
        marker_text.action = Marker.ADD
        marker_text.pose.position = point
        marker_text.scale.z = 0.5
        marker_text.color.a = 1.0
        marker_text.color.r = 0.0
        marker_text.color.g = 1.0
        marker_text.color.b = 0.0
        marker_text.text = label
        marker_text.id = i + 1000  # Ensuring a unique ID for each marker
        marker_publisher.publish(marker_text)

    # Publish the marker
    marker_publisher.publish(marker)
    rospy.loginfo("Marker Published.")
    rospy.spin()

if __name__ == '__main__':
    try:
        publish_markers()
    except rospy.ROSInterruptException:
        pass
