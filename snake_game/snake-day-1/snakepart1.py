from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create segments as many as positions
        for self.position in POSITIONS:
            self.new_segment = Turtle(shape="square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(self.position)
            self.segments.append(self.new_segment)

    def move(self):
        # make previous segment the current segment (so that when the snake turns, the shape is intact and
        # it moves normally
        for seg_num in range(len(self.segments)-1, 0, -1):
            previous_x = self.segments[seg_num - 1].xcor()
            previous_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(previous_x, previous_y)
        # move the head
        self.head.forward(20)

    # let the snake go up if it is not pointing down
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # let the snake go down if it is not pointing up
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # let the snake go right if it is not pointing left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # let the snake go left if it is not pointing right
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

