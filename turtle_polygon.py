from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(side):
    tim.color(random.choice(colours))
    angle = 360 / side
    for _ in range(side):
        tim.forward(100)
        tim.right(angle)

for side in range(3, 11): # draw shape
    draw_shape(side)

myScreen = Screen()
myScreen.exitonclick()
