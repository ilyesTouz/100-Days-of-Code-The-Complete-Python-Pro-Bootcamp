from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

# To keep event on scree
screen.listen()

# Higher Order Functions
# When a key is pressed, the function move_forward is activate (no parenthesis when a function is passed on argument of on another function)
screen.onkey(key="space", fun=move_forwards)


# Exit
screen.exitonclick()