class Color:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
    def getRed(self):
        return self.red
    def getGreen(self):
        return self.green
    def getBlue(self):
        return self.blue
    def setRed(self,value):
        if value >= 0 and value <= 255:
            self.red = value
            return True
        else:
            return False
    def setGreen(self,value):
        if value >= 0 and value <= 255:
            self.green = value
            return True
        else:
            return False
    def setBlue(self,value):
        if value >= 0 and value <= 255:
            self.blue = value
            return True
        else:
            return False
        
    def complement(self):
        red = 255 - self.getRed()
        green = 255 - self.getGreen()
        blue = 255 - self.getBlue()
        self.setRed(red)
        self.setGreen(green)
        self.setBlue(blue)
        return True
    
    def triad(self):
        green = self.getGreen()
        blue = self.getBlue()
        red = self.getRed()
        self.setRed(green)
        self.setGreen(blue)
        self.setBlue(red)
        return True
        
        