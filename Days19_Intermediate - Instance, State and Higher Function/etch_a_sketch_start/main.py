from turtle import Turtle, Screen

# Initialize Objects
tim = Turtle()
screen = Screen()

# Listen event on screen
screen.listen()

# Functions mvt
def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_counter_clockwise():
    tim.setheading(tim.heading() + 10)

def turn_clockwise():
    tim.setheading(tim.heading() - 10)

def screen_clear():
    screen.resetscreen()


# TODO 1 : Create movement events with keyboard
# W: Forwards
# S = Backwards
# A = counter - Clockwise
# D = Clockwise
# C = clear

while True:  

    screen.onkey(key="z", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="q", fun=turn_counter_clockwise)
    screen.onkey(key="d", fun=turn_clockwise)
    screen.onkey(key="c", fun=screen_clear)
    break




# Exit screen
screen.exitonclick()