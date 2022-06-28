from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counterWise():
    tim.setheading(tim.heading() + 10)

def clockwise():
    tim.setheading(tim.heading() - 10)

def cleanScreen():
    tim.clear()
    tim.penup()
    tim.home() # move draw point back to orgin
    tim.pendown()

screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=counterWise, key="a")
screen.onkeypress(fun=clockwise, key="d")
screen.onkey(fun=cleanScreen, key='c')

screen.exitonclick()