class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

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

    def setWidth(self,w):
        if w < 0:
            return False
        elif w != self.w:
            self.w = w
            return True
        else:
            return False

    def setHeight(self,h):
        if h < 0:
            return False
        elif h != self.h:
            self.h = h
            return True
        else:
            return False
