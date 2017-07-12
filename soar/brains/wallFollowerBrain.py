import math

from soar.robot.pioneer import PioneerRobot
from soar.gui.plugin import *
import lib601.sonarDist as sonarDist
from soar.gui.plotWindow import PlotWindow


robot = PioneerRobot()


# called when the brain is loaded
def on_load():
    robot.distance = []     # initialize list of distances to plot
    print(robot.pos.xyt_tuple())


# called when the start button is pushed
def on_start():
    robot.set_forward_velocity(0.1)

# called 10 times per second
def on_step(step_duration):
    sonars = robot.get_sonars()
    distance = sonars[7]
    print("Distance to wall: %.03f" % distance)
    robot.distance.append(distance)   # append new distance to list

    desired = 0.5
    k_r = 1.0

    robot.set_rotational_velocity(k_r*(desired-distance))

# called when the stop button is pushed
def on_stop():
    p = PlotWindow(toplevel=Toplevel)
    p.plot(robot.distance)    # plot the list of distances
    print(2*math.pi/math.atan2(math.sqrt(1.0*0.1*0.1*0.1), 1))

    p.set_title("Gain: {gain}".format(gain="this should show the value of the gain")) # uncomment this line if you wish
    p.set_xlabel("Timesteps")
    p.set_ylabel("DIstance (m)")

# called when brain or world is reloaded (before setup)
def on_shutdown():
    pass