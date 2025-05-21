import rospy
import turtlesim.msg
from geometry_msgs.msg import *
from turtlesim.msg import *
from std_srvs.srv import *
from turtlesim.srv import *


rospy.init_node('turtle', anonymous=True)
rate=rospy.Rate(10)
pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  

var=Twist()
var.linear.x=2.0
var.linear.y=0.0
var.linear.z=0.0

var.angular.x=0.0
var.angular.y=0.0
var.angular.z=2.0
for i in range(50):
    pub.publish(var)
    rate.sleep()

rospy.set_param('/my_turtle/background_b', 80)
rospy.set_param('/my_turtle/background_g', 80)
rospy.set_param('/my_turtle/background_r', 80)

bg_b=rospy.get_param('/my_turtle/background_b')
print('bg_blue-', bg_b)

bg_g=rospy.get_param('/my_turtle/background_g')
print('bg_green-', bg_g)

bg_r=rospy.get_param('/my_turtle/background_b')
print('bg_red-', bg_r)

def cb(data):
    for i in range(50):
        #print("--- Iteration {} ---".format(i+1))        
        #print("x: ",data.x)
        #print("y: ",data.y)
        #print("theta: ",data.theta)
        pass
rospy.Subscriber('/turtle1/pose',Pose, cb) 


clear=rospy.ServiceProxy('/clear', Empty)
clear()
reset=rospy.ServiceProxy('/reset', Empty)   
reset()

spwan=rospy.ServiceProxy('/spawn', Spawn)
spawn_return=spwan(2,7,1.57,'turtle2') 
print(spawn_return)

kill=rospy.ServiceProxy('/kill', Kill)
kill(spawn_return.name)


rospy.spin()