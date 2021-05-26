# This Python file uses the following encoding: utf-8
import sys
import os
import random


from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Assignment16/RandomPasswordGenerator/form.ui')
        self.ui.show()

        self.ui.btn_1.clicked.connect(self.GeneratePass_1)
        self.ui.btn_2.clicked.connect(self.GeneratePass_2)
        self.ui.btn_3.clicked.connect(self.GeneratePass_3)
        self.string = ''

    def GeneratePass_1(self):
        self.string = ''
        uppercase = chr(random.randint(65, 90))
        special_char = chr(random.randint(33, 47))
        number = str(random.randint(0, 9))
        rand_list = random.sample(range(8), 3)

        for i in range(8):
            self.string = self.string + chr(random.randint(97, 122))

        self.string = list(self.string)
        
        self.string[rand_list[0]] = uppercase
        self.string[rand_list[1]] = special_char
        self.string[rand_list[2]] = number

        self.string = "".join(list(self.string))
        self.ui.txt_1.setText(self.string)


    def GeneratePass_2(self):
        
        self.string = ''
        uppercase = random.sample(range(65, 90), 2)
        special_char = random.sample(range(33, 47), 2)
        number = random.sample(range(0, 9), 2) 
        rand_list = random.sample(range(12), 6)
        
        for i in range(12):
            self.string = self.string + chr(random.randint(97, 122))

        self.string = list(self.string)
        self.string[rand_list[0]] = chr(uppercase[0])
        self.string[rand_list[1]] = chr(uppercase[1])
        self.string[rand_list[2]] = chr(special_char[0])
        self.string[rand_list[3]] = chr(special_char[1])
        self.string[rand_list[4]] = str(number[0])
        self.string[rand_list[5]] = str(number[1])

        self.string = "".join(list(self.string))
        self.ui.txt_2.setText(self.string)


    def GeneratePass_3(self):
                
        self.string = ''
        uppercase = random.sample(range(65, 90), 3)
        special_char = random.sample(range(33, 47), 2)
        number = random.sample(range(0, 9), 3) 
        rand_list = random.sample(range(20), 8)
        
        for i in range(20):
            self.string = self.string + chr(random.randint(97, 122))

        self.string = list(self.string)
        self.string[rand_list[0]] = chr(uppercase[0])
        self.string[rand_list[1]] = chr(uppercase[1])
        self.string[rand_list[2]] = chr(uppercase[2])
        self.string[rand_list[3]] = chr(special_char[0])
        self.string[rand_list[4]] = chr(special_char[1])
        self.string[rand_list[5]] = str(number[0])
        self.string[rand_list[6]] = str(number[1])
        self.string[rand_list[7]] = str(number[2])

        self.string = "".join(list(self.string))
        self.ui.txt_3.setText(self.string)


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()
    sys.exit(app.exec_())
