from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.dx = 0    # horizontal velocity
        self.dy = 10   # vertical velocity

    def create_ball(self):
        self.shape("circle")
        self.up()
        self.color("White")

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)