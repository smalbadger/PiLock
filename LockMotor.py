"""
Author:         Sam Badger
Date Created:   March 27, 2019
Description:    Simple servo controller
credits to https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/ for showing how to use a servo motor
"""
import RPi.GPIO as GPIO
import time

class LockMotor():
    def __init__(self, servoPin):
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPin, GPIO.OUT)
        self.motor = GPIO.PWM(servoPin, 50)
        self.motor.start(7.5)   # 7.5% duty cycle puts motor at 90%

    def unlock(self):
        self.motor.ChangeDutyCycle(5)   # 5% duty cycle puts motor at 0 degrees
        
        # wait half a second, then turn off to stop jittering.
        time.sleep(0.5)             
        self.freeze()

    def lock(self):
        self.motor.ChangeDutyCycle(10)  # 10% duty cycle puts motor at 180 degrees
        
        # wait half a second, then turn off to stop jittering.
        time.sleep(0.5)
        self.freeze()
        
    def freeze(self):
        ''' turns the motor off by putting the duty cycle to zero'''
        self.motor.ChangeDutyCycle(0)
