from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.pensize(20)
        new_turtle.goto(0, 0)
        self.segments.append(new_turtle)
        self.add_segment(-20, 0)
        self.add_segment(-40, 0)
    
    def add_segment(self, x, y):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.pensize(20)
        new_turtle.goto(x, y)
        self.segments.append(new_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
            segment.clear()
            del segment
        self.segments.clear()
        self.create_snake()