import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #collision
    if snake.head.distance(food)<13:
        scoreboard.update_score()
        snake.extend()
        food.refresh()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_on=False

    #collision with tail
    for segment in snake.segments[1:]:
        if snake.head.position()==segment.position():
            game_on=False
            scoreboard.game_over()

screen.exitonclick()
