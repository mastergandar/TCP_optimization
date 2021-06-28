# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCP.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(322, 406)
        MainWindow.setMinimumSize(QtCore.QSize(322, 406))
        MainWindow.setMaximumSize(QtCore.QSize(322, 406))
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#151a1e;")
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 301, 381))
        self.splitter.setStyleSheet("background-color:#151a1e;\n"
"")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #1c1f1f;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #2c2f2f;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #1c1f1f;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #2c2f2f;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser.setCurrentFont(QFont("Courier New"))
        self.textBrowser.setFontPointSize(8)
        self.textBrowser.setStyleSheet("QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"    background-color: #222b2e;\n"
"    color: #d3dae3;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TCP Optimizer"))
        self.pushButton.setText(_translate("MainWindow", "Диагностика"))
        self.pushButton_2.setText(_translate("MainWindow", "Оптимизация"))
