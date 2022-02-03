import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QLabel
from PIL import Image
from io import BytesIO

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
        #self.ui.monitor.clear()
        coord = self.ui.line_cord.text()
        if coord == '' or coord == 'Введите координаты':
            pass
        else:
            coord = coord.split()
            try:
                self.show_map(coord)
            except Exception():
                pass

    def show_map(self, coord):
        try:
            delta = self.ui.sp_size.text()
            print(delta)
            toponym_longitude, toponym_lattitude = coord[0], coord[1]
            # Собираем параметры для запроса к StaticMapsAPI:
            map_params = {
                "ll": ",".join([toponym_longitude, toponym_lattitude]),
                "spn": ",".join([delta, delta]),
                "l": "map"
            }
            map_api_server = "http://static-maps.yandex.ru/1.x/"
            # ... и выполняем запрос
            response = requests.get(map_api_server, params=map_params)
            map_file = "data/map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            pixmap = QPixmap('data/map.png')
            self.ui.monitor.setPixmap(pixmap)
        except Exception():
            print('ERROR')


main()
