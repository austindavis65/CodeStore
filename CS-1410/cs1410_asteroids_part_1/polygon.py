from rotatable import Rotatable
import math
import pygame
class Polygon(Rotatable):
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x,y,dx,dy,rotation,world_width,world_height)
        self.mOriginalPolygon = []
        self.mColor = (255,255,255)
    def getPolygon(self):
        return self.mOriginalPolygon

    def getColor(self):
        return self.mColor

    def setPolygon(self,point_list):
        self.mOriginalPolygon = point_list

    def setColor(self,color):
        self.mColor = color

#     def getRadius(self):
#         if not self.mOriginalPolygon:
#             return 0
#         total = 0
#         for (x,y) in self.mOriginalPolygon:
#             d = math.sqrt(x**2 + y**2)
#             total += d
#         return total/len(self.mOriginalPolygon[::])

    def draw(self,surface):
        plist = self.mOriginalPolygon[::]
        plist = self.rotateAndTranslatePointList(self.mOriginalPolygon)
        pygame.draw.polygon(surface,self.mColor,plist,1)
