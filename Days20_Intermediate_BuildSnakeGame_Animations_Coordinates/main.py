from turtle import Screen, Turtle, width
import time
from snake import Snake

# SetUp the Screen # 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)


# 1) Create a snake body # 
snake = Snake()

# 2) Control the snake with keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


# 2) Move the snake # 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# Exit Screen
screen.exitonclick()