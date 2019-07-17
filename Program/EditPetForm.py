#Thomas Thorpe
#Pet Service Edit Pet Details Form

from PetServiceDatabase import *

import re
import ComboAddNew
import PopulateXCombo
from datetime import datetime
from PyQt4.QtGui import *
from ValidationChecking import *
from ValidationDialog import *
from AreYouSureWindow import *
from CreateCustomerForm import *

class EditPetForm(QDialog):
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Edit Pet Details Form")
        self.table_name = "Pet"
        self.record_id = record_id
        self.CreateEditPetWindow()
        self.PopulateWindow()
        self.setLayout(self.edit_pet_details_layout)
        self.exec_()

    def CreateEditPetWindow(self):
        #create widgets
        #label
        self.lbl_name = QLabel("Name")
        self.lbl_species = QLabel("Species")
        self.lbl_breed = QLabel("Breed")
        self.lbl_colours = QLabel("Colours")
        self.lbl_dob = QLabel("Date of Birth")
        self.lbl_food_name = QLabel("Food Name")
        self.lbl_food_frequency = QLabel("Food Frequency")
        self.lbl_lead = QLabel("On Lead?")
        self.lbl_spayed = QLabel("Spayed?")
        self.lbl_behaviour = QLabel("Behaviour")
        self.lbl_commands = QLabel("Commands")
        self.lbl_food_location = QLabel("Food Location")
        self.lbl_owner = QLabel("Owner")
        self.lbl_cleaning = QLabel("Cleaning Requirements")
        self.lbl_night = QLabel("Night Requirements")
        self.lbl_other = QLabel("Other Information")

        #line edit
        self.le_name = QLineEdit()
        self.le_name.setMaxLength(20)
        self.le_species = QLineEdit()
        self.le_species.setMaxLength(30)
        self.le_breed = QLineEdit()
        self.le_breed.setMaxLength(20)
        self.le_colours = QLineEdit()
        self.le_colours.setMaxLength(30)
        self.le_dob = QLineEdit()
        self.le_food_name = QLineEdit()
        self.le_food_name.setMaxLength(20)
        self.le_food_frequency = QLineEdit()
        self.le_food_frequency.setMaxLength(30)

        #combos
        self.lead_combo = QComboBox(self)
        self.lead_combo.addItem("Yes")
        self.lead_combo.addItem("No")

        self.spayed_combo = QComboBox(self)
        self.spayed_combo.addItem("Yes")
        self.spayed_combo.addItem("No")

        self.customer_combo = QComboBox(self)
        self.PopulateCustomerCombo()

        #text edits
        self.tx_behaviour = QTextEdit(self)
        self.tx_behaviour.setMaximumHeight(60)
        self.tx_commands = QTextEdit(self)
        self.tx_commands.setMaximumHeight(60)
        self.tx_food_location = QTextEdit(self)
        self.tx_food_location.setMaximumHeight(60)
        self.tx_cleaning = QTextEdit(self)
        self.tx_cleaning.setMaximumHeight(60)
        self.tx_night = QTextEdit(self)
        self.tx_night.setMaximumHeight(60)
        self.tx_other = QTextEdit(self)
        self.tx_other.setMaximumHeight(60)

        #buttons
        self.submit_button = QPushButton("Sumbit Revisions")
        self.submit_button.setDefault(True)
        self.cancel_button = QPushButton("Cancel")

        #crete layout
        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.lbl_name)
        self.vbox1.addWidget(self.lbl_species)
        self.vbox1.addWidget(self.lbl_breed)
        self.vbox1.addWidget(self.lbl_colours)
        self.vbox1.addWidget(self.lbl_dob)
        self.vbox1.addWidget(self.lbl_food_name)
        self.vbox1.addWidget(self.lbl_food_frequency)
        self.vbox1.addWidget(self.lbl_lead)
        self.vbox1.addWidget(self.lbl_spayed)

        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.le_name)
        self.vbox2.addWidget(self.le_species)
        self.vbox2.addWidget(self.le_breed)
        self.vbox2.addWidget(self.le_colours)
        self.vbox2.addWidget(self.le_dob)
        self.vbox2.addWidget(self.le_food_name)
        self.vbox2.addWidget(self.le_food_frequency)
        self.vbox2.addWidget(self.lead_combo)
        self.vbox2.addWidget(self.spayed_combo)

        self.gridbox3 = QGridLayout()
        self.gridbox3.addWidget(self.lbl_behaviour,0,0)
        self.gridbox3.addWidget(self.lbl_commands,1,0)
        self.gridbox3.addWidget(self.lbl_food_location,2,0)
        self.gridbox3.addWidget(self.lbl_owner,3,0)
        self.gridbox3.addWidget(self.tx_behaviour,0,1)
        self.gridbox3.addWidget(self.tx_commands,1,1)
        self.gridbox3.addWidget(self.tx_food_location,2,1)
        self.gridbox3.addWidget(self.customer_combo,3,1)

        self.gridbox4 = QGridLayout()
        self.gridbox4.addWidget(self.lbl_cleaning,0,0)
        self.gridbox4.addWidget(self.lbl_night,1,0)
        self.gridbox4.addWidget(self.lbl_other,2,0)
        self.gridbox4.addWidget(self.submit_button,3,0)
        self.gridbox4.addWidget(self.tx_cleaning,0,1)
        self.gridbox4.addWidget(self.tx_night,1,1)
        self.gridbox4.addWidget(self.tx_other,2,1)
        self.gridbox4.addWidget(self.cancel_button,3,1)

        self.edit_pet_details_layout = QHBoxLayout()
        self.edit_pet_details_layout.addLayout(self.vbox1)
        self.edit_pet_details_layout.addLayout(self.vbox2)
        self.edit_pet_details_layout.addLayout(self.gridbox3)
        self.edit_pet_details_layout.addLayout(self.gridbox4)

        #connections
        self.cancel_button.clicked.connect(self.BackToParent)
        self.submit_button.clicked.connect(self.EditPet)
        self.customer_combo.activated.connect(self.CheckAddNewCustomer)

    def PopulateWindow(self):
        sql = """SELECT * FROM {0} WHERE PetID={1}""".format(self.table_name, self.record_id)
        data = database.FetchOneResult(sql)

        #setting line edits
        self.le_name.setText(data[2])
        self.le_species.setText(data[3])
        self.le_breed.setText(data[4])
        self.le_colours.setText(data[5])
        self.le_dob.setText(data[6])
        self.le_food_name.setText(data[10])
        self.le_food_frequency.setText(data[12])

        #setting text edits
        self.tx_behaviour.insertPlainText(data[8])
        self.tx_commands.insertPlainText(data[9])
        self.tx_food_location.insertPlainText(data[11])
        self.tx_night.insertPlainText(data[13])
        self.tx_cleaning.insertPlainText(data[14])
        self.tx_other.insertPlainText(data[15])

        #setting up combos
        if data[7] == 1:
            self.spayed_combo.setCurrentIndex(0)
        elif data[7] == 0:
            self.spayed_combo.setCurrentIndex(1)

        if data[16] == 1:
            self.lead_combo.setCurrentIndex(0)
        elif data[16] == 0:
            self.lead_combo.setCurrentIndex(1)

        #setting up foriegn key combos
        customer_id = data[1]
        sql = """SELECT FirstName, LastName FROM Customer WHERE CustomerID={0}""".format(customer_id)
        data = database.FetchOneResult(sql)
        customer_name = "{0} {1}".format(data[0], data[1])

        index = self.customer_combo.findText(customer_name)
        if index >= 0:
            self.customer_combo.setCurrentIndex(index)
        else:
            self.customer_combo.setCurrentIndex(0)

    def ValidateFields(self):
        date = self.le_dob.text()
        messages = []
        check_results = CheckPetDob(date)
        if check_results != "-1":
            messages.append(check_results)

        #make sure an owner is selected (foriegn key exists check)
        if str(self.customer_combo.currentText()) == "Add New Customer":
            messages.append("No owner was selected")

        #make sure no fields are left blank
        if self.le_name.text() == "":
            messages.append("No name was entered")

        if self.le_species.text() == "":
            messages.append("No species was entered")

        if self.le_breed.text() == "":
            messages.append("No breed was entered")

        if self.le_colours.text() == "":
            messages.append("No colours were entered")

        if self.le_food_name.text() == "":
            messages.append("No food name was entered")

        if self.le_food_frequency.text() == "":
            messages.append("No food Frequency was entered")

        if self.tx_behaviour.toPlainText() == "":
            messages.append("The behaviour field was left blank")

        if self.tx_commands.toPlainText() == "":
            messages.append("The commands field was left blank")

        if self.tx_food_location.toPlainText() == "":
            messages.append("The food location field was left blank")

        if self.tx_cleaning.toPlainText() == "":
            messages.append("No cleaning details were entered")

        if self.tx_night.toPlainText() == "":
            messages.append("No night details were entered")

        return messages

    def EditPet(self):
        validation_messages = self.ValidateFields()
        if len(validation_messages) == 0: #if no validation errors
            are_you_sure = ConfirmationWindow(self, "Are you sure you wish to edit this record? This action cannot be undone.")
            are_you_sure.show()
            are_you_sure.raise_()
            self.decision = are_you_sure.exec_() #confirmation
            if self.decision == 1:
                customer_name = str(self.customer_combo.currentText())
                customer_name_split = customer_name.split()
                sql = """SELECT CustomerID FROM Customer WHERE FirstName="{0}" AND LastName="{1}" """.format(customer_name_split[0], customer_name_split[1])
                customer_id = database.FetchAllResult(sql)
                customer_id = int(customer_id[0][0])

                #get bool values
                if self.spayed_combo.currentIndex() == 1:
                    spayed = 0
                elif self.spayed_combo.currentIndex() == 0:
                    spayed = 1

                if self.lead_combo.currentIndex() == 1:
                    on_lead = 0
                elif self.lead_combo.currentIndex() == 0:
                    on_lead = 1

                values = []
                values.append(customer_id)
                values.append(self.le_name.text())
                values.append(self.le_species.text())
                values.append(self.le_breed.text())
                values.append(self.le_colours.text())
                values.append(self.le_dob.text())
                values.append(spayed)
                values.append(self.tx_behaviour.toPlainText())
                values.append(self.tx_commands.toPlainText())
                values.append(self.le_food_name.text())
                values.append(self.tx_food_location.toPlainText())
                values.append(self.le_food_frequency.text())
                values.append(self.tx_night.toPlainText())
                values.append(self.tx_cleaning.toPlainText())
                values.append(self.tx_other.toPlainText())
                values.append(on_lead)

                database.EditRecord(self.table_name, values, self.record_id)
                self.BackToParent()
        else:
            validation_dialog = ValidationDialog(self, validation_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_()

    def BackToParent(self):
        self.close()

    def CheckAddNewCustomer(self): #opens customer creation if selected in dropdown
        ComboAddNew.CheckAddNewOwner(self, self.customer_combo.currentIndex())

    def PopulateCustomerCombo(self):
        PopulateXCombo.PopulateCustomerCombo(self)
