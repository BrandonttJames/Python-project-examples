#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def method1():
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 10)
    rospy.init_node('Robot_HUEHUHE', anonymous = True)
    robo = Twist()
    choice = 0
    lv = 0.15
    av = 1.5708

    while not choice == 'q' :
        choice = raw_input('enter command')
        if choice == '1':
            seconds = raw_input('How many seconds?')
            seconds = float(seconds)
            if seconds <= 2:
                robo.linear.x = lv
                rate = rospy.Rate(10)
                d = rospy.Duration(seconds)
                s = rospy.Time.now()
                while rospy.Time.now() - s < d:
                    pub.publish(robo)
                    rate.sleep()
	elif choice == '2':
            seconds = raw_input('How many seconds?')
            seconds = float(seconds)
            if seconds <= 2:
                robo.linear.x = -1*lv
                rate = rospy.Rate(10)
                d = rospy.Duration(seconds)
                s = rospy.Time.now()
                while rospy.Time.now() - s < d:
                    pub.publish(robo)
                    rate.sleep()
	elif choice == '3':
            dist = raw_input('Enter Meters : ')
            dist = float(dist)
            if dist <= 0.33:
                robo.linear.x = lv
                rate = rospy.Rate(10)
		seconds = dist/abs(lv)
                d = rospy.Duration(seconds)
                s = rospy.Time.now()
                while rospy.Time.now() - s < d:
                    pub.publish(robo)
                    rate.sleep()
	elif choice == '4':
            dist = raw_input('Enter Meters (should be positive): ')
            dist = float(dist)
            if dist <= 0.33:
                robo.linear.x = -1*lv
                rate = rospy.Rate(10)
		seconds = dist/abs(lv)
                d = rospy.Duration(seconds)
                s = rospy.Time.now()
                while rospy.Time.now() - s < d:
                    pub.publish(robo)
                    rate.sleep()
	elif choice == '5':
            	radians = 1.5708
		robo.angular.z = -1*av
		rate = rospy.Rate(10)
		seconds = radians/abs(av)
		d = rospy.Duration(seconds)
		s = rospy.Time.now()
		while rospy.Time.now() - s < d:
		    pub.publish(robo)
		    rate.sleep()
	elif choice == '6':

            	radians = 1.5708
		robo.angular.z = av
		rate = rospy.Rate(10)
		seconds = radians/abs(av)
		d = rospy.Duration(seconds)
		s = rospy.Time.now()
		while rospy.Time.now() - s < d:
		    pub.publish(robo)
		    rate.sleep()
	elif choice == '7':
            degrees = raw_input('Enter how many degrees clockwise: ')
            degrees = float(degrees)
            if degrees <= 180 and degrees >= -180:
                robo.angular.z = -1*av
		radians = degrees*math.pi/180.0
                rate = rospy.Rate(10)
		seconds = radians/abs(av)
                d = rospy.Duration(seconds) 
                s = rospy.Time.now()
                while rospy.Time.now() - s < d:
                    pub.publish(robo)
                    rate.sleep()
	elif choice == '8':
            degrees = raw_input('Enter how many degrees anticlockwise: ')
            degrees = float(degrees)
            if degrees <= 180 and degrees >= -180:
                robo.angular.z = av
		radians = degrees*math.pi/180.0
                rate = rospy.Rate(10)
		seconds = radians/abs(av)
                d = rospy.Duration(seconds) 
                s = rospy.Time.now()
                while rospy.Time.now() - s < d:
                    pub.publish(robo)
                    rate.sleep()
	elif choice == '9':
		change = raw_input('Enter X direction Speed: ')
           	lv = float(change)
		change = raw_input('Enter Angular Speed: ')
           	av = float(change)
		
if __name__ == '__main__':
    method1()
