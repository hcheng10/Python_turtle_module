from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
turtle.colormode(255)
# tim.shape("classic")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) # return tuple

directions = [0, 90, 180, 270]

tim.width(10) #Set the line thickness to width
tim.speed("fastest")

for _ in range(200):
    tim.right(random.choice(directions))
    tim.color(random_color())
    tim.forward(30)

myScreen = Screen()
myScreen.exitonclick()