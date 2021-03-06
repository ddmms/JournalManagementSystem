# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow_registration.ui'
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
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.return_btn.setObjectName("return_btn")
        self.headLine = QtWidgets.QLabel(self.centralwidget)
        self.headLine.setGeometry(QtCore.QRect(310, 50, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 130, 231, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.reader_no = QtWidgets.QLineEdit(self.layoutWidget)
        self.reader_no.setObjectName("reader_no")
        self.gridLayout.addWidget(self.reader_no, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.journal_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.journal_name.setObjectName("journal_name")
        self.gridLayout.addWidget(self.journal_name, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.borrow_date = QtWidgets.QDateEdit(self.layoutWidget)
        self.borrow_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.borrow_date.setCalendarPopup(True)
        self.borrow_date.setObjectName("borrow_date")
        self.gridLayout.addWidget(self.borrow_date, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.return_date = QtWidgets.QDateEdit(self.layoutWidget)
        self.return_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.return_date.setCalendarPopup(True)
        self.return_date.setObjectName("return_date")
        self.gridLayout.addWidget(self.return_date, 3, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(240, 370, 225, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.submit_btn = QtWidgets.QPushButton(self.splitter)
        self.submit_btn.setObjectName("submit_btn")
        self.clear_btn_2 = QtWidgets.QPushButton(self.splitter)
        self.clear_btn_2.setObjectName("clear_btn_2")
        self.clear_btn = QtWidgets.QPushButton(self.splitter)
        self.clear_btn.setObjectName("clear_btn")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(410, 190, 261, 20))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setObjectName("label_5")
        self.year = QtWidgets.QSpinBox(self.splitter_2)
        self.year.setMinimum(1949)
        self.year.setMaximum(2020)
        self.year.setObjectName("year")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        self.label_6.setObjectName("label_6")
        self.volume = QtWidgets.QSpinBox(self.splitter_2)
        self.volume.setMinimum(1)
        self.volume.setMaximum(100)
        self.volume.setObjectName("volume")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        self.label_7.setObjectName("label_7")
        self.number = QtWidgets.QSpinBox(self.splitter_2)
        self.number.setMinimum(1)
        self.number.setMaximum(100)
        self.number.setObjectName("number")
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
        self.clear_btn.clicked.connect(self.reader_no.clear)
        self.clear_btn.clicked.connect(self.journal_name.clear)
        self.clear_btn_2.clicked.connect(MainWindow.Return_regis)
        self.submit_btn.clicked.connect(MainWindow.Borrow_regis)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_btn.setText(_translate("MainWindow", "返回"))
        self.headLine.setText(_translate("MainWindow", "借阅登记"))
        self.label.setText(_translate("MainWindow", "读者号  "))
        self.reader_no.setPlaceholderText(_translate("MainWindow", "请输入读者号"))
        self.label_2.setText(_translate("MainWindow", "期刊名称  "))
        self.journal_name.setPlaceholderText(_translate("MainWindow", "请输入期刊号"))
        self.label_3.setText(_translate("MainWindow", "借阅时间"))
        self.label_4.setText(_translate("MainWindow", "归还时间"))
        self.submit_btn.setText(_translate("MainWindow", "借阅"))
        self.clear_btn_2.setText(_translate("MainWindow", "归还"))
        self.clear_btn.setText(_translate("MainWindow", "清空"))
        self.label_5.setText(_translate("MainWindow", "年"))
        self.label_6.setText(_translate("MainWindow", "卷"))
        self.label_7.setText(_translate("MainWindow", "期"))
