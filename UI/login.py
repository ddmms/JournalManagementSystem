# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        self.headLine.setGeometry(QtCore.QRect(270, 80, 171, 41))
        self.headLine.setStyleSheet("font: 75 18pt \"微软雅黑\";")
        self.headLine.setObjectName("headLine")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 180, 20, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.failureTip = QtWidgets.QLabel(self.centralwidget)
        self.failureTip.setGeometry(QtCore.QRect(360, 340, 241, 21))
        self.failureTip.setText("")
        self.failureTip.setObjectName("failureTip")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 180, 131, 141))
        self.label.setStyleSheet("font: 20pt \"幼圆\";\n"
"background-color: rgb(170, 255, 255);")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 180, 241, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.login_region = QtWidgets.QFormLayout(self.layoutWidget)
        self.login_region.setContentsMargins(0, 10, 0, 10)
        self.login_region.setVerticalSpacing(15)
        self.login_region.setObjectName("login_region")
        self.accountLabel = QtWidgets.QLabel(self.layoutWidget)
        self.accountLabel.setObjectName("accountLabel")
        self.login_region.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.accountLabel)
        self.accountInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.accountInput.setObjectName("accountInput")
        self.login_region.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.accountInput)
        self.passwordLabel = QtWidgets.QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.login_region.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordInput.setInputMask("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.login_region.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.reader_select = QtWidgets.QRadioButton(self.layoutWidget)
        self.reader_select.setObjectName("reader_select")
        self.login_region.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.reader_select)
        self.admin_select = QtWidgets.QRadioButton(self.layoutWidget)
        self.admin_select.setObjectName("admin_select")
        self.login_region.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.admin_select)
        self.login_button = QtWidgets.QPushButton(self.layoutWidget)
        self.login_button.setObjectName("login_button")
        self.login_region.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.login_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.login_button.clicked.connect(MainWindow.show_user_interface)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headLine.setText(_translate("MainWindow", "期刊管理系统"))
        self.label.setText(_translate("MainWindow", "欢迎登录期刊管理系统"))
        self.accountLabel.setText(_translate("MainWindow", "账号  "))
        self.accountInput.setPlaceholderText(_translate("MainWindow", "请输入账号"))
        self.passwordLabel.setText(_translate("MainWindow", "密码  "))
        self.passwordInput.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.reader_select.setText(_translate("MainWindow", "读者"))
        self.admin_select.setText(_translate("MainWindow", "管理员"))
        self.login_button.setText(_translate("MainWindow", "登录"))
