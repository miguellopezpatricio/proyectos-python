# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculinhaWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from modulos.novo_boton import NovoBoton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 859)
        MainWindow.setIconSize(QSize(24, 24))
        self.menuLimpar_2 = QAction(MainWindow)
        self.menuLimpar_2.setObjectName(u"menuLimpar_2")
        self.actionBORRAR = QAction(MainWindow)
        self.actionBORRAR.setObjectName(u"actionBORRAR")
        self.actionMANUAL = QAction(MainWindow)
        self.actionMANUAL.setObjectName(u"actionMANUAL")
        self.actionSOBRE_A_APP = QAction(MainWindow)
        self.actionSOBRE_A_APP.setObjectName(u"actionSOBRE_A_APP")
        self.actionSAIR = QAction(MainWindow)
        self.actionSAIR.setObjectName(u"actionSAIR")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(100, 260, 761, 511))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDous = NovoBoton(self.gridLayoutWidget)
        self.pushButtonDous.setObjectName(u"pushButtonDous")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDous.sizePolicy().hasHeightForWidth())
        self.pushButtonDous.setSizePolicy(sizePolicy)
        self.pushButtonDous.setMinimumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(5)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonDous.setFont(font)
        self.pushButtonDous.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(183, 227, 255) ")

        self.gridLayout.addWidget(self.pushButtonDous, 2, 1, 1, 1)

        self.pushButtonUn = NovoBoton(self.gridLayoutWidget)
        self.pushButtonUn.setObjectName(u"pushButtonUn")
        sizePolicy.setHeightForWidth(self.pushButtonUn.sizePolicy().hasHeightForWidth())
        self.pushButtonUn.setSizePolicy(sizePolicy)
        self.pushButtonUn.setMinimumSize(QSize(100, 100))
        self.pushButtonUn.setFont(font)
        self.pushButtonUn.setToolTipDuration(-1)
        self.pushButtonUn.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(250, 255, 140)")

        self.gridLayout.addWidget(self.pushButtonUn, 2, 0, 1, 1)

        self.pushButtonSeis = NovoBoton(self.gridLayoutWidget)
        self.pushButtonSeis.setObjectName(u"pushButtonSeis")
        sizePolicy.setHeightForWidth(self.pushButtonSeis.sizePolicy().hasHeightForWidth())
        self.pushButtonSeis.setSizePolicy(sizePolicy)
        self.pushButtonSeis.setMinimumSize(QSize(100, 100))
        self.pushButtonSeis.setFont(font)
        self.pushButtonSeis.setToolTipDuration(-1)
        self.pushButtonSeis.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(183, 227, 255) ")

        self.gridLayout.addWidget(self.pushButtonSeis, 1, 2, 1, 1)

        self.pushButtonMultip = NovoBoton(self.gridLayoutWidget)
        self.pushButtonMultip.setObjectName(u"pushButtonMultip")
        sizePolicy.setHeightForWidth(self.pushButtonMultip.sizePolicy().hasHeightForWidth())
        self.pushButtonMultip.setSizePolicy(sizePolicy)
        self.pushButtonMultip.setMinimumSize(QSize(100, 100))
        font1 = QFont()
        font1.setPointSize(5)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButtonMultip.setFont(font1)
        self.pushButtonMultip.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(121, 255, 38)")
        self.pushButtonMultip.setCheckable(True)

        self.gridLayout.addWidget(self.pushButtonMultip, 1, 3, 1, 1)

        self.pushButtonResta = NovoBoton(self.gridLayoutWidget)
        self.pushButtonResta.setObjectName(u"pushButtonResta")
        sizePolicy.setHeightForWidth(self.pushButtonResta.sizePolicy().hasHeightForWidth())
        self.pushButtonResta.setSizePolicy(sizePolicy)
        self.pushButtonResta.setMinimumSize(QSize(100, 100))
        self.pushButtonResta.setFont(font1)
        self.pushButtonResta.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(255, 208, 169)")
        self.pushButtonResta.setCheckable(True)

        self.gridLayout.addWidget(self.pushButtonResta, 2, 3, 1, 1)

        self.pushButtonTres = NovoBoton(self.gridLayoutWidget)
        self.pushButtonTres.setObjectName(u"pushButtonTres")
        sizePolicy.setHeightForWidth(self.pushButtonTres.sizePolicy().hasHeightForWidth())
        self.pushButtonTres.setSizePolicy(sizePolicy)
        self.pushButtonTres.setMinimumSize(QSize(100, 100))
        self.pushButtonTres.setFont(font)
        self.pushButtonTres.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(121, 255, 38)")

        self.gridLayout.addWidget(self.pushButtonTres, 2, 2, 1, 1)

        self.pushButtonNove = NovoBoton(self.gridLayoutWidget)
        self.pushButtonNove.setObjectName(u"pushButtonNove")
        sizePolicy.setHeightForWidth(self.pushButtonNove.sizePolicy().hasHeightForWidth())
        self.pushButtonNove.setSizePolicy(sizePolicy)
        self.pushButtonNove.setMinimumSize(QSize(100, 100))
        self.pushButtonNove.setFont(font)
        self.pushButtonNove.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(121, 255, 38)")

        self.gridLayout.addWidget(self.pushButtonNove, 0, 2, 1, 1)

        self.pushButtonCinco = NovoBoton(self.gridLayoutWidget)
        self.pushButtonCinco.setObjectName(u"pushButtonCinco")
        sizePolicy.setHeightForWidth(self.pushButtonCinco.sizePolicy().hasHeightForWidth())
        self.pushButtonCinco.setSizePolicy(sizePolicy)
        self.pushButtonCinco.setMinimumSize(QSize(100, 100))
        self.pushButtonCinco.setFont(font)
        self.pushButtonCinco.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(255, 208, 169)")

        self.gridLayout.addWidget(self.pushButtonCinco, 1, 1, 1, 1)

        self.pushButtonCatro = NovoBoton(self.gridLayoutWidget)
        self.pushButtonCatro.setObjectName(u"pushButtonCatro")
        sizePolicy.setHeightForWidth(self.pushButtonCatro.sizePolicy().hasHeightForWidth())
        self.pushButtonCatro.setSizePolicy(sizePolicy)
        self.pushButtonCatro.setMinimumSize(QSize(100, 100))
        self.pushButtonCatro.setFont(font)
        self.pushButtonCatro.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(121, 255, 38)")

        self.gridLayout.addWidget(self.pushButtonCatro, 1, 0, 1, 1)

        self.pushButtonDivide = NovoBoton(self.gridLayoutWidget)
        self.pushButtonDivide.setObjectName(u"pushButtonDivide")
        sizePolicy.setHeightForWidth(self.pushButtonDivide.sizePolicy().hasHeightForWidth())
        self.pushButtonDivide.setSizePolicy(sizePolicy)
        self.pushButtonDivide.setMinimumSize(QSize(100, 100))
        self.pushButtonDivide.setBaseSize(QSize(0, 0))
        self.pushButtonDivide.setFont(font1)
        self.pushButtonDivide.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(250, 255, 140)")
        self.pushButtonDivide.setCheckable(True)

        self.gridLayout.addWidget(self.pushButtonDivide, 0, 3, 1, 1)

        self.pushButtonOito = NovoBoton(self.gridLayoutWidget)
        self.pushButtonOito.setObjectName(u"pushButtonOito")
        sizePolicy.setHeightForWidth(self.pushButtonOito.sizePolicy().hasHeightForWidth())
        self.pushButtonOito.setSizePolicy(sizePolicy)
        self.pushButtonOito.setMinimumSize(QSize(100, 100))
        self.pushButtonOito.setFont(font)
        self.pushButtonOito.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(250, 255, 140)")

        self.gridLayout.addWidget(self.pushButtonOito, 0, 1, 1, 1)

        self.pushButtonSete = NovoBoton(self.gridLayoutWidget)
        self.pushButtonSete.setObjectName(u"pushButtonSete")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.pushButtonSete.sizePolicy().hasHeightForWidth())
        self.pushButtonSete.setSizePolicy(sizePolicy1)
        self.pushButtonSete.setMinimumSize(QSize(100, 100))
        self.pushButtonSete.setFont(font)
        self.pushButtonSete.setAutoFillBackground(False)
        self.pushButtonSete.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(183, 227, 255) \n"
"\n"
"")
        self.pushButtonSete.setIconSize(QSize(16, 16))
        self.pushButtonSete.setCheckable(False)

        self.gridLayout.addWidget(self.pushButtonSete, 0, 0, 1, 1)

        self.pushButtonCero = NovoBoton(self.gridLayoutWidget)
        self.pushButtonCero.setObjectName(u"pushButtonCero")
        sizePolicy.setHeightForWidth(self.pushButtonCero.sizePolicy().hasHeightForWidth())
        self.pushButtonCero.setSizePolicy(sizePolicy)
        self.pushButtonCero.setMinimumSize(QSize(100, 100))
        self.pushButtonCero.setFont(font)
        self.pushButtonCero.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(255, 208, 169)")

        self.gridLayout.addWidget(self.pushButtonCero, 3, 0, 1, 1)

        self.pushButtonBorra = NovoBoton(self.gridLayoutWidget)
        self.pushButtonBorra.setObjectName(u"pushButtonBorra")
        sizePolicy.setHeightForWidth(self.pushButtonBorra.sizePolicy().hasHeightForWidth())
        self.pushButtonBorra.setSizePolicy(sizePolicy)
        self.pushButtonBorra.setMinimumSize(QSize(100, 100))
        self.pushButtonBorra.setFont(font)
        self.pushButtonBorra.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:rgb(202, 202, 202)")

        self.gridLayout.addWidget(self.pushButtonBorra, 3, 1, 1, 1)

        self.pushButtonSuma = NovoBoton(self.gridLayoutWidget)
        self.pushButtonSuma.setObjectName(u"pushButtonSuma")
        sizePolicy.setHeightForWidth(self.pushButtonSuma.sizePolicy().hasHeightForWidth())
        self.pushButtonSuma.setSizePolicy(sizePolicy)
        self.pushButtonSuma.setMinimumSize(QSize(100, 100))
        self.pushButtonSuma.setFont(font1)
        self.pushButtonSuma.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color:  rgb(183, 227, 255) \n"
"")
        self.pushButtonSuma.setCheckable(True)

        self.gridLayout.addWidget(self.pushButtonSuma, 3, 3, 1, 1)

        self.pushButtonIgual = NovoBoton(self.gridLayoutWidget)
        self.pushButtonIgual.setObjectName(u"pushButtonIgual")
        sizePolicy.setHeightForWidth(self.pushButtonIgual.sizePolicy().hasHeightForWidth())
        self.pushButtonIgual.setSizePolicy(sizePolicy)
        self.pushButtonIgual.setMinimumSize(QSize(100, 100))
        self.pushButtonIgual.setFont(font1)
        self.pushButtonIgual.setStyleSheet(u"border-radius: 20px;\n"
"color: black;\n"
"background-color: rgb(255, 208, 169)")

        self.gridLayout.addWidget(self.pushButtonIgual, 3, 2, 1, 1)

        self.lineEditDisplay = QLineEdit(self.centralwidget)
        self.lineEditDisplay.setObjectName(u"lineEditDisplay")
        self.lineEditDisplay.setEnabled(True)
        self.lineEditDisplay.setGeometry(QRect(190, 160, 591, 91))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(60)
        font2.setBold(True)
        font2.setWeight(75)
        self.lineEditDisplay.setFont(font2)
        self.lineEditDisplay.setLayoutDirection(Qt.LeftToRight)
        self.lineEditDisplay.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(193, 193, 193);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"\n"
"}")
        self.lineEditDisplay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditDisplay.setClearButtonEnabled(False)
        self.cabeceiraLabel = QLabel(self.centralwidget)
        self.cabeceiraLabel.setObjectName(u"cabeceiraLabel")
        self.cabeceiraLabel.setGeometry(QRect(20, 20, 951, 121))
        self.cabeceiraLabel.setPixmap(QPixmap(u"../imaxes/cabeceira.png"))
        self.cabeceiraLabel.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1015, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setToolTipsVisible(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionBORRAR)
        self.menu.addAction(self.actionMANUAL)
        self.menu.addAction(self.actionSOBRE_A_APP)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSAIR)

        self.retranslateUi(MainWindow)

        self.pushButtonSete.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculi\u00f1a", None))
        self.menuLimpar_2.setText(QCoreApplication.translate("MainWindow", u"actionLimpar", None))
#if QT_CONFIG(tooltip)
        self.menuLimpar_2.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.menuLimpar_2.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionBORRAR.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
#if QT_CONFIG(tooltip)
        self.actionBORRAR.setToolTip(QCoreApplication.translate("MainWindow", u"Borra a pantalla", None))
#endif // QT_CONFIG(tooltip)
        self.actionMANUAL.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
#if QT_CONFIG(tooltip)
        self.actionMANUAL.setToolTip(QCoreApplication.translate("MainWindow", u"Manual da aplicaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.actionSOBRE_A_APP.setText(QCoreApplication.translate("MainWindow", u"SOBRE A APP", None))
#if QT_CONFIG(tooltip)
        self.actionSOBRE_A_APP.setToolTip(QCoreApplication.translate("MainWindow", u"O autor da aplicaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.actionSAIR.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDous.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonDous.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButtonDous.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonUn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonUn.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButtonUn.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonSeis.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonSeis.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButtonSeis.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonMultip.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonMultip.setText(QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(shortcut)
        self.pushButtonMultip.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonResta.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonResta.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.pushButtonResta.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonTres.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonTres.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButtonTres.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonNove.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonNove.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButtonNove.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonCinco.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonCinco.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButtonCinco.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonCatro.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonCatro.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButtonCatro.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonDivide.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonDivide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.pushButtonDivide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonOito.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonOito.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSete.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonSete.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButtonSete.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonCero.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonCero.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.pushButtonBorra.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonBorra.setText(QCoreApplication.translate("MainWindow", u"borra", None))
#if QT_CONFIG(shortcut)
        self.pushButtonBorra.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonSuma.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonSuma.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButtonSuma.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonIgual.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonIgual.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButtonIgual.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.lineEditDisplay.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEditDisplay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"fai os teus c\u00e1lculos", None))
        self.cabeceiraLabel.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"OPCI\u00d3NS", None))
    # retranslateUi

