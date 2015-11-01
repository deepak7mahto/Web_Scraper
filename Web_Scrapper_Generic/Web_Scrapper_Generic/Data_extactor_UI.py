# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Data_extractor_UI.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(759, 485)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 701, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 661, 73))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.textBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 140, 701, 281))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 321, 211))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 211, 19))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 20, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(360, 50, 321, 211))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 20, 301, 19))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 430, 701, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget1 = QtGui.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 681, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.widget1)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.widget1)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_6 = QtGui.QPushButton(self.widget1)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtGui.QPushButton(self.widget1)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Data Extarctor", None))
        self.groupBox.setTitle(_translate("Form", "Load Links File", None))
        self.pushButton.setText(_translate("Form", "Load File", None))
        self.groupBox_2.setTitle(_translate("Form", "Enetr Details of Extaction", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Colum Item Names", None))
        self.pushButton_2.setText(_translate("Form", "Add Item", None))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Corresponding CSS Selector", None))
        self.pushButton_3.setText(_translate("Form", "Save Extraction Details", None))
        self.pushButton_4.setText(_translate("Form", "Load Last Extraction Details", None))
        self.pushButton_6.setText(_translate("Form", "Select CSv File", None))
        self.pushButton_5.setText(_translate("Form", "Start Extaction", None))

