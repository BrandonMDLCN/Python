import FormInicio
import FormAgregar
import FormBuscador
import FormEditar
from PyQt6 import QtCore, QtGui, QtWidgets


class abrirFormularios(QtWidgets, )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Inicio = QtWidgets.QWidget()
    ui = FormInicio.Ui_Form_Inicio()
    ui.setupUi(Form_Inicio)
    Form_Inicio.show()
    sys.exit(app.exec())