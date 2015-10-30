from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtCore import SIGNAL
import Web_Scrapper_Generic_UI

class spidy(object):

    def __init__(self):
        print "initializing"

    def get_links(self):
        print "get links function"
        self.url_lineEdit.setPlaceholderText("Enter URL ")
        self.url_pattern_lineEdit.setPlaceholderText("Enter URL pattern")

        self.url = self.url_lineEdit.text()
        self.url_pattern = self.url_pattern_lineEdit.text()
        self.connect(self.absolute_url_radioButton , SIGNAL("clicked()"), self.url_type_a)
        self.connect(self.relative_url_radioButton , SIGNAL("clicked()"), self.url_type_r)
        self.spidy_object = spidy(self, self.url, self.url_pattern, self.url_type)

    def url_type_a(self):
        self.url_type = "absolute_url"

    def url_type_r(self):
        self.url_type = "relative_url"

class spidy_worker(QtCore.QThread):
    def __init__(self, url, pattern, url_type):
        print "Spidy Initializing"
        print self.url+self.pattern+self.url_type