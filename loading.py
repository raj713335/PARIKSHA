# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingidPIBG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFame = QFrame(self.centralwidget)
        self.DropShadowFame.setObjectName(u"DropShadowFame")
        self.DropShadowFame.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(56, 58, 89);\n"
"	color:rgb(220,220,220);\n"
"	border-radius: 10px;\n"
"}")
        self.DropShadowFame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.DropShadowFame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 60, 661, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.DropShadowFame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 130, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.DropShadowFame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 280, 601, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(98,114,164);\n"
"	color: rgb(200,200,200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255), stop: 1 rgba(170,85,255,255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.DropShadowFame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 300, 661, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.DropShadowFame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 340, 641, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.DropShadowFame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<strong>PARIKSHA</strong>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<strong>Distant Offline Examination System</Strong>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"loading...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<strong>Created :</strong> Arnab Das <strong> For</strong> Hack 2021", None))
    # retranslateUi
