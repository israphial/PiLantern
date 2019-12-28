#python3

from threading import Timer
from gpiozero import PWMLED, Button

blue_led = PWMLED(5)
red_led = PWMLED(6)
green_led = PWMLED(13)
button = Button(2)

def slow_unsynced():

    def blue():
        blue_led.pulse(n=1, fade_in_time=1.5, fade_out_time=1.5)
    
    def red():
        red_led.pulse(n=1, fade_in_time=1.5, fade_out_time=1.5)
    
    def green():
        green_led.pulse(n=1, fade_in_time=1.5, fade_out_time=1.5)
    
    t1 = Timer(0, blue)
    t2 = Timer(1, red)
    t3 = Timer(2, green)
    t1.start()
    t2.start()
    t3.start()

def fast_synced():

    def blue():
        blue_led.pulse(n=6, fade_in_time=0.6, fade_out_time=0.6)
    
    def red():
        red_led.pulse(n=6, fade_in_time=0.6, fade_out_time=0.6)
    
    def green():
        green_led.pulse(n=6, fade_in_time=0.6, fade_out_time=0.6)

    t1 = Timer(0, blue)
    t2 = Timer(0, red)
    t3 = Timer(0, green)
    t1.start()
    t2.start()
    t3.start()

def single_fast_blink():

    def blue():
        blue_led.pulse(n=1, fade_in_time=0.4, fade_out_time=0.4)
    
    def red():
        red_led.pulse(n=1, fade_in_time=0.4, fade_out_time=0.4)
    
    def green():
        green_led.pulse(n=1, fade_in_time=0.4, fade_out_time=0.4)

    t1 = Timer(0, blue)
    t2 = Timer(0, red)
    t3 = Timer(0, green)
    t1.start()
    t2.start()
    t3.start()

class Light:
    def __init__(self, red_led_pulse_length, red_led_fadein, red_led_fadeout, 
                green_led_pulse_length, green_led_fadein_, green_led_fadeout,
                blue_led_pulse_length, blue_led_fadein, blue_led_fadeout,
                red_start_time, blue_start_time, green_start_time, *args):

    def blink_red():
    #accept red params to make red blink according to given values

    def blink_blue():
    #accept blue params to make blue blink according to given values

    def blink_green():
    #accept green params to make green blink according to given values

    t1 = Timer() #take first start_time and color as second value
    t2 = Timer() #take second start_time and color as second value
    t3 = Timer() #take third start_time and color as second value
    #t1.start()
    #t2.start()
    #t3.start()
    #args received as a tuple, else the tuple is "falsy", so this if will only
    #activate if args is not falsy, showing me whatever the arg is
    if args:
        print("Unexpected args given:", args)