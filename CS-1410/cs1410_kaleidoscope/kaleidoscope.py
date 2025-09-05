import turtle
import random

def get_t1():
    t1 = turtle.Turtle()
    t1.color("orange")
    t1.setheading(0)
    t1.shape("turtle")
    t1.pendown()
    t1.pensize(10)
    t1.speed(300)
    return t1
def get_t2():
    t2 = turtle.Turtle()
    t2.color("purple")
    t2.setheading(90)
    t2.shape("turtle")
    t2.pendown()
    t2.pensize(10)
    t2.speed(300)
    return t2
def get_t3():
    t3 = turtle.Turtle()
    t3.color("red")
    t3.setheading(180)
    t3.shape("turtle")
    t3.pendown()
    t3.pensize(10)
    t3.speed(300)
    return t3
def get_t4():
    t4 = turtle.Turtle()
    t4.color("green")
    t4.setheading(270)
    t4.shape("turtle")
    t4.pendown()
    t4.pensize(10)
    t4.speed(300)
    return t4
def shape(turtle):
    shap = random.randrange(1,5)
    if shap == 1:
        turtle.shape("circle")
        return turtle
    elif shap == 2:
        turtle.shape("triangle")
        return turtle
    elif shap == 3:
        turtle.shape("square")
        return turtle
    elif shap == 4:
        turtle.shape("turtle")
        return turtle
def move2(turtle):
    turtle.forward(1)
def move3(turtle):
    turtle.backward(1)
def move(turtle):
    dist = random.randrange(-100,100)
    turtle.forward(dist)
def heading(turtle):
    degrees = random.randrange(0,360)
    turtle.setheading(degrees)
def stamp(turtle):
    turtle.stamp()
def main():
    t1 = get_t1()
    t2 = get_t2()
    t3 = get_t3()
    t4 = get_t4()

    for turtle in range(2000):
        heading(t1)
        heading(t2)
        heading(t3)
        heading(t4)
        move(t1)
        move(t2)
        move(t3)
        move(t4)


main()
