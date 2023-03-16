import time
import random
from sty import fg

def generateRGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)


while True:
    phrase = ["I'm", "randomnly", "changing", "colours", "muahahaha!!", ""]
    for l in phrase:
        red, green, blue = generateRGB()
        colour = generateColour(red, green, blue)
        print(colour, l.upper())
        time.sleep(.25)

