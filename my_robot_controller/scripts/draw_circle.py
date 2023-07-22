import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color

if __name__=='__main__':

    rospy.init_node("draw_circle")

    rospy.loginfo("Circle Node has Started!")

    # first give the exact name of topic to publish command on here in this
    # case it is /turtle1/cmd_vel
    # then give the data type to send

    
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    pub2 = rospy.Publisher("turtlesim/Color",Color, queue_size=10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():

        # publish a cmd
        msg = Twist()  # Message shuld be object of twist
        msg.linear.x = 2.0 
        msg.angular.z = 1.0

        color = Color()
        color.r = 200
        color.g = 10
        color.b = 10
        
        pub.publish(msg)
        pub2.publish(color)
         
        rate.sleep()
