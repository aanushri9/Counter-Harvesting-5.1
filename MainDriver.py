import locale
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget, QFrame, QHBoxLayout, QPushButton 
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
import os

#from FetchData import FetchReportsController
from ui import MainWindow,AddVendor,EditVendors,ManageVendors,RemoveVendorDialog 


# region debug_stuff

def trap_exc_during_debug(*args):
    # when app raises uncaught exception, print info
    print(args)


# install exception hook: without this, uncaught exception would cause application to exit
sys.excepthook = trap_exc_during_debug

# endregion

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

# if __name__ == "__main__":
#     locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

#     app = QApplication(sys.argv)
#     app.setStyleSheet("QWidget {font-family: Segoe UI; font-size: 12pt;}")

#     # Use QMainWindow instead of QWidget for the main window
#     main_window = QMainWindow()
#     main_window_ui = MainWindow.Ui_MainWindow()
#     main_window_ui.setupUi(main_window)
    
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
