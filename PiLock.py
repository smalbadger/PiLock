"""
Author:         Sam Badger
Date Created:   March 27, 2019
Description:    Simple digital passcode locking mechanism for Raspberry Pi Workshop
"""

from IndicatorLights import *
from LockMotor import *
from Display import *
from KeyPad import *


UNLOCKED = 0
LOCKED = 1

state = UNLOCKED
previousState = LOCKED

passcode = []

#################################
#       System Components       #
#################################
indicator = IndicatorLights(7,8)
lockMotor = LockMotor(24)
disp = Display(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13,6,5,11], numbering_mode=GPIO.BCM)
keypad = KeyPad(21,20,16,12,25)


def lock():
    """ sequence of instructions to go into LOCKED mode"""
    global disp
    global indicator
    global state
    global keypad
    global passcode
    global lockMotor
    
    passcode = keypad.getGuess()
    disp.writeMessage("Locked")
    indicator.showRed()
    state = LOCKED
    keypad.reset()
    lockMotor.lock()
    
    
def unlock():
    """ sequence of instructions to go into UNLOCKED mode"""
    global disp
    global indicator
    global state
    global keypad
    global lockMotor
    
    disp.writeMessage("Unlocked")
    indicator.showGreen()
    state = UNLOCKED
    keypad.reset()
    lockMotor.unlock()

def displayCode():
    """ Display the code that's being typed on the LCD """
    disp.displayCode(keypad.getGuess())
    
def checkGuess():
    """ if the lock is in the LOCKED state, check if the guess is correct. Else set the passcode to be the guess. """
    global state
    global keypad
    global passcode
    global indicator
    global lock
    
    if state == LOCKED:
        guess = keypad.getGuess()
        for i in range(len(guess)):
            if int(guess[i]) != int(passcode[i]):
                disp.writeMessage("Still Locked")
                keypad.reset()
                guess = []
                break
                
        if guess != []:
            unlock()
            
    else:
        lock()
    
##############################
#   Connect event handlers   #
##############################

# every time a number button is pressed, display the guess
keypad.events.keyPressed += displayCode

# every time the submit button is pressed, either check the 
# guess or set the passcode.
keypad.events.guessSubmitted += checkGuess





# initially, the lock is unlocked.
unlock()

while True:

    # I don't think this really does anything useful anymore, but 
    # I'm not testing anymore, so I'll leave it in for the demo.

    if state == LOCKED and previousState == UNLOCKED:
        guess = keypad.getGuess()
        if len(guess) == 0:
            disp.writeMessage("Locked")
            
    elif state == UNLOCKED and previousState == LOCKED:
        guess = keypad.getGuess()
        if len(guess) == 0:
            disp.writeMessage("Unlocked")
            
    previousState = state

