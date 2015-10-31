from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QThread
from mechanize import Browser
from bs4 import BeautifulSoup
import Web_Scrapper_Generic_UI, lxml, re

pages = set()

class spidy(object):

    def __init__(self):
        print "initializing"

    def get_links(self):
        print "get links function"
        self.url_lineEdit.setPlaceholderText("Enter URL ")
        self.url_pattern_lineEdit.setPlaceholderText("Enter URL pattern")        
        self.connect(self.absolute_url_radioButton , SIGNAL("clicked()"), self.url_type_a)
        self.connect(self.relative_url_radioButton , SIGNAL("clicked()"), self.url_type_r)        
        self.connect(self.actionSave_Configuration_File, SIGNAL("triggered()"), self.save_configuration_button)
        self.connect(self.actionLoad_Configuration_File, SIGNAL("triggered()"), self.load_configuration_button)

    def url_type_a(self):
        self.url = self.url_lineEdit.text()
        self.url_pattern = self.url_pattern_lineEdit.text()
        self.spidy_object = spidy_worker(self.url, self.url_pattern, "typeA")
        self.connect(self.start_crawling_pushButton, SIGNAL("clicked()"), self.spidy_object.start)
        self.connect(self.stop_crawling_pushButton, SIGNAL("clicked()"), self.stop_crawler_button)
        
    def url_type_r(self):
        self.url = self.url_lineEdit.text()
        self.url_pattern = self.url_pattern_lineEdit.text()
        self.spidy_object = spidy_worker(self.url, self.url_pattern, "typeB")
        self.connect(self.start_crawling_pushButton, SIGNAL("clicked()"), self.spidy_object.start)
        self.connect(self.stop_crawling_pushButton, SIGNAL("clicked()"), self.stop_crawler_button)

    def stop_crawler_button(self):
        print "Stopping Crawler"
        self.spidy_object.terminate()

    def load_configuration_button(self):
        print "Loading Configuration"
        file = open("config.txt", "r")
        str(self.url_lineEdit.setText(file.readline()))
        str(self.url_pattern_lineEdit.setText(file.readline()))
        file.close()

    def save_configuration_button(self):
        print "Saving Configuration"
        file = open("config.txt", "w")
        file.write(str(self.url_lineEdit.text())+"\n")
        file.write(str(self.url_pattern_lineEdit.text()))
        file.close()

class spidy_worker(QThread):
    def __init__(self, url, url_pattern, url_type):
        QThread.__init__(self)
        print "Spidy Initializing"
        self.url = url
        self.url_pattern = url_pattern
        self.url_type = url_type

    def run(self):
        print "Running Thread"
        print "URL : "+str(self.url)
        print "URL Pattern : "+str(self.url_pattern)
        print "URL Type : "+str(self.url_type)

        if self.url_type == "typeA":
            self.getting_links_url_a("" , str(self.url), str(self.url_pattern))
        elif self.url_type == "typeB":
            self.getting_links_url_b("" , str(self.url), str(self.url_pattern))

    def getting_links_url_a(self, pageURL, url , url_pattern):
        print "\nWorker Thread Getting Links A from : "+self.url+"\n"
        global pages
        br = Browser()
        try:
            br.open((url+pageURL))
            bsObj = BeautifulSoup(br.response(), "lxml")
            for link in bsObj.findAll("a", href=re.compile(url_pattern)):
               if 'href' in link.attrs:
                   if link.attrs['href'] not in pages:
                       #to_text = open(file_name, 'a')
                       newPage = link.attrs['href']
                       to_result = '\nLink found ----->\n\n'+newPage
                       print to_result
                       #to_text.writelines((newPage+"\n"))                     
                       #to_text.close()
                       pages.add(newPage)
                       self.getting_links_url_a(newPage, "", url_pattern)    
                   else:
                       return;
               else:
                   return;
                               
        except Exception as e:
            print e 


    def getting_links_url_b(self, pageURL, url , url_pattern):
        print "Worker Threa Getting Links B"
        global pages