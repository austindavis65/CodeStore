class Square:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getWidth(self):
        return self.size

    def getHeight(self):
        return self.size

    def getSize(self):
        return self.size

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

    def setSize(self,size):
        if size < 0:
            return False
        elif size != self.size:
            self.size = size
            return True
        else:
            return False
