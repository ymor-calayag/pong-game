from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.up()
        self.setpos(x=0, y=280)
        self.score = 0
    
    # issue: it should show the initial score zero
    # def update_score(self):
    #     self.score += 1
    #     self.write(f"Score: {self.score}", 
    #                align="center", 
    #                font=("Courier New", 10, "normal"))
        
    def game_over(self):
        self.home()
        self.write(f"Game Over!", 
                   align="center", 
                   font=("Courier New", 20, "normal")) 