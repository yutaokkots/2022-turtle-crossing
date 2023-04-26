from turtle import Turtle

YELLOW = (247, 181, 0)  #rgb for yellow color
WHITE = "white"
REF_LINE = 40
DASHED_LINE = [-80, -20, 105, 165]
WHITE_LINE = [-160, -140, 225, 245]

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color(YELLOW)
        self.pensize(3)
        self.speed(10)

    def draw_median(self):
        reference_line = REF_LINE
        for repeat in range(2):
            self.setposition(-400, reference_line)
            self.pd()
            self.forward(800)
            self.pu()
            reference_line += 5

    def draw_white_lines(self):
        self.color("white")
        for lines in DASHED_LINE:
            self.setposition(-400, lines)
            while self.xcor() < 400:
                self.pd()
                self.forward(30)
                self.pu()
                self.forward(50)
        for lines in WHITE_LINE:
            self.setposition(-400, lines)
            self.pd()
            self.forward(800)
            self.pu()

    def draw_road(self):
        self.draw_median()
        self.draw_white_lines()
