from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from ui_main import Ui_MainWindow
import sys
import random
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.random_number = None
        self.pushButton.clicked.connect(self.check_number)
        self.show_number_temporarily()

    def show_number_temporarily(self):
        # Генерируем случайное число
        self.random_number = random.randint(1, 1000000000)
        self.label_2.setText(str(self.random_number))

        # Таймер на 2 секунды
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(self.clear_label)
        timer.start(2000)

    def clear_label(self):
        # Очистка текста
        self.label_2.setText("")

    def check_number(self):
        user_number = self.spinBox.value()

        # Совпадение с random_number
        if user_number == self.random_number:
            self.label_2.setStyleSheet("background-color: green; color: white;")
        else:
            self.label_2.setStyleSheet("background-color: red; color: white;")
            self.shutdown_computer()

        # Таймер для сброса цвета и генерации нового числа
        reset_timer = QTimer(self)
        reset_timer.setSingleShot(True)
        reset_timer.timeout.connect(self.reset_label_and_generate_new)
        reset_timer.start(2000)

    def reset_label_and_generate_new(self):
        self.label_2.setStyleSheet(u"font-size: 30pt;\n"
                                 "color: rgb(221, 221, 221);\n"
                                 "background-color: rgba(255, 255, 255, 50);\n"
                                 "border: 1px solid rgba(255, 255, 255, 80);\n"
                                 "border-radius: 7px;\n"
                                 "")
        self.show_number_temporarily()

    def shutdown_computer(self):
        if sys.platform == "win32":
            os.system("shutdown /s /t 0")
        else:
            os.system("shutdown -h now")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())