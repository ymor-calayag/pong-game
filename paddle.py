from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.paddle_speed = 6
        self.create_paddle(self.x_pos, self.y_pos)

    # note: when you create the other paddle, 
    # just inherit this and change the pos
    def create_paddle(self, xpos, ypos):
        self.shape("square")
        self.setheading(90)
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("White")
        self.teleport(x=xpos, y=ypos)
        self.speed(self.paddle_speed)

    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)

