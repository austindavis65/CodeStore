class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getY(self):
        return self.y

    def getX(self):
        return self.x

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
    
    def move(self,delta_x,delta_y):
        
        