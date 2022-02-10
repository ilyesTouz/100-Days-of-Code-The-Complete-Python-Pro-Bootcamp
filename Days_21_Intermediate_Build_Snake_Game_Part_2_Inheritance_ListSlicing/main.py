from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# SetUp the Screen # 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

# 1) Create a snake body and the food and the scoreboard# 
food = Food()
snake = Snake()
scoreboard = Scoreboard()

# 2) Control the snake with keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# 3) Play # 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # Refresh food's position
        food.refresh()
        # Add a New Square
        snake.extend()
        # Increase Score
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       game_is_on = False
       # Game over
       scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            # Game over
            scoreboard.game_over()
    


# Exit Screen
screen.exitonclick()