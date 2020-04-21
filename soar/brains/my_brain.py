# This file is intended as an example. Use it as a template for other Soar brains
import soar
from soar.robot.base import BaseRobot
from soar.robot.pioneer import PioneerRobot
from soar.robot.my_bot import MyRobot
from soar.gui.plot_window import PlotWindow
from soar.hooks import sim_completed
from soar.sim.world import Polygon
from soar.sim.world import World
import numpy as np
robot = MyRobot()

print(soar.__file__)

#  This function is called when the brain is loaded
def on_load():
    pass


#  This function is called when the start button is pushed
def on_start():
    # print('Hi Haylee!')
    pass


#  This function is called every step_duration seconds. By default, it is called 10 times/second
def on_step(step_duration):
    # robot._fv = 0
    collided = robot._collided
    # turning = robot._rv != 0
    robot._rv = 0
    x,y,_ = robot.pose

    proximity = np.array(robot._sonars[2:7]) <= .3
    target_headings = np.array(list(robot._target_headings))-2
    try:
        # target_sensors = self._target_headings
        proximity[target_headings] = False
    except:
        pass

    if collided:
        robot._collided = False
        robot._fv = -.5
        robot._rv = 0
    else:
        robot._fv = .5
        robot._rv = 0
    # sonar detects target
    if robot._target_found:
        heading = robot._target_heading
        if heading < 4:
            new_rv = .5
        elif heading > 4:
            new_rv = -.5
        else: # target is dead ahead
            new_rv = 0
            robot._fv = 1

        if np.any(proximity):
            if robot._sonars[2] > robot._sonars[6]:
                new_rv = np.random.choice([2,5,10])
            elif robot._sonars[2] < robot._sonars[6]:
                new_rv = -np.random.choice([2,5,10])
            else:
                new_rv = np.pi

        robot._rv = new_rv

    # wander
    elif np.any(proximity):
        if robot._sonars[2] > robot._sonars[6]:
            new_rv = np.random.choice([2,5,10])
        elif robot._sonars[2] < robot._sonars[6]:
            new_rv = -np.random.choice([2,5,10])
        else:
            new_rv = 10

        robot._rv = new_rv
        robot._fv = 0

    # begin moving
    else:
        robot._rv = 0
        robot._fv = .5

    # if turning and collided and robot._sonars[4] > robot._sonar_max:
    #     print('hi')
    #     robot._rv = 0
    #     robot._fv = .5
    #     turning = False
    #     robot.collided = False
    #
    # elif collided:
    #     print('Ouch!')
    #     robot._rv = 1
    #     robot._fv = 0
    #     turning = True
    #     robot._collided = False
    #
    # if robot._fv == 0 and not collided:
    #     robot._fv = .5

    pass


# This function is called when the stop button is pushed
def on_stop():
    pass


# This function is called when the robot's controller is shut down
def on_shutdown():
    pass
