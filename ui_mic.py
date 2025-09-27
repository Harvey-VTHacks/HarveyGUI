# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'miceQppuA.ui'
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
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(395, 200, 211, 211))  # Centered horizontally in 1000px window
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"    border-radius: 100px;   /* half of width/height \u2192 circle */\n"
"    border: none;\n"
"}\n"
"QToolButton:hover {\n"
"}\n"
"QToolButton:pressed {\n"
"}")
        icon = QIcon()
        icon.addFile(u"muted.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"microphone.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(200, 200))
        # Make the button checkable so it can toggle between On/Off states
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(False)  # Start in Off state

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 100, 600, 40))  # Wider and centered, moved up
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 450, 600, 40))  # Wider and centered, below button
        self.label_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))  # Match window width
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"I'm Harvey, your personal digital assistant. How can I help you today?", None))
        self.label.setStyleSheet("color: #333333;"             
            "font-size: 22px;"
            "font-weight: bold;"
            "qproperty-alignment: AlignCenter;"
            "padding: 10px;")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Click on the microphone button and start speaking.", None))

        self.label_2.setStyleSheet("color: #007bff;"
            "font-size: 18px;"
            "font-weight: italic;"
            "qproperty-alignment: AlignCenter;"
            "margin-top: 15px;")
