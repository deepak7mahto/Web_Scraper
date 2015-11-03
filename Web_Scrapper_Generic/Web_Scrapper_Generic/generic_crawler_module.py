from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QThread
import mechanize
from bs4 import BeautifulSoup
import Web_Scrapper_Generic_UI, lxml, re, urlparse

pages = set()
#set is a data structure which accepts unique values it is required here because we want only unique link at every crawling cycles 

class generic_crawler_class(object):
    # the crawler class
    def get_links(self):
        QtCore.QObject.connect(
        #function is used to get links from the GUI 
        self.status_msgs_listWidget.addItem("Get Links Function")
        #to show the message in the  list Widget  
        print "Get Links Function"
        #to print on the console 
        self.url_lineEdit.setPlaceholderText("Enter URL ")
        #to place the water mark text in the box where we have to enter the url 
        self.url_pattern_lineEdit.setPlaceholderText("Enter URL pattern")
        #to place the water mark text in the box where we have to enter the url
        self.file_name_lineEdit.setPlaceholderText("Enter File Name")
        #to place the water mark text in the box where we have to enter the file name 
        self.connect(self.actionSave_Configuration_File, SIGNAL("triggered()"), self.save_configuration_button)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.actionLoad_Configuration_File, SIGNAL("triggered()"), self.load_configuration_button)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        #The sender is an object that sends a signal. The receiver is the object that receives the signal. The slot is the method that reacts to the signal.
        #A signal is emitted when a particular event occurs A slot can be any Python callable. A slot is called when a signal connected to it is emitted
        self.connect(self.absolute_url_radioButton , SIGNAL("clicked()"), self.url_type_a)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.relative_url_radioButton , SIGNAL("clicked()"), self.url_type_r)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever )

    def url_type_a(self):
        #called when the Absolute button is selected 
        self.status_msgs_listWidget.addItem("Type: Absolute Selected")
        #it displays the message in the status message dailog box .
        self.url = str(self.url_lineEdit.text())
        #fetch the url from the url box and convert it to the string 
        self.url_pattern = str(self.url_pattern_lineEdit.text())
        #fetch the url_pattern from the url_pattern and convert it to the string 
        self.file_name_lineEdit.setText(str(str(urlparse.urlparse(str(self.url)).hostname)).strip(".com")+".txt")
        #the file will be named as the domain name of the target and the extention to the file will be given as the .txt
        self.file_name = str(self.file_name_lineEdit.text())
        #set the file_name to file_name_lineEdit.text() 
        self.generic_crawler_class_object = generic_crawler_class_worker(self.url, self.url_pattern, "typeA", "", self.file_name)
        #an object of type generic_crawler_class_worker object is created and the above initialised elements are passed to it 
        self.connect(self.start_crawling_pushButton, SIGNAL("clicked()"), self.generic_crawler_class_object.start)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.stop_crawling_pushButton, SIGNAL("clicked()"), self.stop_crawler_button)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.generic_crawler_class_object, SIGNAL("result_crawled_links_listWidget(QString)"), self.result_crawled_links_listWidget)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.generic_crawler_class_object, SIGNAL("status_msg_listWidget(QString)"), self.status_msg_listWidget)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
    def url_type_r(self):
        #data for the relative_url_crawler 
        self.status_msgs_listWidget.addItem("Type: Relative Selected")
        #it displays the message in the status message dailog box
        self.url = str(self.url_lineEdit.text()).strip("")
        #to get the relative url
        self.url_pattern = str(self.url_pattern_lineEdit.text())
        #fetch the url_pattern from the url_pattern and convert it to the string 
        self.file_name_lineEdit.setText(str(str(urlparse.urlparse(str(self.url)).hostname)).strip(".com")+".txt")
        #the file will be named as the domain name of the target and the extention to the file will be given as the .txt
        self.file_name = str(self.file_name_lineEdit.text())
        #set the file_name to file_name_lineEdit.text() 
        self.base_url = str(urlparse.urlparse(str(self.url)).hostname)
        #to get the hostname from the entered url 
        self.generic_crawler_class_object = generic_crawler_class_worker(self.url, self.url_pattern, "typeR", self.base_url, self.file_name)
        #make an object of crawler typeR that is the relative crawler  
        self.connect(self.start_crawling_pushButton, SIGNAL("clicked()"), self.generic_crawler_class_object.start)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.stop_crawling_pushButton, SIGNAL("clicked()"), self.stop_crawler_button)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.generic_crawler_class_object, SIGNAL("result_crawled_links_listWidget(QString)"), self.result_crawled_links_listWidget)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.connect(self.generic_crawler_class_object, SIGNAL("status_msg_listWidget(QString)"), self.status_msg_listWidget)
        #self.connect(self.SIGNAL_SENDER,SIGNAL(SIGNAL_TYPE),self.reciever)
        self.emit(SIGNAL("data_emitting(QString)"), self.file_name)
        #to generate the signal 

    def load_configuration_button(self):
        #function to load the configuration file the contains the starting url and the urlpttern
        self.status_msgs_listWidget.addItem("Loading Configuration")
        print "Loading Configuration"
        #print to the terminal
        file = open("config.txt", "r")
        #opening the file in the read mode 
        str(self.url_lineEdit.setText(file.readline()))
        #this set the data in the url dailog box
        str(self.url_pattern_lineEdit.setText(file.readline()))
        #this sets the data in the url_pattern dailog box 
        file.close()
        #this is done to close the file 
    def save_configuration_button(self):
        #Function to save the configuration file 
        self.status_msgs_listWidget.addItem("Saving Configuration")
        #it displays the message in the status message dailog bo
        print "Saving Configuration"
        #print to the terminal
        file = open("config.txt", "w")
        #open file in the write mode 
        file.write(str(self.url_lineEdit.text())+"\n")
        #write url to the configuration file 
        file.write(str(self.url_pattern_lineEdit.text()))
        #write url_pattern to the configuration file 
        file.close()
        #close the file
    def stop_crawler_button(self):
       #function to stop the crawler
        self.status_msgs_listWidget.addItem("Stopping Crawler")
        #it displays the message in the status message dailog box
        print "Stopping Crawler"
        #print in the terminal
        self.generic_crawler_class_object.terminate()
        #

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