import time
from turtle import Screen
from cars import VehicleController
from road import Road
from scoreboard import Scoreboard, GameOver
from turtle_crosser import Turtle_Crosser
import random

#car shape = x-axis +/- 0 -> 17; y-axis: +/- 5
#SHAPE_CAR = ((7, 0),(7, 3), (5, 3), (5, 0), (0, 0), (0, 3), (1, 4), (5, 4), (6, 5), (7, 5), (7, 4), (17, 4), (18, 3), \
#        (18, 0), (18, -3), (17, -4), (7, -4), (7, -5), (6, -5), (5, -4), (1, -4), (0, -3), (0, 0), (5, 0), (5, -3), (7, -3), (7,0))

SHAPE_CAR = ((-2, 0), (-2, 3), (-4, 3), (-4, 0), (-9, 0), (-9, 3), (-8, 4), (-4, 4), (-3, 5), (-2, 5), (-2, 4), (8, 4), (9, 3),
             (9, 0), (9, -3), (8, -4), (-2, -4), (-2, -5), (-3, -5), (-4, -4), (-8, -4), (-9, -3), (-9, 0), (-4, 0), (-4, -3), (-2, -3), (-2, 0))

#truck shape = x-axis +/- 0 -> 56; y-axis: +/- 5
#SHAPE_TRUCK = ((0, 0), (0, 4), (1, 5), (8, 5), (9, 4), (10, 5), (55, 5), (56, 4),
#          (56, -4), (55, -5),(10, -5), (9, -4), (8, -5),(1, -5), (0, -4), (0, 0))

SHAPE_TRUCK = (-28, 0), (-28, 4), (-27, 5), (-20, 5), (-19, 4), (-18, 5), (27, 5), (28, 4), (28, -4), (27, -5), (-18, -5), (-19, -4), (-20, -5), (-27, -5), (-28, -4), (-28, 0)


#bus shape = x-axis +/- 0 -> 31; y-axis: +/- 5
#SHAPE_BUS = ((0, 0), (0, 4), (1, 5), (29, 5), (30, 4), (30, -4), (29, -5), (1, -5), (0, -4), (0, 0))

SHAPE_BUS = ((-15, 0), (-15, 4), (-14, 5), (14, 5), (15, 4), (15, -4), (14, -5), (-14, -5), (-15, -4), (-15, 0))


STRETCH_LEN = 4

screen = Screen()
screen.colormode(255)
screen.bgcolor("gray")
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0, 0)

screen.register_shape("car", SHAPE_CAR)
screen.register_shape("truck", SHAPE_TRUCK)
screen.register_shape("bus", SHAPE_BUS)


vehicle_list = []

score = Scoreboard()
game_over = GameOver()

kame = Turtle_Crosser()

road_line = Road()
road_line.draw_road()

def random_vehicle_generator():
    new_vehicle = VehicleController()
    global vehicle_list
    temp_list = [0, 1, 2]
    chosen_method = random.choice(temp_list)
    if chosen_method == 0:
        new_vehicle.car_generator()
    elif chosen_method == 1:
        new_vehicle.truck_generator()
    elif chosen_method == 2:
        new_vehicle.bus_generator()
    return new_vehicle

def hit_vehicle():
    global vehicle_list
    turtle_is_hit = False
    hit_turtle = False
    temp_list = []
    for vehicle in vehicle_list:
        if vehicle.shape() == "car":
            if vehicle.ycor() - 6*STRETCH_LEN < kame.ycor() < vehicle.ycor() + 6*STRETCH_LEN \
                    and vehicle.xcor() -10*STRETCH_LEN < kame.xcor() < vehicle.xcor() + 10*STRETCH_LEN:
                hit_turtle = True
            else:
                hit_turtle = False
        elif vehicle.shape() == "truck":
            if vehicle.ycor() - 6*STRETCH_LEN < kame.ycor() < vehicle.ycor() + 6*STRETCH_LEN \
                    and vehicle.xcor() -29*STRETCH_LEN < kame.xcor() < vehicle.xcor() + 29*STRETCH_LEN:
                hit_turtle = True
            else:
                hit_turtle = False
        elif vehicle.shape() == "bus":
            if vehicle.ycor() - 6*STRETCH_LEN < kame.ycor() < vehicle.ycor() + 6*STRETCH_LEN \
                    and vehicle.xcor() -16*STRETCH_LEN < kame.xcor() < vehicle.xcor() + 16*STRETCH_LEN:
                hit_turtle = True
            else:
                hit_turtle = False
        temp_list.append(hit_turtle)
    if any(temp_list) == True:
        turtle_is_hit = True
    return turtle_is_hit


def finish():
    if kame.ycor() > 260:
        return True


#listen for keypress
screen.listen()

#listen for turtle movement
screen.onkeypress(fun=kame.move_up, key="Up")
#screen.onkeypress(fun=kame.move_down, key="Down")


game_is_on = True

counter_n = 0
add_speed = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    if len(vehicle_list) > 0:
        for vehicle in vehicle_list:
            vehicle.drive(add_speed)
            if vehicle.xcor() > 700 or vehicle.xcor() < -700:
                vehicle.ht()
                vehicle_list.remove(vehicle)

    if counter_n > 12:
        vehicle_list.append(random_vehicle_generator())
        counter_n = 0
    counter_n += 1

    if hit_vehicle() == True:
        score.clear_gamescore()
        add_speed = 0
        game_over.show_game_over()

        time.sleep(2)
        game_over.clear()
        for vehicle in vehicle_list:
            vehicle.ht()
            vehicle.clear()
        kame.reset_turtle()
        vehicle_list = []

    if finish() == True:
        score.update_score()
        add_speed += 5
        time.sleep(1)
        for vehicle in vehicle_list:
            vehicle.ht()
            vehicle.clear()
        vehicle_list = []
        kame.reset_turtle()
        print(vehicle_list)

screen.update()
screen.exitonclick()
screen.mainloop()