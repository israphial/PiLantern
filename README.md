# PiLantern
LEDs powered by a Raspberry Pi
Started 1/06/20 (originally began ~12/15/19)

Time log: 
1/6/20: 1 hour, general research
1/6/20: 15 min, general research

Current ideas and ETA on finish:
general research: 4 hours ||| ? hours completed
Kivy GUI with 3 buttons: 2 hours ||| ? hours completed
Sender daemon: 3 hours ||| ? hours completed
Receiver daemon: 4 hours ||| ? hours completed
strip.py redo to accept input from daemon: 2 hours ||| ? hours completed
documentation and testing: 2 hours ||| ? hours completed

total project time expected: ~17 hours

to do: 
>
>
>

Notes on time use: 
(fill this in if time used ends up exceeding how long I THOUGHT it would take to do a part of the project, and WHY it took longer, so that I can improve the process)

>
>
>

History:
Project began as a small program to light up three LEDs on a breadboard, red, green, and blue. My final current iteration is a function based threading program that runs the three lights on three separated, timed threads in a while True loop. I'm going to estimate that this small program took me about three hours to research and write. 

Current program is a lot different. The Pi powers an RGB LED strip that cost me 10 bucks. This program has a dictionary with color names, and the values are RGB color integer tuples. When ran, a While True loop watched for user input of a desired color, which is passed to a function that calls the appropriate value from the dict. The value is put into an object that assigns the strip a color using the .fill(RGB int tuple) method. The loop restarts, waiting for the next input. It also currently prints a list of all possible colors if prompted. At this point in the project, as of 1/6/20, the strip connects directly to the pi and draws power thru it. It uses the GPIO pins 3, 6, and 12. 3 is for a 5V power draw, 6 for ground, and 12 for data. 

The next step in the project is where things get really complicated. I want to bump this way up in scope. 

The idea: 
Kivy-based GUI on desktop that uses a daemon to parse and send information to a daemon on the Pi, which receives and calls up the appropriate script, and performs the assigned task depending on what information is received. So, I have a Kivy GUI program with a red, green, and blue button set, each of those buttons has a piece of data it can send to the Pi thru the two daemons (sender and receiver), and the receiver calls whatever function in whatever program it's supposed to (perhaps part of the data sent could be what program "this" command is for). 

This is a very multi-part program, that will require me to build a Kivy GUI, two daemons that do totally different things, and I'll need to rebuild my LED strip activator program, or at least change it enough so that it can be used by other programs. 

Notes and times will be kept here, to track the total hours it takes me to "complete" this program. I will do my best to document what I can, so that I have a good record of this process. I am doing this as an attempt to improve my creation process, and see how long things took me to do. 

Links: 
https://www.github.com/israphial/PiLantern/


Notes section (include dates and times):
for some info on the daemon socket shit, see discord python #microcontrollers, comments from 1/6/20, 5PM, from @sinthrill and me. 

