import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow
import random


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        n = random.randrange(10, 300)
        colors = [Qt.red, Qt.yellow, Qt.green, Qt.blue]
        painter = QPainter(self)
        painter.setBrush(QBrush(random.choice(colors), Qt.SolidPattern))
        painter.drawEllipse(10, 10, n, n)

    def update_draw(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
