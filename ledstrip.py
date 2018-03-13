from neopixel import *
from get_color import get_color
import time

class LEDStrip(object):
    def __init__(self, LED_PIN, LED_COUNT):
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	self.strip.begin()


    def colorWipe(self, color, wait_ms=50):
        strip = self.strip
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)


    def rainbowCycle(self, wait_ms=20, iterations=5):
        strip = self.strip
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)


    def stripOff(self):
        strip = self.strip
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
        strip.show()


    def twoColorWipe(self, color1, color2):
        strip = self.strip
        for i in range(strip.numPixels()):
            if i % 2 == 0:
                strip.setPixelColor(i, color1)
            else:
                strip.setPixelColor(i, color2)
            strip.show()
            time.sleep(50/1000.0)


    def countdown(self, minutes):
        strip = self.strip
        self.colorWipe(get_color('green'))

        leds_off = 0

        for seconds in range(0, 60*minutes):
            if seconds % minutes == 0:
                strip.setPixelColor(strip.numPixels() - (seconds / minutes), Color(0,0,0))
                strip.show()
                leds_off += 1
            time.sleep(1)

            if seconds % 60 == 0:
                for i in range(0, strip.numPixels() - leds_off):
                    if seconds / 60 == 6:
                        pass
                    elif seconds / 60 == 5:
                        pass
                    elif seconds / 60 == 4:
                        pass
                    elif seconds / 60 == 3:
                        pass
                    elif seconds / 60 == 2:
                        strip.setPixelColor(i, Color(255,0,0))
                    elif seconds / 60 == 1:
                        strip.setPixelColor(i, Color(255,140,0))
                strip.show()

        self.stripOff()

    def lightning_talk(self):
        strip = self.strip
        self.solidGreen()


    def wheel(self, pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)
