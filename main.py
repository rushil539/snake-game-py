from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

snake.create_snake()
game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    
    if snake.segments[0].distance(food) < 15:
        food.new_location()
        snake.add_segment(snake.segments[-1].xcor(), snake.segments[-1].ycor())
        score.update_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        snake.reset()
        score.reset()

    for segment in snake.segments[1::]:
        if snake.segments[0].distance(segment) < 10 and snake.segments[0].distance(segment) < 10:
            snake.reset()
            score.reset()
    


screen.exitonclick()