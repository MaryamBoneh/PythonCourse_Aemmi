# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QThread, Qt
import time


class Timer(QThread):
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

        self.timer = Timer()
        self.ui.show()
        self.length = 0

    def pauseStopWatch(self):
        self.timer.terminate()

    def stopStopWatch(self):
        self.timer.terminate()
        self.timer.reset()
        self.ui.lbl_stopwatch.setText("0:0:0")

    def startStopWatch(self):
        self.timer.start()

    def saveStopWatch(self):
        self.length += 1
        # last_saved = self.ui.lbl_stopwatch.text().split(':')
        
        # h = Timer.h - int(last_saved[0])
        # m = Timer.m - int(last_saved[1])
        # s = Timer.s - int(last_saved[2])
        
        # if s < 0:
        #     s += 60
        #     m -= 1
        # if m < 0:
        #     m += 60
        #     h -= 1
        
        label_num = QLabel()
        # label_time = QLabel()
        label_total = QLabel()
        label_num.setText(str(self.length))
        # label_time.setText(f'{h}:{m}:{s}')
        label_total.setText(self.ui.lbl_stopwatch.text())
        label_num.setStyleSheet('max-width: 50px; padding-left: 20px;')
        self.ui.gl_saved_times.addWidget(label_num, self.length, 0, alignment=Qt.Alignment())
        # self.ui.gl_saved_times.addWidget(label_time, self.length, 1, alignment=Qt.Alignment())
        self.ui.gl_saved_times.addWidget(label_total, self.length, 1, alignment=Qt.Alignment())


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
