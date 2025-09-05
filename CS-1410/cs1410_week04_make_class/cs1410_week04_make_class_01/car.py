class Car:
    def __init__(self):
        self.speed = 0.0
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self,speed):
        if speed > -1 and speed < 81:
            self.speed = speed
            return True
        else:
            return False
    
    def accelerate(self,delta_speed):
        if self.speed == 80:
            return False
        elif delta_speed == 0 or delta_speed == 0.0 or delta_speed < 0:
            return False
        elif delta_speed > 0:
            self.speed += delta_speed
            if self.speed > 80:
                self.speed = 80
                return True
            else:
                return True
            
    def brake(self, delta_speed):
        if self.speed == 0 or delta_speed == 0 or delta_speed == 0.0 or delta_speed < 0:
            return False
        elif delta_speed > 0:
            self.speed -= delta_speed
            if self.speed < 0:
                self.speed = 0
                return True
            else:
                return True
