# the turtle starts at coordinate will be (0, 0)
# and depends on the size we specific for example screen_object.setup(width=500, height=400)
# then top edge will have (-250, 200) => (250, 200), left edge will have (-250, -200) => (-250, 200)

from turtle import Turtle, Screen, turtles
import random
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) # set the size of window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for n in range(6):
    new_turtle = Turtle(shape="turtle") # a turtle is 40 by 40 object
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-120 + n*50)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lsoe! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10) # 10 include
        turtle.forward(random_distance)





screen.exitonclick() # exit screen when you click screen