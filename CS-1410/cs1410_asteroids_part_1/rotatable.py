from movable import Movable
import math
class Rotatable(Movable):
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x,y,dx,dy,world_width,world_height) #parameters of movable in super
        self.mRotation = rotation
    def getRotation(self,):
        return self.mRotation
    def rotate(self,delta_rotation):
        self.mRotation += delta_rotation
        self.mRotation %= 360 #divides and gets the remainder
    def splitDeltaVIntoXAndY(self,rotation,delta_velocity):
        radrotation = math.radians(rotation)
        x = delta_velocity*math.cos(radrotation)
        y = delta_velocity*math.sin(radrotation)
        return (x,y) #this is a tuple
    def accelerate(self,delta_velocity):
        x,y = self.splitDeltaVIntoXAndY(self.mRotation,delta_velocity)
        self.mDX += x
        self.mDY += y
    def rotatePoint(self,x,y):
        #change the cartesian coordinates to polar
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y,x)
        #rotate my object and update theta
        theta += math.radians(self.mRotation)
        #change back to cartesian
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        return (x,y)
    def translatePoint(self,x,y):
        x += self.mX
        y += self.mY
        return (x,y)
    def rotateAndTranslatePoint(self,x,y):
        x,y = self.rotatePoint(x,y)
        x,y = self.translatePoint(x,y)
        return (x,y)
    def rotateAndTranslatePointList(self,point_list):
        new_list = []
        for (x,y) in point_list:
            new_list.append(self.rotateAndTranslatePoint(x,y)) #passed in tuple
        return new_list
