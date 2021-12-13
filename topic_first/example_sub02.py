#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun_callback(msg): 
    rospy.loginfo('%s',msg.data) 
    return


if __name__ == '__main__':
    rospy.init_node('sample02_pub')
    rospy.Subscriber('hello_ex', String, callback= fun_callback)
    rospy.spin() 
    pass