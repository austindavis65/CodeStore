class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getRadius(self):
        return self.r

    def setY(self,value):
        if value != self.y:
            self.y = value
            return True
        else:
            return False

    def setX(self,value):
        if value != self.x:
            self.x = value
            return True
        else:
            return False

    def setRadius(self,r):
        if r < 0:
            return False
        elif r != self.r:
            self.r = r
            return True
        else:
            return False
