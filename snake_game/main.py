from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.segments[0].xcor() > 340 or snake.segments[0].ycor() > 340 or snake.segments[0].xcor() < -340 or \
            snake.segments[0].ycor() < -340:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[2:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
