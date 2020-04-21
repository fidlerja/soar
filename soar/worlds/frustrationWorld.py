from soar.sim.world import *

obj1 = [1,4]
obj1 = np.random.uniform(0,8,2)
pts1 = [(obj1[0],obj1[1]),       (obj1[0]+.2,obj1[1]),
        (obj1[0]+.2,obj1[1]+.2), (obj1[0],obj1[1]+.2)]
op1 = {'fill':'purple'}
target = Polygon(pts1, **ob1)

world = World(dimensions=(4, 4), initial_position=(0.5, 0.5, 0),
              objects=[Wall((1, 0), (1, 2)),
                       Wall((1, 2), (2, 2)),
                       Wall((1, 3), (3, 3)),
                       Wall((3, 3), (3, 0)),
                       Wall((3, 1), (2, 1)),
                       target])
