from gpiozero import Button
from events import Events

class KeyPad():

    def __init__(self, btn1Pin, btn2Pin, btn3Pin, btn4Pin, submitPin):
        self.events = Events(('keyPressed', 'guessSubmitted'))
        
        self.combo = []
        self.btn1 = Button(btn1Pin)
        self.btn2 = Button(btn2Pin)
        self.btn3 = Button(btn3Pin)
        self.btn4 = Button(btn4Pin)
        self.btn5 = Button(submitPin)

        self.btn1.when_pressed = self.press1
        self.btn2.when_pressed = self.press2
        self.btn3.when_pressed = self.press3
        self.btn4.when_pressed = self.press4
        self.btn5.when_pressed = self.submit

    def press1(self):
        self.combo.append(1)
        self.events.keyPressed()

    def press2(self):
        self.combo.append(2)
        self.events.keyPressed()

    def press3(self):
        self.combo.append(3)
        self.events.keyPressed()

    def press4(self):
        self.combo.append(4)
        self.events.keyPressed()

    def submit(self):
        if len(self.combo) < 4:
            return

        self.events.guessSubmitted()

    def isGuessReady(self):
        if len(self.combo) >= 4:
            return True
        return False
    

    def getGuess(self):
        if len(self.combo) > 4:
            return self.combo[-4:]
        else:
            return self.combo[:]

    def reset(self):
        self.combo = []
