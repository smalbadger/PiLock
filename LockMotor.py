"""
credits to https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/ for showing how to use a servo motor
"""
import RPi.GPIO as GPIO

class LockMotor():
    def __init__(self, servoPin):
        self.motor = GPIO.PWM(servoPin, 50)
        p.start(25)

    def unlock(self):
        self.motor.ChangeDutyCycle(25)

    def lock(self):
        self.motor.ChangeDutyCycle(75)
