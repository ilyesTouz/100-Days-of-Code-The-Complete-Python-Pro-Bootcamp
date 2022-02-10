from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

INITIALIZE_POSITIONS_LEFT = (-350, 0)
INITIALIZE_POSITIONS_RIGHT = (350, 0)

# 1) Create the Screen
screen = Screen()
screen.bgcolor('black') # black background
screen.setup(800, 600) # screen size
screen.title('My Pong Game')
screen.tracer(0)
#screen.tracer(0) # no tracer

# 2) Create the paddle
paddle_left = Paddle(INITIALIZE_POSITIONS_LEFT)
paddle_right = Paddle(INITIALIZE_POSITIONS_RIGHT)

# KeyBoard move
screen.listen()
screen.onkey(paddle_left.up, 'Up')
screen.onkey(paddle_left.down, 'Down')
screen.onkey(paddle_right.up, 'z')
screen.onkey(paddle_right.down, 's')

# Create the ball
ball = Ball()

##### PLAY THE GAME #####
is_game_on = True

while is_game_on:
    screen.update()


    
    
    
# Exit the screen
screen.exitonclick()

