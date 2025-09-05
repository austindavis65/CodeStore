from ship import Ship
from rock import Rock
from star import Star
from random import uniform
class Asteroids:
    def __init__(self,world_width,world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = Ship(world_width/2,world_height/2,world_width,world_height)
        self.mRocks = []
        for i in range(10):
            rock = Rock(uniform(0,world_width),uniform(0,world_height),world_width,world_height)
            self.mRocks.append(rock)
        self.mStars = []
        for i in range(20):
            star = Star(uniform(0,world_width),uniform(0,world_height),world_width,world_height)
            self.mStars.append(star)
        self.mBullets = []
        self.mObjects = [self.mShip] + self.mRocks+self.mStars
    def getWorldWidth(self):
        return self.mWorldWidth
    def getWorldHeight(self):
        return self.mWorldHeight
    def getShip(self):
        return self.mShip
    def getRocks(self):
        return self.mRocks
    def getObjects(self):
        return self.mObjects
    def getBullets(self):
        return self.mBullets
    def getStars(self):
        return self.mStars
    def fire(self):
        if len(self.mBullets) < 3:
            b = self.mShip.fire()
            self.mBullets.append(b)
            self.mObjects.append(b)
    def turnShipLeft(self,delta_rotation):
        self.mShip.rotate(-delta_rotation)
    def turnShipRight(self,delta_rotation):
        self.mShip.rotate(delta_rotation)
    def accelerateShip(self,delta_velocity):
        self.mShip.accelerate(delta_velocity)
    def collideShipAndRocks(self):
        if self.mShip.getActive():
            for r in self.mRocks:
                if r.hits(self.mShip):
                    self.mShip.setActive(False)
                    r.setActive(False)
    def collideShipAndBullets(self):
        if self.mShip.getActive():
            for b in self.mBullets:
                if b.hits(self.mShip):
                    self.mShip.setActive(False)
                    b.setActive(False)
    def collideRocksAndBullets(self):
        for b in self.mBullets:
            if b.getActive():
                for r in self.mRocks:
                    if b.hits(r):
                        b.setActive(False)
                        r.setActive(False)
    def removeInactiveObjects(self):
        tmp = []
        for obj in self.mBullets:
            if obj.getActive():
                tmp.append(obj)
        self.mBullets = tmp
        tmpR = []
        for obj in self.mRocks:
            if obj.getActive():
                tmpR.append(obj)
        self.mRocks = tmpR
        if self.mShip.getActive():
            self.mObjects = [self.mShip] + self.mBullets + self.mRocks+self.mStars
    def evolveAllObjects(self,dt):
        for obj in self.mObjects:
            obj.evolve(dt)
    def evolve(self,dt):
        self.evolveAllObjects(dt)
        self.collideShipAndBullets()
        self.collideRocksAndBullets()
        self.collideShipAndRocks()
        self.removeInactiveObjects()
    def draw(self,surface):
        surface.fill((0,0,0))
        for ob in self.mObjects:
            if ob.getActive():
                ob.draw(surface)
                
    def gofire(self):
        self.fire()
