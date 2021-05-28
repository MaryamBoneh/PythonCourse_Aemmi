import sys
import os
import urllib.request

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QDir


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('Assignment17/Downloader/form.ui')
        self.ui.show()

        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_browse.clicked.connect(self.browse_file)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(
            self, caption="Save File As", filter="All Files (*.*)", dir=".")
        
        self.ui.txt_dest.setText(save_file[0])

    def download(self):
        url = self.ui.txt_url.text()
        save_location = self.ui.txt_dest.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed!")
            return

        QMessageBox.information(self, "Information", "The download is complete!")
        self.ui.progressBar.setValue(0)
        self.ui.txt_url.setText('')
        self.ui.txt_dest.setText('')

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize

        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.ui.progressBar.setValue(int(percent))


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()
    sys.exit(app.exec_())
