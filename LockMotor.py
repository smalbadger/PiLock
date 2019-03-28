"""
credits to https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/ for showing how to use a servo motor
"""
import RPi.GPIO as GPIO
import time

class LockMotor():
    def __init__(self, servoPin):
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPin, GPIO.OUT)
        self.motor = GPIO.PWM(servoPin, 50)
        self.motor.start(7.5)

    def unlock(self):
        self.motor.ChangeDutyCycle(5)
        time.sleep(0.5)
        self.freeze()

    def lock(self):
        self.motor.ChangeDutyCycle(10)
        time.sleep(0.5)
        self.freeze()
        
    def freeze(self):
        self.motor.ChangeDutyCycle(0)
