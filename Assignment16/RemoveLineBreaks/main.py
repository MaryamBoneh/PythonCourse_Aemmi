# This Python file uses the following encoding: utf-8
import sys
import os


from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Assignment16/RemoveLineBreaks/form.ui')
        self.ui.show()
        self.ui.btn_remove.clicked.connect(self.removeLineBreaks)
        self.ui.btn_reset.clicked.connect(self.reset)


    def removeLineBreaks(self):
        self.ui.txt_input.toPlainText().replace('\n', ' ')
        self.ui.txt_result.setText(self.ui.txt_input.toPlainText().replace('\n', ' '))
        
        
    def reset(self):
        self.ui.txt_input.setText('')
        self.ui.txt_result.setText('')
        

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()
    sys.exit(app.exec_())
