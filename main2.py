from turtle import Turtle, Screen
import random
screen =  Screen()
screen.setup(width=500, height=400)

# user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)

colors = ["red","orange","yellow","green","blue","purple"]
y_axis = [-70,-40,-10,20,50,80]
x_axis = [5,10,15]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-240, y=y_axis[turtle_index])
    tim.color(colors[turtle_index])



screen.exitonclick()