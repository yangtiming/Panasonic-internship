# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 925)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddNameBt = QtWidgets.QPushButton(self.centralwidget)
        self.AddNameBt.setGeometry(QtCore.QRect(170, 100, 141, 23))
        self.AddNameBt.setObjectName("AddNameBt")
        self.ApiLoginBt = QtWidgets.QPushButton(self.centralwidget)
        self.ApiLoginBt.setGeometry(QtCore.QRect(170, 150, 131, 23))
        self.ApiLoginBt.setObjectName("ApiLoginBt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 22))
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
        self.AddNameBt.setText(_translate("MainWindow", "二维码名字增加"))
        self.ApiLoginBt.setText(_translate("MainWindow", "百度API"))

