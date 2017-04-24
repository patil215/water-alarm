# Water Alarm Clock

I kept missing Linear Algebra this semester (10 AMs are rough) so I decided to go to extreme measures. I built an alarm clock that dumps water on my head to wake me up.

The project consists of an internet-connected Raspberry Pi connected to a peristaltic water pump. The two components are mounted on the wall next to my bed. A water container sits under my bed, and a pipe runs up through the peristaltic pump up to the ceiling, right above my bed.

I can set an alarm by connecting to a webapp running on the Raspberry Pi. The webapp uses a recurring weekly cron job, as well as the GPIO library, to turn on the peristaltic motor at the scheduled time. As the motor rotates, it pumps water through the pipes, eventually falling onto my head.

I can SSH into the Pi at any time to manually manage the webapp or run the water alarm.

Here is a video of the alarm clock in action:

[![Water Alarm Video](http://i.imgur.com/wb7acl1.png)](https://vimeo.com/214351737)


The webapp I built to configure the alarm:

![webapp](http://i.imgur.com/mpQujcT.png)


The entire thing as viewed from my bed:

![project](http://i.imgur.com/7WuSX3F.jpg)


The water reservoir under my bed from which the water is pumped from. I can go about a month before needing to refill the bottle:

![water](http://i.imgur.com/zZ8jMCh.jpg)


The Raspberry Pi and peristaltic pump mounted on the wall. Note the small clear pipe coming into and out of the motor. (The small servo also present on the breadboard is used as a mechanical "transistor" in order to step up the voltage for the motor (I didn't have a transistor or relay readily available)):

![pi](http://i.imgur.com/3caNOHt.jpg)


The pipe that hangs over me to wake me up. The water is dumped for about 5 seconds, and the initial pouring is unpleasant enough to leave me wide awake. Thankfully, the water dries up from my bed after about 30 minutes:

![pipe](http://i.imgur.com/2TeOJhI.jpg)



## Setup
1. Git clone
2. ```./script/setup.sh```
3. ```sudo ./run.py```
4. Modify ```config.py``` and change username/password.
5. Configure server to run on boot (instructions [here](http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html)).
