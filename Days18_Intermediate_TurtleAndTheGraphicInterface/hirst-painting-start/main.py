###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
import random

# Extract the image's color
colors = colorgram.extract('image.jpg', 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#print(rgb_colors)


# Create the turtle
screen = Screen()
screen.screensize(250,250)
screen.colormode(255)
t = Turtle()
print(t.pos())
t.setpos(-400, -400)
#t.goto(-250, -250)


#for _ in range(10):
for _ in range(10):
        color = random.choice(rgb_colors)       
        t.dot(20, color)
        t.penup()
        t.forward(50)

# Exit
screen = Screen()
screen.exitonclick()