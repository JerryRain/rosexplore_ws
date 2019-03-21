#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def talker():
    pub = rospy.Publisher('/myrobot', Twist, queue_size=10)
    rospy.init_node('my_robot_keyboard', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        key = raw_input("Enter your input: ")
	rospy.loginfo("I get:: %s",key)
	twist = Twist()

	if key == "w":
		twist.linear.x = 2 
    	elif key == "s":
        	twist.linear.x = -2 
    	elif key == "a":
        	twist.angular.z = 2 
    	elif key == "d":
        	twist.angular.z = -2 
    	elif key == "z":
        	twist.angular.x = 0 
    	pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
