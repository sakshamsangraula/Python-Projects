from turtle import Turtle

POSITIONS = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    # inherit from the Turtle class which is the super class
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create the snake
    def create_snake(self):
        # create a snake with three segments
        for position in range(0, len(POSITIONS)):
            self.add_segments(POSITIONS[position])


    def add_segments(self, position):
        self.new_segment = Turtle(shape="square")
        self.new_segment.penup()
        self.new_segment.color("white")
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    def extend_snake(self):
        # add a segment at the end of the snake
        self.add_segments(self.segments[-1].position())

    # move the snake
    def move(self):
        # loop through the segments in backward order (ex: 2, 1, 0)
        # make the previous segment the current segment and move the head forward
        for segment in range(len(self.segments) - 1, 0, -1):
            previous_x = self.segments[segment - 1].xcor()
            previous_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(previous_x, previous_y)

        self.head.forward(20)

    # control the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

