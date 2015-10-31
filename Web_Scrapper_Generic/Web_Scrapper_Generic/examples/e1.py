import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.btn1 = QPushButton()
        self.btn1.setText("Click me")
        self.btn1.setObjectName("btn1")

        self.display_list = QListWidget()
        self.display_list.setObjectName("display_list")
        
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.display_list)
        self.setLayout(self.layout)

        self.connect(self.btn1, SIGNAL("clicked()"), self.btn1_action)

    def btn1_action(self):
        print "Btn1 Clicked"
        self.display_list.addItem("Button Clicked")
        self.dynamic_buttons()

    def dynamic_buttons(self):
        print "Creating Dynamic Buttons"
        self.btn2 = QPushButton()
        self.btn2.setText("Btn2")
        self.layout.addWidget(self.btn2)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    app.exec_()