# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dialog_pref, webbrowser
from mission import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 372)
        MainWindow.setMinimumSize(QtCore.QSize(641, 372))
        MainWindow.setMaximumSize(QtCore.QSize(641, 372))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(220, 0, 421, 311))
        self.listWidget.setObjectName("listWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 181, 143))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        # self.checkBox.stateChanged.connect(lambda: print(self.checkBox.checkState() == 2))
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        #
        self.pushButton_2.clicked.connect(lambda: self.stopmission())
        self.pushButton_2.setDisabled(1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        # 启动按钮
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        #
        self.pushButton.clicked.connect(lambda: self.startmission())
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, 250, 239, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 641, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionPreferences)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.menuBar.setNativeMenuBar(False)

        self.label_6.setText(u'<a href="https://github.com/chinshin/cqbotgui"><b>Github.com/Chinshin/CQBotGUI</b></a>')
        self.label_6.linkActivated.connect(lambda: webbrowser.open_new('https://github.com/chinshin/CQBotGUI'))

        self.dialog1 = QtWidgets.QDialog()
        self.ui = dialog_pref.Ui_Dialog()
        self.ui.setupUi(self.dialog1)
        self.actionPreferences.triggered.connect(lambda: self.dialog1.open())




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "口袋"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
        self.checkBox_2.setText(_translate("MainWindow", "摩点"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.checkBox_3.setText(_translate("MainWindow", "微博"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "启动"))
        self.label.setText(_translate("MainWindow", "运行状态"))
        self.label_7.setText(_translate("MainWindow", "停止"))
        self.label_5.setText(_translate("MainWindow", "Chinshin Design"))
        self.label_6.setText(_translate("MainWindow", "https://Github.com/Chinshin/CQbotGUI"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))

    def startmission(self):
        # 获取三个checkbox状态
        switch_kd = self.checkBox.checkState()
        switch_md = self.checkBox_2.checkState()
        switch_wb = self.checkBox_3.checkState()
        # 禁止修改checbox
        self.checkBox.setDisabled(1)
        self.checkBox_2.setDisabled(1)
        self.checkBox_3.setDisabled(1)
        # 修改label_7为运行中
        self.label_7.setText('运行中')
        # 禁止点击开始按钮pushbutton
        self.pushButton.setDisabled(1)
        # 可以点击停止按钮pushbutton
        self.pushButton_2.setDisabled(0)
        # 发送 启动任务 请求
        self.listengroupthread = ListenGroup()
        self.listenkdmdwbthread = ListenKdMdWb(switch_kd, switch_md, switch_wb)
        self.listengroupthread.start()
        self.listenkdmdwbthread.start()

    def stopmission(self):
        # 可以修改checbox
        self.checkBox.setDisabled(0)
        self.checkBox_2.setDisabled(0)
        self.checkBox_3.setDisabled(0)
        # 修改label_7为停止
        self.label_7.setText('停止')
        # 可以点击开始按钮pushbutton
        self.pushButton.setDisabled(0)
        # 禁止点击停止按钮pushbutton
        self.pushButton_2.setDisabled(1)
        # 停止任务线程
        self.listengroupthread.terminate()
        self.listenkdmdwbthread.terminate()

    def customlog(self, content):
        self.listWidget.addItem(content)



