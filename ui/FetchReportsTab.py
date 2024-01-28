# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FetchReportsTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FetchReports(object):
    def setupUi(self, FetchReports):
        FetchReports.setObjectName("FetchReports")
        FetchReports.resize(1123, 760)
        FetchReports.setStyleSheet("*{\n"
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
"#FetchReports{\n"
"background-color:#1f232a;\n"
"}\n"
"#EditVendor{\n"
"background-color:#16191d;\n"
"}\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.gridLayout_4 = QtWidgets.QGridLayout(FetchReports)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.centralwidget = QtWidgets.QWidget(FetchReports)
        self.centralwidget.setStyleSheet("*{\n"
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
"#manage_vendor_tab{\n"
"background-color:#1f232a;\n"
"}\n"
"#EditVendor{\n"
"background-color:#16191d;\n"
"}\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("QFrame{\n"
"border: 2px solid grey ; \n"
"border-radius:15px;\n"
"\n"
"}\n"
"QPushButton{\n"
"border: 2px solid grey ;\n"
"border-radius:15px;\n"
"hover:grey\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setEnabled(True)
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lblOptions = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOptions.sizePolicy().hasHeightForWidth())
        self.lblOptions.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblOptions.setFont(font)
        self.lblOptions.setStyleSheet("QLabel{\n"
"border: none ; \n"
"}")
        self.lblOptions.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOptions.setObjectName("lblOptions")
        self.gridLayout_11.addWidget(self.lblOptions, 0, 0, 1, 1)
        self.listView_2 = QtWidgets.QListView(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_2.sizePolicy().hasHeightForWidth())
        self.listView_2.setSizePolicy(sizePolicy)
        self.listView_2.setStyleSheet("color:black;")
        self.listView_2.setMovement(QtWidgets.QListView.Static)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_11.addWidget(self.listView_2, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_6, 1, 2, 1, 1)
        self.frmDateRange = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmDateRange.sizePolicy().hasHeightForWidth())
        self.frmDateRange.setSizePolicy(sizePolicy)
        self.frmDateRange.setAutoFillBackground(False)
        self.frmDateRange.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDateRange.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDateRange.setObjectName("frmDateRange")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frmDateRange)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lblEndDate = QtWidgets.QLabel(self.frmDateRange)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.lblEndDate.setFont(font)
        self.lblEndDate.setStyleSheet("QLabel{\n"
"border: none ; \n"
"}")
        self.lblEndDate.setObjectName("lblEndDate")
        self.gridLayout_10.addWidget(self.lblEndDate, 2, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.lblBeginDate = QtWidgets.QLabel(self.frmDateRange)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.lblBeginDate.setFont(font)
        self.lblBeginDate.setStyleSheet("QLabel{\n"
"border: none ; \n"
"}")
        self.lblBeginDate.setObjectName("lblBeginDate")
        self.gridLayout_10.addWidget(self.lblBeginDate, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.dateedit1_2 = QtWidgets.QDateEdit(self.frmDateRange)
        self.dateedit1_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateedit1_2.sizePolicy().hasHeightForWidth())
        self.dateedit1_2.setSizePolicy(sizePolicy)
        self.dateedit1_2.setStyleSheet("color:black; font-size:15;")
        self.dateedit1_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 4, 5), QtCore.QTime(0, 0, 0)))
        self.dateedit1_2.setDisplayFormat("yyyy-mm")
        self.dateedit1_2.setCalendarPopup(False)
        self.dateedit1_2.setDate(QtCore.QDate(2023, 4, 5))
        self.dateedit1_2.setObjectName("dateedit1_2")
        self.gridLayout_10.addWidget(self.dateedit1_2, 1, 1, 1, 1)
        self.dateedit1_3 = QtWidgets.QDateEdit(self.frmDateRange)
        self.dateedit1_3.setStyleSheet("color:black;")
        self.dateedit1_3.setCalendarPopup(False)
        self.dateedit1_3.setDate(QtCore.QDate(2024, 1, 1))
        self.dateedit1_3.setObjectName("dateedit1_3")
        self.gridLayout_10.addWidget(self.dateedit1_3, 2, 1, 1, 1)
        self.lblFetchAllReport_4 = QtWidgets.QLabel(self.frmDateRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFetchAllReport_4.sizePolicy().hasHeightForWidth())
        self.lblFetchAllReport_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblFetchAllReport_4.setFont(font)
        self.lblFetchAllReport_4.setAutoFillBackground(False)
        self.lblFetchAllReport_4.setStyleSheet("border:none")
        self.lblFetchAllReport_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFetchAllReport_4.setObjectName("lblFetchAllReport_4")
        self.gridLayout_10.addWidget(self.lblFetchAllReport_4, 0, 0, 1, 2, QtCore.Qt.AlignTop)
        self.gridLayout_7.addWidget(self.frmDateRange, 0, 2, 1, 1)
        self.frmSelectVenders = QtWidgets.QFrame(self.frame_2)
        self.frmSelectVenders.setAutoFillBackground(False)
        self.frmSelectVenders.setStyleSheet("QFrame{\n"
"border: 2px solid grey ; \n"
"}")
        self.frmSelectVenders.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmSelectVenders.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmSelectVenders.setObjectName("frmSelectVenders")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frmSelectVenders)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblFetchAllReport_3 = QtWidgets.QLabel(self.frmSelectVenders)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblFetchAllReport_3.setFont(font)
        self.lblFetchAllReport_3.setAutoFillBackground(False)
        self.lblFetchAllReport_3.setStyleSheet("border:none")
        self.lblFetchAllReport_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFetchAllReport_3.setObjectName("lblFetchAllReport_3")
        self.gridLayout_6.addWidget(self.lblFetchAllReport_3, 0, 0, 1, 2)
        self.listView = QtWidgets.QListView(self.frmSelectVenders)
        self.listView.setStyleSheet("color:black;")
        self.listView.setObjectName("listView")
        self.gridLayout_6.addWidget(self.listView, 2, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frmSelectVenders)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("text-align:center;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frmSelectVenders)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("text-align:center;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frmSelectVenders, 0, 0, 2, 1)
        self.frmSelectReportType = QtWidgets.QFrame(self.frame_2)
        self.frmSelectReportType.setAutoFillBackground(False)
        self.frmSelectReportType.setStyleSheet("QFrame{\n"
"border: 2px solid grey ; \n"
"}")
        self.frmSelectReportType.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmSelectReportType.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmSelectReportType.setObjectName("frmSelectReportType")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frmSelectReportType)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.frmSelectReportType)
        self.frame_8.setStyleSheet("border:none")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:2px solid grey;\n"
"text-align:center;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_8.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 2, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.frmSelectReportType)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_13.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_13.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_13.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_13.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("text-align:center;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_13.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("text-align:center;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_13.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.frame_5, 1, 0, 1, 2)
        self.lblFetchAllReport_5 = QtWidgets.QLabel(self.frmSelectReportType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFetchAllReport_5.sizePolicy().hasHeightForWidth())
        self.lblFetchAllReport_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblFetchAllReport_5.setFont(font)
        self.lblFetchAllReport_5.setAutoFillBackground(False)
        self.lblFetchAllReport_5.setStyleSheet("border:none")
        self.lblFetchAllReport_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFetchAllReport_5.setObjectName("lblFetchAllReport_5")
        self.gridLayout_9.addWidget(self.lblFetchAllReport_5, 0, 0, 1, 2)
        self.frame_9 = QtWidgets.QFrame(self.frmSelectReportType)
        self.frame_9.setStyleSheet("b")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(1)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"border:none;\n"
" }\n"
" ")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit.setStyleSheet("color:black;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_12.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("text-align:center;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_9, 4, 0, 1, 2)
        self.btnFetchSelectedReports = QtWidgets.QPushButton(self.frmSelectReportType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFetchSelectedReports.sizePolicy().hasHeightForWidth())
        self.btnFetchSelectedReports.setSizePolicy(sizePolicy)
        self.btnFetchSelectedReports.setMinimumSize(QtCore.QSize(300, 0))
        self.btnFetchSelectedReports.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.btnFetchSelectedReports.setFont(font)
        self.btnFetchSelectedReports.setStyleSheet("QPushButton{\n"
"border:3px solid grey;\n"
"border-color:grey;\n"
"text-align:center;\n"
"border-radius:15px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"}")
        self.btnFetchSelectedReports.setObjectName("btnFetchSelectedReports")
        self.gridLayout_9.addWidget(self.btnFetchSelectedReports, 6, 0, 1, 2)
        self.gridLayout_7.addWidget(self.frmSelectReportType, 0, 1, 2, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 4, 0, 1, 1)
        self.lblAdvanceFetchReport = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lblAdvanceFetchReport.setFont(font)
        self.lblAdvanceFetchReport.setAutoFillBackground(False)
        self.lblAdvanceFetchReport.setStyleSheet("QLabel{\n"
"border:2px solid grey;\n"
" border:none;}")
        self.lblAdvanceFetchReport.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAdvanceFetchReport.setObjectName("lblAdvanceFetchReport")
        self.gridLayout_3.addWidget(self.lblAdvanceFetchReport, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("QFrame{\n"
"border:2px solid grey;\n"
"border-radius:15px;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblYear = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lblYear.setFont(font)
        self.lblYear.setStyleSheet("QLabel{\n"
"border: none ; \n"
"alignment: AlignCenter;\n"
"\n"
"}")
        self.lblYear.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblYear.setObjectName("lblYear")
        self.horizontalLayout.addWidget(self.lblYear)
        self.All_reports_edit_fetch = QtWidgets.QDateEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.All_reports_edit_fetch.sizePolicy().hasHeightForWidth())
        self.All_reports_edit_fetch.setSizePolicy(sizePolicy)
        self.All_reports_edit_fetch.setStyleSheet("color:black;")
        self.All_reports_edit_fetch.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.All_reports_edit_fetch.setObjectName("All_reports_edit_fetch")
        self.horizontalLayout.addWidget(self.All_reports_edit_fetch)
        self.btnFetchAllReport = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.btnFetchAllReport.setFont(font)
        self.btnFetchAllReport.setStyleSheet("text-align:center;")
        self.btnFetchAllReport.setObjectName("btnFetchAllReport")
        self.horizontalLayout.addWidget(self.btnFetchAllReport)
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.centralwidget, 0, 0, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(FetchReports)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 21))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(FetchReports)
        QtCore.QMetaObject.connectSlotsByName(FetchReports)

    def retranslateUi(self, FetchReports):
        _translate = QtCore.QCoreApplication.translate
        FetchReports.setWindowTitle(_translate("FetchReports", "MainWindow"))
        self.lblOptions.setText(_translate("FetchReports", "Select Standard View"))
        self.lblEndDate.setText(_translate("FetchReports", "End Date"))
        self.lblBeginDate.setText(_translate("FetchReports", "Begin Date"))
        self.dateedit1_3.setDisplayFormat(_translate("FetchReports", "yyyy-mm"))
        self.lblFetchAllReport_4.setText(_translate("FetchReports", "Date Range"))
        self.lblFetchAllReport_3.setText(_translate("FetchReports", "Select Vendors"))
        self.pushButton_4.setText(_translate("FetchReports", "Deselect All"))
        self.pushButton_3.setText(_translate("FetchReports", "Select All"))
        self.pushButton_2.setText(_translate("FetchReports", "Select more options"))
        self.checkBox_3.setText(_translate("FetchReports", "DR"))
        self.checkBox_2.setText(_translate("FetchReports", "TR"))
        self.checkBox.setText(_translate("FetchReports", "PR"))
        self.checkBox_4.setText(_translate("FetchReports", "IR"))
        self.pushButton_5.setText(_translate("FetchReports", "Select all"))
        self.pushButton_6.setText(_translate("FetchReports", "Deselect all "))
        self.lblFetchAllReport_5.setText(_translate("FetchReports", "Select Report Types"))
        self.label_2.setText(_translate("FetchReports", "Report(s) will be saved to:"))
        self.pushButton.setText(_translate("FetchReports", "Browse"))
        self.btnFetchSelectedReports.setText(_translate("FetchReports", "Fetch Selected Reports"))
        self.lblAdvanceFetchReport.setText(_translate("FetchReports", "Advanced Fetch Reports"))
        self.label.setText(_translate("FetchReports", "Fetch Report"))
        self.lblYear.setText(_translate("FetchReports", "Year"))
        self.All_reports_edit_fetch.setDisplayFormat(_translate("FetchReports", "yyyy"))
        self.btnFetchAllReport.setText(_translate("FetchReports", "Fetch All Reports"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FetchReports = QtWidgets.QWidget()
    ui = Ui_FetchReports()
    ui.setupUi(FetchReports)
    FetchReports.show()
    sys.exit(app.exec_())
