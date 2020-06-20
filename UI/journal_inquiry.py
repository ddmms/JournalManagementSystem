# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'journal_inquiry.ui'
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
        self.headLine.setGeometry(QtCore.QRect(310, 40, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.return_btn.setObjectName("return_btn")
        self.result = QtWidgets.QTableWidget(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(70, 160, 591, 301))
        self.result.setObjectName("result")
        self.result.setColumnCount(7)
        self.result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result.setHorizontalHeaderItem(6, item)
        self.operation = QtWidgets.QSplitter(self.centralwidget)
        self.operation.setGeometry(QtCore.QRect(90, 120, 321, 23))
        self.operation.setOrientation(QtCore.Qt.Horizontal)
        self.operation.setObjectName("operation")
        self.keywordLabel = QtWidgets.QLabel(self.operation)
        self.keywordLabel.setObjectName("keywordLabel")
        self.input_keyword = QtWidgets.QLineEdit(self.operation)
        self.input_keyword.setObjectName("input_keyword")
        self.quiry_btn = QtWidgets.QPushButton(self.operation)
        self.quiry_btn.setObjectName("quiry_btn")
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
        self.quiry_btn.clicked.connect(MainWindow.Search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headLine.setText(_translate("MainWindow", "期刊查询"))
        self.return_btn.setText(_translate("MainWindow", "返回"))
        item = self.result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期刊名称"))
        item = self.result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "年"))
        item = self.result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "卷"))
        item = self.result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "期"))
        item = self.result.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "相关论文"))
        item = self.result.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "作者"))
        item = self.result.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "页码"))
        self.keywordLabel.setText(_translate("MainWindow", "关键字"))
        self.input_keyword.setPlaceholderText(_translate("MainWindow", "请输入关键字"))
        self.quiry_btn.setText(_translate("MainWindow", "查询"))
