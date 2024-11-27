from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Snake Game...")
screen.tracer(0)

snake = Snake()
food = Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increse_Score()

    #wall

    if snake.head.xcor() > 440 or snake.head.xcor() < -440 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        game_is_on=False
        score.gameover()

    for segment in snake.segments:
        if segment==snake.head:
            pass

        elif snake.head.distance(segment)<10:
            game_is_on=False
            score.gameover

    

screen.exitonclick()