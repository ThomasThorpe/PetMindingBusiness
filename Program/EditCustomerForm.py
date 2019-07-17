#Thomas Thorpe
#Pet Service Edit Customer Form

from PetServiceDatabase import *

import re
from PyQt4.QtGui import *
from ValidationChecking import *
from ValidationDialog import *
from CreateEmergencyContactForm import *
from CreateVetForm import *
from AreYouSureWindow import *
import ComboAddNew
import PopulateXCombo

class EditCustomerWindow(QDialog):
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Edit Customer Form")
        self.table_name = "Customer"
        self.record_id = record_id
        self.CreateEditCustomerWindow()
        self.PopulateWindow()
        self.setLayout(self.edit_customer_layout)
        self.exec_()

    def CreateEditCustomerWindow(self):
        #create widgets
        #labels
        self.lbl_first_name = QLabel("First Name")
        self.lbl_last_name = QLabel("Last Name")
        self.lbl_addr1 = QLabel("Address Line 1")
        self.lbl_addr2 = QLabel("Address Line 2")
        self.lbl_addr3 = QLabel("Address Line 3")
        self.lbl_addr4 = QLabel("Address Line 4")
        self.lbl_vet = QLabel("Vet Contact")
        self.lbl_postcode = QLabel("Post Code")
        self.lbl_mobile = QLabel("Mobile Number")
        self.lbl_home = QLabel("Home Number")
        self.lbl_email_addr = QLabel("Email Address")
        self.lbl_permission_vet = QLabel("Permission For Vet")
        self.lbl_picture_usuage = QLabel("Permission For Picture Usuage")
        self.lbl_emergency = QLabel("Emergency Conact")

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
        self.le_postcode.setMaxLength(8)
        self.le_mobile = QLineEdit()
        self.le_mobile.setMaxLength(12)
        self.le_home = QLineEdit()
        self.le_home.setMaxLength(12)
        self.le_email_addr = QLineEdit()
        self.le_email_addr.setMaxLength(30)

        #combos
        self.vet_combo = QComboBox(self)
        self.PopulateVetCombo()

        self.emergency_combo = QComboBox(self)
        self.PopulateEmergencyCombo()

        self.permission_vet_combo = QComboBox(self)
        self.permission_vet_combo.addItem("Yes")
        self.permission_vet_combo.addItem("No")

        self.picture_usuage_combo = QComboBox(self)
        self.picture_usuage_combo.addItem("Yes")
        self.picture_usuage_combo.addItem("No")

        self.submit_button = QPushButton("Submit Revisions To Customer")
        self.submit_button.setDefault(True)
        self.cancel_button = QPushButton("Cancel")

        #create layout
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.lbl_first_name,0,0)
        self.grid_layout.addWidget(self.lbl_last_name,1,0)
        self.grid_layout.addWidget(self.lbl_addr1,2,0)
        self.grid_layout.addWidget(self.lbl_addr2,3,0)
        self.grid_layout.addWidget(self.lbl_addr3,4,0)
        self.grid_layout.addWidget(self.lbl_addr4,5,0)
        self.grid_layout.addWidget(self.lbl_postcode,6,0)

        self.grid_layout.addWidget(self.le_first_name,0,1)
        self.grid_layout.addWidget(self.le_last_name,1,1)
        self.grid_layout.addWidget(self.le_addr1,2,1)
        self.grid_layout.addWidget(self.le_addr2,3,1)
        self.grid_layout.addWidget(self.le_addr3,4,1)
        self.grid_layout.addWidget(self.le_addr4,5,1)
        self.grid_layout.addWidget(self.le_postcode,6,1)

        self.grid_layout.addWidget(self.lbl_mobile,0,2)
        self.grid_layout.addWidget(self.lbl_home,1,2)
        self.grid_layout.addWidget(self.lbl_email_addr,2,2)
        self.grid_layout.addWidget(self.lbl_permission_vet,3,2)
        self.grid_layout.addWidget(self.lbl_picture_usuage,4,2)
        self.grid_layout.addWidget(self.lbl_vet,5,2)
        self.grid_layout.addWidget(self.lbl_emergency,6,2)

        self.grid_layout.addWidget(self.le_mobile,0,3)
        self.grid_layout.addWidget(self.le_home,1,3)
        self.grid_layout.addWidget(self.le_email_addr,2,3)
        self.grid_layout.addWidget(self.permission_vet_combo,3,3)
        self.grid_layout.addWidget(self.picture_usuage_combo,4,3)
        self.grid_layout.addWidget(self.vet_combo,5,3)
        self.grid_layout.addWidget(self.emergency_combo,6,3)

        self.bottom_bar_layout = QHBoxLayout()
        self.bottom_bar_layout.addWidget(self.submit_button)
        self.bottom_bar_layout.addWidget(self.cancel_button)

        self.edit_customer_layout = QVBoxLayout()
        self.edit_customer_layout.addLayout(self.grid_layout)
        self.edit_customer_layout.addLayout(self.bottom_bar_layout)

        #connections
        self.cancel_button.clicked.connect(self.BackToParent)
        self.submit_button.clicked.connect(self.EditCustomer)
        self.emergency_combo.activated.connect(self.CheckAddNewEmergencyContact)
        self.vet_combo.activated.connect(self.CheckAddNewVet)

    def BackToParent(self):
        self.close()

    def PopulateWindow(self):
        sql = """SELECT * FROM {0} WHERE CustomerID={1}""".format(self.table_name, self.record_id)
        data = database.FetchOneResult(sql)

        #setting line edits
        self.le_first_name.setText(data[3])
        self.le_last_name.setText(data[4])
        self.le_addr1.setText(data[5])
        self.le_addr2.setText(data[6])
        self.le_addr3.setText(data[7])
        self.le_addr4.setText(data[8])
        self.le_postcode.setText(data[9])
        self.le_mobile.setText(data[10])
        self.le_home.setText(data[11])
        self.le_email_addr.setText(data[12])

        #setting combos
        if data[13] == 1:
            self.permission_vet_combo.setCurrentIndex(0)
        elif data[13] == 0:
            self.permission_vet_combo.setCurrentIndex(1)

        if data[14] == 1:
            self.picture_usuage_combo.setCurrentIndex(0)
        elif data[14] == 0:
            self.picture_usuage_combo.setCurrentIndex(1)

        #setting up foriegn key combos
        emergency_id = data[1]
        vet_id = data[2]

        sql = """SELECT EmFirstName, EmLastName FROM Emergency WHERE EmergencyID={0}""".format(emergency_id)
        data = database.FetchOneResult(sql)
        emergency_name = "{0} {1}".format(data[0], data[1])

        sql = """SELECT VetFirstName, VetLastName FROM Vet WHERE VetID={0}""".format(vet_id)
        data = database.FetchOneResult(sql)
        vet_name = "{0} {1}".format(data[0], data[1])

        index = self.emergency_combo.findText(emergency_name)
        if index >= 0:
            self.emergency_combo.setCurrentIndex(index)
        else:
            self.emergency_combo.setCurrentIndex(0)

        index = self.vet_combo.findText(vet_name)
        if index >= 0:
            self.vet_combo.setCurrentIndex(index)
        else:
            self.vet_combo.setCurrentIndex(0)

    def ValidateFields(self):
        messages = []
        #Regex validations
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

        #make sure foriegn keys are selected
        if str(self.emergency_combo.currentText()) == "Add New Emergency Contact":
            messages.append("No emergency contact was selected")

        if str(self.vet_combo.currentText()) == "Add New Vet":
            messages.append("No vet was selected")

        #make sure no fields are empty
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

    def EditCustomer(self):
        validation_messages = self.ValidateFields()
        if len(validation_messages) == 0: #if no validation errors
            are_you_sure = ConfirmationWindow(self, "Are you sure you wish to edit this record? This action cannot be undone.")
            are_you_sure.show()
            are_you_sure.raise_()
            self.decision = are_you_sure.exec_() #confirmation
            if self.decision == 1:
                emergency_name = str(self.emergency_combo.currentText())
                emergency_name_split = emergency_name.split()
                sql = """SELECT EmergencyID FROM Emergency WHERE EmFirstName="{0}" AND EmLastName="{1}" """.format(emergency_name_split[0], emergency_name_split[1])
                emergency_id = database.FetchAllResult(sql)
                emergency_id = int(emergency_id[0][0]) #get emergency contact id

                vet_name = str(self.vet_combo.currentText())
                vet_name_split = vet_name.split()
                sql = """SELECT VetID FROM Vet WHERE VetFirstName="{0}" AND VetLastName="{1}" """.format(vet_name_split[0], vet_name_split[1])
                vet_id = database.FetchAllResult(sql)
                vet_id = int(vet_id[0][0]) #get vet id

                #get bool values for permissions
                if self.permission_vet_combo.currentIndex() == 1:
                    permission_vet = 0
                elif self.permission_vet_combo.currentIndex() == 0:
                    permission_vet = 1

                if self.picture_usuage_combo.currentIndex() == 1:
                    picture_permission = 0
                elif self.picture_usuage_combo.currentIndex() == 0:
                    picture_permission = 1

                values = []
                values.append(emergency_id)
                values.append(vet_id)
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
                values.append(permission_vet)
                values.append(picture_permission)

                database.EditRecord(self.table_name, values, self.record_id)
                self.BackToParent()
        else:
            validation_dialog = ValidationDialog(self, validation_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_()

    def CheckAddNewEmergencyContact(self): #check if new emergency contact was selected from combo
        ComboAddNew.CheckAddNewEmergencyContact(self, self.emergency_combo.currentIndex())

    def CheckAddNewVet(self): #check if new vet was selected from combo
        ComboAddNew.CheckAddNewVet(self, selection_num = self.vet_combo.currentIndex())

    def PopulateVetCombo(self):
        PopulateXCombo.PopulateVetCombo(self)

    def PopulateEmergencyCombo(self):
        PopulateXCombo.PopulateEmergencyCombo(self)