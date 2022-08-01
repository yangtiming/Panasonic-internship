# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Api.ui'
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
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/lay/ApiBackground.PNG);}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FacesendBt = QtWidgets.QPushButton(self.centralwidget)
        self.FacesendBt.setGeometry(QtCore.QRect(110, 410, 120, 30))
        self.FacesendBt.setMinimumSize(QtCore.QSize(120, 30))
        self.FacesendBt.setMaximumSize(QtCore.QSize(120, 30))
        self.FacesendBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 6pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127)")
        self.FacesendBt.setObjectName("FacesendBt")
        self.GoBackBt = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBt.setGeometry(QtCore.QRect(530, 410, 120, 30))
        self.GoBackBt.setMinimumSize(QtCore.QSize(120, 30))
        self.GoBackBt.setMaximumSize(QtCore.QSize(120, 30))
        self.GoBackBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 6pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127)")
        self.GoBackBt.setObjectName("GoBackBt")
        self.DeleteBt = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBt.setGeometry(QtCore.QRect(560, 260, 130, 30))
        self.DeleteBt.setMinimumSize(QtCore.QSize(120, 30))
        self.DeleteBt.setMaximumSize(QtCore.QSize(130, 30))
        self.DeleteBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"font: 75 6pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127)")
        self.DeleteBt.setObjectName("DeleteBt")
        self.CodesendBt = QtWidgets.QPushButton(self.centralwidget)
        self.CodesendBt.setGeometry(QtCore.QRect(320, 410, 120, 30))
        self.CodesendBt.setMinimumSize(QtCore.QSize(120, 30))
        self.CodesendBt.setMaximumSize(QtCore.QSize(120, 30))
        self.CodesendBt.setStyleSheet("border-radius:10px;padding:2px 4px;\n"
"background-color: rgb(255, 170, 127);\n"
"font: 75 6pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.CodesendBt.setObjectName("CodesendBt")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(550, 120, 150, 30))
        self.name.setMinimumSize(QtCore.QSize(150, 30))
        self.name.setMaximumSize(QtCore.QSize(300, 40))
        self.name.setStyleSheet("")
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 120, 65, 30))
        self.label.setMinimumSize(QtCore.QSize(65, 30))
        self.label.setMaximumSize(QtCore.QSize(100, 40))
        self.label.setStyleSheet("font: 75 13pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 180, 65, 30))
        self.label_3.setMinimumSize(QtCore.QSize(65, 30))
        self.label_3.setMaximumSize(QtCore.QSize(100, 40))
        self.label_3.setStyleSheet("font: 75 13pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.Groupname = QtWidgets.QLineEdit(self.centralwidget)
        self.Groupname.setGeometry(QtCore.QRect(550, 180, 150, 30))
        self.Groupname.setMinimumSize(QtCore.QSize(150, 30))
        self.Groupname.setMaximumSize(QtCore.QSize(300, 40))
        self.Groupname.setStyleSheet("")
        self.Groupname.setObjectName("Groupname")
        self.CameraShow = QtWidgets.QLabel(self.centralwidget)
        self.CameraShow.setGeometry(QtCore.QRect(70, 100, 301, 201))
        self.CameraShow.setMinimumSize(QtCore.QSize(280, 180))
        self.CameraShow.setMaximumSize(QtCore.QSize(900, 650))
        self.CameraShow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 12pt \"华文中宋\";\n"
"color: rgb(255, 255, 255);")
        self.CameraShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CameraShow.setText("")
        self.CameraShow.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraShow.setObjectName("CameraShow")
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
        self.FacesendBt.setText(_translate("MainWindow", "人脸信息录入"))
        self.GoBackBt.setText(_translate("MainWindow", "返回初始界面"))
        self.DeleteBt.setText(_translate("MainWindow", "信息删除"))
        self.CodesendBt.setText(_translate("MainWindow", "健康码录入"))
        self.label.setText(_translate("MainWindow", "姓名"))
        self.label_3.setText(_translate("MainWindow", "分组"))

import welcome_rc
