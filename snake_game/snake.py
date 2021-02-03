from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

# HAVE TO USE SELF WHEN WORKING WITH A CLASS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # loop through the positions and create the number of snakes
        for self.segment in self.positions:
            self.new_segment = Turtle(shape="square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(self.segment)
            # add the segment to the list
            self.segments.append(self.new_segment)

    def move(self):

        for self.segnum in range(len(self.segments) - 1, 0, -1):
            # set previous segment to current segment
            previous_x = self.segments[self.segnum-1].xcor()
            previous_y = self.segments[self.segnum-1].ycor()
            # make the previous segment come to the current segment
            self.segments[self.segnum].goto(previous_x, previous_y)

        # move the head
        self.head.forward(20)

    # change the direction of the head to north (90 degrees)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # change the direction of the head to south (270 degrees)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # change the direction of the head to west (180 degrees)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # change the direction of the head to east (0 degrees)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)








