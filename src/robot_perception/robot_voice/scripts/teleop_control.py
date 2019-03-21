#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def talker():
	pub = rospy.Publisher('/myrobot', Twist, queue_size=10)
	rospy.init_node('my_robot_keyboard', anonymous=True)
	rate = rospy.Rate(100) # 10hz
	while 1:
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
	    	elif key == "q":
			twist.angular.y = 1
		elif key == "z":
			twist.angular.x = 0
#		elif key == '\x03':
#			dal.send_signal(signal.CTRL_C_EVENT)
	    	pub.publish(twist)
		rate.sleep()

if __name__ == '__main__':
	try:	
		talker()
	except:
		pass
