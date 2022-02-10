from turtle import Turtle, Screen, color
import random

# Initiliaze the screen
screen = Screen()

# Setup the screen
screen.setup(500,400)

# Put a text input 
user_bet = screen.textinput("Make your bet", prompt="Which Turtle will win the race ? Enter a color")
print(user_bet)

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

# Turtle's colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Turtle y positions
y_positions = [-70, -40, -10, 20, 50, 80]

# Create the turtles, Append to the list and Move the turtle to initial position
all_turtles = []
for turtles_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtles_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y=y_positions[turtles_index])
    all_turtles.append(new_turtle)

# Check if user make a bet
is_race_on = bool(user_bet)

# Launch the race
while is_race_on: 
    for turtle in all_turtles:
        # Check if a turtle win
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("You've won ! The winner is ".format({winning_turtle}))
            else:
                print("You've lost ! The winner is ".format({winning_turtle}))
        # Initiliaze the random distance
        rand_distance = random.randint(0, 10)
        # Move forward with a rand distance
        turtle.forward(rand_distance)

# Exit the screen
screen.exitonclick()