import os
import sys
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from ui import ManageVendors  # Import the ManageVendors module

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # Load the main window UI
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(script_dir, "ui", "MainWindow.ui")
        loadUi(ui_file_path, self)

        self.menu_num = 0
        self.MenuButton.clicked.connect(self.menubar)

        # Create an instance of the ManageVendors UI
        self.manage_vendors_ui = ManageVendors.Ui_ManageVendors()

        # Connect the manageVendorsButton clicked signal to the show_manage_vendors() slot
        self.manageVendorsButton.clicked.connect(self.show_manage_vendors)

    def show_manage_vendors(self):
        # Display the ManageVendors UI in the frame_4
        self.frame_4.setLayout(self.manage_vendors_ui.setupUi(self.frame_4))
        self.frame_4.show()

    def menubar(self):
        print("pressed")
        if self.menu_num == 0:
            self.animate_menu(55, 250)
            self.menu_num = 1
        else:
            self.animate_menu(250, 40)
            self.menu_num = 0

    def animate_menu(self, start_value, end_value):
        animation = QPropertyAnimation(self.leftSubContainer, b"minimumWidth")
        animation1 = QPropertyAnimation(self.leftMenu, b"minimumWidth")
        animation.setDuration(250)
        animation.setStartValue(start_value)
        animation.setEndValue(end_value)
        animation.setEasingCurve(QEasingCurve.InOutQuart)
        animation1.setDuration(250)
        animation1.setStartValue(start_value)
        animation1.setEndValue(end_value)
        animation1.setEasingCurve(QEasingCurve.InOutQuart)
        animation.start()
        animation1.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
