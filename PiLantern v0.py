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
    
def slow():
    t1 = Timer(0, blue)
    t2 = Timer(1, red)
    t3 = Timer(2, green)
    t1.start()
    t2.start()
    t3.start()

class fast():

    def blue():
        blue_led.pulse(n=1, fade_in_time=0.8, fade_out_time=0.8)
    
    def red():
        red_led.pulse(n=1, fade_in_time=0.8, fade_out_time=0.8)
    
    def green():
        green_led.pulse(n=1, fade_in_time=0.8, fade_out_time=0.8)

    t1 = Timer(0, blue)
    t2 = Timer(1, red)
    t3 = Timer(2, green)

for _ in range(10):
    fast


#button.when_pressed = Lantern()

#function = generates a random number every time via lambda? 
#the idea is to generate a random number between 5 and 15 seconds, and 
#put that n into a threading timer. idk how to do this though. 

#a timer must be ran every x seconds, where x is random, and upon the
#timer running, a new random n must be generated, and Lantern called.
