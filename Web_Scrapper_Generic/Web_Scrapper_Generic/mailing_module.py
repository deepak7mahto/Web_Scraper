from datetime import datetime
import smtplib
import sys, mechanize, re, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate, COMMASPACE
from bs4 import BeautifulSoup
from PyQt4 import QtCore, QtGui, Qt

class mailing_main_class(object):
    """description of class"""
    def mailing(self):
        #initializing mailing system
        self.statusbox_listWidget_emailtab.addItem("Mailing System Initialized")
        print "Starting Mailing System "
        self.sendto_textEdit_emailtab.setText("deepak7mahto@gmail.com,krhemant.cool@gmail.com,tushar.kashyap619@gmail.com,urbancod3r@gmail.com,gta267@gmail.com, shalutyagi47@yahoo.com,leovarsha.chaudhary1993@gmail.com,adityabhel93@gmail.com,prn826@gmail.com,scrapperweb@gmail.com")
        self.add_text_message_textEdit_emailtab.setText("Please find the attachment")        
        self.select_file_lineEdit_emailtab.setPlaceholderText("Select CSV File Using Selct Button")
        self.select_file_lineEdit_emailtab_2.setPlaceholderText("Select Links File Using Selct Button")
        self.connect(self.send_mail_pushButton_emailtab, QtCore.SIGNAL("clicked()"), self.mailing_operation)
        self.connect(self.select_file_pushButton_emailtab, QtCore.SIGNAL("pressed()"), self.getting_file_name_emailtab)
        self.connect(self.select_file_pushButton_emailtab_2, QtCore.SIGNAL("pressed()"), self.getting_file_name_emailtab_2)       

    def mailing_operation(self):
        self.statusbox_listWidget_emailtab.addItem("Mailing Operations Started")
        print "Starting Mailing Operation"        
        self.text_to_be_added = str(self.add_text_message_textEdit_emailtab.toPlainText())
        print "Message Body : "+ self.text_to_be_added
        self.to_address_list = (self.sendto_textEdit_emailtab.toPlainText())
        self.file_name1 = self.select_file_lineEdit_emailtab.text()
        self.file_name2 = self.select_file_lineEdit_emailtab_2.text()
        print "File Name : "+self.file_name1+"\n"+self.file_name2
        self.mailing_object = EmailTab_worker_thread_mailing(self.to_address_list, self.text_to_be_added, self.file_name1, self.file_name2)
        self.mailing_object.start()
        self.connect(self.mailing_object, QtCore.SIGNAL("status_msg_emailtab(QString)"), self.status_msg_emailtab)        
        self.connect(self.stop_mail_pushButton_emailtab, QtCore.SIGNAL("clicked()"), self.mailing_stop_button)
        self.send_mail_pushButton_emailtab.setDisabled(True)

    def mailing_stop_button(self):
        self.statusbox_listWidget_emailtab.addItem("Stopping Mailing")
        print "Stopping Mailing"
        self.mailing_object.terminate()
        self.send_mail_pushButton_emailtab.setEnabled(True)

    def getting_file_name_emailtab(self):
        print "Getting File Path"
        self.select_file_lineEdit_emailtab_2.setText((Qt.QString(QtGui.QFileDialog.getOpenFileName())))
        
    def getting_file_name_emailtab_2(self):
        print "Getting File Path"
        self.select_file_lineEdit_emailtab.setText((Qt.QString(QtGui.QFileDialog.getOpenFileName())))

    def status_msg_emailtab(self, msg):
        self.statusbox_listWidget_emailtab.addItem(msg)        


class EmailTab_worker_thread_mailing(QtCore.QThread):
    def __init__(self, to_address_list, text_to_be_added, file_name1, file_name2):
        QtCore.QThread.__init__(self)
        print "Email Thread Initialized"
        self.to_address_list = to_address_list
        self.text_to_be_added = text_to_be_added
        self.file_name1 = file_name1
        self.file_name2 = file_name2

    def run(self):
        print "Email Thread Satarted"
        self.emit(QtCore.SIGNAL("status_msg_emailtab(QString)"), "Email Thread Satarted")
        self.mailing_function(self.to_address_list, self.text_to_be_added, self.file_name1, self.file_name2)

    def mailing_function(self, to_address_list, text_to_be_added, file_name1, file_name2):
        self.username = raw_input("Enter Email ID -> ")
        self.password = raw_input("Enter Password -> ")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        try:
            #mailing
            self.emit(QtCore.SIGNAL("status_msg_emailtab(QString)"), "Started Setting Up Mail Server")  
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()
            server.ehlo() 
            server.login(self.username, self.password)
            self.emit(QtCore.SIGNAL("status_msg_emailtab(QString)"), "Mail Server Setup Complete")
            from_address = self.username
            to_address = list(str(self.to_address_list).split(","))
            print "Sending To : "+str(to_address)
            print "File Name : "+str(self.file_name1)
            print "File Name : "+str(self.file_name2)

            #msg_start
            msg = MIMEMultipart()
            msg['Subject'] = "Scrapper Subject"
            msg['From'] = from_address
            msg['Date'] = formatdate(localtime = True)        
            msg.attach(MIMEText(self.text_to_be_added))
            msg.attach(MIMEText(file(str(self.file_name1)).read(), 'text'))
            msg.attach(MIMEText(file(str(self.file_name2)).read(), 'text'))
        
            print "Sending Mail"
            self.emit(QtCore.SIGNAL("status_msg_emailtab(QString)"), "Sending Mail")
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            print "Mail Sent"
            self.emit(QtCore.SIGNAL("status_msg_emailtab(QString)"), "Mail Sent")
       
        except Exception as e:
            self.emit(QtCore.SIGNAL("status_msg_emailtab(QString)"), str(e))
