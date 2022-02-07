import sys

import API

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./untitled.ui", self)
        MyWidget.setWindowTitle(self, "YandexMaps")

        self.pushButton.clicked.connect(self.view_picture)
        self.maps = API.Maps()

    def view_picture(self):
        try:
            self.maps.coords = (int(self.lineEdit_2.text()), int(self.lineEdit_3.text()))
            self.maps.zoom = int(self.lineEdit_3.text())
        except ValueError:
            print("Вы ввели некоректные данные")

        self.im = QPixmap("./abc.jpg")
        self.label_4.setPixmap(self.im)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
