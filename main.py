from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.listen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("Black")

paddle = Paddle()

screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

screen.exitonclick()