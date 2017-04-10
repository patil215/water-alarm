# Water Alarm Clock
This project takes a Raspberry Pi and, web-enabling it, turns it into a water alarm
clock. The Pi is attached to a Peristaltic pump connected to a water reservoir, which
dumps water on my face from my ceiling for a period of 5 seconds to wake me up.

The alarm is configured through a web interface.

## Setup
1. Git clone
2. ```./script/setup.sh```
3. ```sudo ./run.py```
4. Configure server to run on boot (instructions [here](http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html)).
