import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Mi login")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont('Ariel', 10))
        user_label.move(20,54)

        user_input = QLineEdit(self)
        user_input.resize(250,24)
        user_input.move(90,50)

        password_label = QLabel(self)
        password_label.setText("password: ")
        password_label.setFont(QFont('Ariel', 10))
        password_label.move(20,86)

        password_input = QLineEdit(self)
        password_input.resize(250,24)
        password_input.move(90,82)
        password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())