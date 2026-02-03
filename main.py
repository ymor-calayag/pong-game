from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.listen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("Black")
screen.tracer(0)

cpu_paddle = Paddle(-380, 0)
# for now it creates an object from paddle,
# but i think if its like a cpu paddle maybe
# it needs its own class that just inherits from Paddle
player_paddle = Paddle(380, 0)
ball = Ball()

screen.onkey(player_paddle.move_up, "Up")
screen.onkey(player_paddle.move_down, "Down")

game_over = False
while not game_over:
    # screen updates every 0.1 second
    screen.update()
    time.sleep(0.1)

    ball.move()

    # ball collision with paddle
    if ball.distance(player_paddle) <= 21:
        # Reverse horizontal direction
        ball.dx = -ball.dx
        
        # Calculate offset to adjust vertical speed
        # normalize it by dividing it by the height of the paddle
        # 4 * 20, 20 is the default turtle size
        get_offset = ball.ycor() - player_paddle.ycor()
        normalized_offset = get_offset / 80
        ball.dy = normalized_offset * 10

screen.exitonclick()