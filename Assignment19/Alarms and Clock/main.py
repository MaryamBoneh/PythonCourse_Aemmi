# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QProgressBar, QPushButton, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QThread, Qt, QLine
from PySide6.QtGui import QIcon
from functools import partial
import time


class Alarm(QThread):
    def __init__(self):
        QThread.__init__(self)
        pass


class Timer(QThread):
    duration = []

    def __init__(self):
        QThread.__init__(self)
        self.h = 0
        self.m = 0
        self.s = 0

    def add(self):
        gLaout = QGridLayout()
        self.label_name = QLabel()
        self.label_time = QLabel()
        # self.progressbar = QProgressBar()
        btn_del = QPushButton()
        btn_start = QPushButton()
        self.label_name.setText(widget.ui.txt_name_timer.text())
        self.label_time.setText(widget.ui.txt_value_timer.text())
        btn_del.setText('×')
        # self.progressbar.setValue(0)
        
        btn_start.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/play.png'))
        btn_del.setStyleSheet('min-width: 30px; max-width: 30px; font-size: 18px; min-height: 30px; border-radius: 15px; background-color: #000; color: #fff; margin-bottom: 15px;')
        btn_start.setStyleSheet('min-width: 30px; max-width: 30px; min-height: 30px; border-radius: 15px; background-color: #000; color: #fff; margin-bottom: 15px;')
        self.label_time.setStyleSheet('font: "Seven Segment"; font-size: 16px; padding-left: 20px; margin-bottom: 15px;')
        self.label_name.setStyleSheet('font: "Assignment19/Alarms and Clock/assets/font/Seven Segment"; font-size: 16px; padding-left: 5px; margin-bottom: 15px;')

        widget.ui.vl_timers.addLayout(gLaout, widget.length_timr)
        gLaout.addWidget(self.label_name, 0, 0, alignment=Qt.Alignment())
        gLaout.addWidget(self.label_time, 0, 1, alignment=Qt.Alignment())
        gLaout.addWidget(btn_del, 0, 2, alignment=Qt.Alignment())
        # gLaout.addWidget(self.progressbar, 2, 0, alignment=Qt.Alignment())
        gLaout.addWidget(btn_start, 0, 3, alignment=Qt.Alignment())

        btn_start.clicked.connect(Timer.pause)
        widget.length_timr += 1
        Timer.duration = self.label_time.text().split(':')
        self.h = int(Timer.duration[0])
        self.m = int(Timer.duration[1])
        self.s = int(Timer.duration[2])
        
        # self.total_sec = self.passed_sec = (self.h*3600 + self.m*60 + self.s)

    def decrease(self):
        # self.passed_sec -= 1
        if self.h == 0 and self.m == 0 and self.s == 0:
            return

        if self.s == 0 and self.m > 0:
            self.s = 59
            self.m -= 1

        if self.m == 0 and self.h > 0:
            self.m = 59
            self.h -= 1
        self.s -= 1

    def run(self):
        while True:
            self.decrease()
            # self.percent = (self.total_sec - self.passed_sec) * 100 / self.total_sec
            # self.progressbar.setValue(int(self.percent))
            self.label_time.setText(f"{self.h}:{self.m}:{self.s}")
            time.sleep(1)

    def pause(self):
        print('in pause')


class Stopwatch(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.h = 0
        self.m = 0
        self.s = 0

    def reset(self):
        self.h = 0
        self.m = 0
        self.s = 0

    def increase(self):
        self.s += 1
        if self.s >= 60:
            self.s = 0
            self.m += 1

        if self.m >= 60:
            self.m = 0
            self.h += 1

    def run(self):
        while True:
            self.increase()
            widget.ui.lbl_stopwatch.setText(f"{self.h}:{self.m}:{self.s}")
            time.sleep(1)


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Assignment19/Alarms and Clock/form.ui')

        self.ui.btn_stopwatch_start.clicked.connect(self.startStopWatch)
        self.ui.btn_stopwatch_save.clicked.connect(self.saveStopWatch)
        self.ui.btn_stopwatch_stop.clicked.connect(self.stopStopWatch)
        self.ui.btn_add_timer.clicked.connect(self.addTimer)
        self.ui.btn_add_timer.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/add.png'))

        self.stopwatch = Stopwatch()
        self.ui.show()
        self.length_stw = 0
        self.length_timr = 0

# -------------------------------------STOP WATCH----------------------------------------

    def pauseStopWatch(self):
        self.stopwatch.terminate()

    def stopStopWatch(self):
        self.stopwatch.terminate()
        self.stopwatch.reset()
        self.ui.lbl_stopwatch.setText("0:0:0")

    def startStopWatch(self):
        self.stopwatch.start()

    def saveStopWatch(self):
        self.length_stw += 1

        label_num = QLabel()
        label_total = QLabel()
        label_num.setText(str(self.length_stw))
        label_total.setText(self.ui.lbl_stopwatch.text())
        label_num.setStyleSheet('max-width: 50px; padding-left: 20px;')
        self.ui.gl_saved_times.addWidget(label_num, self.length_stw, 0, alignment=Qt.Alignment())
        self.ui.gl_saved_times.addWidget(label_total, self.length_stw, 1, alignment=Qt.Alignment())

# ---------------------------------------- TIMER -----------------------------------------

    def addTimer(self):
        self.timer = Timer()
        self.timer.add()
        self.timer.start()


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
