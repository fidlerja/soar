from soar.sim.world import *
import numpy as np

np.random.seed(10)
np.random.seed(11)
np.random.seed(20)
dimensions = (8.05, 8.05)
obj1 = [2,1]
obj1 = np.random.uniform(0,8,2)
pts1 = [(obj1[0],obj1[1]),       (obj1[0]+.2,obj1[1]),
        (obj1[0]+.2,obj1[1]+.2), (obj1[0],obj1[1]+.2)]
op1 = {'fill':'purple'}
target = Polygon(pts1, **op1)

objects = [target]
for _ in range(10):
    obj_ = np.random.uniform(0,8,2)
    pts_ = [(obj_[0], obj_[1]),       (obj_[0]+.4, obj_[1]),
            (obj_[0]+.4, obj_[1]+.4), (obj_[0], obj_[1]+.4)]
    objects.append(Polygon(pts_))

world = World(dimensions=dimensions, initial_position=(1.0, 1.0, 0.0),
              objects=[Polygon(pts1, **op1)] + objects)
