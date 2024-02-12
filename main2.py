import turtle
from turtle import Turtle, Screen
import random
screen =  Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
is_race_on = False

colors = ["red","orange","yellow","green","blue","purple"]
y_axis = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_axis[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()