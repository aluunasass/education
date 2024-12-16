import time

import keyboard
import mouse


def change():
    global work
    work = not work


def speed_up():
    global speed
    speed /= 2


def speed_down():
    global speed
    speed *= 2


speed = 1
work = False
keyboard.add_hotkey("q", change)
keyboard.add_hotkey("w", speed_up)
keyboard.add_hotkey("s", speed_down)

while True:
    if work:
        mouse.click(button="left")
        time.sleep(speed)
