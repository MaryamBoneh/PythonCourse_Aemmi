# This Python file uses the following encoding: utf-8
import sys
import os
from Database import Database

from PySide6.QtWidgets import QApplication, QLabel, QMessageBox, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Assignment18/MessageBox/form.ui')
        self.ui.show()

        self.ui.btn_send.clicked.connect(self.addNewMessage)
        self.readMessages()

    def readMessages(self):
        messages = Database.select()
        for message in messages:
            label = QLabel()
            label.setText(message[1] + ": " + message[2])
            self.ui.vl_messages.addWidget(label)

    def addNewMessage(self):
        name = self.ui.txt_name.text()
        text = self.ui.txt_message.text()

        if name != "" and text != "":
            response = Database.insert(name, text)
            if response:
                label = QLabel()
                label.setText(name + ": " + text)
                self.ui.vl_messages.addWidget(label)

                self.ui.txt_name.setText("")
                self.ui.txt_message.setText("")

                msg_box = QMessageBox()
                msg_box.setText("Your message sent successfully!")
                msg_box.exec_()

            else:
                msg_box = QMessageBox()
                msg_box.setText("Database error!")
                msg_box.exec_()
        else:
            msg_box = QMessageBox()
            msg_box.setText("Error: feilds are empty!")
            msg_box.exec_()


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
