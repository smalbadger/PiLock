from IndicatorLights import *
from LockMotor import *
from Display import *
from KeyPad import *


UNLOCKED = 0
LOCKED = 1

state = UNLOCKED
previousState = LOCKED

passcode = []

indicator = IndicatorLights(7,8)
lockMotor = LockMotor(24)
disp = Display(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13,6,5,11], numbering_mode=GPIO.BCM)
keypad = KeyPad(21,20,16,12,25)

def lock():
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
	disp.displayCode(keypad.getGuess())
	
def checkGuess():
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
	
keypad.events.keyPressed += displayCode
keypad.events.guessSubmitted += checkGuess

unlock()

while True:
	if state == LOCKED and previousState == UNLOCKED:
		guess = keypad.getGuess()
		if len(guess) == 0:
			disp.writeMessage("Locked")
			
	elif state == UNLOCKED and previousState == LOCKED:
		guess = keypad.getGuess()
		if len(guess) == 0:
			disp.writeMessage("Unlocked")
			
	previousState = state

