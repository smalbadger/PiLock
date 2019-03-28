"""
Credits to http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/ for showing how to interface with LCD in python.
"""
from RPLCD import CharLCD

class Display():
    def __init__(self, *args, **kwargs):
        self.lcd = CharLCD(*args, **kwargs)

    def displayCode(self, code):
        
        strCode = ""
        for num in code:
            strCode += str(num)
            
        print(strCode)
        self.clear()
        self.lcd.write_string(strCode)

    def writeMessage(self, msg):
        self.clear()
        self.lcd.write_string(msg)

    def clear(self):
        self.lcd.clear()
