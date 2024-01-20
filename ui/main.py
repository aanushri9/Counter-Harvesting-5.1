from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("MainWindow.ui", self)

        self.menu_num = 0
        self.MenuButton.clicked.connect(self.menubar)

    def menubar(self):
        print("pressed")
        if self.menu_num == 0:
            self.animation = QPropertyAnimation(self.leftSubContainer, b"minimumWidth")
            self.animation1 = QPropertyAnimation(self.leftMenu, b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(55)
            self.animation.setEndValue(250)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            self.animation1.setDuration(250)
            self.animation1.setStartValue(55)
            self.animation1.setEndValue(250)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.menu_num = 1
        else:
            self.animation = QPropertyAnimation(self.leftSubContainer, b"minimumWidth")
            self.animation1 = QPropertyAnimation(self.leftMenu, b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(250)
            self.animation.setEndValue(40)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            self.animation1.setDuration(250)
            self.animation1.setStartValue(250)
            self.animation1.setEndValue(40)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.menu_num = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
