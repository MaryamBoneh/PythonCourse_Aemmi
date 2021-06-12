# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QProgressBar, QPushButton, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QThread, Qt, QLine
from PySide6.QtGui import  QIcon
from PySide6 import QtGui
from win10toast import ToastNotifier
from functools import partial
from datetime import datetime
import time
import winsound


class Alarm(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.h = widget.ui.spinBox_h.value()
        self.m = widget.ui.spinBox_m.value()
        self.s = widget.ui.spinBox_s.value()
        
    def check(self):    
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = current_time.split(':')
        
        if self.h == int(current_time[0]) and self.m == int(current_time[1]) and self.s == int(current_time[2]):
            self.toast = ToastNotifier()
            self.toast.show_toast("Alarm Time", "barkhiiiiiz azizam", duration=20, icon_path="Assignment19/Alarms and Clock/assets/img/icon.png")

    def run(self):
        while True:
            self.check()
            time.sleep(1)


class Timer(QThread):
    duration = []

    def __init__(self):
        QThread.__init__(self)
        self.h = 0
        self.m = 0
        self.s = 0

    def add(self):
        widget.ui.lbl_name_timer.setText(widget.ui.txt_name_timer.text())
        widget.ui.lbl_time_timer.setText(widget.ui.txt_value_timer.text())
        
        Timer.duration = widget.ui.lbl_time_timer.text().split(':')
        self.h = int(Timer.duration[0])
        self.m = int(Timer.duration[1])
        self.s = int(Timer.duration[2])

        
    def decrease(self):
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
            widget.ui.lbl_time_timer.setText(f"{self.h}:{self.m}:{self.s}")
            time.sleep(1)
        

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
        self.ui.setWindowIcon(QtGui.QIcon('Assignment19/Alarms and Clock/assets/img/icon.png'))
        self.ui.show()
        

#----------------------------------- STOP WATCH UI --------------------------------------

        self.ui.btn_stopwatch_start.clicked.connect(self.startStopWatch)
        self.ui.btn_stopwatch_save.clicked.connect(self.saveStopWatch)
        self.ui.btn_stopwatch_stop.clicked.connect(self.stopStopWatch)
        self.ui.btn_add_timer.clicked.connect(self.addTimer)
        self.ui.btn_add_timer.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/add.png'))
        self.ui.btn_stopwatch_start.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/play.png'))
        self.ui.btn_stopwatch_stop.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/pause.png'))
        self.ui.btn_stopwatch_save.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/flag.png'))

        self.stopwatch = Stopwatch()
        self.length_stw = 0
        
#-------------------------------------- TIMER UI ----------------------------------------
       
        self.ui.timer_btn_start.clicked.connect(self.resumeTimer)
        self.ui.timer_btn_pause.clicked.connect(self.pauseTimer)
        self.ui.timer_btn_del.clicked.connect(self.stopTimer)
        self.ui.timer_btn_start.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/play.png'))
        self.ui.timer_btn_pause.setIcon(QIcon('Assignment19/Alarms and Clock/assets/img/pause.png'))
        self.ui.timer_btn_del.setText('×')
        
#-------------------------------------- ALARM UI ----------------------------------------

        self.ui.btn_alarm_set.clicked.connect(self.setAlarm)
        self.alarmOn = False

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

    def pauseTimer(self):
        self.timer.terminate()
        
    def resumeTimer(self):
        self.timer.start()        
        
    def stopTimer(self):
        self.timer.terminate()
        self.ui.lbl_name_timer.setText("")
        self.ui.lbl_time_timer.setText("0:0:0")
        self.ui.txt_name_timer.setText("")
        self.ui.txt_value_timer.setText("")
        
# ---------------------------------------- ALARM -----------------------------------------

    def setAlarm(self):
        self.alarm = Alarm()
        self.alarm.start()


       
if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
