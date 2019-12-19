#python3

from threading import Timer
from gpiozero import PWMLED

blue_led = PWMLED(5)
red_led = PWMLED(6)
green_led = PWMLED(13)

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

Lantern()
    
"""    
try:
    Lantern()
except Exception as e:
    print("fatal error, debug - %s", e)
finally: #forces gpio slots off
    blue_led.close()
    red_led.close()
    green_led.close()
    
"""