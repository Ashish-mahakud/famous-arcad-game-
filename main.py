from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Paddle, ball, and scoreboard setup
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Control paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the ball speed
    screen.update()
    ball.move()

    # Detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses (right side out of bounds)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if left paddle misses (left side out of bounds)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Exit the game when clicked
screen.exitonclick()
