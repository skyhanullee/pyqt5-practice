from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, time

from timer_ver_1 import Ui_WorkTimer


class QTimerWithPause(QTimer):
    def __init__(self, parent=None):
        QTimer.__init__(self, parent)
        self.startTime = 0
        self.interval = 0

    def start_timer(self, interval):
        self.interval = interval
        self.startTime = time.time()
        QTimer.start(self, interval, True)

    def pause(self):
        if self.isActive():
            self.stop()
            elapsedTime = self.startTime - time.time()
            self.startTime -= elapsedTime
            self.interval -= int(elapsedTime * 1000)

    def resume(self):
        if not self.isActive():
            self.start(self.interval)


class WorkTimer(QMainWindow):#, Ui_WorkTimer):
    # def __init__(self, parent=None):
    #     super(WorkTimer, self).__init__(parent)
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # self.setupUi(self)
        self.ui = Ui_WorkTimer()
        self.ui.setupUi(self)

        # Starting here is my edit.
        self.ui.start_stop_button.clicked.connect(self.print_test)
        self.ui.timer_lcd.display("10:00") # works
        # self.start_stop_button.clicked.connect(self.print_test)
        # self.timer_lcd.display("10:00") # works
        self.ex_timer = QTimerWithPause(self)
        self.ex_timer.setInterval(10)
        self.ex_timer.timeout.connect(self.update_time)

    def update_time(self):
        current_time = "00:00"
        self.timer_lcd.display(current_time)

    def print_test(self):
        alert = QtWidgets.QMessageBox()
        alert.setText("Successfully clicked.")
        alert.exec_()

    def show_child_window(self):
        self.child_window = Ui_WorkTimer(self)
        self.child_window.show()

    def setup_Ui(self, QMainWindow):
        test_window = Ui_WorkTimer()

        test_window.setupUi(MainWindow)

        self.ui.start_stop_button.clicked.connect(self.print_test)
        self.ui.timer_lcd.display("10:00") # works
        # self.start_stop_button.clicked.connect(self.print_test)
        # self.timer_lcd.display("10:00") # works
        self.ex_timer = QTimer(self)
        self.ex_timer.setInterval(10)
        self.ex_timer.timeout.connect(self.update_time)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    workout_timer_test = WorkTimer()
    # workout_timer_test.setupUi(MainWindow)
    workout_timer_test.setup_Ui(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_WorkTimer()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
