import socket
import threading
import pickle

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QFont

import main_window_file


class MemoryGame(QMainWindow, main_window_file.Ui_MainWindow):
    def __init__(self):
        super(MemoryGame, self).__init__()
        self.setupUi(self)

        self.client = socket.socket()
        self.client.connect(('127.0.0.1', 5116))

        self.pushButton.clicked.connect(self.nickname_was_chosen)

        self.pushButton_1.clicked.connect(lambda: self.btn_clicked(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.btn_clicked(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.btn_clicked(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.btn_clicked(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.btn_clicked(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.btn_clicked(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.btn_clicked(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.btn_clicked(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.btn_clicked(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: self.btn_clicked(self.pushButton_10))
        self.pushButton_11.clicked.connect(lambda: self.btn_clicked(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.btn_clicked(self.pushButton_12))
        self.pushButton_13.clicked.connect(lambda: self.btn_clicked(self.pushButton_13))
        self.pushButton_14.clicked.connect(lambda: self.btn_clicked(self.pushButton_14))
        self.pushButton_15.clicked.connect(lambda: self.btn_clicked(self.pushButton_15))
        self.pushButton_16.clicked.connect(lambda: self.btn_clicked(self.pushButton_16))
        self.pushButton_17.clicked.connect(lambda: self.btn_clicked(self.pushButton_17))
        self.pushButton_18.clicked.connect(lambda: self.btn_clicked(self.pushButton_18))
        self.pushButton_19.clicked.connect(lambda: self.btn_clicked(self.pushButton_19))
        self.pushButton_20.clicked.connect(lambda: self.btn_clicked(self.pushButton_20))
        self.pushButton_21.clicked.connect(lambda: self.btn_clicked(self.pushButton_21))
        self.pushButton_22.clicked.connect(lambda: self.btn_clicked(self.pushButton_22))
        self.pushButton_23.clicked.connect(lambda: self.btn_clicked(self.pushButton_23))
        self.pushButton_24.clicked.connect(lambda: self.btn_clicked(self.pushButton_24))
        self.pushButton_25.clicked.connect(lambda: self.btn_clicked(self.pushButton_25))
        self.pushButton_26.clicked.connect(lambda: self.btn_clicked(self.pushButton_26))
        self.pushButton_27.clicked.connect(lambda: self.btn_clicked(self.pushButton_27))
        self.pushButton_28.clicked.connect(lambda: self.btn_clicked(self.pushButton_28))
        self.pushButton_29.clicked.connect(lambda: self.btn_clicked(self.pushButton_29))
        self.pushButton_30.clicked.connect(lambda: self.btn_clicked(self.pushButton_30))
        self.pushButton_31.clicked.connect(lambda: self.btn_clicked(self.pushButton_31))
        self.pushButton_32.clicked.connect(lambda: self.btn_clicked(self.pushButton_32))
        self.pushButton_33.clicked.connect(lambda: self.btn_clicked(self.pushButton_33))
        self.pushButton_34.clicked.connect(lambda: self.btn_clicked(self.pushButton_34))
        self.pushButton_35.clicked.connect(lambda: self.btn_clicked(self.pushButton_35))
        self.pushButton_36.clicked.connect(lambda: self.btn_clicked(self.pushButton_36))

        self.buttons_list = [self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                             self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8,
                             self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12,
                             self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16,
                             self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20,
                             self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24,
                             self.pushButton_25, self.pushButton_26, self.pushButton_27, self.pushButton_28,
                             self.pushButton_29, self.pushButton_30, self.pushButton_31, self.pushButton_32,
                             self.pushButton_33, self.pushButton_34, self.pushButton_35, self.pushButton_36]

    def nickname_was_chosen(self):
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)

        # self.client.send(self.lineEdit.text().encode('utf-8'))
        self.player_1.setText(f'Игрок: {self.lineEdit.text()}')
        self.label.setText(f'Счет: 0')
        #
        # thread = threading.Thread(args=(client,))
        # thread.start()

    # def all_letters(self):
    #     data = self.client.recv(4096)
    #     n_data = pickle.loads(data)
    #     return n_data

    def btn_clicked(self, b):
        # position = self.buttons_list.index(b)
        # self.client.send(str(position).encode('utf-8'))
        # p = self.client.recv(1024).decode('utf-8')

        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        b.setFont(font)
        b.setText('e')
        b.setEnabled(False)

    def two_btn_clicked(self):
        while True:
            for i in range(36):
                for j in range(36):
                    if i == j:
                        continue
                    elif not self.buttons_list[i].isEnabled() and not self.buttons_list[j].isEnabled():
                        for el in self.buttons_list:
                            el.setEnabled(False)


app = QApplication([])
window = MemoryGame()
window.show()
app.exec()
