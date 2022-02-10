from turtle import Turtle, ycor
import time

UP = 90

class Paddle(Turtle):
    
    # Attributes
    def __init__(self, init_positions):
        super().__init__() # Inheritance
        self.init_positions = init_positions
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.init_positions)

    # Create up move
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    
    # Create down move
    def down(self):   
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
