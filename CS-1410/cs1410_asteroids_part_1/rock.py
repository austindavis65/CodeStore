from polygon import Polygon
from random import randrange, uniform
import math
class Rock(Polygon):
    def __init__(self,x,y,world_width,world_height):
        super().__init__(x,y,0,0,uniform(0.0,359.9),world_width,world_height)
        self.mSpinRate = uniform(-90,90)
        self.setPolygon(self.createRandomPolygon(uniform(15,20),randrange(5,9)))
        self.accelerate(uniform(10,20))
    def createRandomPolygon(self,radius,number_of_points):
        plist = []
        theta = (math.pi*2)/number_of_points
        for i in range(number_of_points):
            r = uniform(radius*.7,radius*1.3)
            x = r*math.cos(theta*i)
            y = r*math.sin(theta*i)
            plist.append((x,y))
        return plist
    def getSpinRate(self):
        return self.mSpinRate
    def setSpinRate(self,spin_rate):
        self.mSpinRate = spin_rate
    def evolve(self,dt):
        self.rotate(self.mSpinRate*dt)
        self.move(dt)
