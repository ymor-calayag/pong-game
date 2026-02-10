from turtle import Turtle

class Score(Turtle):
    def __init__(self, player, x_cor, y_cor):
        super().__init__()
        self.player = player
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.hideturtle()
        self.color("White")
        self.up()
        self.setpos(self.x_cor, self.y_cor)
        self.score = 0
    
    def update_score(self):
        self.score += 1
        self.write(f"{self.player} score: {self.score}", 
                   align="center", 
                   font=("Courier New", 10, "normal"))
        
    def game_over(self):
        self.home()
        self.write(f"Game Over! {self.player} wins!", 
                   align="center", 
                   font=("Courier New", 20, "normal")) 