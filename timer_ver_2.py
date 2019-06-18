# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hanul\PycharmProjects\personal_projects\pyqt5_projects\timer_ver_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer, Qt, QElapsedTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber, QWidget, QGridLayout, QPushButton, QLayout
import time

# class Ui_TimerTwo(object):
#     def setupUi(self, TimerTwo):
#         TimerTwo.setObjectName("TimerTwo")
#         TimerTwo.resize(651, 413)
#         self.timer_lcd = QtWidgets.QLCDNumber(TimerTwo)
#         self.timer_lcd.setGeometry(QtCore.QRect(30, 30, 591, 211))
#         self.timer_lcd.setObjectName("timer_lcd")
#         start_stop_button = QtWidgets.QPushButton(TimerTwo)
#         start_stop_button.setGeometry(QtCore.QRect(30, 280, 281, 91))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         start_stop_button.setFont(font)
#         start_stop_button.setObjectName("start_stop_button")
#         pause_button = QtWidgets.QPushButton(TimerTwo)
#         pause_button.setGeometry(QtCore.QRect(340, 280, 281, 91))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         pause_button.setFont(font)
#         pause_button.setObjectName("pause_button")
#
#         self.retranslateUi(TimerTwo)
#         QtCore.QMetaObject.connectSlotsByName(TimerTwo)
#     def retranslateUi(self, TimerTwo):
#         _translate = QtCore.QCoreApplication.translate
#         TimerTwo.setWindowTitle(_translate("TimerTwo", "TimerTwo"))
#         start_stop_button.setText(_translate("TimerTwo", "Start/Stop"))
#         pause_button.setText(_translate("TimerTwo", "Pause"))


class TimerThree(QWidget):
    def __init__(self, parent=None):
        super(TimerThree, self).__init__(parent)

        self.setObjectName("TimerThree")
        self.setWindowTitle("TimerThree")
        self.resize(651, 413)

        self.timer_lcd = QtWidgets.QLCDNumber(self)
        # timer_lcd.setGeometry(QtCore.QRect(30, 30, 591, 211))
        self.timer_lcd.setObjectName("timer_lcd")
        self.timer_lcd.setSegmentStyle(QLCDNumber.Filled)

        self.isStarted = False
        self.isPaused = False

        start_stop_button = QPushButton("&Start/Stop")
        # start_stop_button.setGeometry(QtCore.QRect(30, 280, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        start_stop_button.setFont(font)
        start_stop_button.setObjectName("start_stop_button")
        start_stop_button.setFocusPolicy(Qt.NoFocus)

        pause_button = QPushButton("Pause")
        # pause_button.setGeometry(QtCore.QRect(340, 280, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        pause_button.setFont(font)
        pause_button.setObjectName("pause_button")
        pause_button.setFocusPolicy(Qt.NoFocus)

        main_layout = QGridLayout()
        # main_layout.setSizeConstraint(QLayout.SetFixedSize) # Cannot resize.
        main_layout.addWidget(start_stop_button, 2, 0)
        main_layout.addWidget(pause_button, 2, 1)
        main_layout.addWidget(self.timer_lcd, 1, 0, 1, 2)
        self.setLayout(main_layout)

        self.timer = QTimer()
        # start_stop_button.clicked.connect(self.basic_countdown())
        start_stop_button.clicked.connect(self.timer_start)
        self.el_timer = QElapsedTimer()
        pause_button.clicked.connect(self.timer_pause)

    def timer_start(self):
        if self.isPaused:
            return

        self.isStarted = True
        self.basic_countdown("00:05")

        # self.timer.start(self.timeoutTime(), self)

    def timer_pause(self):
        # if not self.isStarted:
        #     return
        #
        # self.isPaused = not self.isPaused
        # if self.isPaused:
        #     self.timer.stop()
        # else:
        #     # self.timer.start(self.timeoutTime(), self)
        #     print("")
        # self.update()
        self.timer_lcd.display("--:--")

    def show_time(self):
        time = QTime.currentTime()
        # time = self.timer.start(10)
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.timer_lcd.display(text)
        self.updateUi()

    def basic_countdown(self, input_time):
        # some_input = "00:05"
        some_input = input_time
        user_mins, user_secs = some_input.split(':')
        total_seconds = (int(user_mins) * 60) + int(user_secs)
        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            time.sleep(1)
            total_seconds -= 1
            self.timer_lcd.display(time_format)
            app.processEvents()  # just this one line allows display of 'i'
        time.sleep(1)
        self.timer_lcd.display("00:00")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # timer = Ui_TimerTwo()
    # timer.show()
    timer = TimerThree()
    timer.show()
    sys.exit(app.exec_())
