from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_speed = 15
        self.dx = self.ball_speed  # horizontal velocity
        self.dy = 0                # vertical velocity

    def create_ball(self):
        self.shape("circle")
        self.up()
        self.color("White")

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)