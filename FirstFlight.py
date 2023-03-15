
from djitellopy import Tello

tello = Tello()

tello.connect()
print(f" batt: {tello.get_battery()}")
tello.takeoff()

tello.move_left(50)
tello.rotate_clockwise(90)
tello.move_forward(100)

tello.land()