import time

from neopixel import *
from flask import Flask
from ledstrip import LEDStrip

from get_color import get_color

import argparse
import signal
import sys

app = Flask(__name__)

led_strip = LEDStrip(18, 60)


@app.route('/colorwipe/<string:color>')
def colorWipe(color):
    led_strip.colorWipe(get_color(color))
    return 'color wipe activated'


@app.route('/colorswipe/<string:color1>&<string:color2>')
def colorsWipe(color1, color2):
    led_strip.twoColorWipe(get_color(color1), get_color(color2))
    return 'color wipe activated'


@app.route('/rainbow')
def rainbow():
    led_strip.rainbowCycle()
    return 'rainbow cycle activated'


@app.route('/clear')
def off():
    led_strip.stripOff()
    return 'turned strip off'


@app.route('/infinite')
def infin():
    while True:
        led_strip.rainbowCycle()


@app.route('/timer/<int:minutes>')
def timer(minutes):
    led_strip.countdown(minutes)
    return 'timer completed'


@app.route('/colorrun')
def colorRun():
    led_strip.colorWipe(get_color('red'))
    led_strip.colorWipe(get_color('blue'))
    led_strip.colorWipe(get_color('green'))
    led_strip.rainbowCycle()
    return 'completed'


# Main program logic follows:
if __name__ == '__main__':
        app.run('192.168.0.104')
