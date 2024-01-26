import locale
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget, QFrame, QHBoxLayout, QPushButton, QTabWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
import os
#from FetchData import FetchReportsController
from ui import AddVendor, MainWindow,EditVendors,ManageVendorsTab,RemoveVendorDialog, Search,Settingtab
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
        self.manage_vendors_tab_index = -1
        self.fetch_report_tab_index = -1
        self.search_tab_index = -1
        self.settings_tab_index = -1
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the UI file
        ui_file_path = os.path.join(script_dir, "ui", "MainWindow.ui")

        # Load the UI file
        loadUi(ui_file_path, self)
        self.menu_num = 0
        self.tabWidget.setStyleSheet("QTabBar::tab { color: black; }")
        for i in range(self.tabWidget.count()):
            self.tabWidget.setStyleSheet("QTabBar::tab { color: black; }")

        self.menu_num = 0
    
        self.MenuButton.clicked.connect(self.menubar)
       

    
    # Connect the manageVendorButton clicked signal to the show_manage_vendors slot
        self.manageVendorsButton.clicked.connect(self.show_manage_vendors)
        self.searchRepotsButton.clicked.connect(self.show_search)
        self.settingsButton.clicked.connect(self.show_settingTab)
        self.FetchReportsButton.clicked.connect(self.show_Fetch_reports)

    def show_manage_vendors(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        manage_vendors_ui_file_path = os.path.join(script_dir, "ui", "ManageVendorsTab.ui")
        manage_vendors_widget = QWidget()
        loadUi(manage_vendors_ui_file_path, manage_vendors_widget)
        if self.manage_vendors_tab_index == -1:
            # Add the manage_vendors_widget to the QTabWidget
            self.manage_vendors_tab_index = self.tabWidget.addTab(manage_vendors_widget, "Manage Vendors")
        else:
            # Switch to the existing manage vendors tab
            self.tabWidget.setCurrentIndex(self.manage_vendors_tab_index)
        self.tabWidget.show()

    def show_Fetch_reports(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the ManageVendorsTab UI file
        fetch_reports_tab_ui_file_path = os.path.join(script_dir, "ui", "FetchReportsTab.ui")

        # Create an instance of QWidget (or any other QWidget) and load the UI into it
        fetch_reports_tab_widget = QWidget()
        loadUi(fetch_reports_tab_ui_file_path, fetch_reports_tab_widget)

        # Add the fetch_vendor_widget to the QTabWidget
        if self.fetch_report_tab_index == -1:
            # Add the manage_vendors_widget to the QTabWidget
            self.fetch_report_tab_index = self.tabWidget.addTab(fetch_reports_tab_widget, "Fetch Reports")
        else:
            # Switch to the existing manage vendors tab
            self.tabWidget.setCurrentIndex(self.fetch_report_tab_index)
        self.tabWidget.show()
        

    def show_search(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the ManageVendorsTab UI file
        search_ui_file_path = os.path.join(script_dir, "ui", "Search.ui")

        # Create an instance of QWidget (or any other QWidget) and load the UI into it
        search_widget = QWidget()
        loadUi(search_ui_file_path, search_widget)

        # Add the fetch_vendor_widget to the QTabWidget
        if self.search_tab_index == -1:
            # Add the manage_vendors_widget to the QTabWidget
            self.search_tab_index = self.tabWidget.addTab(search_widget, "Search Vendors")
        else:
            # Switch to the existing manage vendors tab
            self.tabWidget.setCurrentIndex(self.search_tab_index)
        self.tabWidget.show()
        

    def show_settingTab(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the ManageVendorsTab UI file
        settingTab_ui_file_path = os.path.join(script_dir, "ui", "Settingtab.ui")

        # Create an instance of QWidget (or any other QWidget) and load the UI into it
        settingTab_widget = QWidget()
        loadUi(settingTab_ui_file_path, settingTab_widget)

        # Add the fetch_vendor_widget to the QTabWidget
        if self.settings_tab_index == -1:
            # Add the manage_vendors_widget to the QTabWidget
            self.settings_tab_index= self.tabWidget.addTab(settingTab_widget, "Settings")
        else:
            # Switch to the existing manage vendors tab
            self.tabWidget.setCurrentIndex(self.settings_tab_index)
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

            # Hide the Frame4 widget
            self.frame_4.hide()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())