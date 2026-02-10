from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
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
left_paddle_score = Score("Player One", -200, 280)
right_paddle_score = Score("Player Two", 200, 280)

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

    if left_paddle_score.score == 10:
        game_over = True
        left_paddle_score.game_over()
    elif right_paddle_score.score == 10:
        game_over = True
        right_paddle_score.game_over()

    # right side out of bounds + left paddle scores
    if ball.xcor() > 420:
        left_paddle_score.clear()
        left_paddle_score.update_score()
        ball.home()
        ball.bounce_x()

    # left side out of bounds + right paddle scores
    if ball.xcor() < -420:
        right_paddle_score.clear()
        right_paddle_score.update_score()
        ball.home()
        ball.bounce_x()

screen.exitonclick()