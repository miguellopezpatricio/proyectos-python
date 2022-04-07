""" Módulo principal da aplicación Calculiña

"""

# Módulos a importar necesarios para o funcionamento da aplicación
import sys
from pathlib import Path
from os import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QApplication, QLabel, QWidget, QMessageBox, QGraphicsPixmapItem, QGraphicsScene, QMainWindow, QVBoxLayout
from PySide2.QtGui import QPixmap
from modulos.InfoVentanaAp import InfoVentana
from modulos.calculinhaWindow import Ui_MainWindow
from modulos.ventana_pdf import PdfWindow



class CalculinhaApp(QMainWindow):
    """ Clase CalculinhaApp do módulo principal da aplicación
        Xera a ventana principal que amosará a calculadora
    """

    """ Propiedades da clase """
   
    primeiro_num = None
    """ float: Variable primeiro_num """

    escribindo_segundo_num = False
    """ boolean: Variable escribindo_segundo_num  """

    def __init__(self):
        """ método construtor da clase
        """

        super().__init__()
        self.ui = Ui_MainWindow()
        

        # amosando imaxe cabeceira  
        
        self.cabeceira  = QLabel(self)
        self.cabeceira.setGeometry(10,50, 600,100)
        self.pixmap = QPixmap('./imaxes/cabeceira.png')
        
        self.cabeceira.setPixmap(self.pixmap)
        self.cabeceira.resize(self.pixmap.width(),self.pixmap.height())
        

        # fixando o tamaño da ventana principal
        ancho = 620
        alto = 780
   
        self.setFixedSize(ancho, alto)

        self.ui.setupUi(self)
        
        # creamos un obxecto InfoVentana para a opción do menú: información sobre a app
        self.sobreAapp = InfoVentana()

        

        self.show()

       
        """ engadindo iconas e axuda textual a cada botón
        """
        self.ui.pushButtonCero.engade_icona_info_txt("imaxes/cero.png","do número cero")
        self.ui.pushButtonUn.engade_icona_info_txt("imaxes/un.png","do número un")
        self.ui.pushButtonDous.engade_icona_info_txt("imaxes/dous.png","do número dous")
        self.ui.pushButtonTres.engade_icona_info_txt("imaxes/tres.png","do número tres")
        self.ui.pushButtonCatro.engade_icona_info_txt("imaxes/catro.png","do número catro")
        self.ui.pushButtonCinco.engade_icona_info_txt("imaxes/cinco.png","do número cinco")
        self.ui.pushButtonSeis.engade_icona_info_txt("imaxes/seis.png","do número seis")
        self.ui.pushButtonSete.engade_icona_info_txt("imaxes/sete.png","do número sete")
        self.ui.pushButtonOito.engade_icona_info_txt("imaxes/oito.png","do número oito")
        self.ui.pushButtonNove.engade_icona_info_txt("imaxes/nove.png","do número nove")

        self.ui.pushButtonBorra.engade_icona_info_txt("imaxes/lixo.png","de borrar a pantalla")
        self.ui.pushButtonSuma.engade_icona_info_txt("imaxes/suma.png","para sumar")
        self.ui.pushButtonResta.engade_icona_info_txt("imaxes/resta.png","para restar")
        self.ui.pushButtonMultip.engade_icona_info_txt("imaxes/multiplica.png","para multiplicar")
        self.ui.pushButtonDivide.engade_icona_info_txt("imaxes/divide.png","para dividir")
        self.ui.pushButtonIgual.engade_icona_info_txt("imaxes/igual.png","do igual")

        """ Axuda textual das opcións do menú
        """
        self.ui.menu.setToolTipsVisible(True) # activamos a axuda textual en opcións do menú
        
        self.ui.actionBORRAR.setToolTip("Borra a pantalla")
        self.ui.actionMANUAL.setToolTip("Accede ao manual técnico")
        self.ui.actionSAIR.setToolTip("Sae da aplicación")
        self.ui.actionSOBRE_A_APP.setToolTip("Información sobre a aplicación")       
        

        """ sinais e eventos dos botóns dos números da calculadora
        """
        self.ui.pushButtonUn.clicked.connect(self.preme_num)
        self.ui.pushButtonDous.clicked.connect(self.preme_num)
        self.ui.pushButtonTres.clicked.connect(self.preme_num)
        self.ui.pushButtonCatro.clicked.connect(self.preme_num)
        self.ui.pushButtonCinco.clicked.connect(self.preme_num)
        self.ui.pushButtonSeis.clicked.connect(self.preme_num)
        self.ui.pushButtonSete.clicked.connect(self.preme_num)
        self.ui.pushButtonOito.clicked.connect(self.preme_num)
        self.ui.pushButtonNove.clicked.connect(self.preme_num)
        self.ui.pushButtonCero.clicked.connect(self.preme_num)


        """ sinais e eventos dos botóns das operacións matemáticas da calculadora
        """
        self.ui.pushButtonSuma.clicked.connect(self.preme_operacion)
        self.ui.pushButtonResta.clicked.connect(self.preme_operacion)
        self.ui.pushButtonDivide.clicked.connect(self.preme_operacion)
        self.ui.pushButtonMultip.clicked.connect(self.preme_operacion)
        
        # sinal e evento do botón de resultado
        self.ui.pushButtonIgual.clicked.connect(self.preme_resultado)

        # sinal e evento do botón AC
        self.ui.pushButtonBorra.clicked.connect(self.limpa_display)


        # sinais e eventos para opcions menú
        self.ui.actionSOBRE_A_APP.triggered.connect(lambda x: self.sobreAapp.amosar_ventana())
        self.ui.actionBORRAR.triggered.connect(self.limpa_display)
        self.ui.actionMANUAL.triggered.connect(self.manual_app)
        self.ui.actionSAIR.triggered.connect(self.closeEvent)


    
    def preme_num(self):
        """ Método que amosará os números que se premen    

        """

        boton_premido = self.sender()  # esta variable gardará o sinal do botón premido
        """object: variable boton_premido garda o sinal do botón premido """


        """ si algún botón de operación foi premido pois gardamos o número que estaba en pantalla
            verifica que non hai 

        """ 
        if((self.ui.pushButtonSuma.isChecked() or self.ui.pushButtonResta.isChecked() or
         self.ui.pushButtonMultip.isChecked() or self.ui.pushButtonDivide.isChecked()) and
         (not self.escribindo_segundo_num)):

            nova_etiqueta = format(float(boton_premido.text()),'.15g') # o formato aplicado é para eliminar o cero da esquerda eliminar decimais
            self.escribindo_segundo_num = True

        else:# caso contrario seguimos acumulando números 
            nova_etiqueta = format(float(self.ui.lineEditDisplay.text()+ boton_premido.text()),'.15g')
        
        
        self.ui.lineEditDisplay.setText(nova_etiqueta) # amosamos o resultado na pantalla da calculadora



    def preme_resultado(self):
        """ Método para ofrecer o resultado da operación
            Cando o usuario preme '=' garda o número que se estea amosando
            e se ofrecerá o resultado da operación
            Pon a False o botón da operación realizada
        
        """

        segundo_num = float(self.ui.lineEditDisplay.text()) # pasamos a float o texto do display e o gardamos 
        """ float: Variable segundo_numero garda o dato actual en lineEditDisplay """

        # compróbase se algún dos botóns de operación están pulsados
        if self.ui.pushButtonSuma.isChecked():
            display_numero = self.primeiro_num + segundo_num    # facemos a operación e gardamos o resultado
            nova_etiqueta = format(display_numero, '.15g')      # formateamos o resultado
            self.ui.lineEditDisplay.setText(nova_etiqueta)      # amosamos o resultado por pantalla        
            self.ui.pushButtonSuma.setChecked(False)            # cambiamos o estado do botón

        elif self.ui.pushButtonResta.isChecked():
            display_numero = self.primeiro_num - segundo_num
            nova_etiqueta = format(display_numero, '.15g')
            self.ui.lineEditDisplay.setText(nova_etiqueta)        
            self.ui.pushButtonResta.setChecked(False)

        elif self.ui.pushButtonDivide.isChecked():
            display_numero = self.primeiro_num / segundo_num
            nova_etiqueta = format(display_numero, '.15g')
            self.ui.lineEditDisplay.setText(nova_etiqueta)        
            self.ui.pushButtonDivide.setChecked(False)

        elif self.ui.pushButtonMultip.isChecked():
            display_numero = self.primeiro_num * segundo_num
            nova_etiqueta = format(display_numero, '.15g')
            self.ui.lineEditDisplay.setText(nova_etiqueta)        
            self.ui.pushButtonMultip.setChecked(False)

        self.escribindo_segundo_num = False

    def preme_operacion(self):
        """ Cando o usuario preme algún botón de operación
            este método gardará o número amosado na pantalla como primeiro número

        """

        boton_premido = self.sender() 
        self.primeiro_num = float(self.ui.lineEditDisplay.text())

        boton_premido.setChecked(True)


    def limpa_display(self):
        """ Método que borra a pantalla amosando un cero

        """

        self.ui.lineEditDisplay.setText('0')

    def manual_app(self):
        """ Método que amosará o manual do código da aplicación en formato pdf
            Crea un obxecto da clase PdfWindow e chama ao método showPdf 
            enviando a ruta e nome do arquivo pdf
        """

        self.pdf_window = PdfWindow(self)
        self.pdf_window.showPdf("doc/calculinha.pdf")

        

       
    def sair(self):
        """ Método para sair da aplicación

        """

        sys.exit()
      


    
    def closeEvent(self, evento):
        """ Método para preguntar ao usuario se confirma a saída da aplicación

        Args:          
            param2 (event): evento co que se relaciona.
       
        """
        # almacenamos a opción pulsada no QMessageBox
        queFacer = QMessageBox.question(self, 'Sair', 'Seguro que quere sair?', QMessageBox.Ok|QMessageBox.No)

        if queFacer == QMessageBox.Ok: # si OK entón sáese da app
            #evento.accept()
            sys.exit()
        else:
            evento.ignore() # caso contrario continúa a app    



if __name__ == '__main__':
    """ Inicialización e execución da app

    """

    app = QApplication(sys.argv)
    ui = CalculinhaApp()
    ui.show()
    sys.exit(app.exec_())
