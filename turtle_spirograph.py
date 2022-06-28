from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
turtle.colormode(255)
# tim.shape("classic")
# tim.width(5) #Set the line thickness to width
# tim.speed("fastest") # set the motion speed

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) # return tuple

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(radius=100)
        tim.setheading(tim.heading() + size_of_gap)

tim.speed("fastest")
draw_spirograph(5)

myScreen = Screen()
myScreen.exitonclick()