
""" Módulo ventana_pdf 
    para xerar a ventana que amosará o manual da aplicación

"""

""" Módulos a importar """
from PySide2 import QtCore
from PySide2.QtCore import QUrl, QFileInfo
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings



class PdfWindow(QMainWindow):
    """ Clase PdfWindow para xerar unha ventana que amosará o manual en pdf
    """

    def __init__(self, parent=None):
        """ Método construtor da clase
        """

        super(PdfWindow, self).__init__(parent)
        self.setWindowTitle("Manual da aplicación")
        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.web.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.setCentralWidget(self.web)

    def showPdf(self, dir_arquivo: str):
        """ Método para amosar o pdf nunha ventana
            Recibe como parámetro a ruta co nome do arquivo

        Args:
            dir_arquivo (str): Ruta ao pdf

        """

        try:
            absolute_path = QFileInfo(dir_arquivo).absoluteFilePath()
            url_to_manual = QUrl.fromLocalFile(absolute_path)
            self.web.load(url_to_manual)
            self.showMaximized()
        except Exception as e:
            print(str(e))
