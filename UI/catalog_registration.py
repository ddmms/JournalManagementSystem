# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catalog_registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headLine = QtWidgets.QLabel(self.centralwidget)
        self.headLine.setGeometry(QtCore.QRect(280, 30, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.new_catalog = QtWidgets.QTableWidget(self.centralwidget)
        self.new_catalog.setGeometry(QtCore.QRect(50, 90, 641, 311))
        self.new_catalog.setRowCount(15)
        self.new_catalog.setObjectName("new_catalog")
        self.new_catalog.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_catalog.setHorizontalHeaderItem(6, item)
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.return_btn.setObjectName("return_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(60, 420, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.operation_set = QtWidgets.QSplitter(self.centralwidget)
        self.operation_set.setGeometry(QtCore.QRect(210, 420, 281, 23))
        self.operation_set.setOrientation(QtCore.Qt.Horizontal)
        self.operation_set.setHandleWidth(60)
        self.operation_set.setObjectName("operation_set")
        self.submit_btn = QtWidgets.QPushButton(self.operation_set)
        self.submit_btn.setObjectName("submit_btn")
        self.clear_btn = QtWidgets.QPushButton(self.operation_set)
        self.clear_btn.setObjectName("clear_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear_btn.clicked.connect(self.new_catalog.clearContents)
        self.return_btn.clicked.connect(MainWindow.Return)
        self.add_btn.clicked.connect(MainWindow.AddLine)
        self.submit_btn.clicked.connect(MainWindow.Submit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headLine.setText(_translate("MainWindow", "期刊目录登记"))
        item = self.new_catalog.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期刊名称"))
        item = self.new_catalog.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ISSN"))
        item = self.new_catalog.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CN刊号"))
        item = self.new_catalog.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "邮发代号"))
        item = self.new_catalog.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "出版周期"))
        item = self.new_catalog.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "出版地"))
        item = self.new_catalog.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "主办单位"))
        self.return_btn.setText(_translate("MainWindow", "返回"))
        self.add_btn.setText(_translate("MainWindow", "添加"))
        self.submit_btn.setText(_translate("MainWindow", "提交"))
        self.clear_btn.setText(_translate("MainWindow", "清空"))
