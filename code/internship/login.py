# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/lay/login.PNG);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(330, 310))
        self.frame.setMaximumSize(QtCore.QSize(600, 415))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(350, 130, 70, 30))
        self.label.setMinimumSize(QtCore.QSize(70, 30))
        self.label.setMaximumSize(QtCore.QSize(70, 45))
        self.label.setStyleSheet("font: 13pt \"新宋体\";")
        self.label.setObjectName("label")
        self.keywrongshow = QtWidgets.QLineEdit(self.frame)
        self.keywrongshow.setGeometry(QtCore.QRect(400, 250, 200, 30))
        self.keywrongshow.setMinimumSize(QtCore.QSize(200, 30))
        self.keywrongshow.setMaximumSize(QtCore.QSize(200, 45))
        self.keywrongshow.setStyleSheet("border:none\n"
"")
        self.keywrongshow.setAlignment(QtCore.Qt.AlignCenter)
        self.keywrongshow.setReadOnly(True)
        self.keywrongshow.setObjectName("keywrongshow")
        self.LoginOKBt = QtWidgets.QPushButton(self.frame)
        self.LoginOKBt.setGeometry(QtCore.QRect(400, 300, 80, 40))
        self.LoginOKBt.setMinimumSize(QtCore.QSize(80, 40))
        self.LoginOKBt.setMaximumSize(QtCore.QSize(80, 60))
        self.LoginOKBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);")
        self.LoginOKBt.setObjectName("LoginOKBt")
        self.keybox = QtWidgets.QLineEdit(self.frame)
        self.keybox.setGeometry(QtCore.QRect(420, 190, 180, 30))
        self.keybox.setMinimumSize(QtCore.QSize(180, 30))
        self.keybox.setMaximumSize(QtCore.QSize(300, 45))
        self.keybox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keybox.setObjectName("keybox")
        self.LoginReturnBt = QtWidgets.QPushButton(self.frame)
        self.LoginReturnBt.setGeometry(QtCore.QRect(520, 300, 80, 40))
        self.LoginReturnBt.setMinimumSize(QtCore.QSize(80, 40))
        self.LoginReturnBt.setMaximumSize(QtCore.QSize(80, 60))
        self.LoginReturnBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);")
        self.LoginReturnBt.setObjectName("LoginReturnBt")
        self.RegistLink = QtWidgets.QCommandLinkButton(self.frame)
        self.RegistLink.setGeometry(QtCore.QRect(450, 350, 150, 60))
        self.RegistLink.setMinimumSize(QtCore.QSize(150, 40))
        self.RegistLink.setMaximumSize(QtCore.QSize(150, 60))
        self.RegistLink.setStyleSheet("font: 6pt \"Agency FB\";")
        self.RegistLink.setObjectName("RegistLink")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 70, 30))
        self.label_2.setMinimumSize(QtCore.QSize(70, 30))
        self.label_2.setMaximumSize(QtCore.QSize(70, 45))
        self.label_2.setStyleSheet("font: 13pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        self.accountbox = QtWidgets.QLineEdit(self.frame)
        self.accountbox.setGeometry(QtCore.QRect(420, 130, 180, 30))
        self.accountbox.setMinimumSize(QtCore.QSize(180, 30))
        self.accountbox.setMaximumSize(QtCore.QSize(300, 45))
        self.accountbox.setObjectName("accountbox")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "神荼系统"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.LoginOKBt.setText(_translate("MainWindow", "登录"))
        self.LoginReturnBt.setText(_translate("MainWindow", "取消"))
        self.RegistLink.setText(_translate("MainWindow", "没有账号？立即注册"))
        self.label_2.setText(_translate("MainWindow", "密码"))

import trainmark_rc
