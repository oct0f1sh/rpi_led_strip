from gpiozero import LED, Button
from time import sleep

#led = LED(18)
button = Button(5)

while True:
    print(button.is_pressed)
    if button.is_pressed:
        print('pressed button')
##        led.on()
    else:
##        led.off()
        pass
