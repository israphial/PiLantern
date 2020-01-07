#this program forces the LED strip off and quits itself
#this program requires SUDO ACCESS!

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 60)

pixels.fill((0, 0, 0))
quit()