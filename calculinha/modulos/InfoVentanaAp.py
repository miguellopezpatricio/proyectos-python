""" Módulo da clase InfoVentana 
    para xerar a ventana de información da aplicación
    
"""

# Módulos a importar
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from modulos.info_ventana import Ui_infoWindow

class InfoVentana(QMainWindow):
    """
    Clase InfoVentana que usaremos para crear unha ventana de información sobre a aplicación
    """


    def __init__(self):
        """
        Método construtor da clase Infoventana
        """

        super().__init__()
        self.ui = Ui_infoWindow()
        self.ui.setupUi(self)

 
    def amosar_ventana(self):
        """
        Método para amosar ventana
        """

        self.show()


if __name__ == '__main__':
    """
    Inicialización e execución
    """

    app = QApplication(sys.argv)
    ui = Ui_infoWindow()
    ui.show()
    sys.exit(app.exec_())