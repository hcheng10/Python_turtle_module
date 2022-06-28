from turtle import Turtle, Screen

tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("red")

for _ in range(4): # draw square
    tim.forward(100)
    tim.left(90) # turn 90 degree to the right

tim.right(180)

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() # only exit when we click the screen