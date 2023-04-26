from turtle import Turtle

SHAPE = "turtle"
OUTLINE_COLOR = (255, 255, 255)
FILL_COLOR = (0, 128, 0)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10
START_POSITION = 0, -180

class Turtle_Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color(OUTLINE_COLOR, FILL_COLOR)
        self.shape(SHAPE)
        self.setposition(START_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(MOVE_DISTANCE)

    def move_right(self):
        self.right(MOVE_DISTANCE)

    def move_left(self):
        self.left(MOVE_DISTANCE)

    def reset_turtle(self):
        self.setposition(START_POSITION)


