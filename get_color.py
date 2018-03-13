from neopixel import *

def get_color(color):
    if color.lower() == 'red':
        return Color(255,0,0)
    if color.lower() == 'green':
        return Color(0,255,0)
    elif color.lower() == 'blue':
        return Color(0,0,255)
    elif color.lower() == 'clear':
        return Color(0,0,0)
    elif color.lower() == 'orange':
        return Color(255,140,0)
    else:
        return Color(0,0,0)