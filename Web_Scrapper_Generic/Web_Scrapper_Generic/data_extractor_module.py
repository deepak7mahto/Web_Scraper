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
        self.show_coloumn_name_listWidget.addItem(item1)
        self.show_css_selectors_listWidget.addItem(item2)

    def get_items(self):
        print "Getting items"        
        column_name_list = []
        css_selectors_list = []
        for x in range(50):
            try:
                column_name_list.append(str(self.show_coloumn_name_listWidget.item(x).text()))
                css_selectors_list.append(str(self.show_css_selectors_listWidget.item(x).text()))        
            except:
                continue
            print "Loop Counter "+str(x)
        self.extractor_worker_object = extractor_main_class_worker(column_name_list, css_selectors_list, self.file_)
        self.extractor_worker_object.start()

class extractor_main_class_worker(QThread):
    def __init__(self, column_name_list, css_selectors_list, file_name):
        QThread.__init__(self)
        print "Extractor Thread Initialized"
        self.column_name_list = column_name_list
        self.css_selectors_list = css_selectors_list
        self.file_name = file_name

    def run(self):
        print "Thread Started"
        print str(self.column_name_list)+str(self.css_selectors_list)+str(self.file_name)
        self.get_data(self.column_name_list, self.css_selectors_list, self.file_name)

    def get_data(self, column_name_list, css_selectors_list, file_name ):
        data = open(file_name, 'r')
        csv_file_name = str(file_name[:-4]+".csv")
        print "show data for : "+csv_file_name
        csv_file = open(csv_file_name, "a")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow((column_name_list))
            #csv_writer.writerow(("Link", "Title", "Company Name", "Experience", "Location", "Salary", "Openings", "Job Description", "Industry Type", "Functional Area", "Role Category", "Role", "Key Skills", "UG Requirements", "PG Requirements", "Docterate Requirements", "Additional Requirements", "Company Description"))
        row = 1
        nauk
        for link1 in data:
            br = mechanize.Browser()
            if row>len(css_selectors_list):
                try:
                    br.open(link1)
                    bsObj = BeautifulSoup(br.response(), 'lxml')

                    for text in css_selectors_list:
                        naukaridotcom_job = bsObj.select(text).get_text().strip().encode("utf-8")
                    """
                    naukaridotcom_job_heading = bsObj.select("div.hdSec h1.small_title")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_company_name = bsObj.select("a.pHead")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_experience = bsObj.select("div.p span")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_location = bsObj.select("div.loc a")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_salary = bsObj.select("span.sal")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_no_of_openings = bsObj.select("div.sumFoot span")[2].get_text().strip().encode("utf-8")
                    naukaridotcom_job_description = bsObj.select("div.JD ul")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_industry_type = bsObj.select("div.jDisc p")[1].get_text().strip("Industry:").strip().encode("utf-8")
                    naukaridotcom_job_functional_area = bsObj.select("div.jDisc p")[2].get_text().strip("Functional Area:").strip().encode("utf-8")
                    naukaridotcom_job_role_category = bsObj.select("div.jDisc p")[3].get_text().strip("Role Category:").strip().encode("utf-8")
                    naukaridotcom_job_role = bsObj.select("div.jDisc p")[4].get_text().strip("Role:").strip().encode("utf-8")
                    naukaridotcom_job_key_skills = bsObj.select("div.ksTags")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_educational_ug_req = bsObj.select("div.edu p span")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_educational_pg_req = bsObj.select("div.edu p span")[1].get_text().strip().encode("utf-8")
                    naukaridotcom_job_educational_doctorate_req = bsObj.select("div.edu p span")[2].get_text().strip().encode("utf-8")
                    naukaridotcom_job_additional_req = bsObj.select("ul.mt15")[0].get_text().strip().encode("utf-8")
                    naukaridotcom_job_about_company = bsObj.select("div.discp")[0].get_text().strip().encode("utf-8")
                    """
                    csv_writer.writerow((link1, naukaridotcom_job_heading, naukaridotcom_job_company_name, naukaridotcom_job_experience,  naukaridotcom_job_location, naukaridotcom_job_salary, naukaridotcom_job_no_of_openings, naukaridotcom_job_description, naukaridotcom_job_industry_type, naukaridotcom_job_functional_area, naukaridotcom_job_role_category, naukaridotcom_job_role, naukaridotcom_job_key_skills, naukaridotcom_job_educational_ug_req, naukaridotcom_job_educational_pg_req, naukaridotcom_job_educational_doctorate_req, naukaridotcom_job_additional_req, naukaridotcom_job_about_company))
                
                    row += 1
                
                    self.emit(QtCore.SIGNAL("showing_data(QString)"), naukaridotcom_job_heading )

                    print "Done CSV Writing for -->\n"+naukaridotcom_job_heading
                    
                except Exception as e:
                    print e
               
        csv_file.close()
        data.close() 