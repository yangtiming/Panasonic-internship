from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QPixmap
import PyQt5.QtGui as QtGui
import pyzbar.pyzbar as pyzbar
import threading
import cv2
import sys
import logging as log
import datetime as dt
from aip import AipFace
import base64
import os
import time
import numpy as np
import requests
from PIL import Image

# 导入 Qt designer 设计的页面
from Systemoff import Ui_Sysoffwindow as Off_Ui
from welcome import Ui_Openpanel as Welcome_Ui
from login import Ui_MainWindow as Login_Ui
from AccountRegist import Ui_MainWindow as Regist_Ui
from Api import Ui_MainWindow as Api_Ui
from Main import Ui_MainWindow




# 关机窗口
class OffWindow(QtWidgets.QMainWindow, Off_Ui):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号

    def __init__(self):
        super(OffWindow, self).__init__()
        self.setupUi(self)
        self.OpenBt.clicked.connect(self.goWelcome)

    def goWelcome(self):
        self.switch_window1.emit()
        self.close()




# 欢迎窗口
class WelcomeWindow(QtWidgets.QMainWindow, Welcome_Ui):
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window9 = QtCore.pyqtSignal()
    switch_window10 = QtCore.pyqtSignal()

    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.LoginBt.clicked.connect(self.goLogin)
        self.PowerOffBt.clicked.connect(self.goOff)
        self.RecogBt.clicked.connect(self.rec)

    def rec(self):
        self.switch_window10.emit()
        self.close()

    def goLogin(self):
        self.switch_window2.emit()
        self.close()

    def goOff(self):
        self.switch_window3.emit()
        self.close()




#登录窗口
class LoginWindow(QtWidgets.QMainWindow, Login_Ui):
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.admin = []
        self.RegistLink.clicked.connect(self.goRegist)
        self.LoginReturnBt.clicked.connect(self.goOff)
        self.LoginOKBt.clicked.connect(self.goManage)
        self.idfile = open("account.txt")
        for line in self.idfile.readlines():
            line = line.strip("\n")
            if line != '':
                self.admin.append(line)
        self.idfile.close()
        self.turnallow = 0

    def goRegist(self):
        self.switch_window4.emit()
        self.close()

    def goOff(self):
        self.switch_window5.emit()
        self.close()

    def goManage(self):
        self.account = self.accountbox.text()
        self.key = self.keybox.text()
        for item in self.admin:
            item=eval(item)
            if self.account == item.get('account') and self.key == item.get('key'):
                self.turnallow = 1
            continue
        if self.turnallow == 1:
            self.keywrongshow.setText('登录成功')
            self.keywrongshow.setStyleSheet("color:rgb(0,170,0);\nborder:none")
            self.switch_window6.emit()
            self.close()
        else:
            self.keywrongshow.setText('账号不存在或密码错误')
            self.keywrongshow.setStyleSheet("color:rgb(255,0,0);\nborder:none")
            self.account = self.accountbox.setText('')
            self.key = self.keybox.setText('')




#注册窗口
class RegistWindow(QtWidgets.QMainWindow, Regist_Ui):
    switch_window7 = QtCore.pyqtSignal()

    def __init__(self):
        super(RegistWindow, self).__init__()
        self.setupUi(self)
        self.allaccount = list()
        self.admin = dict()
        self.NewIdBt.clicked.connect(self.NewAccount)
        # self.AccountOKBt.clicked.connect(self.accountrecord)
        self.AccountBackBt.clicked.connect(self.goOff)

    def NewAccount(self):
        self.account = self.NewAccountBox.text()
        self.key = self.NewKeyBox.text()
        self.keysure = self.SureBox.text()
        self.allowappend = 1
        self.setallow = 1
        self.idname=[]
        self.idfile = open("account.txt")
        for line in self.idfile.readlines():
            line = line.strip("\n")
            if line != '':
                self.idname.append(line)
            self.idfile.close()
        for item in self.idname:
            item = eval(item)
            if self.account == item.get('account'):
                self.setallow = 0
            continue
        if self.account == '':
            self.RegistcaseShow.setText("账号名不可为空")
            self.RegistcaseShow.setStyleSheet("color: rgb(255,0,0);\nborder:none")
        elif self.key == '':
            self.RegistcaseShow.setText("请输入密码")
            self.RegistcaseShow.setStyleSheet("color: rgb(255,0,0);\nborder:none")
        elif self.keysure == '':
            self.RegistcaseShow.setText("请确认密码")
            self.RegistcaseShow.setStyleSheet("color: rgb(255,0,0);\nborder:none")
        elif len(self.key)<7:
            self.RegistcaseShow.setText("请输入长度大于6位的密码")
            self.RegistcaseShow.setStyleSheet("color: rgb(255,0,0);\nborder:none")
            self.key = self.NewKeyBox.setText('')
            self.keysure = self.SureBox.setText('')
        elif self.key == self.keysure:
            if self.setallow == 1:
                self.RegistcaseShow.setText("账号创建成功")
                self.RegistcaseShow.setStyleSheet("color: rgb(0,170,0);\nborder:none")
                self.admin['account']=self.account
                self.admin['key']=self.key
                for item in self.allaccount:
                    if self.admin == item:
                        self.allowappend = 0
                    continue
                if self.allowappend == 1:
                    self.allaccount.append(self.admin)
                self.account = self.NewAccountBox.setText('')
                self.key = self.NewKeyBox.setText('')
                self.keysure = self.SureBox.setText('')
                self.accountrecord()
            else:
                self.RegistcaseShow.setText("账号已被创建")
                self.RegistcaseShow.setStyleSheet("color: rgb(255,0,0);\nborder:none")
                self.account = self.NewAccountBox.setText('')
                self.key = self.NewKeyBox.setText('')
                self.keysure = self.SureBox.setText('')
        else:
            self.RegistcaseShow.setText("两次输入的密码不一致，账户创建失败")
            self.RegistcaseShow.setStyleSheet("color: rgb(255,0,0);\nborder:none")
            self.account = self.NewAccountBox.setText('')
            self.key = self.NewKeyBox.setText('')
            self.keysure = self.SureBox.setText('')

    def goOff(self):
        self.switch_window7.emit()
        self.close()

    def accountrecord(self):
        self.accountfile = open("account.txt", 'a')
        self.accountfile.writelines("\n"+str(self.admin))
        self.accountfile.close()


#Api人脸数据上传窗口
class ApiWindow(QtWidgets.QMainWindow, Api_Ui):
    switch_window8 = QtCore.pyqtSignal()

    def __init__(self):
        super(ApiWindow, self).__init__()
        self.setupUi(self)
        self.GoBackBt.clicked.connect(self.goOff)
        self.FacesendBt.clicked.connect(self.enroll)
        self.DeleteBt.clicked.connect(self.Deletename)
        self.CodesendBt.clicked.connect(self.coder)
        self.video_cap = cv2.VideoCapture(0)
        self.video_cap1 = cv2.VideoCapture(1)
        self.switchnum = 0

    def goOff(self):
        self.switchnum = 1
        self.switch_window8.emit()
        if self.video_cap.isOpened():
            cv2.waitKey(1)
            self.video_cap.release()
        if self.video_cap.isOpened():
            cv2.waitKey(1)
            self.video_cap1.release()
        self.close()

    def DispImg(self):
        dst = cv2.resize(self.Image, (301, 201))
        img = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        # qimg = QtGui.QImage(img.data,img.shape[1],img.shape[0],QtGui.QImage.Format_RGB888)
        qimg = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.CameraShow.setPixmap(QPixmap.fromImage(qimg))
        self.CameraShow.show()

    def enroll(self):

        self.FacesendBt.setEnabled(False)
        self.FacesendBt.setStyleSheet("border-radius:10px;padding:2px 4px;font: 75 6pt \n\"Arial\";color: rgb(255, 255, 255);background-color: rgb(255, 170, 127)")
        """ 你的 APPID AK SK """
        APP_ID = '24575241'
        API_KEY = 'reaBGjgYwHfUjDCqc8PZcNTf'
        SECRET_KEY = 'D74au6gHiZzCjmnAcDTfLmmVXTpTn7ra'
        client = AipFace(APP_ID, API_KEY, SECRET_KEY)
        '''注册'''
        '''人脸检测图片参数传入'''
        # filepath='./2.jpg'
        def add(filepath, groupId, userId):
            with open(filepath, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            image = str(base64_data, 'utf-8')
            imageType = 'BASE64'
            ''' 调用人脸注册 '''
            result = client.addUser(image, imageType, groupId, userId);
        def changesize(x, y, w, h, betha):
            x = int(x - (w * betha - w) / 2)
            y = int(y - (h * betha - h) / 2)
            w = int(w * betha)
            h = int(h * betha)
            return x, y, w, h
        def api_baidu_add(groupId, userId):
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            anterior = 0
            count = 0
            while True:
                if self.switchnum == 1:
                    break
                if len(userId) == 0:
                    self.CameraShow.setText("名字不能为空")
                    self.FacesendBt.setEnabled(True)
                    break
                if len(groupId) == 0:
                    self.CameraShow.setText("组号不能为空")
                    self.FacesendBt.setEnabled(True)
                    break
                # Capture frame-by-frame
                ret, frame = self.video_cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.03,
                    minNeighbors=5,
                    minSize=(100, 100)
                )
                # Draw a rectangle around the faces
                big_num = 0
                big = 0
                if len(faces) == 0:
                    count = 0
                if len(faces) != 0:
                    count = count + 1
                    for i in range(len(faces)):
                        if faces[i][3] * faces[i][2] > big:
                            big = faces[i][3] * faces[i][2]
                            big_num = i
                    x = faces[big_num][0]
                    y = faces[big_num][1]
                    w = faces[big_num][2]
                    h = faces[big_num][3]
                    if ret and (count % 100 == 0):
                        # 制作缩略图
                        x, y, w, h = changesize(x, y, w, h, 1.4)
                        image = Image.fromarray(cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2RGB))
                        image.thumbnail((500, 300))
                        if not os.path.exists('./add'):
                            os.mkdir('./add')
                        imageFilePath = "./add/face" + dt.datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg";
                        image.save(imageFilePath, format='jpeg')
                        add(imageFilePath, groupId, userId)
                        self.FacesendBt.setEnabled(True)
                        return 1
                        del image
                        # del frame, ret, image
                        # break
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if anterior != len(faces):
                    anterior = len(faces)
                    log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))
                # Display the resulting frame
                self.Image = cv2.flip(frame,1)
                self.DispImg()
                cv2.waitKey(3)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.FacesendBt.setEnabled(True)
                    break
        groupId = self.Groupname.text()
        userId = self.name.text()
        self.CameraShow.setText("人脸正在录入请等待")
        cv2.waitKey(2000)
        status = api_baidu_add(groupId, userId)
        if status == 1:
            self.CameraShow.setText("录入人脸成功")
            self.FacesendBt.setEnabled(True)

    def Deletename(self):
        self.DeleteBt.setEnabled(False)
        self.DeleteBt.setStyleSheet("border-radius:10px;padding:2px 4px;font: 75 6pt \n\"Arial\";color: rgb(255, 255, 255);background-color: rgb(255, 170, 127)")
        """ 你的 APPID AK SK """
        APP_ID = '24575241'
        API_KEY = 'reaBGjgYwHfUjDCqc8PZcNTf'
        SECRET_KEY = 'D74au6gHiZzCjmnAcDTfLmmVXTpTn7ra'
        client = AipFace(APP_ID, API_KEY, SECRET_KEY)
        def api_baidu_sub(groupId, userId):
            flag_groupid=1
            flag_user=1
            if len(userId) == 0:
                self.CameraShow.setText("名字不能为空")
                flag_user=0
            if len(groupId) == 0:
                self.CameraShow.setText("组号不能为空")
                flag_groupid = 0
            if flag_user and flag_groupid:
                client.deleteUser(groupId, userId)
                self.CameraShow.setText("删除成功！")
        groupId = self.Groupname.text()
        userId = self.name.text()
        api_baidu_sub(groupId, userId)
        self.DeleteBt.setEnabled(True)

    def coder(self):

        self.CodesendBt.setEnabled(False)
        self.CodesendBt.setStyleSheet("border-radius:10px;padding:2px 4px;font: 75 6pt \n\"Arial\";color: rgb(255, 255, 255);background-color: rgb(255, 170, 127)")
        def center(x1, y1, x2, y2):
            c1_x = (x1 + x2) / 2
            c1_y = (y1 + y2) / 2
            c2_x = (c1_x + x2) / 2
            c2_y = (c1_y + y2) / 2
            c3_x = int((c2_x + x2) / 2)
            c3_y = int((c2_y + y2) / 2)
            c4_x = int((c3_x + x2) / 2)
            c4_y = int((c3_y + y2) / 2)
            return c3_x, c3_y
        def cmpHash(hash1, hash2):
            # Hash值对比
            # 算法中1和0顺序组合起来的即是图片的指纹hash。顺序不固定，但是比较的时候必须是相同的顺序。
            # 对比两幅图的指纹，计算汉明距离，即两个64位的hash值有多少是不一样的，不同的位数越小，图片越相似
            # 汉明距离：一组二进制数据变成另一组数据所需要的步骤，可以衡量两图的差异，汉明距离越小，则相似度越高。汉明距离为0，即两张图片完全一样
            n = 0
            # hash长度不同则返回-1代表传参出错
            if len(hash1) != len(hash2):
                return -1
            # 遍历判断
            for i in range(len(hash1)):
                # 不相等则n计数+1，n最终为相似度
                if hash1[i] != hash2[i]:
                    n = n + 1
            return n
        def aHash(img):
            # 均值哈希算法
            # 缩放为8*8
            img = cv2.resize(img, (8, 8))
            # 转换为灰度图
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # s为像素和初值为0，hash_str为hash值初值为''
            s = 0
            hash_str = ''
            # 遍历累加求像素和
            for i in range(8):
                for j in range(8):
                    s = s + gray[i, j]
            # 求平均灰度
            avg = s / 64
            # 灰度大于平均值为1相反为0生成图片的hash值
            for i in range(8):
                for j in range(8):
                    if gray[i, j] > avg:
                        hash_str = hash_str + '1'
                    else:
                        hash_str = hash_str + '0'
            return hash_str
        def right_dir(a, b, c, d):
            # 所需要确定位置的四个坐标
            coordinate = [a, b, c, d]  # 常规矩形坐标
            # coordinate = [[0, 1], [1, 0], [1, 2], [2, 1]]  # 非常规（菱形）矩形坐标，用以验证代码
            coordinate = np.array(coordinate)
            center = coordinate[0]
            for _ in range(1, 4):
                center = center + coordinate[_]
            center = center / 4
            coordinate_temp = coordinate.copy()  # 复制一份坐标，避免原坐标被破坏
            left_coordinate = []  # 存储x轴小于中心坐标点的点
            delete_index = []
            # 将 x轴小于中心坐标点的点 存储进left_coordinate
            for _ in range(4):
                if (coordinate[_][0] < center[0]):
                    left_coordinate.append(coordinate[_])
                    delete_index.append(_)
            # 将存储进 left_coordinate 的元素从coordinate_temp中删除
            coordinate_temp = np.delete(coordinate_temp, delete_index, axis=0)
            left_coordinate_temp = left_coordinate.copy()  # 避免程序过程因为left_coordinate的变动而导致最初的条件判断错误
            if (len(left_coordinate_temp) == 2):
                # 比较左边两个点的y轴，大的为左上
                if (left_coordinate[0][1] < left_coordinate[1][1]):
                    left_bottom = left_coordinate[0]
                    left_top = left_coordinate[1]
                elif (left_coordinate[0][1] > left_coordinate[1][1]):
                    left_bottom = left_coordinate[1]
                    left_top = left_coordinate[0]
                # 比较右边两个点的y轴，大的为右上
                if (coordinate_temp[0][1] < coordinate_temp[1][1]):
                    right_bottom = coordinate_temp[0]
                    right_top = coordinate_temp[1]
                elif (coordinate_temp[0][1] > coordinate_temp[1][1]):
                    right_bottom = coordinate_temp[1]
                    right_top = coordinate_temp[0]
            elif (len(left_coordinate_temp) == 1):
                left_bottom = left_coordinate[0]
                delete_index = []
                for _ in range(3):
                    if (coordinate_temp[_][0] == center[0] and coordinate_temp[_][1] > center[1]):
                        left_top = coordinate_temp[_]
                        delete_index.append(_)
                    if (coordinate_temp[_][0] == center[0] and coordinate_temp[_][1] < center[1]):
                        right_bottom = coordinate_temp[_]
                        delete_index.append(_)
                coordinate_temp = np.delete(coordinate_temp, delete_index, axis=0)
                right_top = coordinate_temp[0]
            return left_top, right_top, left_bottom, right_bottom
        def find_num(x_u, y_u, x_d, y_d, lamda):
            X = int(x_u * (1 + lamda) - lamda * x_d)
            Y = int(y_u * (1 + lamda) - lamda * y_d)
            return X, Y
        def diff(img, id):
            img = cv2.resize(img,(300,200))
            img = cv2.flip(img, 0)
            self.Image = img
            self.DispImg()
            cv2.waitKey(3)
            if not os.path.exists('./name'):
                os.mkdir('./name')
            cv2.imwrite('./name/' + id + '.png', img)
        def fan(a,b):
            temp=a
            a=b
            b=temp
            return a,b
        def name_main(id):
            count = 0
            # end_save = 0
            SUM_num_X_d_l = 0
            SUM_num_Y_d_l = 0
            SUM_num_X_u_l = 0
            SUM_num_Y_u_l = 0
            SUM_num_X_d_r = 0
            SUM_num_Y_d_r = 0
            SUM_num_X_u_r = 0
            SUM_num_Y_u_r = 0
            flag_wending = 0
            count_wending = 0
            time_start = time.time()
            while True:
                if self.switchnum == 1:
                    break
                if len(id) == 0:
                    self.CameraShow.setText("名字不能为空")
                    self.CodesendBt.setEnabled(True)
                    break
                success, img = self.video_cap1.read()
                try:
                    barcodes = pyzbar.decode(img)
                except:
                    continue
                if len(barcodes) == 0 and (time.time() - time_start) > 5:
                    self.CameraShow.setText("录入超时或未检测出健康码")
                    self.CodesendBt.setEnabled(True)
                    break
                if len(barcodes) != 0:
                    time_start = time.time()
                for barcode in barcodes:
                    pts = np.array([barcode.polygon], np.int32)

                    pts = pts.reshape((-1, 1, 2))
                    left_bottom, right_bottom, left_top, right_top = right_dir(pts[3][0], pts[2][0], pts[1][0],
                                                                               pts[0][0])
                    x_u, y_u = center(right_top[0], right_top[1], left_top[0], left_top[1])
                    x_d, y_d = center(right_bottom[0], right_bottom[1], left_bottom[0], left_bottom[1])
                    num_X_d_r, num_Y_d_r = find_num(x_u, y_u, x_d, y_d, 1 / 1.1)
                    num_X_u_r, num_Y_u_r = find_num(x_u, y_u, x_d, y_d, 1 / 1.26)
                    num_X_d_l, num_Y_d_l = find_num(left_top[0], left_top[1], left_bottom[0], left_bottom[1], 1 / 1.1)
                    num_X_u_l, num_Y_u_l = find_num(left_top[0], left_top[1], left_bottom[0], left_bottom[1], 1 / 1.26)
                    num_X_d_l = int(num_X_d_l * 0.96)
                    num_X_u_l = int(num_X_u_l * 0.96)
                    num_X_d_r = int(num_X_d_r * 1.05)
                    num_X_u_r = int(num_X_u_r * 1.05)
                    lens = 50
                    if count_wending != lens:
                        count_wending = count_wending + 1
                        SUM_num_X_d_l = SUM_num_X_d_l + num_X_d_l
                        SUM_num_Y_d_l = SUM_num_Y_d_l + num_Y_d_l
                        SUM_num_X_u_l = SUM_num_X_u_l + num_X_u_l
                        SUM_num_Y_u_l = SUM_num_Y_u_l + num_Y_u_l
                        SUM_num_X_d_r = SUM_num_X_d_r + num_X_d_r
                        SUM_num_Y_d_r = SUM_num_Y_d_r + num_Y_d_r
                        SUM_num_X_u_r = SUM_num_X_u_r + num_X_u_r
                        SUM_num_Y_u_r = SUM_num_Y_u_r + num_Y_u_r
                    else:
                        count_wending= 0
                        flag_wending = 1
                        num_X_d_l = int(SUM_num_X_d_l/lens)
                        num_Y_d_l = int(SUM_num_Y_d_l/lens)
                        num_X_u_l = int(SUM_num_X_u_l/lens)
                        num_Y_u_l = int(SUM_num_Y_u_l/lens)
                        num_X_d_r = int(SUM_num_X_d_r/lens)
                        num_Y_d_r = int(SUM_num_Y_d_r/lens)
                        num_X_u_r = int(SUM_num_X_u_r/lens)
                        num_Y_u_r = int(SUM_num_Y_u_r/lens)
                    num_Y_u_r,num_Y_u_l = fan(num_Y_u_r,num_Y_u_l)
                    num_Y_d_r, num_Y_d_l = fan(num_Y_d_r, num_Y_d_l)
                    num_X_u_r,num_X_u_l = fan(num_X_u_r,num_X_u_l)
                    num_X_d_r, num_X_d_l = fan(num_X_d_r, num_X_d_l)
                    pts_before = np.float32([[num_X_d_r, num_Y_d_r], [num_X_u_r, num_Y_u_r], [num_X_d_l, num_Y_d_l],
                                             [num_X_u_l, num_Y_u_l]])
                    pts_after = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
                    M = cv2.getPerspectiveTransform(pts_before, pts_after)

                    dst = cv2.warpPerspective(img, M, (300, 300))
                    cv2.circle(img, (num_X_d_r, num_Y_d_r), 4, (0, 0, 255), 0)
                    cv2.circle(img, (num_X_u_r, num_Y_u_r), 4, (0, 0, 255), 0)
                    cv2.circle(img, (num_X_d_l, num_Y_d_l), 4, (0, 0, 255), 0)
                    cv2.circle(img, (num_X_u_l, num_Y_u_l), 4, (0, 0, 255), 0)
                    codeData = barcode.data.decode('utf-8')
                    pts = np.array([barcode.polygon], np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                    pts2 = barcode.rect
                    count = count + 1
                    if count != 0:
                        try:
                            if flag_wending == 1:
                                diff(dst, id)
                            # end_save = end_save + 1
                        except:
                            continue
                self.Image = img
                self.DispImg()
                cv2.waitKey(3)
                # if end_save == 10:
                if flag_wending == 1:
                    flag_wending = 0
                    self.CameraShow.setText("健康码录入成功")
                    self.CodesendBt.setEnabled(True)
                    break
        id = self.name.text().lower()
        name_main(id)




class MyThread(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None




class RecognitionWindow(QMainWindow,Ui_MainWindow):
    switch_window9 = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        super(RecognitionWindow,self).__init__(parent)
        self.setupUi(self)
        self.prew_disp = threading.Thread(target=self.PrepWidgets)#初始化控件
        self.prep_disp = threading.Thread(target=self.PrepParameters)#初始化参数
        self.cb_disp = threading.Thread(target=self.CallBackFunctions)#回调函数
        self.Timer = QTimer()
        self.timerset()
        self.prew_disp.start()
        self.prep_disp.start()
        self.cb_disp.start()
        self.prew_disp.join()
        self.prep_disp.join()
        self.cb_disp.join()
        self.gostop.setText("初始化完成")
        self.Timer.timeout.connect(self.settiime)

    def PrepWidgets(self):
        self.camera = cv2.VideoCapture(0)
        self.camera1 = cv2.VideoCapture(1)
        self.filepath = os.getcwd()
        self.landmark = self.filepath + "\data\data_dlib\shape_predictor_68_face_landmarks.dat"
        self.modelname = self.filepath + "\data\data_dlib\dlib_face_recognition_resnet_model_v1.dat"
        self.csvname = self.filepath + "\data\\features_all.csv"

    def PrepParameters(self):
        self.Image_num = 0
        self.switchnum = 0
        self.quitnum = 0

    def CallBackFunctions(self):
        self.ShowBt.clicked.connect(self.ShowBtOn)
        self.Outscreen.clicked.connect(self.Qnum)

    def ShowBtOn(self):
        self.switchnum = 1
        self.dnum = 0
        self.ShowBt.setEnabled(False)
        self.ShowBt.setStyleSheet("background-color: rgb(193, 193, 193);\ncolor: rgb(0, 0, 0);")
        self.facerecognize()

    def Qnum(self):
        if self.switchnum == 1:
            self.switchnum = 2
        if self.switchnum == 0:
            self.switchnum = 2
            self.TimerOutFun()

    def Quit(self):
        if self.camera.isOpened():
            cv2.waitKey(1)
            self.camera.release()
        if self.camera1.isOpened():
            cv2.waitKey(1)
            self.camera1.release()
        self.ShowBt.setEnabled(True)
        self.switch_window9.emit()
        self.close()

    def TimerOutFun(self):
        t_disp = threading.Thread(target=self.DispImg)
        if self.switchnum == 1:
            img=self.img_rd
        else:
            success,img = self.camera.read()
            img=cv2.flip(img, 1)
        self.Image=img
        if self.switchnum !=2:
            if self.dnum == 0:
                t_disp.start()
                self.dnum = self.dnum + 1
            else:
                if threading.Thread.is_alive(t_disp) == False:
                    t_disp.start()
        else:
            if threading.Thread.is_alive(t_disp) == True:
                t_disp.join()
            self.Quit()

    def DispImg(self):
        dst = cv2.resize(self.Image, (580, 270))
        img = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        # data = np.array(img).reshape(580,270).astype(np.int32)
        qimg = QtGui.QImage(img[:],img.shape[1], img.shape[0],img.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.DispLb.setPixmap(QPixmap.fromImage(qimg))
        self.DispLb.show()

    def timerset(self):
        self.Timer.start(1)

    def settiime(self):
        times = str(time.strftime("%S"))
        timeM = str(time.strftime("%M"))
        timeh = str(time.strftime("%H"))
        timey = str(time.strftime("%Y"))
        timem = str(time.strftime("%m"))
        timed = str(time.strftime("%d"))
        self.time_fm.setText(timey + "年" + timem + "月" + timed + "日 " + timeh + ":" + timeM + ":" + times)
        self.time_fm.setAlignment(Qt.AlignCenter)#居中显示

    def numsee(self):
        def center(x1, y1, x2, y2):
            c1_x = (x1 + x2) / 2
            c1_y = (y1 + y2) / 2
            c2_x = (c1_x + x2) / 2
            c2_y = (c1_y + y2) / 2
            c3_x = int((c2_x + x2) / 2)
            c3_y = int((c2_y + y2) / 2)
            c4_x = int((c3_x + x2) / 2)
            c4_y = int((c3_y + y2) / 2)
            return c4_x, c4_y
        def cmpHash(hash1, hash2):
            # Hash值对比
            # 算法中1和0顺序组合起来的即是图片的指纹hash。顺序不固定，但是比较的时候必须是相同的顺序。
            # 对比两幅图的指纹，计算汉明距离，即两个64位的hash值有多少是不一样的，不同的位数越小，图片越相似
            # 汉明距离：一组二进制数据变成另一组数据所需要的步骤，可以衡量两图的差异，汉明距离越小，则相似度越高。汉明距离为0，即两张图片完全一样
            n = 0
            # hash长度不同则返回-1代表传参出错
            if len(hash1) != len(hash2):
                return -1
            # 遍历判断
            for i in range(len(hash1)):
                # 不相等则n计数+1，n最终为相似度
                if hash1[i] != hash2[i]:
                    n = n + 1
            return n

        def aHash(img):
            # 均值哈希算法
            # 缩放为8*8
            img = cv2.resize(img, (8, 8))
            # 转换为灰度图
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # s为像素和初值为0，hash_str为hash值初值为''
            s = 0
            hash_str = ''
            # 遍历累加求像素和
            for i in range(8):
                for j in range(8):
                    s = s + gray[i, j]
            # 求平均灰度
            avg = s / 64
            # 灰度大于平均值为1相反为0生成图片的hash值
            for i in range(8):
                for j in range(8):
                    if gray[i, j] > avg:
                        hash_str = hash_str + '1'
                    else:
                        hash_str = hash_str + '0'
            return hash_str

        def right_dir(a, b, c, d):
            # 所需要确定位置的四个坐标
            coordinate = [a, b, c, d]  # 常规矩形坐标
            # coordinate = [[0, 1], [1, 0], [1, 2], [2, 1]]  # 非常规（菱形）矩形坐标，用以验证代码
            coordinate = np.array(coordinate)
            center = coordinate[0]
            for _ in range(1, 4):
                center = center + coordinate[_]
            center = center / 4
            coordinate_temp = coordinate.copy()  # 复制一份坐标，避免原坐标被破坏
            left_coordinate = []  # 存储x轴小于中心坐标点的点
            delete_index = []
            # 将 x轴小于中心坐标点的点 存储进left_coordinate
            for _ in range(4):
                if (coordinate[_][0] < center[0]):
                    left_coordinate.append(coordinate[_])
                    delete_index.append(_)
            # 将存储进 left_coordinate 的元素从coordinate_temp中删除
            coordinate_temp = np.delete(coordinate_temp, delete_index, axis=0)
            left_coordinate_temp = left_coordinate.copy()  # 避免程序过程因为left_coordinate的变动而导致最初的条件判断错误
            if (len(left_coordinate_temp) == 2):
                # 比较左边两个点的y轴，大的为左上
                if (left_coordinate[0][1] < left_coordinate[1][1]):
                    left_bottom = left_coordinate[0]
                    left_top = left_coordinate[1]
                elif (left_coordinate[0][1] > left_coordinate[1][1]):
                    left_bottom = left_coordinate[1]
                    left_top = left_coordinate[0]
                # 比较右边两个点的y轴，大的为右上
                if (coordinate_temp[0][1] < coordinate_temp[1][1]):
                    right_bottom = coordinate_temp[0]
                    right_top = coordinate_temp[1]
                elif (coordinate_temp[0][1] > coordinate_temp[1][1]):
                    right_bottom = coordinate_temp[1]
                    right_top = coordinate_temp[0]
            elif (len(left_coordinate_temp) == 1):
                left_bottom = left_coordinate[0]
                delete_index = []
                for _ in range(3):
                    if (coordinate_temp[_][0] == center[0] and coordinate_temp[_][1] > center[1]):
                        left_top = coordinate_temp[_]
                        delete_index.append(_)
                    if (coordinate_temp[_][0] == center[0] and coordinate_temp[_][1] < center[1]):
                        right_bottom = coordinate_temp[_]
                        delete_index.append(_)
                coordinate_temp = np.delete(coordinate_temp, delete_index, axis=0)
                right_top = coordinate_temp[0]
            return left_top, right_top, left_bottom, right_bottom

        def find_num(x_u, y_u, x_d, y_d, lamda):
            X = int(x_u * (1 + lamda) - lamda * x_d)
            Y = int(y_u * (1 + lamda) - lamda * y_d)
            return X, Y

        def fan(a, b):
            temp = a
            a = b
            b = temp
            return a, b

        def diff(img, img1):
            hash1 = aHash(img)
            hash2 = aHash(img1)
            n5 = cmpHash(hash1, hash2)
            return n5

        count = 0
        flag_count = 1
        new1 = 0
        new2 = 0
        new3 = 0
        count_n5 = 0
        sum_count    = []
        time_start=time.time()
        SUM_num_X_d_l = 0
        SUM_num_Y_d_l = 0
        SUM_num_X_u_l = 0
        SUM_num_Y_u_l = 0
        SUM_num_X_d_r = 0
        SUM_num_Y_d_r = 0
        SUM_num_X_u_r = 0
        SUM_num_Y_u_r = 0
        flag_wending = 0
        count_wending = 0
        while True:
            success, img = self.camera1.read()
            try:
                barcodes = pyzbar.decode(img)
            except:
                continue
            if len(barcodes) == 0 and (time.time()-time_start)>5:
                self.gostop.setText("长时间未检测到健康码")
                cv2.waitKey(2000)
                self.facerecognize()
            if self.switchnum != 1:
                break
            if len(barcodes) != 0:
                time_start = time.time()
            for barcode in barcodes:
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                left_bottom, right_bottom, left_top, right_top = right_dir(pts[3][0], pts[2][0], pts[1][0],
                                                                           pts[0][0])
                x_u, y_u = center(left_top[0], left_top[1], right_top[0], right_top[1])
                x_d, y_d = center(left_bottom[0], left_bottom[1], right_bottom[0], right_bottom[1])
                num_X_d_r, num_Y_d_r = find_num(x_u, y_u, x_d, y_d, 1 / 9)
                num_X_u_r, num_Y_u_r = find_num(x_u, y_u, x_d, y_d, 1 / 6)
                num_X_d_l, num_Y_d_l = find_num(right_top[0], right_top[1], right_bottom[0], right_bottom[1], 1 / 9)
                num_X_u_l, num_Y_u_l = find_num(right_top[0], right_top[1], right_bottom[0], right_bottom[1], 1 / 6)
                num_X_d_l = int(num_X_d_l * 0.95)
                num_X_u_l = int(num_X_u_l * 0.95)
                lens = 80
                if count_wending != lens:
                    count_wending = count_wending + 1
                    SUM_num_X_d_l = SUM_num_X_d_l + num_X_d_l
                    SUM_num_Y_d_l = SUM_num_Y_d_l + num_Y_d_l
                    SUM_num_X_u_l = SUM_num_X_u_l + num_X_u_l
                    SUM_num_Y_u_l = SUM_num_Y_u_l + num_Y_u_l
                    SUM_num_X_d_r = SUM_num_X_d_r + num_X_d_r
                    SUM_num_Y_d_r = SUM_num_Y_d_r + num_Y_d_r
                    SUM_num_X_u_r = SUM_num_X_u_r + num_X_u_r
                    SUM_num_Y_u_r = SUM_num_Y_u_r + num_Y_u_r
                else:
                    count_wending = 0
                    flag_wending = 1
                    num_X_d_l = int(SUM_num_X_d_l / lens)
                    num_Y_d_l = int(SUM_num_Y_d_l / lens)
                    num_X_u_l = int(SUM_num_X_u_l / lens)
                    num_Y_u_l = int(SUM_num_Y_u_l / lens)
                    num_X_d_r = int(SUM_num_X_d_r / lens)
                    num_Y_d_r = int(SUM_num_Y_d_r / lens)
                    num_X_u_r = int(SUM_num_X_u_r / lens)
                    num_Y_u_r = int(SUM_num_Y_u_r / lens)
                num_Y_u_r, num_Y_u_l = fan(num_Y_u_r, num_Y_u_l)
                num_Y_d_r, num_Y_d_l = fan(num_Y_d_r, num_Y_d_l)
                pts_before = np.float32([[num_X_d_r, num_Y_d_r], [num_X_u_r, num_Y_u_r], [num_X_d_l, num_Y_d_l],[num_X_u_l, num_Y_u_l]])
                pts_after = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
                M = cv2.getPerspectiveTransform(pts_before, pts_after)
                dst = cv2.warpPerspective(img, M, (300, 300))
                cv2.circle(img, (num_X_d_r, num_Y_d_r), 4, (0, 255, 0), 0)
                cv2.circle(img, (num_X_u_r, num_Y_u_r), 4, (0, 0, 255), 0)
                cv2.circle(img, (num_X_d_l, num_Y_d_l), 4, (0, 0, 255), 0)
                cv2.circle(img, (num_X_u_l, num_Y_u_l), 4, (0, 0, 255), 0)
                self.img_rd = img
                self.TimerOutFun()
                cv2.waitKey(3)
                if count % 30 == 0:
                    flag_count = flag_count + 1
                    new3 = 1
                if flag_count % 2 == 0 and new3:
                    new1 = 1
                    dst_temp = dst.copy()
                if flag_count % 2 != 0 and new3:
                    new2 = 1
                    dst_temp1 = dst.copy()
                count = count + 1
                if count != 0:
                    try:
                        if new1 or new2:
                            if flag_wending == 1:
                                count_n5 = count_n5 + 1
                                n5 = diff(dst_temp1, dst_temp)
                            new1 = 0
                            new2 = 0
                            new3 = 0
                            if count_n5 != 10:
                                sum_count.append(n5)
                                self.gostop.setText("正在验证健康码请等待"+'('+str(count_n5+1)+'/'+'10'+')')
                            if count_n5 == 10:
                                sum_count.remove(max(sum_count))
                                sum_count.remove(min(sum_count))
                                sum_count.remove(max(sum_count))
                                sum_count.remove(min(sum_count))
                                return sum(sum_count) / len(sum_count)
                                break
                    except:
                        continue
            k = cv2.waitKey(10)
            if k == 27:
                break
            if self.switchnum != 1:
                break

    def cor(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        lower_red = np.array([0, 127, 128])  # 红色阈值下界
        higher_red = np.array([10, 255, 255])  # 红色阈值上界
        lower_green = np.array([35, 50, 106])  # 绿色阈值下界
        higher_green = np.array([77, 255, 255])  # 绿色阈值上界
        START_TIME= time.time()
        if (1):
            waitnum = 0
            while (True):
                ret, frame = self.camera1.read()  # 按帧读取，这是读取一帧
                img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask_red = cv2.inRange(img_hsv, lower_red, higher_red)  # 可以认为是过滤出红色部分，获得红色的掩膜
                mask_green = cv2.inRange(img_hsv, lower_green, higher_green)  # 获得绿色部分掩膜
                mask_green = cv2.medianBlur(mask_green, 7)  # 中值滤波
                mask_red = cv2.medianBlur(mask_red, 7)  # 中值滤波
                mask = cv2.bitwise_or(mask_green, mask_red)  # 三部分掩膜进行按位或运算
                cnts1, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓检测
                cnts3, hierarchy3 = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                if len(cnts1)==0 and len(cnts3)==0 and (time.time()-START_TIME)>5:
                    self.gostop.setText("长时间未进行颜色识别")
                    cv2.waitKey(200)
                    self.facerecognize()
                self.img_rd = frame
                self.TimerOutFun()
                cv2.waitKey(200)
                if (len(cnts1) > len(cnts3)):
                    return "red"
                else:
                    return "green"
                k = cv2.waitKey(20)
                if k == 27:
                    break
                if self.switchnum != 1:
                    break

    def name(self,id):
        def center(x1, y1, x2, y2):
            c1_x = (x1 + x2) / 2
            c1_y = (y1 + y2) / 2
            c2_x = (c1_x + x2) / 2
            c2_y = (c1_y + y2) / 2
            c3_x = int((c2_x + x2) / 2)
            c3_y = int((c2_y + y2) / 2)
            c4_x = int((c3_x + x2) / 2)
            c4_y = int((c3_y + y2) / 2)
            return c3_x, c3_y

        def cmpHash(hash1, hash2):
            # Hash值对比
            # 算法中1和0顺序组合起来的即是图片的指纹hash。顺序不固定，但是比较的时候必须是相同的顺序。
            # 对比两幅图的指纹，计算汉明距离，即两个64位的hash值有多少是不一样的，不同的位数越小，图片越相似
            # 汉明距离：一组二进制数据变成另一组数据所需要的步骤，可以衡量两图的差异，汉明距离越小，则相似度越高。汉明距离为0，即两张图片完全一样
            n = 0
            # hash长度不同则返回-1代表传参出错
            if len(hash1) != len(hash2):
                return -1
            # 遍历判断
            for i in range(len(hash1)):
                # 不相等则n计数+1，n最终为相似度
                if hash1[i] != hash2[i]:
                    n = n + 1
            return n

        def aHash(img):
            # 均值哈希算法
            # 缩放为8*8
            img = cv2.resize(img, (8, 8))
            # 转换为灰度图
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # s为像素和初值为0，hash_str为hash值初值为''
            s = 0
            hash_str = ''
            # 遍历累加求像素和
            for i in range(8):
                for j in range(8):
                    s = s + gray[i, j]
            # 求平均灰度
            avg = s / 64
            # 灰度大于平均值为1相反为0生成图片的hash值
            for i in range(8):
                for j in range(8):
                    if gray[i, j] > avg:
                        hash_str = hash_str + '1'
                    else:
                        hash_str = hash_str + '0'
            return hash_str

        def pHash(img):
            # 感知哈希算法
            # 缩放32*32
            img = cv2.resize(img, (32, 32))  # , interpolation=cv2.INTER_CUBIC
            # 转换为灰度图
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 将灰度图转为浮点型，再进行dct变换
            dct = cv2.dct(np.float32(gray))
            # opencv实现的掩码操作
            dct_roi = dct[0:8, 0:8]
            hash = []
            avreage = np.mean(dct_roi)
            for i in range(dct_roi.shape[0]):
                for j in range(dct_roi.shape[1]):
                    if dct_roi[i, j] > avreage:
                        hash.append(1)
                    else:
                        hash.append(0)
            return hash

        def calculate(image1, image2):
            # 灰度直方图算法
            # 计算单通道的直方图的相似值
            hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
            hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
            # 计算直方图的重合度
            degree = 0
            for i in range(len(hist1)):
                if hist1[i] != hist2[i]:
                    degree = degree + \
                             (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
                else:
                    degree = degree + 1
            degree = degree / len(hist1)
            return degree


        def classify_hist_with_split(image1, image2, size=(256, 256)):
            # RGB每个通道的直方图相似度
            # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
            image1 = cv2.resize(image1, size)
            image2 = cv2.resize(image2, size)
            sub_image1 = cv2.split(image1)
            sub_image2 = cv2.split(image2)
            sub_data = 0
            for im1, im2 in zip(sub_image1, sub_image2):
                sub_data += calculate(im1, im2)
            sub_data = sub_data / 3
            return sub_data
        def right_dir(a, b, c, d):
            # 所需要确定位置的四个坐标
            coordinate = [a, b, c, d]  # 常规矩形坐标
            # coordinate = [[0, 1], [1, 0], [1, 2], [2, 1]]  # 非常规（菱形）矩形坐标，用以验证代码
            coordinate = np.array(coordinate)
            center = coordinate[0]
            for _ in range(1, 4):
                center = center + coordinate[_]
            center = center / 4
            coordinate_temp = coordinate.copy()  # 复制一份坐标，避免原坐标被破坏
            left_coordinate = []  # 存储x轴小于中心坐标点的点
            delete_index = []
            # 将 x轴小于中心坐标点的点 存储进left_coordinate
            for _ in range(4):
                if (coordinate[_][0] < center[0]):
                    left_coordinate.append(coordinate[_])
                    delete_index.append(_)
            # 将存储进 left_coordinate 的元素从coordinate_temp中删除
            coordinate_temp = np.delete(coordinate_temp, delete_index, axis=0)

            left_coordinate_temp = left_coordinate.copy()  # 避免程序过程因为left_coordinate的变动而导致最初的条件判断错误
            if (len(left_coordinate_temp) == 2):
                # 比较左边两个点的y轴，大的为左上
                if (left_coordinate[0][1] < left_coordinate[1][1]):
                    left_bottom = left_coordinate[0]
                    left_top = left_coordinate[1]
                elif (left_coordinate[0][1] > left_coordinate[1][1]):
                    left_bottom = left_coordinate[1]
                    left_top = left_coordinate[0]
                # 比较右边两个点的y轴，大的为右上
                if (coordinate_temp[0][1] < coordinate_temp[1][1]):
                    right_bottom = coordinate_temp[0]
                    right_top = coordinate_temp[1]
                elif (coordinate_temp[0][1] > coordinate_temp[1][1]):
                    right_bottom = coordinate_temp[1]
                    right_top = coordinate_temp[0]
            elif (len(left_coordinate_temp) == 1):
                left_bottom = left_coordinate[0]
                delete_index = []
                for _ in range(3):
                    if (coordinate_temp[_][0] == center[0] and coordinate_temp[_][1] > center[1]):
                        left_top = coordinate_temp[_]
                        delete_index.append(_)
                    if (coordinate_temp[_][0] == center[0] and coordinate_temp[_][1] < center[1]):
                        right_bottom = coordinate_temp[_]
                        delete_index.append(_)
                coordinate_temp = np.delete(coordinate_temp, delete_index, axis=0)
                right_top = coordinate_temp[0]
            return left_top, right_top, left_bottom, right_bottom

        def find_num(x_u, y_u, x_d, y_d, lamda):
            X = int(x_u * (1 + lamda) - lamda * x_d)
            Y = int(y_u * (1 + lamda) - lamda * y_d)
            return X, Y

        def fan(a, b):
            temp = a
            a = b
            b = temp
            return a, b

        def diff(img, id):
            cmp = cv2.imread('./name/' + id + '.png', 1)
            hash1 = aHash(img)
            hash2 = aHash(cmp)
            n5 = cmpHash(hash1, hash2)
            hash1 = pHash(img)
            hash2 = pHash(cmp)
            n3 = cmpHash(hash1, hash2)
            n4 = classify_hist_with_split(img, cmp)
            return n4

        count = 0
        count_n5 = 0
        sum_count_n5 = 0
        sum_count = []
        SUM_num_X_d_l = 0
        SUM_num_Y_d_l = 0
        SUM_num_X_u_l = 0
        SUM_num_Y_u_l = 0
        SUM_num_X_d_r = 0
        SUM_num_Y_d_r = 0
        SUM_num_X_u_r = 0
        SUM_num_Y_u_r = 0
        flag_wending = 0
        count_wending = 0
        time_start = time.time()
        while True:
            success, img = self.camera1.read()
            try:
                barcodes = pyzbar.decode(img)
            except:
                continue
            if len(barcodes) == 0 and (time.time()-time_start)>5:
                self.gostop.setText("长时间未检测到健康码返回")
                cv2.waitKey(2000)
                self.facerecognize()
            for barcode in barcodes:
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                left_bottom, right_bottom, left_top, right_top = right_dir(pts[3][0], pts[2][0], pts[1][0], pts[0][0])
                x_u, y_u = center(right_top[0], right_top[1], left_top[0], left_top[1])
                x_d, y_d = center(right_bottom[0], right_bottom[1], left_bottom[0], left_bottom[1])
                num_X_d_r, num_Y_d_r = find_num(x_u, y_u, x_d, y_d, 1 / 1.1)
                num_X_u_r, num_Y_u_r = find_num(x_u, y_u, x_d, y_d, 1 / 1.26)
                num_X_d_l, num_Y_d_l = find_num(left_top[0], left_top[1], left_bottom[0], left_bottom[1], 1 / 1.1)
                num_X_u_l, num_Y_u_l = find_num(left_top[0], left_top[1], left_bottom[0], left_bottom[1], 1 / 1.26)
                num_X_d_l = int(num_X_d_l * 0.96)
                num_X_u_l = int(num_X_u_l * 0.96)
                num_X_d_r = int(num_X_d_r * 1.05)
                num_X_u_r = int(num_X_u_r * 1.05)
                lens = 50
                if count_wending != lens:
                    count_wending = count_wending + 1
                    SUM_num_X_d_l = SUM_num_X_d_l + num_X_d_l
                    SUM_num_Y_d_l = SUM_num_Y_d_l + num_Y_d_l
                    SUM_num_X_u_l = SUM_num_X_u_l + num_X_u_l
                    SUM_num_Y_u_l = SUM_num_Y_u_l + num_Y_u_l
                    SUM_num_X_d_r = SUM_num_X_d_r + num_X_d_r
                    SUM_num_Y_d_r = SUM_num_Y_d_r + num_Y_d_r
                    SUM_num_X_u_r = SUM_num_X_u_r + num_X_u_r
                    SUM_num_Y_u_r = SUM_num_Y_u_r + num_Y_u_r
                else:
                    count_wending = 0
                    flag_wending = 1
                    num_X_d_l = int(SUM_num_X_d_l / lens)
                    num_Y_d_l = int(SUM_num_Y_d_l / lens)
                    num_X_u_l = int(SUM_num_X_u_l / lens)
                    num_Y_u_l = int(SUM_num_Y_u_l / lens)
                    num_X_d_r = int(SUM_num_X_d_r / lens)
                    num_Y_d_r = int(SUM_num_Y_d_r / lens)
                    num_X_u_r = int(SUM_num_X_u_r / lens)
                    num_Y_u_r = int(SUM_num_Y_u_r / lens)
                pts_before = np.float32(
                    [[num_X_d_r, num_Y_d_r], [num_X_u_r, num_Y_u_r], [num_X_d_l, num_Y_d_l], [num_X_u_l, num_Y_u_l]])
                pts_after = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
                M = cv2.getPerspectiveTransform(pts_before, pts_after)
                dst = cv2.warpPerspective(img, M, (300, 300))
                cv2.circle(img, (num_X_d_r, num_Y_d_r), 4, (0, 0, 255), 0)
                cv2.circle(img, (num_X_u_r, num_Y_u_r), 4, (0, 0, 255), 0)
                cv2.circle(img, (num_X_d_l, num_Y_d_l), 4, (0, 0, 255), 0)
                cv2.circle(img, (num_X_u_l, num_Y_u_l), 4, (0, 0, 255), 0)
                codeData = barcode.data.decode('utf-8')
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                self.img_rd = img
                self.TimerOutFun()
                cv2.waitKey(3)
                count = count + 1
                if count != 0:
                    if (os.path.exists("./name/"+id+".png"))==False:
                        self.gostop.setText("健康码未登记")
                        cv2.waitKey(2000)
                        self.facerecognize()
                    try:
                        if flag_wending == 1:
                            n5 = diff(dst, id)
                            count_n5 = count_n5 + 1
                        if count_n5 != 10:
                            sum_count_n5 = sum_count_n5 + n5
                            sum_count.append(n5)
                        if count_n5 == 10:
                            sum_count.remove(max(sum_count))
                            sum_count.remove(min(sum_count))
                            sum_count.remove(max(sum_count))
                            sum_count.remove(min(sum_count))
                            return sum(sum_count) / len(sum_count)
                            break
                    except:
                        continue
            k = cv2.waitKey(20)
            if k == 27:
                break
            if self.switchnum != 1:
                break


    def ApiConnect(self):
        """ 你的 APPID AK SK """
        APP_ID = '24575241'
        API_KEY = 'reaBGjgYwHfUjDCqc8PZcNTf'
        SECRET_KEY = 'D74au6gHiZzCjmnAcDTfLmmVXTpTn7ra'
        client = AipFace(APP_ID, API_KEY, SECRET_KEY)
        self.netconnect = 1
        def face_test(imageBase64):
            # f = get_file_content(face_image_path)  # f读取图片
            # data = base64.b64encode(f)  # 将图片内容处理成base64数据

            result = client.search(imageBase64, "BASE64", "01");  # 在百度云人脸库中寻找有没有匹配的人脸
            print(result)
            # TODO
            if result['error_msg'] == 'SUCCESS':  # 如果成功了
                name = result['result']['user_list'][0]['user_id']  # 获取名字
                score = result['result']['user_list'][0]['score']  # 获取相似度
                if score > 80:  # 如果相似度大于80
                    # TODO
                    name = name
                else:
                    self.gostop.setText("人脸验证失败，请购票")
                    return 0

                curren_time = time.asctime(time.localtime(time.time()))  # 获取当前时间
                # 将人员出入的记录保存到Log.txt中
                f = open('Log.txt', 'a')
                f.write("Person: " + name + "     " + "Time:" + str(curren_time) + '\n')
                f.close()
            if result['error_msg'] == 'pic not has face':
                self.gostop.setText("检测不到人脸")
                time.sleep(2)
                return 0
            output = name
            return output

        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        log.basicConfig(filename='webcam.log', level=log.INFO)
        anterior = 0
        count = 0
        while True:
            # Capture frame-by-frame
            ret, frame = self.camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Draw a rectangle around the faces

            big_num = 0
            big = 0
            if len(faces) != 0:
                count = count + 1
                for i in range(len(faces)):
                    if faces[i][3] * faces[i][2] > big:
                        big = faces[i][3] * faces[i][2]
                        big_num = i

                x = faces[big_num][0]
                y = faces[big_num][1]
                w = faces[big_num][2]
                h = faces[big_num][3]

                if ret and (count % 100 == 0):
                    # 制作缩略图
                    image = Image.fromarray(cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2RGB))
                    image.thumbnail((500, 300))
                    if not os.path.exists('./picture'):
                        os.mkdir('./picture')
                    imageFilePath = "./picture/face" + dt.datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg";
                    image.save(imageFilePath, format='jpeg')
                    with open(imageFilePath, 'rb') as imageFile:
                        base64_data = base64.b64encode(imageFile.read())
                        imageBase64 = base64_data.decode()
                    del image
                    # del frame, ret, image
                    # break
                    du_disp = MyThread(face_test,(imageBase64,))  # 回调函数
                    du_disp.start()
                    du_disp.join()

                    name_OUTPUT = du_disp.get_result()
                    if name_OUTPUT==0:
                        continue

                    #name_OUTPUT = face_test(imageBase64)

                    return name_OUTPUT


                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.img_rd = cv2.flip(frame, 1)
            self.TimerOutFun()
            cv2.waitKey(3)

            if anterior != len(faces):
                anterior = len(faces)
                log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if self.switchnum !=1:
                break



    def facerecognize(self):
        if self.switchnum == 1:
            self.gostop.setText("正在识别中")
            output = self.ApiConnect()
            id = output
            print(id)
            if output is not None:
                self.gostop.setText("姓名"+id+"，人脸识别通过")
                cv2.waitKey(2000)
                self.gostop.setText("请出示健康码")
            else:
                self.Quit()
            if self.switchnum == 1:
                flag_num_active = self.numsee()

                if flag_num_active is None:
                    self.facerecognize()
                else:
                    print(flag_num_active)
                    if flag_num_active < 10:
                        self.gostop.setText("请打开动态健康码")
                        cv2.waitKey(2000)
                        flag_num = 0
                        self.facerecognize()
                    else:
                        flag_num = 1
            else:
                self.Quit()
            if self.switchnum == 1:
                color = self.cor()
                if color == "green":
                    self.gostop.setText("健康码为绿码")
                    cv2.waitKey(3000)
                    flag_color = 1
                else:
                    self.gostop.setText("红码，禁止进入车站")
                    cv2.waitKey(3000)
                    flag_color = 0
                    self.facerecognize()
            if self.switchnum == 1:
                name_num = self.name(output.lower())
                print(name_num)
                if name_num is None:
                    self.gostop.setText("没有检测到名字")
                    self.facerecognize()
                else:
                    if  name_num > 0.65:
                        flag_name = 1
                    else:
                        self.gostop.setText("不允许使用别人的健康码")
                        cv2.waitKey(4000)
                        flag_name = 0
                        self.facerecognize()
            if self.switchnum == 1:
                # judge
                if  flag_num and flag_color and flag_name:
                    self.gostop.setText("验证通过，欢迎进入联合车站！")
                    cv2.waitKey(8000)
                    if self.switchnum == 1:
                        self.facerecognize()
                else:
                    if self.switchnum == 1:
                        self.facerecognize()
        else:
            self.Quit()




# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    # 跳转到关机窗口
    def show_Off(self):
        self.Off = OffWindow()
        self.Off.show()
        self.Off.switch_window1.connect(self.show_welcome)
    # 跳转到欢迎窗口,并关闭原页面
    def show_welcome(self):
        self.welcome = WelcomeWindow()
        self.welcome.show()
        self.welcome.switch_window2.connect(self.show_login)
        self.welcome.switch_window3.connect(self.show_Off)
        self.welcome.switch_window10.connect(self.show_recognition)
    # 跳转到识别窗口，并关闭原页面
    def show_recognition(self):
        self.recognition = RecognitionWindow()
        self.recognition.show()
        self.recognition.switch_window9.connect(self.show_welcome)
    # 跳转到登录窗口,并关闭原页面
    def show_login(self):
        self.login = LoginWindow()
        self.login.show()
        self.login.switch_window4.connect(self.show_regist)
        self.login.switch_window5.connect(self.show_welcome)
        self.login.switch_window6.connect(self.show_Api)
    # 跳转到注册窗口,并关闭原页面
    def show_regist(self):
        self.regist = RegistWindow()
        self.regist.show()
        self.regist.switch_window7.connect(self.show_login)
    def show_Api(self):
        self.Api = ApiWindow()
        self.Api.show()
        self.Api.switch_window8.connect(self.show_welcome)


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()  # 控制器实例
    controller.show_Off()  # 默认展示的是关机页面
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




