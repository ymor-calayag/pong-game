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

player_two_paddle = Paddle(-380, 0)
player_paddle = Paddle(380, 0)
ball = Ball()

screen.onkey(player_paddle.move_up, "Up")
screen.onkey(player_paddle.move_down, "Down")
screen.onkey(player_two_paddle.move_up, "w")
screen.onkey(player_two_paddle.move_down, "s")

game_over = False
while not game_over:
    # screen updates every 0.1 second
    time.sleep(0.1)
    screen.update()

    ball.move()

    #ball collision with upper wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball collision with paddle - right
    if ball.distance(player_paddle) < 50 and ball.xcor() > 350:
        # Reverse horizontal direction
        ball.bounce_x()
        
        # Calculate offset to adjust vertical speed
        # normalize it by dividing it by the height of the paddle
        # 4 * 20, 20 is the default turtle size
        get_offset = ball.ycor() - player_paddle.ycor()
        normalized_offset = get_offset / 80
        ball.dy = normalized_offset * 10

    # ball collision with paddle - left
    if ball.distance(player_two_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        get_offset = ball.ycor() - player_two_paddle.ycor()
        normalized_offset = get_offset / 80
        ball.dy = normalized_offset * 10

screen.exitonclick()