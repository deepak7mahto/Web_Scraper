from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QThread
import mechanize
from bs4 import BeautifulSoup
import Web_Scrapper_Generic_UI, lxml, re, urlparse

pages = set()

class generic_crawler_class(object):

    def get_links(self):
        self.status_msgs_listWidget.addItem("Get Links Function")
        print "Get Links Function"
        self.url_lineEdit.setPlaceholderText("Enter URL ")
        self.url_pattern_lineEdit.setPlaceholderText("Enter URL pattern")
        self.file_name_lineEdit.setPlaceholderText("Enter File Name")
        
        self.connect(self.actionSave_Configuration_File, SIGNAL("triggered()"), self.save_configuration_button)
        self.connect(self.actionLoad_Configuration_File, SIGNAL("triggered()"), self.load_configuration_button)

        self.connect(self.absolute_url_radioButton , SIGNAL("clicked()"), self.url_type_a)
        self.connect(self.relative_url_radioButton , SIGNAL("clicked()"), self.url_type_r)
        
    def url_type_a(self):
        self.status_msgs_listWidget.addItem("Type: Absolute Selected")
        self.url = str(self.url_lineEdit.text())
        self.url_pattern = str(self.url_pattern_lineEdit.text())
        self.file_name_lineEdit.setText(str(str(urlparse.urlparse(str(self.url)).hostname)).strip(".com")+".txt")
        self.file_name = str(self.file_name_lineEdit.text())
        self.generic_crawler_class_object = generic_crawler_class_worker(self.url, self.url_pattern, "typeA", "", self.file_name)
        self.connect(self.start_crawling_pushButton, SIGNAL("clicked()"), self.generic_crawler_class_object.start)
        self.connect(self.stop_crawling_pushButton, SIGNAL("clicked()"), self.stop_crawler_button)
        self.connect(self.generic_crawler_class_object, SIGNAL("result_crawled_links_listWidget(QString)"), self.result_crawled_links_listWidget)
        self.connect(self.generic_crawler_class_object, SIGNAL("status_msg_listWidget(QString)"), self.status_msg_listWidget)

    def url_type_r(self):
        self.status_msgs_listWidget.addItem("Type: Relative Selected")
        self.url = str(self.url_lineEdit.text()).strip("")
        self.url_pattern = str(self.url_pattern_lineEdit.text())
        self.file_name_lineEdit.setText(str(str(urlparse.urlparse(str(self.url)).hostname)).strip(".com")+".txt")
        self.file_name = str(self.file_name_lineEdit.text())
        self.base_url = str(urlparse.urlparse(str(self.url)).hostname)
        self.generic_crawler_class_object = generic_crawler_class_worker(self.url, self.url_pattern, "typeR", self.base_url, self.file_name)
        self.connect(self.start_crawling_pushButton, SIGNAL("clicked()"), self.generic_crawler_class_object.start)
        self.connect(self.stop_crawling_pushButton, SIGNAL("clicked()"), self.stop_crawler_button)
        self.connect(self.generic_crawler_class_object, SIGNAL("result_crawled_links_listWidget(QString)"), self.result_crawled_links_listWidget)
        self.connect(self.generic_crawler_class_object, SIGNAL("status_msg_listWidget(QString)"), self.status_msg_listWidget)
        self.emit(SIGNAL("data_emitting(QString)"), self.file_name)


    def load_configuration_button(self):
        self.status_msgs_listWidget.addItem("Loading Configuration")
        print "Loading Configuration"
        file = open("config.txt", "r")
        str(self.url_lineEdit.setText(file.readline()))
        str(self.url_pattern_lineEdit.setText(file.readline()))
        file.close()

    def save_configuration_button(self):
        self.status_msgs_listWidget.addItem("Saving Configuration")
        print "Saving Configuration"
        file = open("config.txt", "w")
        file.write(str(self.url_lineEdit.text())+"\n")
        file.write(str(self.url_pattern_lineEdit.text()))
        file.close()

    def stop_crawler_button(self):
        self.status_msgs_listWidget.addItem("Stopping Crawler")
        print "Stopping Crawler"
        self.generic_crawler_class_object.terminate()

    def result_crawled_links_listWidget(self, add_to_list):
        self.crawled_links_listWidget.addItem(add_to_list)        

    def status_msg_listWidget(self, msg):
        self.status_msgs_listWidget.addItem(msg)

class generic_crawler_class_worker(QThread):

    def __init__(self, url, url_pattern, url_type, base_url, file_name):
        QThread.__init__(self)
        self.emit(SIGNAL("status_msg_listWidget(QString)"), "generic_crawler_class Initializing")
        print "generic_crawler_class Initializing"
        self.url = url
        self.url_pattern = url_pattern
        self.url_type = url_type
        self.base_url = base_url
        self.file_name = file_name

    def run(self):
        self.emit(SIGNAL("status_msg_listWidget(QString)"), "Running Thread , Starting Crawler")
        print "Running Thread"
        print "URL : "+self.url
        print "URL Pattern : "+self.url_pattern
        print "URL Type : "+self.url_type
        print "Base URl : "+self.base_url
        print "File Name : "+self.file_name


        if self.url_type == "typeA":
            self.getting_links_url_a("" , self.url, self.url_pattern, self.file_name)
        elif self.url_type == "typeR":
            self.getting_links_url_r("" , self.url, self.url_pattern, self.base_url, self.file_name)

    def getting_links_url_a(self, pageURL, url , url_pattern, file_name):
        global pages
        br = mechanize.Browser()
        try:
            br.open((url+pageURL))
            bsObj = BeautifulSoup(br.response(), "lxml")
            for link in bsObj.findAll("a", href=re.compile(url_pattern)):
               if 'href' in link.attrs:
                   if link.attrs['href'] not in pages:
                       to_text = open(file_name, "a")
                       newPage = link.attrs['href']
                       to_result = newPage
                       self.emit(SIGNAL("result_crawled_links_listWidget(QString)"), to_result)
                       print '\nLink found ----->\n\n'+to_result
                       to_text.writelines(newPage+"\n")
                       to_text.close()
                       pages.add(newPage)
                       self.getting_links_url_a(newPage, "", url_pattern, file_name)
                   else:
                       return;
               else:
                   return;
        except Exception as e:
            print e

    def getting_links_url_r(self, pageURL, url , url_pattern, base_url, file_name):
        global pages
        print str(file_name)

        br = mechanize.Browser()
        br.set_handle_robots(False)
        try:
            br = mechanize.Browser()
            if len(pages) == 0:
                print "Page Len :-> "+str(len(pages))
                br.open((url))
                print url
            else:
                print "Page Len :-> "+str(len(pages))
                br.open((r"http://"+base_url+pageURL))

            bsObj = BeautifulSoup(br.response(), "lxml")

            for link in bsObj.findAll("a"):

                if 'href' in link.attrs:
                    if link.attrs['href'] not in pages:
                        to_text = open(file_name, "a")
                        newPage = link.attrs['href']
                        if base_url not in newPage:
                            to_be_written = r"http://"+base_url+newPage
                        elif base_url in newPage:
                            to_be_written = newPage
                        print "\nCrawled : "+to_be_written+"\n"
                        if url_pattern in to_be_written:
                            print '\nLink found ----->\n\n'+to_be_written
                            self.emit(SIGNAL("result_crawled_links_listWidget(QString)"), to_be_written)
                            to_text.writelines((to_be_written+"\n"))
                        to_text.close()
                        pages.add(newPage)
                        self.getting_links_url_r(newPage, url, url_pattern, base_url, file_name)

        except Exception as e:
            print e