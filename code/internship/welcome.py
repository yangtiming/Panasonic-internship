# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Openpanel(object):
    def setupUi(self, Openpanel):
        Openpanel.setObjectName("Openpanel")
        Openpanel.resize(800, 480)
        Openpanel.setMinimumSize(QtCore.QSize(800, 480))
        Openpanel.setMaximumSize(QtCore.QSize(800, 480))
        Openpanel.setStyleSheet("#Openpanel{border-image: url(:/lay/welcome.PNG);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Openpanel)
        self.centralwidget.setObjectName("centralwidget")
        self.PowerOffBt = QtWidgets.QPushButton(self.centralwidget)
        self.PowerOffBt.setGeometry(QtCore.QRect(300, 350, 200, 40))
        self.PowerOffBt.setMinimumSize(QtCore.QSize(200, 40))
        self.PowerOffBt.setMaximumSize(QtCore.QSize(200, 40))
        self.PowerOffBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 13pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);")
        self.PowerOffBt.setFlat(False)
        self.PowerOffBt.setObjectName("PowerOffBt")
        self.RecogBt = QtWidgets.QPushButton(self.centralwidget)
        self.RecogBt.setGeometry(QtCore.QRect(300, 290, 200, 40))
        self.RecogBt.setMinimumSize(QtCore.QSize(200, 40))
        self.RecogBt.setMaximumSize(QtCore.QSize(200, 40))
        self.RecogBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 13pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);")
        self.RecogBt.setFlat(False)
        self.RecogBt.setObjectName("RecogBt")
        self.LoginBt = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBt.setGeometry(QtCore.QRect(300, 230, 200, 40))
        self.LoginBt.setMinimumSize(QtCore.QSize(200, 40))
        self.LoginBt.setMaximumSize(QtCore.QSize(200, 40))
        self.LoginBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 13pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);")
        self.LoginBt.setFlat(False)
        self.LoginBt.setObjectName("LoginBt")
        Openpanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Openpanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Openpanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Openpanel)
        self.statusbar.setObjectName("statusbar")
        Openpanel.setStatusBar(self.statusbar)

        self.retranslateUi(Openpanel)
        QtCore.QMetaObject.connectSlotsByName(Openpanel)

    def retranslateUi(self, Openpanel):
        _translate = QtCore.QCoreApplication.translate
        Openpanel.setWindowTitle(_translate("Openpanel", "神荼系统"))
        self.PowerOffBt.setText(_translate("Openpanel", "关机"))
        self.RecogBt.setText(_translate("Openpanel", "主界面"))
        self.LoginBt.setText(_translate("Openpanel", "登录"))
import welcome_rc