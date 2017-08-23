#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def method1():
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 10)
	rospy.init_node('Robot_HUEHUE', anonymous = True)
	robo = Twist()
	#robo.linear.x = 0.15
	#robo.angular.x = .33
	robo.angular.z = 1
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		pub.publish(robo)
		rate.sleep()

if __name__ == '__main__':
	method1()
