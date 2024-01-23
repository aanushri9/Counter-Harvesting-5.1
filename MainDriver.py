import locale
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget,QSizePolicy, QWidget, QFrame, QHBoxLayout, QPushButton 
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
import os

#from FetchData import FetchReportsController
from ui import AddVendorDialog, MainWindow,EditVendors,ManageVendorsTab,RemoveVendorDialog#, SettingsTab
#from ManageVendors import ManageVendorsController 
#import GeneralUtils
#import ManageDB
#from Constants import *

"""
from FetchData import FetchReportsController, FetchSpecialReportsController
from Settings import SettingsController, SettingsModel

from ImportFile import ImportReportController
from Costs import CostsController
from Search import SearchController

from Visual import VisualController
from Visual2 import VisualController
"""

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
    
    # Connect the manageVendorButton clicked signal to the show_manage_vendors slot
        self.manageVendorsButton.clicked.connect(self.show_manage_vendors)
        self.settingsButton.clicked.connect(self.show_settings)


    def show_manage_vendors(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the ManageVendorsTab UI file
        manage_vendors_ui_file_path = os.path.join(script_dir, "ui", "ManageVendorsTab.ui")

        # Create an instance of QWidget (or any other QWidget) and load the UI into it
        manage_vendors_widget = QWidget()
        loadUi(manage_vendors_ui_file_path, manage_vendors_widget)

       # Set the size policy of the manage_vendors_widget
        manage_vendors_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add the manage_vendors_widget to the QTabWidget
        self.tabWidget.addTab(manage_vendors_widget, "Manage Vendors")

        # Set the size policy of the QWidget in the mainBodyContainer
        self.mainBodyContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Show the QTabWidget
        self.tabWidget.show()

    def show_settings(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the settings.ui file
        settings_ui_file_path = os.path.join(script_dir, "ui", "SettingsTab.ui")

        # Create an instance of QWidget (or any other QWidget) and load the UI into it
        settings_widget = QWidget()
        loadUi(settings_ui_file_path, settings_widget)

        # Set the size policy of the settings_widget
        settings_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add the settings_widget to the QTabWidget
        self.tabWidget.addTab(settings_widget, "Settings")

        # Set the size policy of the QWidget in the mainBodyContainer
        self.mainBodyContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Show the QTabWidget
        self.tabWidget.show()

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