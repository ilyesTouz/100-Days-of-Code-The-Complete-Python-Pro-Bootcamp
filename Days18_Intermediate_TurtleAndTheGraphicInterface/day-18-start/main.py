from turtle import Turtle, Screen
import random

# Initialize Turtle
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
"""
# TODO 1 : Draw a scare
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# Exit
screen = Screen()
screen.exitonclick()
"""
"""
# TODO 2 : Draw a Dashed Line
for _ in range(10):
    
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
# Exit
screen = Screen()
screen.exitonclick()
"""
"""
# TODO 3 : Draw different shapes
def draw_shape(num_sides, m=100):
    angle = 360/num_sides
    
    # Select a random color
    color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
    
    for _ in range(num_sides):
        # Change the pen's color
        timmy_the_turtle.pencolor(color)
        timmy_the_turtle.forward(m)
        timmy_the_turtle.right(angle)

for nb_sides in range(3, 20):
    draw_shape(nb_sides)

# Exit
screen = Screen()
screen.exitonclick()
"""

"""
# TODO 4 : Draw random walk
timmy_the_turtle.pensize(10)

for _ in range(100):
    # Generate random attributes
    random_forward = random.uniform(1, 100)
    random_angle = random.randrange(0, 270, 90)
    random_color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
    
    # Change color and move forward with random attributes
    timmy_the_turtle.pencolor(random_color)
    timmy_the_turtle.right(random_angle)
    timmy_the_turtle.forward(random_forward)
    
# Exit
screen = Screen()
screen.exitonclick()
"""


# TODO 5 : Draw a spirograph
timmy_the_turtle.speed(0)
# Create a circle
for _ in range(35):
    random_color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
    timmy_the_turtle.pencolor(random_color)
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(10)
# Exit
screen = Screen()
screen.exitonclick()