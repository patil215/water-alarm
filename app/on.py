#!/usr/bin/env python
from light_driver import LightDriver

from RPi import GPIO
import time

def setServo(pwm, angle):
    duty = float(angle) / 10.0 + 2.5 
    pwm.ChangeDutyCycle(duty)


def main():
    onAngle = 72
    offAngle = 90

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    pwm = GPIO.PWM(17, 100)
    pwm.start(5)


    for i in range(0, 10):
        setServo(pwm, onAngle)
        time.sleep(1)
        setServo(pwm, offAngle)
        time.sleep(1)

if __name__ == "__main__":
	main()
