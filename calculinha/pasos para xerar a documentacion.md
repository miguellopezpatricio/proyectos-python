# ESTES SON OS PASOS REALIZADOS PARA XERAR A DOCUMENTACIÓN DA APLICACIÓN:

***ACTUALIZACIÓN. ENGADO ISTO EN conf.py E CONSIGO QUE ME RECOÑEZA MÁIS MÓDULOS: sys.path.append('../modulos')
*** Tamén tiven que executar: sphinx-apidoc -f -M -o source/api/ ../modulos
* ACTUALIZACIÓN* tema que instalo: pip install caktus-sphinx-theme

1. creo carpeta doc
2. abro o terminal e me sitúo dentro da carpeta doc 
3. executo sphinx-quickstart
4. contesto Y a "separate source and build directories" e poño os datos que correspondan ao resto das preguntas

CONFIGURAMOS ficheiro /doc/source/conf.py
5. Engado as importacións:
                            
    import caktus_theme
    import os
    import sys
    import datetime

    e engado:    sys.path.insert(0, os.path.abspath('../..')) 
    aquí hai que incluir o directorio raiz por iso poño ../.. Estou en 'docs' e retrocedo duas veces ata chegar ao raiz.

    *** ENGADO ISTO:  sys.path.append('../modulos')

6. Engado as extensións:     
    [ "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",]

7. Liñas a engadir para o tema que me interesa:    

html_theme = "caktus"
html_sidebars = caktus_theme.default_sidebars()
html_theme_path = [caktus_theme.get_theme_dir()]



8. CONFIGURAMOS ficheiro /doc/source/index.srt
    modificando o título e engadindo README e as carpetas para os ficheiros rst autoxerados

9. Seguindo na carpeta 'docs' executamos:  sphinx-apidoc -f -M -o source/api/ ../..
10. Exportar a html con: make html 

*** AQUÍ AMOSA OS SEGUINTES ERROS ***

C:\Users\Miguel\Desktop\practica_qt_py\a20miguellp\a20miguellp\a20miguellp-UD5-PR5\doc\source\index.rst:9: WARNING: toctree contains reference to nonexisting document 'README'
C:\Users\Miguel\Desktop\practica_qt_py\a20miguellp\a20miguellp\a20miguellp-UD5-PR5\doc\source\index.rst:9: WARNING: toctree contains reference to nonexisting document 'api'
C:\Users\Miguel\Desktop\practica_qt_py\a20miguellp\a20miguellp\a20miguellp-UD5-PR5\doc\source\index.rst:9: WARNING: toctree contains reference to nonexisting document 'api/modulos'

checking consistency... C:\Users\Miguel\Desktop\practica_qt_py\a20miguellp\a20miguellp\a20miguellp-UD5-PR5\doc\source\api\modules.rst: WARNING: document isn't included in any toctree

11. Xerando o pdf da documentación en html: make latexpdf
O último punto para crear o pdf falla ao non xerar o html correctamente.

*** ACTUALIZACIÓN *** Conseguín que xerase un html cos módulos. Aínda que con erros.
Xeramos o pdf con make latexpdf pero o resultado é NEGATIVO. 
