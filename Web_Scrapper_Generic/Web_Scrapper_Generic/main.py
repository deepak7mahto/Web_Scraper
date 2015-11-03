from PyQt4 import QtCore, QtGui, Qt
import Web_Scrapper_Generic_UI, sys, generic_crawler_module, Data_extactor_UI, data_extractor_module, Mailing_UI, mailing_module


class Web_Scrapper_Generic(QtGui.QMainWindow, Web_Scrapper_Generic_UI.Ui_MainWindow, generic_crawler_module.generic_crawler_class):
    #initialization of main  windows    
    def __init__(self):
        super(Web_Scrapper_Generic, self).__init__()
        self.setupUi(self)
        self.get_links()

class Extactor(QtGui.QDialog, Data_extactor_UI.Ui_Form, data_extractor_module.extractor_main_class):
    def __init__(self):
        super(Extactor, self).__init__()
        self.setupUi(self)
        self.get_data()
        
class Mailing(QtGui.QDialog, Mailing_UI.Ui_mailing_dialog, mailing_module.mailing_main_class):
    def __init__(self, *args):
        super(Mailing, self).__init__()
        self.setupUi(self)



def main():
    app = QtGui.QApplication(sys.argv)
    #Every PyQt4 application must create an application object. The application object is located in the QtGui module
    #The sys.argv parameter is a list of arguments from the command line.
    scrapper = Web_Scrapper_Generic()
    #the object for the  Web_Scrapper_Generic is created 
    scrapper.show()
    #The show() method displays the window on the screen. A window is first created in memory and later shown on the screen. 
    extractor = Extactor()
    #the object for tje class eExtractor is created 
    mailing = Mailing()
    QtCore.QObject.connect(scrapper.data_extraction_pushButton, QtCore.SIGNAL("clicked()"), extractor.show)
    QtCore.QObject.connect(scrapper.mailing_pushButton, QtCore.SIGNAL("clicked()"), mailing.show)
    app.exec_()
    """
     the mainloop of the application. is entered as soon as the object of te class is createdThe event handling starts from this point. The mainloop receives events from the window system and dispatches them to the application widgets. The mainloop ends if we call the exit() method or the main widget is destroyed. The sys.exit() method ensures a clean exit. The environment will be informed how the application ended .The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.    
    """

if __name__ == "__main__":
    main()

#hello