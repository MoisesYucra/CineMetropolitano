from PyQt5 import QtWidgets, uic
from controller import LoginController
from controller import AgregarController
from controller import EliminarController


class PrincipalController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("views/Maincine.ui")
        self.ventana.show()
        self.ventana.actionLogin.triggered.connect(self.actionLoginClick)
        self.ventana.actionAgregar_Pelicula.triggered.connect(self.actionAgregar_PeliculaClick)
        self.ventana.actionEliminar_Pelicula.triggered.connect(self.actionEliminar_PeliculaClick)
        app.exec()

    def actionLoginClick(self):
        self.Login = LoginController()
        self.Login.ventana.show()
    
    def actionAgregar_PeliculaClick(self):
        self.frmPeliculas = AgregarController()
        self.frmPeliculas.ventana.show()

    def actionEliminar_PeliculaClick(self):
        self.frmPeliculas = EliminarController()
        self.frmPeliculas.ventana.show()