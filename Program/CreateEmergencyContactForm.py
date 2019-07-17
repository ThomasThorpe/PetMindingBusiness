#Thomas Thorpe
#Pet Service Create Emergency Contact Window

from PetServiceDatabase import *

import re
from PyQt4.QtGui import *
from ValidationChecking import *
from ValidationDialog import *

class CreateEmergencyContactWindow(QDialog):
    def __init__(self, came_from):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Create Emegency Contact Form")
        self.CreateNewEmergencyContactWindow()
        self.setLayout(self.create_emergency_contact_layout)
        self.exec_()

    def CreateNewEmergencyContactWindow(self):
        #create widgets
        #labels
        self.lbl_first_name = QLabel("First Name")
        self.lbl_last_name = QLabel("Last Name")
        self.lbl_addr1 = QLabel("Address Line 1")
        self.lbl_addr2 = QLabel("Address Line 2")
        self.lbl_addr3 = QLabel("Address Line 3")
        self.lbl_addr4 = QLabel("Address Line 4")
        self.lbl_postcode = QLabel("Post Code")
        self.lbl_mobile = QLabel("Mobile Number")
        self.lbl_home = QLabel("Home Number")
        self.lbl_email_addr = QLabel("Email Address")

        #line edits
        self.le_first_name = QLineEdit()
        self.le_first_name.setMaxLength(20)
        self.le_last_name = QLineEdit()
        self.le_last_name.setMaxLength(20)
        self.le_addr1 = QLineEdit()
        self.le_addr1.setMaxLength(30)
        self.le_addr2 = QLineEdit()
        self.le_addr2.setMaxLength(30)
        self.le_addr3 = QLineEdit()
        self.le_addr3.setMaxLength(30)
        self.le_addr4 = QLineEdit()
        self.le_addr4.setMaxLength(30)
        self.le_postcode = QLineEdit()
        self.le_postcode.setPlaceholderText("LLDD DLL")
        self.le_postcode.setMaxLength(8)
        self.le_mobile = QLineEdit()
        self.le_mobile.setMaxLength(14)
        self.le_home = QLineEdit()
        self.le_home.setMaxLength(12)
        self.le_email_addr = QLineEdit()
        self.le_email_addr.setMaxLength(30)

        #buttons
        self.submit_button = QPushButton("Submit New Emergency Contact Details")
        self.submit_button.setDefault(True)
        self.cancel_button = QPushButton("Cancel")

        #create layout
        self.grid_layout = QGridLayout()

        self.grid_layout.addWidget(self.lbl_first_name,0,0)
        self.grid_layout.addWidget(self.lbl_last_name,1,0)
        self.grid_layout.addWidget(self.lbl_addr1,2,0)
        self.grid_layout.addWidget(self.lbl_addr2,3,0)
        self.grid_layout.addWidget(self.lbl_addr3,4,0)

        self.grid_layout.addWidget(self.le_first_name,0,1)
        self.grid_layout.addWidget(self.le_last_name,1,1)
        self.grid_layout.addWidget(self.le_addr1,2,1)
        self.grid_layout.addWidget(self.le_addr2,3,1)
        self.grid_layout.addWidget(self.le_addr3,4,1)

        self.grid_layout.addWidget(self.lbl_addr4,0,2)
        self.grid_layout.addWidget(self.lbl_postcode,1,2)
        self.grid_layout.addWidget(self.lbl_mobile,2,2)
        self.grid_layout.addWidget(self.lbl_home,3,2)
        self.grid_layout.addWidget(self.lbl_email_addr,4,2)

        self.grid_layout.addWidget(self.le_addr4,0,3)
        self.grid_layout.addWidget(self.le_postcode,1,3)
        self.grid_layout.addWidget(self.le_mobile,2,3)
        self.grid_layout.addWidget(self.le_home,3,3)
        self.grid_layout.addWidget(self.le_email_addr,4,3)

        self.bottom_bar_layout = QHBoxLayout()
        self.bottom_bar_layout.addWidget(self.submit_button)
        self.bottom_bar_layout.addWidget(self.cancel_button)

        self.create_emergency_contact_layout = QVBoxLayout()
        self.create_emergency_contact_layout.addLayout(self.grid_layout)
        self.create_emergency_contact_layout.addLayout(self.bottom_bar_layout)

        #connections
        self.cancel_button.clicked.connect(self.BackToParent)
        self.submit_button.clicked.connect(self.AddEmergencyContact)

    def BackToParent(self):
        self.close()

    def ValidateFields(self):
        messages = []
        #regex validation
        check_result = CheckPostcode(self.le_postcode.text())
        if check_result != "-1":
            messages.append(check_result)

        check_result = CheckMobileNumber(self.le_mobile.text())
        if check_result != "-1":
            messages.append(check_result)

        check_result = CheckHomeNumber(self.le_home.text())
        if check_result != "-1":
            messages.append(check_result)

        check_result = CheckEmailAddress(self.le_email_addr.text())
        if check_result != "-1":
            messages.append(check_result)

        #no text fields are empty
        if self.le_first_name.text() == "":
            messages.append("No first name was enterd")

        if self.le_last_name.text() == "":
            messages.append("No last name was entered")

        if self.le_addr1.text() == "":
            messages.append("Address line 1 wasn't entered")

        if self.le_addr2.text() == "":
            messages.append("Address line 2 wasn't entered")

        if self.le_addr3.text() == "":
            messages.append("Address line 3 wasn't entered")

        if self.le_addr4.text() == "":
            messages.append("Address line 4 wasn't entered")
        
        return messages

    def AddEmergencyContact(self):
        validation_messages = self.ValidateFields()
        if len(validation_messages) == 0: #make sure no validation errors
            values = []
            values.append(self.le_first_name.text())
            values.append(self.le_last_name.text())
            values.append(self.le_addr1.text())
            values.append(self.le_addr2.text())
            values.append(self.le_addr3.text())
            values.append(self.le_addr4.text())
            values.append(self.le_postcode.text())
            values.append(self.le_mobile.text())
            values.append(self.le_home.text())
            values.append(self.le_email_addr.text())

            database.AddRecord("Emergency", values)

            self.BackToParent()
        else:
            validation_dialog = ValidationDialog(self, validation_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_()
