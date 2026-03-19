from graphics import *

def main():
    win = GraphWin("My Circle", 500, 500)

    xlow = -10
    xhigh = +10
    ylow = -10
    yhigh = +10
    win.setBackground('white')
    win.setCoords(xlow,ylow,xhigh,yhigh)

    for x in range(xlow, xhigh):
        y = x*x
        c = Line(Point(x,y),Point(y,x))
        c.draw(win)


    #c = Circle(Point(50,50), 10)
    #c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()