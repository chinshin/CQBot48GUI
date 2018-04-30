# -*- coding: utf-8 -*-
import sys
import mainwindow, dialog_pref
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

if __name__ == '__main__':
    # init
    app = QApplication(sys.argv)
    # main

    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # quit
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # dialog1 = QDialog()
    # ui = dialog_pref.Ui_Dialog()
    # ui.setupUi(dialog1)
    # dialog1.show()
    # sys.exit(app.exec_())

#
# self.dialog1 = QtWidgets.QDialog()
# self.ui = dialog_pref.Ui_Dialog()
# self.ui.setupUi(self.dialog1)
#
# self.actionPreferences.triggered.connect(lambda: self.dialog1.open())
#
# self.menuBar.setNativeMenuBar(False)
# self.label_6.setText(u'<a href="https://github.com/chinshin/cqbotgui"><b>Github.com/Chinshin/CQBotGUI</b></a>')
# self.label_6.linkActivated.connect(lambda: webbrowser.open_new('https://github.com/chinshin/CQBotGUI'))
#
