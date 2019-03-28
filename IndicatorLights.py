from gpiozero import LED

class IndicatorLights():

    def __init__(self, redPin, greenPin):
        self.red = LED(redPin)
        self.green = LED(greenPin)

    def showRed(self):
        self.red.on()
        self.green.off()

    def showGreen(self):
        self.green.on()
        self.red.off()
