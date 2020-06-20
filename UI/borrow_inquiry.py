# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow_inquiry.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headLine = QtWidgets.QLabel(self.centralwidget)
        self.headLine.setGeometry(QtCore.QRect(300, 30, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.return_btn.setObjectName("return_btn")
        self.borrow_result = QtWidgets.QTableWidget(self.centralwidget)
        self.borrow_result.setGeometry(QtCore.QRect(80, 120, 601, 331))
        self.borrow_result.setObjectName("borrow_result")
        self.borrow_result.setColumnCount(6)
        self.borrow_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrow_result.setHorizontalHeaderItem(5, item)
        self.notReturnOnly = QtWidgets.QCheckBox(self.centralwidget)
        self.notReturnOnly.setGeometry(QtCore.QRect(80, 90, 111, 16))
        self.notReturnOnly.setObjectName("notReturnOnly")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.return_btn.clicked.connect(MainWindow.Return)
        self.notReturnOnly.clicked.connect(MainWindow.SiftNotReturn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headLine.setText(_translate("MainWindow", "我的借阅"))
        self.return_btn.setText(_translate("MainWindow", "返回"))
        item = self.borrow_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期刊名称"))
        item = self.borrow_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "年"))
        item = self.borrow_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "卷"))
        item = self.borrow_result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "期"))
        item = self.borrow_result.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "借阅时间"))
        item = self.borrow_result.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "是否归还"))
        self.notReturnOnly.setText(_translate("MainWindow", "只显示未归还"))
