# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'journal_whereabouts.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.return_btn.setObjectName("return_btn")
        self.headLine = QtWidgets.QLabel(self.centralwidget)
        self.headLine.setGeometry(QtCore.QRect(280, 30, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.whereabouts_result = QtWidgets.QTableWidget(self.centralwidget)
        self.whereabouts_result.setGeometry(QtCore.QRect(50, 130, 621, 331))
        self.whereabouts_result.setObjectName("whereabouts_result")
        self.whereabouts_result.setColumnCount(5)
        self.whereabouts_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.whereabouts_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.whereabouts_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.whereabouts_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.whereabouts_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.whereabouts_result.setHorizontalHeaderItem(4, item)
        self.operation = QtWidgets.QSplitter(self.centralwidget)
        self.operation.setGeometry(QtCore.QRect(50, 90, 291, 23))
        self.operation.setOrientation(QtCore.Qt.Horizontal)
        self.operation.setObjectName("operation")
        self.label = QtWidgets.QLabel(self.operation)
        self.label.setObjectName("label")
        self.journal_no = QtWidgets.QLineEdit(self.operation)
        self.journal_no.setObjectName("journal_no")
        self.inquiry_btn = QtWidgets.QPushButton(self.operation)
        self.inquiry_btn.setObjectName("inquiry_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.return_btn.clicked.connect(MainWindow.Return)
        self.inquiry_btn.clicked.connect(MainWindow.Search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_btn.setText(_translate("MainWindow", "返回"))
        self.headLine.setText(_translate("MainWindow", "期刊去向查询"))
        item = self.whereabouts_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "读者号"))
        item = self.whereabouts_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "读者名"))
        item = self.whereabouts_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "借阅天数"))
        item = self.whereabouts_result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "借阅时间"))
        item = self.whereabouts_result.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "归还时间"))
        self.label.setText(_translate("MainWindow", "期刊号"))
        self.journal_no.setPlaceholderText(_translate("MainWindow", "请输入期刊号"))
        self.inquiry_btn.setText(_translate("MainWindow", "查询"))
