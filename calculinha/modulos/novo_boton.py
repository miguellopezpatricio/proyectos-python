""" Módulo novo_boton
    para xerar obxectos personalizados de tipo botón 

"""

""" Módulos a importar """
from PySide2 import QtCore, QtGui, QtWidgets


class NovoBoton(QtWidgets.QPushButton):
    """ Clase personalizada NovoBoton hereda de QPushButton
    """

    def __init__(self, parent = None):
        """ Método construtor da clase 
        """

        super(NovoBoton, self).__init__(parent)

        self.setFixedSize(120,120) # axustamos o tamaño do botón
        self.setCheckable(True)


        
    def engade_icona_info_txt(self, icona,txt):
        """ Método para engadir icona, axustar o seu tamaño e engadir axuda textual a cada obxecto da clase NovoBoton
            Recibe como parámetros o nome da icona e un texto que formará parte da axuda textual do botón
        Args:
            param1 (str): nome do arquivo de imaxe a amosar no botón
            param2 (str): axuda textual
    
        """

        self.setIcon(QtGui.QIcon(icona))
        self.setIconSize(QtCore.QSize(100,100)) 
        self.setToolTip("Este é o botón " + txt)

  

   

