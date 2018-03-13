from flask import Flask
from time import sleep
from gpiozero import LED, Button
import dht11

instance = dht11.DHT11(pin=3)
led = LED(18)
button = Button(2)

def button_pressed():
    print('Temperature: %d F' % in_farenheit(result.temperature))
        
def get_temperature():
    while True:
        result = instance.read()
        if result.is_valid():
            return in_farenheit(result.temperature)
    
button.when_pressed = button_pressed

app = Flask(__name__)

@app.route('/temp')
def temperature():
    return 'Temperature: %d F' % get_temperature()

@app.route('/light_on')
def hello():
    led.on()
    return 'light on'

@app.route('/light_off')
def hello2():
    led.off()
    return 'light off'

@app.route('/blink')
def blink():
    led.blink()
    return 'blinking'

@app.route('/status')
def status():
    if led.is_lit:
        return 'light is on'
    elif not led.is_lit:
        return 'light is off'
    
def in_farenheit(temp):
    return (temp * (9/5)) + 32
        
if __name__ == '__main__':
    app.run('192.168.0.107')
