import locale
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget, QFrame, QHBoxLayout, QPushButton 
from PyQt5.QtGui import QIcon, QPixmap
#from FetchData import FetchReportsController

from ui import MainWindow,FetchReports#,FetchReportsTab, ManageVendorsTab, SettingsTab, FetchSpecialReportsTab, ImportReportTab,\
  # SearchTab, VisualTab, CostsTab
"""
import GeneralUtils

from ManageVendors import ManageVendorsController
from FetchData import FetchReportsController, FetchSpecialReportsController
from Settings import SettingsController, SettingsModel

from ImportFile import ImportReportController
from Costs import CostsController
from Search import SearchController

from Visual import VisualController
from Visual2 import VisualController

import ManageDB
from Constants import *
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

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget {font-family: Segoe UI; font-size: 12pt;}")

    # Use QMainWindow instead of QWidget for the main window
    main_window = QMainWindow()
    main_window_ui = MainWindow.Ui_mainWindow()
    main_window_ui.setupUi(main_window)

    # Create an instance of the FetchReportsTab class
    fetch_reports_tab = QWidget(main_window)
    fetch_reports_ui = FetchReports.Ui_FetchReportTab()
    fetch_reports_ui.setupUi(fetch_reports_tab)

    # Add the FetchReportsTab instance to the central widget of the QMainWindow
    main_window.setCentralWidget(fetch_reports_tab)

    # ... (Add other components and tabs as needed)

    main_window.show()
    sys.exit(app.exec_())