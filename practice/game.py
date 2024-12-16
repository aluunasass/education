import time
import turtle

import keyboard

keyboard.add_hotkey("w", lambda: turtle.forward(10))
keyboard.add_hotkey("s", lambda: turtle.backward(10))
keyboard.add_hotkey("a", lambda: turtle.left(90))
keyboard.add_hotkey("d", lambda: turtle.right(90))
x = 1
y = 1
turtle.left(60)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45 + 90)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45 + 90)
turtle.exitonclick()
