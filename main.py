
from djitellopy import Tello

tello = Tello()

tello.connect()
print(f" batt: {tello.get_battery()}")