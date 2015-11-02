from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QThread
import mechanize, csv
from bs4 import BeautifulSoup
import Web_Scrapper_Generic_UI, lxml, re, urlparse, generic_crawler_module

class extractor_main_class(object):    

    def get_data(self):
        print "Getting Data"
        self.connect(self.load_file_pushButton, SIGNAL("clicked()"), self.load_file_function)
        self.connect(self.add_item_pushButton, SIGNAL("clicked()"), self.add_items_function)
        self.connect(self.load_extraction_details_pushButton, SIGNAL("clicked()"), self.get_items)  

    def load_file_function(self):
        print "loading file"
        self.show_file_name_textBrowser.setText(QtGui.QFileDialog().getOpenFileName())
        print str(self.show_file_name_textBrowser.toPlainText())
        self.file_ = str(self.show_file_name_textBrowser.toPlainText())

    def add_items_function(self):
        print "Adding Items"
        item1 = self.column_names_lineEdit.text()
        item2 = self.css_selector_lineEdit.text()
        item3 = self.css_list_spinBox.text()
        self.show_coloumn_name_listWidget.addItem(item1)
        self.show_css_selectors_listWidget.addItem((item2+"["+item3+"]"))        

    def get_items(self):
        print "Getting items"        
        column_name_list = []
        css_selectors_list = []
        css_list_num = []
        for x in range(50):
            try:
                column_name_list.append(str(self.show_coloumn_name_listWidget.item(x).text()))
                css_selectors_list.append(str(self.show_css_selectors_listWidget.item(x).text())) 
                css_list_num.append(int(self.css_list_spinBox.text()))
            except:
                continue
            print "Loop Counter "+str(x)
        self.extractor_worker_object = extractor_main_class_worker(column_name_list, css_selectors_list, css_list_num, self.file_)
        self.extractor_worker_object.start()

class extractor_main_class_worker(QThread):
    def __init__(self, column_name_list, css_selectors_list, css_list_num, file_name):
        QThread.__init__(self)
        print "Extractor Thread Initialized"
        self.column_name_list = column_name_list
        self.css_selectors_list = css_selectors_list
        self.css_list_num = css_list_num
        self.file_name = file_name

    def run(self):
        print "Thread Started"
        print str(self.column_name_list)+str(self.css_selectors_list)+str(self.file_name)
        self.get_data(self.column_name_list, self.css_selectors_list, self.css_list_num, self.file_name)

    def get_data(self, column_name_list, css_selectors_list, css_list_num ,file_name ):
        data = open(file_name, 'r')
        csv_file_name = str(file_name[:-4]+".csv")
        print "show data for : "+csv_file_name
        csv_file = open(csv_file_name, "a")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow((column_name_list))
        row = 0
        
        for link1 in data:
            br = mechanize.Browser()
            if row<10:
                try:
                    br.open(link1)
                    bsObj = BeautifulSoup(br.response(), 'lxml')
                    print str(css_selectors_list)
                    row_list = []
                    for text, num in css_selectors_list:
                        print "flag"
                        t1 = bsObj.select(text)[num].get_text().strip().encode("utf-8")
                        row_list.append(t1)
                        print t1           
                    print str(row_list)
                    csv_writer.writerow((row_list))   
                    row += 1
                    print "Done CSV Writing for -->\n"+row_list[0]
                except Exception as e:
                    continue
               
        csv_file.close()
        data.close() 