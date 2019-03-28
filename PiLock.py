from PySide2.QtCore import *

UNLOCKED = 0
LOCKED = 1

if __name__ == "__main__":
    app = QApplication()

    indicator = IndicatorLights(7,8)
    lock = LockMotor(24)
    disp = Display(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
    keypad = KeyPad(21,20,16,12,25)

    sys.exit(app.exec_())
