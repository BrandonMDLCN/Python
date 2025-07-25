from PyQt6 import QtCore, QtGui, QtWidgets
import FormAgregar
import sys

class Ui_Form_Inicio(object):
    def setupUi(self, Form_Inicio):
        Form_Inicio.setObjectName("Form_Inicio")
        Form_Inicio.resize(256, 99)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form_Inicio)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAgregar = QtWidgets.QPushButton(parent=Form_Inicio)
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnAgregar.clicked.connect(self.clicked_btn)
        self.horizontalLayout.addWidget(self.btnAgregar)
        self.btnBuscar = QtWidgets.QPushButton(parent=Form_Inicio)
        self.btnBuscar.setObjectName("btnBuscar")
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form_Inicio)
        QtCore.QMetaObject.connectSlotsByName(Form_Inicio)

    def retranslateUi(self, Form_Inicio):
        _translate = QtCore.QCoreApplication.translate
        Form_Inicio.setWindowTitle(_translate("Form_Inicio", "Inicio"))
        self.btnAgregar.setText(_translate("Form_Inicio", "Añadir"))
        self.btnBuscar.setText(_translate("Form_Inicio", "Buscar"))

    def clicked_btn(self):
        formAgregar = QtWidgets.QWidget()
        uii = FormAgregar.Ui_formAgregar()
        uii.setupUi(formAgregar)
        formAgregar.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Inicio = QtWidgets.QWidget()
    ui = Ui_Form_Inicio()
    ui.setupUi(Form_Inicio)
    Form_Inicio.show()
    sys.exit(app.exec())
