#Thomas Thorpe
#Pet Service Creat Pet Window

from PetServiceDatabase import *

import re
import ComboAddNew
import PopulateXCombo
from datetime import datetime
from PyQt4.QtGui import *
from ValidationChecking import *
from ValidationDialog import *
from CreateCustomerForm import *

class CreatePetWindow(QDialog):
    def __init__(self, came_from):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Create Pet Form")
        self.CreateNewPetWindow()
        self.setLayout(self.create_pet_layout)
        self.exec_()

    def CreateNewPetWindow(self):
        #create widgets
        #labels
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

        #line edits
        self.le_name = QLineEdit()
        self.le_name.setMaxLength(20)
        self.le_species = QLineEdit()
        self.le_species.setMaxLength(30)
        self.le_breed = QLineEdit()
        self.le_breed.setMaxLength(20)
        self.le_colours = QLineEdit()
        self.le_colours.setMaxLength(30)
        self.le_dob = QLineEdit()
        self.le_dob.setPlaceholderText("DD/MM/YYYY")
        self.le_food_name = QLineEdit()
        self.le_food_name.setMaxLength(20)
        self.le_food_frequency = QLineEdit()
        self.le_food_frequency.setMaxLength(30)

        #bool combos
        self.lead_combo = QComboBox(self)
        self.lead_combo.addItem("Yes")
        self.lead_combo.addItem("No")
        self.lead_combo.setCurrentIndex(1)

        self.spayed_combo = QComboBox(self)
        self.spayed_combo.addItem("Yes")
        self.spayed_combo.addItem("No")
        self.spayed_combo.setCurrentIndex(1)

        #foriegn key combo
        self.customer_combo = QComboBox(self)
        self.PopulateCustomerCombo()

        #text edits (bigger line edits basically)
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
        self.submit_button = QPushButton("Sumbit New Pet Details")
        self.submit_button.setDefault(True)
        self.cancel_button = QPushButton("Cancel")

        #create layout
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

        self.create_pet_layout = QHBoxLayout()
        self.create_pet_layout.addLayout(self.vbox1)
        self.create_pet_layout.addLayout(self.vbox2)
        self.create_pet_layout.addLayout(self.gridbox3)
        self.create_pet_layout.addLayout(self.gridbox4)

        #connections
        self.cancel_button.clicked.connect(self.BackToParent)
        self.submit_button.clicked.connect(self.AddNewPet)
        self.customer_combo.activated.connect(self.CheckAddNewCustomer)

    def BackToParent(self):
        self.close()

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

    def AddNewPet(self):
        validation_messages = self.ValidateFields()
        if len(validation_messages) == 0:
            #get forigen key IDs
            customer_name = str(self.customer_combo.currentText())
            customer_name_split = customer_name.split()
            sql = """SELECT CustomerID FROM Customer WHERE FirstName="{0}" AND LastName="{1}" """.format(customer_name_split[0], customer_name_split[1])
            customer_id = database.FetchAllResult(sql)
            customer_id = int(customer_id[0][0]) #get foriegn key id of customer

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

            database.AddRecord("Pet", values)
            self.BackToParent()
        else:
            validation_dialog = ValidationDialog(self, validation_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_()

    def CheckAddNewCustomer(self):
        ComboAddNew.CheckAddNewOwner(self, self.customer_combo.currentIndex())

    def PopulateCustomerCombo(self):
        PopulateXCombo.PopulateCustomerCombo(self)
