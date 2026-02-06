from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.dx = 20    # horizontal velocity
        self.dy = 0   # vertical velocity

    def create_ball(self):
        self.shape("circle")
        self.up()
        self.color("White")

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1


# note: add a way to randomize the start movement of the ball