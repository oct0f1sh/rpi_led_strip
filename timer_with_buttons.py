from gpiozero import Button
import RPi.GPIO as GPIO

start = Button(5)
stop = Button(6)
reset = Button(13)

while True:
    if start.is_pressed:
        print('start')