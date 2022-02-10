from turtle import Turtle

# CONSTANTE: In Python, in Upper Case
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Snake Class
class Snake:
    
    # Attributes
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    # Create the snake
    def create_snake(self):    
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)     

    # Move the square into a new position : the tail has to follow the snake's head
    def move(self):
        for seg_num in range(len(self.segments)-1, 0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE) 

    # Control the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    # Control the snake
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    # Control the snake
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    # Control the snake
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




