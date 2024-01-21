import locale
import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QHBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtGui import QIcon, QPixmap
from ui import MainWindow, AddVendor, EditVendors, ManageVendors, RemoveVendorDialog
import os
from PyQt5.uic import loadUi

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the UI file
        ui_file_path = os.path.join(script_dir, "ui", "MainWindow.ui")

        # Load the UI file
        loadUi(ui_file_path, self)

        self.menu_num = 0
        self.MenuButton.clicked.connect(self.menubar)

        # Create an instance of the ManageVendors UI
        self.manage_vendors_ui = ManageVendors.Ui_ManageVendors()

        # Connect the manageVendorsButton clicked signal to the show_manage_vendors() slot
        self.manageVendorsButton.clicked.connect(self.show_manage_vendors)

    def show_manage_vendors(self):
        # Display the ManageVendors UI in the frame_4
        self.manage_vendors_ui.setupUi(self.frame_4)
        self.frame_4.show()

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