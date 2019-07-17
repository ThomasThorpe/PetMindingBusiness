#Thomas Thorpe
#Pet Service Are You Sure Pop-Up

from PyQt4.QtGui import *

class ConfirmationWindow(QDialog):
    def __init__(self, came_from, message):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Are You Sure?")
        self.CreateConfirmationWindow(message)
        self.setLayout(self.confirmation_layout)

    def CreateConfirmationWindow(self, message):
        #create widgets
        self.message = QLabel("{0}".format(message))
        self.yes_button = QPushButton("Yes")
        self.no_button = QPushButton("No")

        #create layout
        self.bottom_bar = QHBoxLayout()
        self.bottom_bar.addWidget(self.yes_button)
        self.bottom_bar.addWidget(self.no_button)

        self.confirmation_layout = QVBoxLayout()
        self.confirmation_layout.addWidget(self.message)
        self.confirmation_layout.addLayout(self.bottom_bar)

        #connections
        self.yes_button.clicked.connect(self.ReturnTrue)
        self.no_button.clicked.connect(self.ReturnFalse)

    def ReturnTrue(self):
        self.accept()

    def ReturnFalse(self):
        self.reject()
