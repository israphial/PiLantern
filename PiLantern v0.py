#python3

from threading import Timer
from gpiozero import PWMLED, Button

blue_led = PWMLED(5)
red_led = PWMLED(6)
green_led = PWMLED(13)
button = Button(2)

def blue():
    blue_led.pulse(n=1, fade_in_time=1.5, fade_out_time=1.5)
    
def red():
    red_led.pulse(n=1, fade_in_time=1.5, fade_out_time=1.5)
    
def green():
    green_led.pulse(n=1, fade_in_time=1.5, fade_out_time=1.5)
    
def Lantern():
    t1 = Timer(0, blue)
    t2 = Timer(1, red)
    t3 = Timer(2, green)
    t1.start()
    t2.start()
    t3.start()



button.when_pressed = Lantern()
>>>>>>> 9c30771ecb75dd144142bc6718b09d9eb8b90268
