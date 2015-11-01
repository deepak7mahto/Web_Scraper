from PyQt4 import QtCore, QtGui, Qt
import Web_Scrapper_Generic_UI, sys, generic_crawler_module, Data_extactor_UI


class Web_Scrapper_Generic(QtGui.QMainWindow, Web_Scrapper_Generic_UI.Ui_MainWindow, generic_crawler_module.spidy):
    #initialization of main  windows    
    def __init__(self):
        super(Web_Scrapper_Generic, self).__init__()
        generic_crawler_module.spidy.__init__(self)
        self.setupUi(self)
        self.get_links()

class Extactor(QtGui.QDialog, Data_extactor_UI.Ui_Form):
    def __init__(self, *args):
        super(Extactor, self).__init__()
        self.setupUi(self)
    


def main():
    app = QtGui.QApplication(sys.argv)
    scrapper = Web_Scrapper_Generic()
    scrapper.show()
    extractor = Extactor()
    QtCore.QObject.connect(scrapper.data_extraction_pushButton, QtCore.SIGNAL("extractor.show()"), extractor.show)
    app.exec_()

if __name__ == "__main__":
    main()