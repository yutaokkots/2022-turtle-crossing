#from turtle import Turtle, Screen
from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

left_or_right = ["left", "right"]

START_FR_RIGHT = -400
Y_AXIS_LEFT = [-110, -50, 10]
TILT_ANGLE_LEFT = 270

START_FR_LEFT = 400
Y_AXIS_RIGHT = [75, 135, 195]
TILT_ANGLE_RIGHT = 270

SPEED = [2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
COLORS = ["light gray", "light blue", "firebrick", "orange", "floral white", "royal blue", "dim gray", "crimson", "tomato"]
VEHICLE_TYPE = ["car", "bus", "truck"]

# randomly generate new cars, with various variables:
# save class in list? after saving in list, call out from list

# frequency of new cars
# speed of new cars (varies by level)
#divide subclasses by each lane?


class VehicleController(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.vehicle_list = []


    def color_generator(self):
        self.vehicle_color = random.choice(COLORS)
        return self.vehicle_color


    def left_or_right_direction(self):
        chosen_direction = random.choice(left_or_right)
        if chosen_direction == "right":
            x_axis = START_FR_RIGHT
            y_axis = random.choice(Y_AXIS_LEFT)
            self.setposition(x_axis, y_axis)
            self.tilt(TILT_ANGLE_LEFT)

        elif chosen_direction == "left":
            x_axis = START_FR_LEFT
            y_axis = random.choice(Y_AXIS_RIGHT)
            self.setheading(180)
            self.setposition(x_axis, y_axis)
            self.tilt(TILT_ANGLE_RIGHT)

    def car_generator(self):
        self.pu()
        self.shape("car")
        self.showturtle()
        self.color(self.color_generator())
        self.pencolor("white")
        self.shapesize(stretch_wid= 4, stretch_len=4)
        self.left_or_right_direction()
        return self

    def truck_generator(self):
        self.pu()
        self.shape("truck")
        self.showturtle()
        self.color(self.color_generator())
        self.pencolor("white")
        self.shapesize(stretch_wid=4, stretch_len=4)
        self.left_or_right_direction()
        return self


    def bus_generator(self):
        self.pu()
        self.shape("bus")
        self.showturtle()
        self.color(self.color_generator())
        self.pencolor("white")
        self.shapesize(stretch_wid=4, stretch_len=4)
        self.left_or_right_direction()
        return self


    def drive(self, move_level_up):
        self.forward(MOVE_INCREMENT + move_level_up)

    def location(self):
        pass

    def random_vehicle_generator(self):
        function_list = [self.car_generator()] # self.truck_generator()] #self.bus_generator()
        new_vehicle = random.choice(function_list)
        print(new_vehicle)
        return new_vehicle

