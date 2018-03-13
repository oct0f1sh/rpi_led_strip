from gpiozero import LED, Button
import time

led = LED(18)
button = Button(2)

def button_pressed():
    print('button pressed')

def button_released():
    print('button released')

button.when_pressed = button_pressed
button.when_released = button_released
