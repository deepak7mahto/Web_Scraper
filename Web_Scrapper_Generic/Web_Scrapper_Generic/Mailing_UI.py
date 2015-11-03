# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mailing_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mailing_dialog(object):
    def setupUi(self, mailing_dialog):
        mailing_dialog.setObjectName(_fromUtf8("mailing_dialog"))
        mailing_dialog.resize(815, 580)
        self.verticalLayoutWidget = QtGui.QWidget(mailing_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(710, 370, 91, 191))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.send_mail_pushButton_emailtab = QtGui.QPushButton(self.verticalLayoutWidget)
        self.send_mail_pushButton_emailtab.setFlat(False)
        self.send_mail_pushButton_emailtab.setObjectName(_fromUtf8("send_mail_pushButton_emailtab"))
        self.verticalLayout_2.addWidget(self.send_mail_pushButton_emailtab)
        self.stop_mail_pushButton_emailtab = QtGui.QPushButton(self.verticalLayoutWidget)
        self.stop_mail_pushButton_emailtab.setObjectName(_fromUtf8("stop_mail_pushButton_emailtab"))
        self.verticalLayout_2.addWidget(self.stop_mail_pushButton_emailtab)
        self.reset_pushButton_emailtab = QtGui.QPushButton(self.verticalLayoutWidget)
        self.reset_pushButton_emailtab.setObjectName(_fromUtf8("reset_pushButton_emailtab"))
        self.verticalLayout_2.addWidget(self.reset_pushButton_emailtab)
        self.quit_pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.quit_pushButton.setObjectName(_fromUtf8("quit_pushButton"))
        self.verticalLayout_2.addWidget(self.quit_pushButton)
        self.groupBox_3 = QtGui.QGroupBox(mailing_dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 90, 789, 141))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.sendto_textEdit_emailtab = QtGui.QTextEdit(self.groupBox_3)
        self.sendto_textEdit_emailtab.setGeometry(QtCore.QRect(10, 20, 769, 101))
        self.sendto_textEdit_emailtab.setObjectName(_fromUtf8("sendto_textEdit_emailtab"))
        self.groupBox_5 = QtGui.QGroupBox(mailing_dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 791, 71))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_5)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 20, 771, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.select_file_pushButton_emailtab = QtGui.QPushButton(self.layoutWidget)
        self.select_file_pushButton_emailtab.setObjectName(_fromUtf8("select_file_pushButton_emailtab"))
        self.horizontalLayout.addWidget(self.select_file_pushButton_emailtab)
        self.select_file_lineEdit_emailtab_2 = QtGui.QLineEdit(self.layoutWidget)
        self.select_file_lineEdit_emailtab_2.setObjectName(_fromUtf8("select_file_lineEdit_emailtab_2"))
        self.horizontalLayout.addWidget(self.select_file_lineEdit_emailtab_2)
        self.select_file_pushButton_emailtab_2 = QtGui.QPushButton(self.layoutWidget)
        self.select_file_pushButton_emailtab_2.setObjectName(_fromUtf8("select_file_pushButton_emailtab_2"))
        self.horizontalLayout.addWidget(self.select_file_pushButton_emailtab_2)
        self.select_file_lineEdit_emailtab = QtGui.QLineEdit(self.layoutWidget)
        self.select_file_lineEdit_emailtab.setObjectName(_fromUtf8("select_file_lineEdit_emailtab"))
        self.horizontalLayout.addWidget(self.select_file_lineEdit_emailtab)
        self.groupBox_6 = QtGui.QGroupBox(mailing_dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(12, 362, 691, 201))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.statusbox_listWidget_emailtab = QtGui.QListWidget(self.groupBox_6)
        self.statusbox_listWidget_emailtab.setGeometry(QtCore.QRect(10, 20, 671, 161))
        self.statusbox_listWidget_emailtab.setAutoFillBackground(False)
        self.statusbox_listWidget_emailtab.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.statusbox_listWidget_emailtab.setAlternatingRowColors(False)
        self.statusbox_listWidget_emailtab.setProperty("isWrapping", True)
        self.statusbox_listWidget_emailtab.setWordWrap(True)
        self.statusbox_listWidget_emailtab.setObjectName(_fromUtf8("statusbox_listWidget_emailtab"))
        self.groupBox_4 = QtGui.QGroupBox(mailing_dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 240, 791, 121))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.add_text_message_textEdit_emailtab = QtGui.QTextEdit(self.groupBox_4)
        self.add_text_message_textEdit_emailtab.setGeometry(QtCore.QRect(10, 20, 771, 81))
        self.add_text_message_textEdit_emailtab.setObjectName(_fromUtf8("add_text_message_textEdit_emailtab"))

        self.retranslateUi(mailing_dialog)
        QtCore.QObject.connect(self.quit_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), mailing_dialog.close)
        QtCore.QObject.connect(self.reset_pushButton_emailtab, QtCore.SIGNAL(_fromUtf8("clicked()")), self.select_file_lineEdit_emailtab_2.clear)
        QtCore.QObject.connect(self.reset_pushButton_emailtab, QtCore.SIGNAL(_fromUtf8("clicked()")), self.select_file_lineEdit_emailtab.clear)
        QtCore.QObject.connect(self.reset_pushButton_emailtab, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendto_textEdit_emailtab.clear)
        QtCore.QObject.connect(self.reset_pushButton_emailtab, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_text_message_textEdit_emailtab.clear)
        QtCore.QMetaObject.connectSlotsByName(mailing_dialog)

    def retranslateUi(self, mailing_dialog):
        mailing_dialog.setWindowTitle(_translate("mailing_dialog", "Mailing", None))
        self.send_mail_pushButton_emailtab.setText(_translate("mailing_dialog", "Send", None))
        self.stop_mail_pushButton_emailtab.setText(_translate("mailing_dialog", "Stop", None))
        self.reset_pushButton_emailtab.setText(_translate("mailing_dialog", "Reset Boxes", None))
        self.quit_pushButton.setText(_translate("mailing_dialog", "Quit", None))
        self.groupBox_3.setTitle(_translate("mailing_dialog", "Send To", None))
        self.groupBox_5.setTitle(_translate("mailing_dialog", "Select Files", None))
        self.select_file_pushButton_emailtab.setText(_translate("mailing_dialog", "Links Text File", None))
        self.select_file_pushButton_emailtab_2.setText(_translate("mailing_dialog", "Data CSV File", None))
        self.groupBox_6.setTitle(_translate("mailing_dialog", "Status Messages", None))
        self.statusbox_listWidget_emailtab.setSortingEnabled(False)
        self.groupBox_4.setTitle(_translate("mailing_dialog", "Add Text to Message", None))

