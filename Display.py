"""
Credits to http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/ for showing how to interface with LCD in python.
"""
from RPLCD import CharLCD

class Diplay():
    def __init__(self, *args, **kwargs):
        self.lcd = CharLCD(*args, **kwargs)

    def displayCode(self, code):
        self.clear()
        self.lcd.write_string("".join(code))

    def writeMessage(self, msg):
        self.clear()
        self.lcd.write_string(msg)

    def clear():
        self.lcd.clear()
