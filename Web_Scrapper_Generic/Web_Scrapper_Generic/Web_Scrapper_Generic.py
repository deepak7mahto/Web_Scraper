from PyQt4 import QtCore, QtGui, Qt
import Web_Scrapper_Generic_UI
class Web_Scrapper_Generic(QtGui.QDialog,Web_Scrapper_Generic_UI.Ui_MainWindow):
    #initialization of main  windows 
    def __init__(self):
        QtGui.QDialog().__init__(self)
        self.set