from RPi import GPIO
import time

def setServo(pwm, angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 100)
pwm.start(5)

onAngle = 72
offAngle = 90

while True:
    setServo(pwm, onAngle)
    time.sleep(1)
    setServo(pwm, offAngle)
    time.sleep(1)
