from PySide2.QtCore import Signal, QObject
from gpiozero import Button

class KeyPad(QObject):
    keyPressed = Signal()
    guessSubmitted = Signal()

    def __init__(self, btn1Pin, btn2Pin, btn3Pin, btn4Pin, submitPin):
        self.state = WAITING
        self.combo = []
        self.guess = []
        self.btn1 = Button(btn1Pin)
        self.btn2 = Button(btn2Pin)
        self.btn3 = Button(btn3Pin)
        self.btn4 = Button(btn4Pin)
        self.btn5 = Button(submitPin)

        self.btn1.when_pressed = self.press1
        self.btn2.when_pressed = self.press2
        self.btn3.when_pressed = self.press3
        self.btn4.when_pressed = self.press4
        self.btn5.when_pressed = submit

    def press1(self):
        self.combo.append(1)
        keyPressed.emit()

    def press2(self):
        self.combo.append(2)
        keyPressed.emit()

    def press3(self):
        self.combo.append(3)
        keyPressed.emit()

    def press4(self):
        self.combo.append(4)
        keyPressed.emit()

    def submit(self):
        if len(self.combo) < 4:
            return

        self.guessSubmitted.emit()

    def isGuessReady(self):
        if len(self.combo) >= 4:
            return True
        return False

    def getGuess(self):
        if len(self.combo) > 4:
            return self.combo[-4:]
        else
            return self.combo[:]

    def reset(self):
        self.combo = []
