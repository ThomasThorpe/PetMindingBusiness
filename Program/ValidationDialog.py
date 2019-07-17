#Thomas Thorpe
#Pet Service Validation Dialog

from PyQt4.QtGui import *

class ValidationDialog(QDialog):
    def __init__(self, came_from, messages):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Validation Error")
        self.messages = messages #take error messages from pervious window
        self.CreateValidationDialog(messages)
        self.setLayout(self.validation_layout)
        self.exec_()

    def CreateValidationDialog(self, messages):
        #create widgets
        self.top_lbl = QLabel("The following information has been entered incorrectly:")
        count = 0
        self.message = [] #will contain list of label widgets for error messages

        for each in messages: #for each error message create a lable widget displaying them and add to list
            self.message.append(QLabel("\t {0}".format(each)))
            count = count + 1

        self.ok_button = QPushButton("Ok")
        self.ok_button.isDefault()

        #create layout
        self.validation_layout = QVBoxLayout()
        self.validation_layout.addWidget(self.top_lbl)

        for each in self.message:
            self.validation_layout.addWidget(each)

        self.validation_layout.addWidget(self.ok_button)

        #connectons
        self.ok_button.clicked.connect(self.Close)

    def Close(self):
        self.close()



