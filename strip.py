#LED strip working test

#> sudo pip install adafruit-circuitpython-neopixel

from time import sleep
import board
import neopixel

#CONSTS
DictKeyValue = None
pixels = neopixel.NeoPixel(board.D18, 60, brightness=1)
#.fill method syntax is pixels.fill((int, int, int))

ColorsDict = {
	
	'red': (128,0,0),
	'green': (0,128,0),
	'blue': (0,0,128),
        'yellow': (128, 128, 0),
        'cyan': (0, 255, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'off': (0, 0, 0),
        'crimson': (220, 20, 60),
        'coral': (255, 127, 80),
        'indigo': (75, 0, 130),
        'magenta': (140, 0, 140),
        'azure': (210, 255, 255),
        'steel blue': (176, 196, 222),
        'midnight blue': (25, 25, 112),
        'aquamarine': (127, 255, 212),
        'gold': (210, 105, 30),
        'brown': (139, 69, 19),
                 
}

#Takes in the input KeyContainer, uses it to retrieve the corresponding dict value,
#and fills the pixels.fill() command with that resulting tuple
def DictValueRetriever(KeyContainer):
    global DictKeyValue
    DictKeyValue = ColorsDict.get(KeyContainer)
    pixels.fill(DictKeyValue)


while True:
    try:
        print("LED strip controller v1")
        KeyContainer = input("""Color? type 'colors' for a list of available colors""").lower()
        if KeyContainer == "colors":
            print(ColorsDict.keys())
            continue
        if KeyContainer == "stay on":
                print("closing program and leaving lights on...")
                sleep(2)
                quit()
        if KeyContainer not in ColorsDict:
            print("""the value you entered does not appear to be in the color list, restarting...""")
            continue        

        DictValueRetriever(KeyContainer)

    #exits program and turns light off upon keyboard interrupt, will not
    #break outer scripts
    except KeyboardInterrupt:
        print("Exiting program, turning lights off in 2 seconds...")
        sleep(2)
        pixels.fill((0, 0, 0))
        quit()
