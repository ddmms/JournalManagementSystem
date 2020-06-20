# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instock_registration.ui'
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
        self.headLine = QtWidgets.QLabel(self.centralwidget)
        self.headLine.setGeometry(QtCore.QRect(280, 20, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.operation_set = QtWidgets.QSplitter(self.centralwidget)
        self.operation_set.setGeometry(QtCore.QRect(210, 410, 281, 23))
        self.operation_set.setOrientation(QtCore.Qt.Horizontal)
        self.operation_set.setHandleWidth(60)
        self.operation_set.setObjectName("operation_set")
        self.submit_btn = QtWidgets.QPushButton(self.operation_set)
        self.submit_btn.setObjectName("submit_btn")
        self.clear_btn = QtWidgets.QPushButton(self.operation_set)
        self.clear_btn.setObjectName("clear_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(60, 410, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.new_instock = QtWidgets.QTableWidget(self.centralwidget)
        self.new_instock.setGeometry(QtCore.QRect(50, 80, 621, 311))
        self.new_instock.setRowCount(15)
        self.new_instock.setObjectName("new_instock")
        self.new_instock.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.new_instock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_instock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_instock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.new_instock.setHorizontalHeaderItem(3, item)
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.return_btn.setObjectName("return_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear_btn.clicked.connect(self.new_instock.clearContents)
        self.return_btn.clicked.connect(MainWindow.Return)
        self.submit_btn.clicked.connect(MainWindow.Submit)
        self.add_btn.clicked.connect(MainWindow.AddLine)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headLine.setText(_translate("MainWindow", "期刊入库登记"))
        self.submit_btn.setText(_translate("MainWindow", "提交"))
        self.clear_btn.setText(_translate("MainWindow", "清空"))
        self.add_btn.setText(_translate("MainWindow", "添加"))
        item = self.new_instock.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期刊名称"))
        item = self.new_instock.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "年"))
        item = self.new_instock.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "卷"))
        item = self.new_instock.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "期"))
        self.return_btn.setText(_translate("MainWindow", "返回"))
