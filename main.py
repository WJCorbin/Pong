from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkeypress(key="w", fun=paddle1.move_up)
screen.onkeypress(key="s", fun=paddle1.move_down)
screen.onkeypress(key="Up", fun=paddle2.move_up)
screen.onkeypress(key="Down", fun=paddle2.move_down)

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    scoreboard.write_score()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.increase_score(1)
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.increase_score(2)

screen.exitonclick()
