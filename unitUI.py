import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont, QIcon
from writeNumber import buttonHandler as bh


bh = bh()


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.unitUI()
        self.save_operation = []

    def unitUI(self):
        # отрисовка программы
        # главное окно
        window = QWidget(self)
        window.setGeometry(0, 0, 330, 460)
        window.setStyleSheet("background-color: rgb(126, 227, 255);"
                             "background-image: url(pngtree-beautiful-anime-scene-background-image_810743.jpg)")
        self.setGeometry(200, 200, 330, 460)

        # вывод
        self.label = QLabel('0', self)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setGeometry(QRect(0, 0, 310, 60))
        self.label.setStyleSheet("background-color: rgb(223, 140, 255); color: rgb(255, 255, 255); padding: 28px 0 0 0")
        self.label.move(10, 20)
        self.label.setAlignment(Qt.AlignRight)

        # вывод
        self.label_2 = QLabel('0', self)
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setGeometry(QRect(0, 0, 310, 30))
        self.label_2.setStyleSheet(
            "background-color: rgb(223, 140, 255); color: rgb(255, 255, 255); padding: 10px 5px 0 0")
        self.label_2.move(10, 20)
        self.label_2.setAlignment(Qt.AlignRight)

        # кнопка С
        self.button_c = QPushButton('c', self)
        self.button_c.setFont(font)
        self.button_c.setGeometry(10, 100, 70, 60)
        self.button_c.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка дел
        self.button_del = QPushButton('del', self)
        self.button_del.setFont(font)
        self.button_del.setGeometry(90, 100, 70, 60)
        self.button_del.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка процент
        self.button_percent = QPushButton('%', self)
        self.button_percent.setFont(font)
        self.button_percent.setGeometry(170, 100, 70, 60)
        self.button_percent.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка *
        self.button_star = QPushButton('*', self)
        self.button_star.setFont(font)
        self.button_star.setGeometry(250, 100, 70, 60)
        self.button_star.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 7
        self.button_7 = QPushButton('7', self)
        self.button_7.setFont(font)
        self.button_7.setGeometry(10, 170, 70, 60)
        self.button_7.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 8
        self.button_8 = QPushButton('8', self)
        self.button_8.setFont(font)
        self.button_8.setGeometry(90, 170, 70, 60)
        self.button_8.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 9
        self.button_9 = QPushButton('9', self)
        self.button_9.setFont(font)
        self.button_9.setGeometry(170, 170, 70, 60)
        self.button_9.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка /
        self.button_div = QPushButton('/', self)
        self.button_div.setFont(font)
        self.button_div.setGeometry(250, 170, 70, 60)
        self.button_div.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 4
        self.button_4 = QPushButton('4', self)
        self.button_4.setFont(font)
        self.button_4.setGeometry(10, 240, 70, 60)
        self.button_4.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 5
        self.button_5 = QPushButton('5', self)
        self.button_5.setFont(font)
        self.button_5.setGeometry(90, 240, 70, 60)
        self.button_5.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 6
        self.button_6 = QPushButton('6', self)
        self.button_6.setFont(font)
        self.button_6.setGeometry(170, 240, 70, 60)
        self.button_6.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка -
        self.button_minus = QPushButton('-', self)
        self.button_minus.setFont(font)
        self.button_minus.setGeometry(250, 240, 70, 60)
        self.button_minus.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 1
        self.button_1 = QPushButton('1', self)
        self.button_1.setFont(font)
        self.button_1.setGeometry(10, 310, 70, 60)
        self.button_1.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 2
        self.button_2 = QPushButton('2', self)
        self.button_2.setFont(font)
        self.button_2.setGeometry(90, 310, 70, 60)
        self.button_2.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 3
        self.button_3 = QPushButton('3', self)
        self.button_3.setFont(font)
        self.button_3.setGeometry(170, 310, 70, 60)
        self.button_3.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка +
        self.button_plus = QPushButton('+', self)
        self.button_plus.setFont(font)
        self.button_plus.setGeometry(250, 310, 70, 60)
        self.button_plus.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 0
        self.button_0 = QPushButton('0', self)
        self.button_0.setFont(font)
        self.button_0.setGeometry(10, 380, 150, 60)
        self.button_0.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка dot
        self.button_dot = QPushButton('.', self)
        self.button_dot.setFont(font)
        self.button_dot.setGeometry(170, 380, 70, 60)
        self.button_dot.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка =
        self.button_equal = QPushButton('=', self)
        self.button_equal.setFont(font)
        self.button_equal.setGeometry(250, 380, 70, 60)
        self.button_equal.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")
        self.functions()
        self.show()

    def functions(self):
        # кнопки цифры
        self.button_1.clicked.connect(lambda: bh.write_number(self.button_1.text(), self.label, self.display_2, self.save_operation))
        self.button_2.clicked.connect(lambda: bh.write_number(self.button_2.text(), self.label, self.display_2, self.save_operation))
        self.button_3.clicked.connect(lambda: bh.write_number(self.button_3.text(), self.label, self.display_2, self.save_operation))
        self.button_4.clicked.connect(lambda: bh.write_number(self.button_4.text(), self.label, self.display_2, self.save_operation))
        self.button_5.clicked.connect(lambda: bh.write_number(self.button_5.text(), self.label, self.display_2, self.save_operation))
        self.button_6.clicked.connect(lambda: bh.write_number(self.button_6.text(), self.label, self.display_2, self.save_operation))
        self.button_7.clicked.connect(lambda: bh.write_number(self.button_7.text(), self.label, self.display_2, self.save_operation))
        self.button_8.clicked.connect(lambda: bh.write_number(self.button_8.text(), self.label, self.display_2, self.save_operation))
        self.button_9.clicked.connect(lambda: bh.write_number(self.button_9.text(), self.label, self.display_2, self.save_operation))
        self.button_0.clicked.connect(lambda: bh.write_number(self.button_0.text(), self.label, self.display_2, self.save_operation))

        # кнопки операторы
        self.button_plus.clicked.connect(lambda: bh.func_operation(self.button_plus.text(), self.label, self.display_2, self.save_operation))
        self.button_minus.clicked.connect(lambda: bh.func_operation(self.button_minus.text(), self.label, self.display_2, self.save_operation))
        self.button_div.clicked.connect(lambda: bh.func_operation(self.button_div.text(), self.label, self.display_2, self.save_operation))
        self.button_star.clicked.connect(lambda: bh.func_operation(self.button_star.text(), self.label, self.display_2, self.save_operation))
        self.button_dot.clicked.connect(lambda: bh.func_dot(self.label, self.save_operation))

        # функция равно и процент
        self.button_equal.clicked.connect(lambda: bh.func_equal(self.label, self.display_2, self.save_operation))
        self.button_percent.clicked.connect(lambda: bh.func_percent(self.save_operation))

        # del c
        self.button_del.clicked.connect(lambda: bh.func_del(self.label, self.display_2, self.save_operation))
        self.button_c.clicked.connect(lambda: bh.func_c(self.label, self.display_2, self.save_operation))

    def display_2(self, mean):
        display2 = ''.join(mean)
        self.label_2.setText(display2)
        if self.save_operation == []:
            self.label_2.setText(display2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appCalc = UI()
    appCalc.setWindowTitle('Calculator')
    app.setWindowIcon(QIcon('imgCalc.png'))
    MainWindow = QMainWindow()
    MainWindow.setWindowIcon(QIcon('imgCalc.png'))
    sys.exit(app.exec_())
