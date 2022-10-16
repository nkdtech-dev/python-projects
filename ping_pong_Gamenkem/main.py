from turtle import Screen, Turtle
import time
from pardle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("ping_pong Game")
screen.bgcolor("black")


center=Turtle()
center.penup()
center.color("white")
center.goto(0,-300)
center.hideturtle()
center.setheading(90)
for _ in range(30):
    center.pendown()
    center.forward(10)
    center.penup()
    center.forward(10)
screen.tracer(0)
R_paddle = Paddle(380, 0)
L_paddle = Paddle(-380, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeyrelease(R_paddle.move_down, "Down")
screen.onkeyrelease(R_paddle.move_up, "Up")
screen.onkeyrelease(L_paddle.move_down, "s")
screen.onkeyrelease(L_paddle.move_up, "w")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(R_paddle) < 50 and ball.xcor() > 340 or ball.distance(
            L_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
