from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        # Inheritance
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    # Write the intial score on the board    
    def update_scoreboard(self):
        self.write(arg=f'Score : {self.score}', align=ALIGNEMENT, font=FONT)

    # Delete and Increase the last score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score : {self.score}', align=ALIGNEMENT, font=FONT)
    
    # Game Over
    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNEMENT, font=FONT)