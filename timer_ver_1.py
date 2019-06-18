# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hanul\PycharmProjects\personal_projects\pyqt5_projects\timer_ver_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_WorkTimer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 466)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.list_display = QtWidgets.QListView(self.centralwidget)
        self.list_display.setGeometry(QtCore.QRect(370, 150, 161, 251))
        self.list_display.setObjectName("list_display")

        self.start_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_button.setGeometry(QtCore.QRect(20, 150, 141, 31))
        self.start_stop_button.setObjectName("start_stop_button")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.table_display = QtWidgets.QTableWidget(self.centralwidget)
        self.table_display.setGeometry(QtCore.QRect(180, 150, 161, 251))
        self.table_display.setObjectName("table_display")
        self.table_display.setColumnCount(0)
        self.table_display.setRowCount(0)

        self.timer_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.timer_lcd.setGeometry(QtCore.QRect(20, 10, 511, 121))
        self.timer_lcd.setObjectName("timer_lcd")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 20))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_stop_button.setText(_translate("MainWindow", "Start/Stop"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))


#
# class WorkTimer(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_WorkTimer()
#         self.ui.setupUi(self)
#
#         # Starting here is my edit.
#         # self.ui.start_stop_button.clicked.connect(self.print_test)
#     #     self.ui.timer_lcd.display("10:00") # works
#     #     self.ex_timer = QTimer(self)
#     #     self.ex_timer.setInterval(10)
#     #     self.ex_timer.timeout.connect(self.update_time)
#     #
#     # def update_time(self):
#     #     current_time = "00:00"
#     #     self.timer_lcd.display(current_time)
#     #
#     # def print_test(self):
#     #     alert = QtWidgets.QMessageBox()
#     #     alert.setText("Successfully clicked.")
#     #     alert.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_WorkTimer()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

