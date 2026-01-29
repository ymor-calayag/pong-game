from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.listen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("Black")

player_paddle = Paddle(-380, 0)
# for now it creates an object from paddle,
# but i think if its like a cpu paddle maybe
# it needs its own class that just inherits from Paddle
cpu_paddle = Paddle(380, 0)

screen.onkey(player_paddle.move_up, "Up")
screen.onkey(player_paddle.move_down, "Down")

screen.exitonclick()