# for mac and linux, from a terminal, type:
    # sudo apt-get install python3-tk

from graphics import *
from infixpostfix import *

def main():
    PrintDirections()
    infix = input("Enter your expression: ")
    postfix = InfixToPostfix(infix)
    
    win = GraphWin("My Equation", 850, 850)
    win.setBackground('white')

    xlow = -20
    xhigh = +20
    ylow = -20
    yhigh = +20
    win.setCoords(xlow, ylow, xhigh, yhigh)
    resolution = .1
    x = xlow
    
    x_axis = Line(Point(xlow, 0), Point(xhigh, 0))
    y_axis = Line(Point(0, ylow), Point(0, yhigh))
    x_axis.draw(win)
    y_axis.draw(win)
    
    while x < xhigh:
        y = EvaluatePostfix(postfix, x)
        x2 = x+resolution
        y2 = EvaluatePostfix(postfix, x2)
        l = Line(Point(x,y), Point(x2,y2))
        l.setWidth(2)
        l.draw(win)
        x += resolution
        
    

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()