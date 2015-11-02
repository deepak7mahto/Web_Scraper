from PyQt4 import QtCore, QtGui, Qt
import Web_Scrapper_Generic_UI, sys, generic_crawler_module, Data_extactor_UI, data_extractor_module


class Web_Scrapper_Generic(QtGui.QMainWindow, Web_Scrapper_Generic_UI.Ui_MainWindow, generic_crawler_module.generic_crawler_class):
    #initialization of main  windows    
    def __init__(self):
        super(Web_Scrapper_Generic, self).__init__()
        generic_crawler_module.generic_crawler_class.__init__(self)
        self.setupUi(self)
        self.get_links()

class Extactor(QtGui.QDialog, Data_extactor_UI.Ui_Form, data_extractor_module.extractor_main_class):
    def __init__(self):
        super(Extactor, self).__init__()
        data_extractor_module.extractor_main_class.__init__(self)
        self.setupUi(self)
        self.get_data()
        #self.add_items_function()
        #self.load_file_function()
        #self.get_items()

def main():
    app = QtGui.QApplication(sys.argv)
    scrapper = Web_Scrapper_Generic()
    scrapper.show()
    extractor = Extactor()
    QtCore.QObject.connect(scrapper.data_extraction_pushButton, QtCore.SIGNAL("clicked()"), extractor.show)
    #extractor.show()
    app.exec_()

if __name__ == "__main__":
    main()

#hello