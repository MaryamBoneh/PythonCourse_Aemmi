import sys
import os
import math

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from functools import partial


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Assignment15/form.ui')
        self.ui.show()
        self.ui.textEdit.setText('0')
        
        self.num = ''
        self.temp_num = ''
        self.opr = ''

        self.ui.btn_zero.clicked.connect(partial(self.enter_num, 0))
        self.ui.btn_one.clicked.connect(partial(self.enter_num, 1))
        self.ui.btn_two.clicked.connect(partial(self.enter_num, 2))
        self.ui.btn_three.clicked.connect(partial(self.enter_num, 3))
        self.ui.btn_four.clicked.connect(partial(self.enter_num, 4))
        self.ui.btn_five.clicked.connect(partial(self.enter_num, 5))
        self.ui.btn_six.clicked.connect(partial(self.enter_num, 6))
        self.ui.btn_seven.clicked.connect(partial(self.enter_num, 7))
        self.ui.btn_eight.clicked.connect(partial(self.enter_num, 8))
        self.ui.btn_nine.clicked.connect(partial(self.enter_num, 9))

        self.ui.btn_mul.clicked.connect(self.enter_mul)
        self.ui.btn_divide.clicked.connect(self.enter_divid)
        self.ui.btn_sub.clicked.connect(self.enter_sub)
        self.ui.btn_plus.clicked.connect(self.enter_plus)
        self.ui.btn_tan.clicked.connect(self.enter_tan)
        self.ui.btn_cos.clicked.connect(self.enter_cos)
        self.ui.btn_sin.clicked.connect(self.enter_sin)

        self.ui.btn_equal.clicked.connect(self.enter_equal)
        self.ui.btn_clear.clicked.connect(self.enter_clear)
        self.ui.btn_dote.clicked.connect(self.enter_dote)

    def enter_num(self, n):
        self.num = self.num + str(n)
        if self.temp_num:
            self.ui.textEdit.setText(
                str(self.temp_num) + (self.opr) + str(self.num))
        else:
            self.ui.textEdit.setText(str(self.num))

    def enter_mul(self):
        if (self.num or self.temp_num):
            if self.opr:
                if self.num:
                    self.temp_num = str(self.amaliat())
                    self.num = ''
                    self.ui.textEdit.setText((str(self.temp_num) + "*"))
                else:
                    self.ui.textEdit.setText((str(self.temp_num) + "*"))
            else:
                self.ui.textEdit.setText((str(self.num) + "*"))
                self.temp_num = self.num
                self.num = ''
            self.opr = '*'

    def enter_divid(self):
        if (self.num or self.temp_num):
            if self.opr:
                if self.num:
                    self.temp_num = str(self.amaliat())
                    self.num = ''
                    self.ui.textEdit.setText((str(self.temp_num) + "/"))
                else:
                    self.ui.textEdit.setText((str(self.temp_num) + "/"))
            else:
                self.ui.textEdit.setText((str(self.num) + "/"))
                self.temp_num = self.num
                self.num = ''
            self.opr = '/'

    def enter_sub(self):
        if (self.num or self.temp_num):
            if self.opr:
                if self.num:
                    self.temp_num = str(self.amaliat())
                    self.num = ''
                    self.ui.textEdit.setText((str(self.temp_num) + "-"))
                else:
                    self.ui.textEdit.setText((str(self.temp_num) + "-"))

            else:
                self.ui.textEdit.setText((str(self.num) + "-"))
                self.temp_num = self.num
                self.num = ''
            self.opr = '-'

    def enter_plus(self):
        if (self.num or self.temp_num):
            if self.opr:
                if self.num:
                    self.temp_num = str(self.amaliat())
                    self.num = ''
                    self.ui.textEdit.setText((str(self.temp_num) + "+"))
                else:
                    self.ui.textEdit.setText((str(self.temp_num) + "+"))
            else:
                self.ui.textEdit.setText((str(self.num) + "+"))
                self.temp_num = self.num
                self.num = ''
            self.opr = '+'

    def enter_tan(self):
        if self.num:
            self.ui.textEdit.setText(str(math.tan(float(self.num))))
        elif self.temp_num:
            self.ui.textEdit.setText(str(math.tan(float(self.temp_num))))
        self.num = ''

    def enter_cos(self):
        if self.num:
            self.ui.textEdit.setText(str(math.cos(float(self.num))))
        elif self.temp_num:
            self.ui.textEdit.setText(str(math.cos(float(self.temp_num))))
        self.num = ''

    def enter_sin(self):
        if self.num:
            self.ui.textEdit.setText(str(math.sin(float(self.num))))
        elif self.temp_num:
            self.ui.textEdit.setText(str(math.sin(float(self.temp_num))))
        self.num = ''

    def enter_dote(self):
        if (self.num.count('.') == 0):
            self.num = self.num + '.'
            if self.temp_num:
                self.ui.textEdit.setText(
                    str(self.temp_num) + (self.opr) + str(self.num))
            else:
                self.ui.textEdit.setText(str(self.num))

    def enter_equal(self):
        self.temp_num = float("{:.2f}".format(float(self.temp_num)))
        self.num = float("{:.2f}".format(float(self.num)))
        if self.opr == '*':
            self.ui.textEdit.setText(str(self.temp_num * self.num))
            self.temp_num = self.num * self.temp_num
        elif self.opr == '/':
            self.ui.textEdit.setText(str(self.temp_num / self.num))
            self.temp_num = self.num / self.temp_num
        elif self.opr == '-':
            self.ui.textEdit.setText(str(self.temp_num - self.num))
            self.temp_num = self.num - self.temp_num
        elif self.opr == '+':
            self.ui.textEdit.setText(str(self.temp_num + self.num))
            self.temp_num = self.num + self.temp_num
        else:
            self.ui.textEdit.setText('')
        self.num = ''

    def amaliat(self):
        self.temp_num = float("{:.2f}".format(float(self.temp_num)))
        self.num = float("{:.2f}".format(float(self.num)))
        if self.opr == '*':
            return float("{:.2f}".format(float(self.temp_num * self.num)))
        elif self.opr == '/':
            return float("{:.2f}".format(float(self.temp_num / self.num)))
        elif self.opr == '-':
            return float("{:.2f}".format(float(self.temp_num - self.num)))
        else:
            return float("{:.2f}".format(float(self.temp_num + self.num)))

    def enter_clear(self):
        self.num = ''
        self.temp_num = ''
        self.opr = ''
        self.ui.textEdit.setText("0")

#------------------- END CLASS MAIM -------------------#


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
