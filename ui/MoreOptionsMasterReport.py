from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MoreOptionsDialog(object):
    def setupUi(self, MoreOptionsDialog):
        MoreOptionsDialog.setObjectName("MoreOptionsDialog")
        MoreOptionsDialog.resize(401, 511)
        MoreOptionsDialog.setMinimumSize(QtCore.QSize(300, 0))
        MoreOptionsDialog.setStyleSheet("QMainWindow{\n"
                                        "background-color: #323232;\n"
                                        "color: white;\n"
                                        "}")
        self.centralwidget = QtWidgets.QWidget(MoreOptionsDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 9, 401, 490))
        self.verticalFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.options_frame_main = QtWidgets.QFrame(self.verticalFrame)
        self.options_frame_main.setObjectName("options_frame_main")
        self.options_frame_main.setStyleSheet("color: white;")
        self.options_frame = QtWidgets.QGridLayout(self.options_frame_main)
        self.options_frame.setObjectName("options_frame")
        self.verticalLayout.addWidget(self.options_frame_main, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalFrame)
        self.buttonBox.setStyleSheet("color: white;")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        # Setting the text color for the cancel button to black
        cancel_button = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
        cancel_button.setStyleSheet("color: black;")
        MoreOptionsDialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(MoreOptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(MoreOptionsDialog)

    def retranslateUi(self, MoreOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        MoreOptionsDialog.setWindowTitle(_translate("MoreOptionsDialog", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MoreOptionsDialog = QtWidgets.QMainWindow()
    ui = Ui_MoreOptionsDialog()
    ui.setupUi(MoreOptionsDialog)
    MoreOptionsDialog.show()
    sys.exit(app.exec_())
