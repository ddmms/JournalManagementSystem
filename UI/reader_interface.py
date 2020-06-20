# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 90, 179, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.info = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.info.setContentsMargins(0, 0, 0, 0)
        self.info.setObjectName("info")
        self.mode_info = QtWidgets.QLabel(self.layoutWidget)
        self.mode_info.setObjectName("mode_info")
        self.info.addWidget(self.mode_info)
        self.logout = QtWidgets.QPushButton(self.layoutWidget)
        self.logout.setObjectName("logout")
        self.info.addWidget(self.logout)
        self.headLine = QtWidgets.QLabel(self.centralwidget)
        self.headLine.setGeometry(QtCore.QRect(280, 30, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 370, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.operations = QtWidgets.QSplitter(self.centralwidget)
        self.operations.setGeometry(QtCore.QRect(120, 170, 471, 171))
        self.operations.setOrientation(QtCore.Qt.Horizontal)
        self.operations.setHandleWidth(15)
        self.operations.setObjectName("operations")
        self.journal_quiry = QtWidgets.QPushButton(self.operations)
        self.journal_quiry.setObjectName("journal_quiry")
        self.borrow_quiry = QtWidgets.QPushButton(self.operations)
        self.borrow_quiry.setObjectName("borrow_quiry")
        self.booked_quiry = QtWidgets.QPushButton(self.operations)
        self.booked_quiry.setObjectName("booked_quiry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.logout.clicked.connect(MainWindow.log_out)
        self.journal_quiry.clicked.connect(MainWindow.journal_inquiry)
        self.borrow_quiry.clicked.connect(MainWindow.borrow_inquiry)
        self.booked_quiry.clicked.connect(MainWindow.book_and_inquiry)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mode_info.setText(_translate("MainWindow", "当前模式：读者"))
        self.logout.setText(_translate("MainWindow", "退出"))
        self.headLine.setText(_translate("MainWindow", "期刊管理系统"))
        self.journal_quiry.setText(_translate("MainWindow", "我要找书"))
        self.borrow_quiry.setText(_translate("MainWindow", "我的借阅"))
        self.booked_quiry.setText(_translate("MainWindow", "我的预定"))
