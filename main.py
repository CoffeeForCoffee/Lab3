from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from ui_main import Ui_MainWindow
import sys
import random

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show_number_temporarily()

    def show_number_temporarily(self):
        # Генерируем случайное число
        random_number = random.randint(1, 1000000000)
        self.label_2.setText(str(random_number))

        # Создаем таймер
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(self.clear_label)
        timer.start(2000)

    # Исчезновение числа
    def clear_label(self):
        self.label_2.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())