# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddVendor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 876)
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
"\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"border-botton-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"\n"
"QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame_3)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout_6.addWidget(self.openGLWidget, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("text-align:centre;")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.AddNewVendor = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        self.AddNewVendor.setFont(font)
        self.AddNewVendor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddNewVendor.setObjectName("AddNewVendor")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.AddNewVendor)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)
        self.name_validation_label = QtWidgets.QLabel(self.AddNewVendor)
        self.name_validation_label.setObjectName("name_validation_label")
        self.gridLayout_5.addWidget(self.name_validation_label, 1, 1, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.nameEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_5.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.customerIdEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.customerIdEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.customerIdEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.customerIdEdit.setObjectName("customerIdEdit")
        self.gridLayout_5.addWidget(self.customerIdEdit, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)
        self.All_reports_edit_fetch = QtWidgets.QDateEdit(self.AddNewVendor)
        self.All_reports_edit_fetch.setEnabled(True)
        self.All_reports_edit_fetch.setMinimumSize(QtCore.QSize(0, 30))
        self.All_reports_edit_fetch.setStyleSheet("QDateEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.All_reports_edit_fetch.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.All_reports_edit_fetch.setObjectName("All_reports_edit_fetch")
        self.gridLayout_5.addWidget(self.All_reports_edit_fetch, 3, 1, 1, 1)
        self.apiKeyEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.apiKeyEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.apiKeyEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.apiKeyEdit.setObjectName("apiKeyEdit")
        self.gridLayout_5.addWidget(self.apiKeyEdit, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 7, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.AddNewVendor)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 7, 1, 1, 1)
        self.requesterIdEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.requesterIdEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.requesterIdEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.requesterIdEdit.setObjectName("requesterIdEdit")
        self.gridLayout_5.addWidget(self.requesterIdEdit, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 9, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.AddNewVendor)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 9, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 10, 0, 1, 1)
        self.notesEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesEdit.sizePolicy().hasHeightForWidth())
        self.notesEdit.setSizePolicy(sizePolicy)
        self.notesEdit.setMinimumSize(QtCore.QSize(339, 0))
        self.notesEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.notesEdit.setObjectName("notesEdit")
        self.gridLayout_5.addWidget(self.notesEdit, 10, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.AddNewVendor)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 8, 1, 1, 1)
        self.companiesText = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.companiesText.setFont(font)
        self.companiesText.setObjectName("companiesText")
        self.gridLayout_5.addWidget(self.companiesText, 12, 0, 1, 1)
        self.providerEdit = QtWidgets.QLineEdit(self.AddNewVendor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.providerEdit.sizePolicy().hasHeightForWidth())
        self.providerEdit.setSizePolicy(sizePolicy)
        self.providerEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #cccccc;\n"
"    border-radius: 20px; \n"
"}\n"
"")
        self.providerEdit.setObjectName("providerEdit")
        self.gridLayout_5.addWidget(self.providerEdit, 12, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.AddNewVendor)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 8, 0, 1, 1)
        self.gridLayout_6.addWidget(self.AddNewVendor, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-color: rgb(226, 226, 226);")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_6.addWidget(self.buttonBox, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Add New Vendor"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Customer ID"))
        self.name_validation_label.setText(_translate("MainWindow", "Validation label"))
        self.label_2.setText(_translate("MainWindow", "Base URL"))
        self.label_10.setText(_translate("MainWindow", "Starting Year"))
        self.All_reports_edit_fetch.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.label_8.setText(_translate("MainWindow", "2 Attempts needed"))
        self.label_4.setText(_translate("MainWindow", "Requester ID"))
        self.label_5.setText(_translate("MainWindow", "API Key"))
        self.label_11.setText(_translate("MainWindow", "Request throttled"))
        self.label_28.setText(_translate("MainWindow", "Notes"))
        self.companiesText.setText(_translate("MainWindow", "Provider"))
        self.label_9.setText(_translate("MainWindow", "IP Checking required"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())