from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def rotate_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def rotate_anticlockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key='a', fun=rotate_clockwise)
screen.onkey(key='d', fun=rotate_anticlockwise)
screen.exitonclick()