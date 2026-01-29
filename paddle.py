from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    # note: when you create the other paddle, 
    # just inherit this and change the pos
    def create_paddle(self):
        self.shape("square")
        self.setheading(90)
        self.up()
        self.shapesize(stretch_len=3, stretch_wid=0.5)
        self.color("White")
        self.teleport(x=-380, y=0)

    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)

