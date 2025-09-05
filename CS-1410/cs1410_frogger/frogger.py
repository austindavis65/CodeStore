import froggerlib, pygame, main
from star import Star
from random import uniform
LANESIZE = 50
OBJECT_HEIGHT = 40
HALFGAP = 5
BEFORESTAGE = 11
STAGE1 = 10
ROAD1 = 9
ROAD2 = 8
ROAD3 = 7
ROAD4 = 6
STAGE2 = 5
WATER1 = 4
WATER2 = 3
WATER3 = 2
WATER4 = 1
END = 0

class Frogger:
    def __init__(self,width,height):
        self.reset = False
        self.jesus_frog = False
        self.waterfrog = False
        self.god_frog = False
        self.width = width
        self.height = height
        self.gameover = False
        self.win = False
        self.frog = froggerlib.Frog(width/2-20,
                                    STAGE1*LANESIZE+HALFGAP,
                                    40,
                                    OBJECT_HEIGHT,
                                    width/2-20,
                                    STAGE1*LANESIZE+HALFGAP,
                                    20,
                                    LANESIZE,
                                    LANESIZE)

#         self.car1 = froggerlib.Car(width/2,
#                                    ROAD1*LANESIZE+HALFGAP,
#                                    10,
#                                    OBJECT_HEIGHT,
#                                    width, #dx
#                                    ROAD1*LANESIZE+HALFGAP,#dy
#                                    30)#speed
#

        self.god_box = froggerlib.Stage(0,BEFORESTAGE*LANESIZE,
                                      100,LANESIZE)

        self.jesus_box = froggerlib.Stage(0,BEFORESTAGE*LANESIZE,
                                      50,LANESIZE)

        self.right_trucks = []
        for i in range(2):
            x = width/2*i
            y = ROAD1*LANESIZE+HALFGAP
            w = 80
            self.right_trucks.append(froggerlib.Truck(x,y,w,OBJECT_HEIGHT,-w,y,5))

        self.left_cars = []
        for i in range(3):
            x = width/3 * i - 250
            y = ROAD2*LANESIZE+HALFGAP
            w = 40
            self.left_cars.append(froggerlib.Car(x,y,w,OBJECT_HEIGHT,width,y,10))

        self.left_dozers = []
        for i in range(2):
            x = width/2 * i - 250
            y = ROAD3*LANESIZE+HALFGAP
            w = 100
            self.left_dozers.append(froggerlib.Dozer(x,y,w,OBJECT_HEIGHT,width,y,2))

        self.right_cars = []
        for i in range(2):
            x = width/2*i
            y = ROAD4 * LANESIZE+HALFGAP
            w = 40
            self.right_cars.append((froggerlib.Car(x,y,w,OBJECT_HEIGHT,-w,y,15)))

        self.right_logs1 = []
        for i in range(3):
            x = width/3 * i
            y = WATER1*LANESIZE+HALFGAP
            w = 90
            self.right_logs1.append(froggerlib.Log(x,y,w,OBJECT_HEIGHT,-w,y,5))

        self.right_turtles = []
        for i in range(4):
            x = width/4 * i
            y = WATER3*LANESIZE+HALFGAP
            w = 70
            self.right_turtles.append(froggerlib.Turtle(x,y,w,OBJECT_HEIGHT,-w,y,5))

        self.left_logs1 = []
        for i in range(1):
            x = width/1 * i - 250
            y = WATER2*LANESIZE+HALFGAP
            w = 300
            self.left_logs1.append(froggerlib.Log(x,y,w,OBJECT_HEIGHT,width,y,5))

        self.left_logs2 = []
        for i in range(2):
            x = width/2 * i - 250
            y = WATER4*LANESIZE+HALFGAP
            w = 150
            self.left_logs2.append(froggerlib.Log(x,y,w,OBJECT_HEIGHT,width,y,5))


        self.stage1 = froggerlib.Stage(0,STAGE1*LANESIZE,
                                      width,LANESIZE)
        self.stage2 = froggerlib.Stage(0,STAGE2*LANESIZE,
                                      width,LANESIZE)
#         self.road1 = froggerlib.Road(0,ROAD1*LANESIZE,
#                                       width,LANESIZE)
        self.roads = []
        x, y = 0, ROAD1 * LANESIZE
        for i in range(4):
            self.roads.append(froggerlib.Road(x,y-i*50,width,LANESIZE))

        self.waters = []
        x, y = 0, WATER1 * LANESIZE
        for i in range(4):
            self.waters.append(froggerlib.Water(x,y-i*50,width,LANESIZE))

        self.grasses = []
        x, y = 0, 0
        for i in range(4):
            self.grasses.append(froggerlib.Grass(x,y,130,50))
            x+=225

        self.homes = []
        x, y = 130, 0
        for i in range(3):
            self.homes.append(froggerlib.Home(x,y,95,50))
            x+=225

        self.mStars = []
        for i in range(20):
            star = Star(uniform(0,width),uniform(0,height),width,height)
            self.mStars.append(star)


    def evolve(self, dt):
        if self.gameover:
            return
        self.frog.move()
        for truck in self.right_trucks:
            truck.move()
            if truck.atDesiredLocation(): #boundary
                truck.setX(self.width)
            if self.god_frog == False:
                if truck.hits(self.frog):
                    self.gameover = True

        for car in self.left_cars:
            car.move()
            if car.atDesiredLocation(): #boundary
                car.setX(-car.getWidth())
            if self.god_frog == False:
                if car.hits(self.frog):
                    self.gameover = True

        for dozer in self.left_dozers:
            dozer.move()
            if dozer.atDesiredLocation(): #boundary
                dozer.setX(-dozer.getWidth())
            if self.god_frog == False:
                if dozer.hits(self.frog):
                    self.gameover = True

        for car in self.right_cars:
            car.move()
            if car.atDesiredLocation():
                car.setX(self.width)
            if self.god_frog == False:
                if car.hits(self.frog):
                    self.gameover = True

        for log in self.left_logs1:
            log.move()
            if log.atDesiredLocation():
                log.setX(-log.getWidth())
            if self.god_frog == False:
                log.supports(self.frog)

        for log in self.right_logs1:
            log.move()
            if log.atDesiredLocation():
                log.setX(self.width)
            if self.god_frog == False:
                log.supports(self.frog)

        for log in self.left_logs2:
            log.move()
            if log.atDesiredLocation():
                log.setX(-log.getWidth())
            if self.god_frog == False:
                log.supports(self.frog)

        for turtle in self.right_turtles:
            turtle.move()
            if turtle.atDesiredLocation():
                turtle.setX(self.width)
            if self.god_frog == False:
                turtle.supports(self.frog)

        for home in self.homes:
            if home.hits(self.frog):
                self.win = True

        if self.jesus_frog == False:
            if self.god_frog == False:
                for water in self.waters:
                    if water.hits(self.frog):
                        self.waterfrog = True
                        self.gameover = True

        if self.god_frog == False:
            if self.frog.outOfBounds(self.width,self.height):
                self.gameover = True

            for grass in self.grasses:
                if grass.hits(self.frog):
                    self.gameover = True

        elif self.god_frog == True:
            if self.frog.outOfBounds(self.width,self.height):
                if self.frog.getX() >= self.width:
                    self.frog.setX(self.frog.getX() - self.width)

                elif self.frog.getX() < 0:
                    self.frog.setX(self.width + self.frog.getX())

                if self.frog.getY() >= self.height:
                    self.frog.setY(self.frog.getY() - self.height)

                elif self.frog.getY() < 0:
                    self.frog.setY(self.height + self.frog.getY())

        if self.win:
            for star in self.mStars:
                star.evolve(60)

    def fancyDraw(self,surface,obj,color):
        rect = pygame.Rect(int(obj.getX()),int(obj.getY()),int(obj.getWidth()),int(obj.getHeight()))
        pygame.draw.rect(surface,color,rect)

    def draw(self, surface):
        surface.fill((0,0,0))
        #draw stages
        self.fancyDraw(surface,self.stage1,(37, 125, 0))
        self.fancyDraw(surface,self.stage2,(37, 125, 0))

        #draw roads
        for road in self.roads:
            self.fancyDraw(surface,road,(85,85,85))
        #draw waters
        for water in self.waters:
            self.fancyDraw(surface,water,(0,157,196))
        #draw grass
        for grass in self.grasses:
            self.fancyDraw(surface,grass,(0,102,38))
        #draw home
        for home in self.homes:
            self.fancyDraw(surface,home,(57,0,102))
        #draw logs
        for log in self.left_logs1:
            self.fancyDraw(surface,log,(97, 63, 0))

        for log in self.right_logs1:
            self.fancyDraw(surface,log,(97, 63, 0))

        for log in self.left_logs2:
            self.fancyDraw(surface,log,(97, 63, 0))

        for turtle in self.right_turtles:
            self.fancyDraw(surface,turtle,(69, 192, 108))
        #draw frog
        if self.waterfrog == True:
            self.fancyDraw(surface,self.frog,(0,157,196))
        else:
            self.fancyDraw(surface,self.frog,(95,209,0))
        #draw cars
        for truck in self.right_trucks:
            self.fancyDraw(surface,truck,(130,0,0))

        for car in self.left_cars:
            self.fancyDraw(surface,car,(130,0,0))

        for dozer in self.left_dozers:
            self.fancyDraw(surface,dozer,(130,0,0))

        for car in self.right_cars:
            self.fancyDraw(surface,car,(130,0,0))

        if self.god_frog == False:
            self.fancyDraw(surface,self.god_box,(0,0,0))
        elif self.god_frog == True:
            self.fancyDraw(surface,self.god_box,(255,255,255))

        if self.jesus_frog == False:
            self.fancyDraw(surface,self.jesus_box,(0,0,0))
        elif self.jesus_frog == True:
            self.fancyDraw(surface,self.jesus_box,(95,209,0))

        #draw win screen
        if self.win:
            rect = pygame.Rect(0,0,800,600)
            pygame.draw.rect(surface,(0,0,0),rect)
            for star in self.mStars:
                star.draw(surface)

        return

    def act_on_pressUP(self):
        self.frog.up()

    def act_on_pressDOWN(self):
        self.frog.down()

    def act_on_pressLEFT(self):
        self.frog.left()

    def act_on_pressRIGHT(self):
        self.frog.right()

    def act_on_pressj(self):
        if self.jesus_frog == False:
            self.jesus_frog = True
        elif self.jesus_frog == True:
            self.jesus_frog = False

    def act_on_pressg(self):
        if self.god_frog == False:
            self.god_frog = True
        elif self.god_frog == True:
            self.god_frog = False

    def act_on_pressr(self):
        main.main()
