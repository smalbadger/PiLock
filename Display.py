"""
Author:         Sam Badger
Date Created:   March 27, 2019
Description:    Custom wrapper for the LCD.
Credits to http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/ for showing how to interface with LCD in python.
"""
from RPLCD import CharLCD

class Display():
    def __init__(self, *args, **kwargs):
        self.lcd = CharLCD(*args, **kwargs)

    def displayCode(self, code):
        """ displays the code being typed.
        code is a list of numbers
        """
        strCode = ""
        for num in code:
            strCode += str(num)
        self.clear()
        self.lcd.write_string(strCode)

    def writeMessage(self, msg):
        """ write a message to the LCD """
        self.clear()
        self.lcd.write_string(msg)

    def clear(self):
        """ clears the LCD """
        self.lcd.clear()
