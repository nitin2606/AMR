import rospy
 

if __name__=='__main__':

    rospy.init_node("test_node")

    rospy.loginfo("Test Node Started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():


        rospy.loginfo('Hello')
        
        rate.sleep()

    '''rospy.logwarn("Warning from test node")
    rospy.logerr("Error Occurred")

    rospy.sleep(1)  # duration in secarted

    rospy.loginfo("End of program")'''

 