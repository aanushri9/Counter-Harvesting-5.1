# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 615)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("*{\n"
"    \n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"\n"
"\n"
"\n"
"#centralwidget{\n"
"background-color:#1f232a;\n"
"}\n"
"#leftSubContainer{\n"
"background-color:#16191d;\n"
"}\n"
"#leftSubContainer QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"border-botton-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"color:white;}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leftMenu.setObjectName("leftMenu")
        self.gridLayout = QtWidgets.QGridLayout(self.leftMenu)
        self.gridLayout.setContentsMargins(11, -1, 0, -1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.leftSubContainer = QtWidgets.QWidget(self.leftMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.leftSubContainer.sizePolicy().hasHeightForWidth())
        self.leftSubContainer.setSizePolicy(sizePolicy)
        self.leftSubContainer.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leftSubContainer.setStyleSheet("\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}\n"
"\n"
"")
        self.leftSubContainer.setObjectName("leftSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftSubContainer)
        self.verticalLayout_2.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 11, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.MenuButton.setFont(font)
        self.MenuButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MenuButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuButton.setIcon(icon)
        self.MenuButton.setObjectName("MenuButton")
        self.horizontalLayout_2.addWidget(self.MenuButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.leftSubContainer)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 174))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.manageVendorsButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.manageVendorsButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/management.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manageVendorsButton.setIcon(icon1)
        self.manageVendorsButton.setIconSize(QtCore.QSize(24, 24))
        self.manageVendorsButton.setFlat(False)
        self.manageVendorsButton.setObjectName("manageVendorsButton")
        self.verticalLayout_3.addWidget(self.manageVendorsButton)
        self.FetchReportsButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.FetchReportsButton.setFont(font)
        self.FetchReportsButton.setToolTipDuration(-1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/data-transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FetchReportsButton.setIcon(icon2)
        self.FetchReportsButton.setObjectName("FetchReportsButton")
        self.verticalLayout_3.addWidget(self.FetchReportsButton)
        self.searchRepotsButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.searchRepotsButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/loupe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchRepotsButton.setIcon(icon3)
        self.searchRepotsButton.setObjectName("searchRepotsButton")
        self.verticalLayout_3.addWidget(self.searchRepotsButton)
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.leftSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsButton = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.settingsButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon4)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout_4.addWidget(self.settingsButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Resources/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.leftSubContainer, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("#frame_4{background-color:rgb(204, 204, 204)}")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.mainBodyContainer)
        self.widget.setObjectName("widget")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(-31, -1, 791, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.manageVendorTab = QtWidgets.QWidget()
        self.manageVendorTab.setObjectName("manageVendorTab")
        self.tabWidget.addTab(self.manageVendorTab, "")
        self.fetchReportTab = QtWidgets.QWidget()
        self.fetchReportTab.setObjectName("fetchReportTab")
        self.tabWidget.addTab(self.fetchReportTab, "")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MenuButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003d59;\">Menu</span></p></body></html>"))
        self.MenuButton.setText(_translate("MainWindow", "Menu"))
        self.manageVendorsButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003d59;\">Manage Vendors</span></p></body></html>"))
        self.manageVendorsButton.setText(_translate("MainWindow", "Manage Vendors"))
        self.FetchReportsButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003d59;\">Fetch Reports</span></p></body></html>"))
        self.FetchReportsButton.setText(_translate("MainWindow", "Fetch Reports"))
        self.searchRepotsButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003d59;\">Search</span></p></body></html>"))
        self.searchRepotsButton.setText(_translate("MainWindow", "Search"))
        self.settingsButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003d59;\">Settings</span></p></body></html>"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003d59;\">Help</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manageVendorTab), _translate("MainWindow", "Manage Vendor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fetchReportTab), _translate("MainWindow", "Fetch Reports"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
