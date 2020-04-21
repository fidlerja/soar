from soar.sim.world import *
import numpy as np

obj1 = [1,4]
obj1 = np.random.uniform(0,8,2)
pts1 = [(obj1[0],obj1[1]),       (obj1[0]+.2,obj1[1]),
        (obj1[0]+.2,obj1[1]+.2), (obj1[0],obj1[1]+.2)]
op1 = {'fill':'purple'}
target = Polygon(pts1, **op1)

world = World(dimensions=(8, 8), initial_position=(1.0, 1.0, 0),
              objects=[Block((2, 0), (2, 4)),
                       Block((2, 4), (4, 4)),
                       Block((2, 6), (6, 6)),
                       Block((6, 6), (6, 0)),
                       Block((6, 2), (4, 2)),
                       target])
