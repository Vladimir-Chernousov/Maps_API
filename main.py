import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QLabel

import main_window_designe


def main():
    # создаём приложение и запускаем его
    app2 = QApplication(sys.argv)
    ex2 = MainProgramm()
    ex2.show()
    app2.exec_()


class MainProgramm(QWidget):
    def __init__(self):
        super(MainProgramm, self).__init__()
        self.ui = main_window_designe.Ui_Form()
        self.ui.setupUi(self)
        pixmap = QPixmap('data/fon_maps.png')
        self.ui.monitor.setPixmap(pixmap)
        self.ui.btn_search.clicked.connect(self.run)

    def run(self):
        self.ui.monitor.clear()


main()
