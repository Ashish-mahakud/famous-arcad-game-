from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 6  # Increase starting horizontal speed
        self.y_move = 6  # Increase starting vertical speed
        self.move_speed = 0.05  # Faster initial movement speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Slightly increase speed after bouncing

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05  # Reset to a faster speed after a point
        self.bounce_x()
