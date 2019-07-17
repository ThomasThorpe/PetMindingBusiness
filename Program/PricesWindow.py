#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Thomas Thorpe
#Pet Service Prices Window

from PetServiceDatabase import *
import GetSummaryInformation
import re
from ValidationDialog import *
from AreYouSureWindow import *
from datetime import datetime
from PyQt4.QtGui import *


class PricesWindow(QMainWindow):
    def __init__(self, came_from, record_id):
        super(QMainWindow,self).__init__(came_from)
        self.came_from = came_from #parent window
        self.table_name = "Prices"
        self.setWindowTitle("Prices Information")
        self.GetPrices()

        self.customer_details, self.summary_number, self.summary_word, self.start_date, self.end_date, self.total_cost = GetSummaryInformation.CreateSummary(record_id) #get info for summary

        self.CreatePricesWindow()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.prices_layout)
        self.setCentralWidget(self.central_widget)

    def CreatePricesWindow(self):
        #create widgets
        #dog walking widgets group
        self.dog_walking_box = QGroupBox("Dog Walking")
        self.lbl_single_half = QLabel("Single Half Hour")
        self.lbl_single_hour = QLabel("Single 1 Hour")
        self.lbl_3_hour = QLabel("Up To 3 For 1 Hour Per Dog")
        self.lbl_3_half = QLabel("Up To 3 For Half Hour Per Dog")
        self.le_single_half = QLineEdit()
        self.le_single_half.setText("£{0:.2f}".format(self.prices_information[1][0] / 100))
        self.le_single_hour = QLineEdit()
        self.le_single_hour.setText("£{0:.2f}".format(self.prices_information[0][0] / 100))
        self.le_3_half = QLineEdit()
        self.le_3_half.setText("£{0:.2f}".format(self.prices_information[3][0] / 200))
        self.le_3_hour = QLineEdit()
        self.le_3_hour.setText("£{0:.2f}".format(self.prices_information[2][0] / 200))
        self.dog_walking_layout = QGridLayout()
        self.dog_walking_layout.addWidget(self.lbl_single_half,0,0)
        self.dog_walking_layout.addWidget(self.lbl_single_hour,1,0)
        self.dog_walking_layout.addWidget(self.lbl_3_half,2,0)
        self.dog_walking_layout.addWidget(self.lbl_3_hour,3,0)
        self.dog_walking_layout.addWidget(self.le_single_half,0,1)
        self.dog_walking_layout.addWidget(self.le_single_hour,1,1)
        self.dog_walking_layout.addWidget(self.le_3_half,2,1,)
        self.dog_walking_layout.addWidget(self.le_3_hour,3,1)
        self.dog_walking_box.setLayout(self.dog_walking_layout)

        #animal boardig widgets group
        self.animal_boarding_box = QGroupBox("Animal Boarding")
        self.lbl_dog = QLabel("Dogs Per 24 Hours")
        self.lbl_small_animals = QLabel("Small Animals Per 24 Hours")
        self.lbl_birds = QLabel("Birds Per 24 Hours")
        self.le_dogs = QLineEdit()
        self.le_dogs.setText("£{0:.2f}".format(self.prices_information[6][0] / 100))
        self.le_small_animals = QLineEdit()
        self.le_small_animals.setText("£{0:.2f}".format(self.prices_information[7][0] / 100))
        self.le_birds = QLineEdit()
        self.le_birds.setText("£{0:.2f}".format(self.prices_information[8][0] / 100))
        self.animal_boarding_layout = QGridLayout()
        self.animal_boarding_layout.addWidget(self.lbl_dog,0,0)
        self.animal_boarding_layout.addWidget(self.lbl_small_animals,1,0)
        self.animal_boarding_layout.addWidget(self.lbl_birds,2,0)
        self.animal_boarding_layout.addWidget(self.le_dogs,0,1)
        self.animal_boarding_layout.addWidget(self.le_small_animals,1,1)
        self.animal_boarding_layout.addWidget(self.le_birds,2,1)
        self.animal_boarding_box.setLayout(self.animal_boarding_layout)

        #pet setting widgets group
        self.pet_sitting_box = QGroupBox("Pet Sitting")
        self.lbl_half = QLabel("Half Hour Visit")
        self.lbl_hour = QLabel("Hour Visit")
        self.le_half = QLineEdit()
        self.le_half.setText("£{0:.2f}".format(self.prices_information[9][0] / 100))
        self.le_hour = QLineEdit()
        self.le_hour.setText("£{0:.2f}".format(self.prices_information[10][0] / 100))
        self.pet_sitting_layout = QGridLayout()
        self.pet_sitting_layout.addWidget(self.lbl_half,0,0)
        self.pet_sitting_layout.addWidget(self.lbl_hour,1,0)
        self.pet_sitting_layout.addWidget(self.le_half,0,1)
        self.pet_sitting_layout.addWidget(self.le_hour,1,1)
        self.pet_sitting_box.setLayout(self.pet_sitting_layout)

        #left side layout of groups
        self.left_side = QVBoxLayout()
        self.left_side.addWidget(self.dog_walking_box)
        self.left_side.addWidget(self.animal_boarding_box)
        self.left_side.addWidget(self.pet_sitting_box)

        #set information and uneditable
        self.customer_box = QGroupBox("Customer Information")
        self.le_name = QLineEdit()
        self.le_name.setText("{0} {1}".format(self.customer_details[0], self.customer_details[1]))
        self.le_name.setEnabled(False)
        self.le_addr1 = QLineEdit()
        self.le_addr1.setText("{0}".format(self.customer_details[2]))
        self.le_addr1.setEnabled(False)
        self.le_addr2 = QLineEdit()
        self.le_addr2.setText("{0}".format(self.customer_details[3]))
        self.le_addr2.setEnabled(False)
        self.le_addr3 = QLineEdit()
        self.le_addr3.setText("{0}".format(self.customer_details[4]))
        self.le_addr3.setEnabled(False)
        self.le_addr4 = QLineEdit()
        self.le_addr4.setText("{0}".format(self.customer_details[5]))
        self.le_addr4.setEnabled(False)
        self.le_postcode = QLineEdit()
        self.le_postcode.setText("{0}".format(self.customer_details[6]))
        self.le_postcode.setEnabled(False)
        self.customer_layout = QVBoxLayout()
        self.customer_layout.addWidget(self.le_name)
        self.customer_layout.addWidget(self.le_addr1)
        self.customer_layout.addWidget(self.le_addr2)
        self.customer_layout.addWidget(self.le_addr3)
        self.customer_layout.addWidget(self.le_addr4)
        self.customer_layout.addWidget(self.le_postcode)
        self.customer_box.setLayout(self.customer_layout)

        self.summary_box = QGroupBox("Summary")
        self.le_summary_text = QTextEdit()
        self.le_summary_text.setMaximumHeight(60)
        self.le_summary_text.setText("{0} {1} from {2} to {3} has a total cost of £{4:.2f}".format(self.summary_number, self.summary_word, self.start_date, self.end_date, self.total_cost)) #make summary
        self.le_summary_text.setEnabled(False) #uneditable
        self.summary_layout = QVBoxLayout()
        self.summary_layout.addWidget(self.le_summary_text)
        self.summary_box.setLayout(self.summary_layout)

        #buttons
        self.submit_button = QPushButton("Submit Changes to Prices")
        self.back_button = QPushButton("Back")

        #create layout
        self.right_side = QVBoxLayout()
        self.right_side.addWidget(self.customer_box)
        self.right_side.addWidget(self.summary_box)
        self.right_side.addWidget(self.submit_button)
        self.right_side.addWidget(self.back_button)

        self.prices_layout = QHBoxLayout()
        self.prices_layout.addLayout(self.left_side)
        self.prices_layout.addLayout(self.right_side)

        #connections
        self.submit_button.clicked.connect(self.SubmitPrices)
        self.back_button.clicked.connect(self.BackToSearch)

    def GetPrices(self):
        sql = """SELECT Price FROM Prices"""
        self.prices_information = database.FetchAllResult(sql)

    def ValidateFields(self):
        messages = []

        allowed_chars = set("£1234567890.")

        #make sure only correct chars are used
        ##Acknowledgement: https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters - 2nd reply
        if set(self.le_single_half.text()) <= allowed_chars and set(self.le_single_hour.text()) <= allowed_chars and set(self.le_3_half.text()) <= allowed_chars and set(self.le_3_hour.text()) <= allowed_chars and set(self.le_dogs.text()) <= allowed_chars and set(self.le_small_animals.text()) <= allowed_chars and set(self.le_birds.text()) <= allowed_chars and set(self.le_half.text()) <= allowed_chars and set(self.le_hour.text()) <= allowed_chars:
            pass
        else:
            messages.append("Please make sure you only use correct \"£\", \".\" or numbers")

        #make sure there is something in the field before checking first char for £ sign
        if len(self.le_single_half.text()) != 0 and len(self.le_single_hour.text()) != 0 and len(self.le_3_half.text()) != 0 and len(self.le_3_hour.text()) != 0 and len(self.le_dogs.text()) != 0 and len(self.le_small_animals.text()) != 0 and len(self.le_birds.text()) != 0 and len(self.le_half.text()) != 0 and len(self.le_hour.text()) != 0:
            #make sure first char is "£" sign
            if self.le_single_half.text()[0] != "£" or self.le_single_hour.text()[0] != "£" or self.le_3_half.text()[0] != "£" or self.le_3_hour.text()[0] != "£" or self.le_dogs.text()[0] != "£" or self.le_small_animals.text()[0] != "£" or self.le_birds.text()[0] != "£" or self.le_half.text()[0] != "£" or self.le_hour.text()[0] != "£":
                messages.append("Please make sure you start with a pound sign for all entries")

            #make sure decimal is in correct spot
            if self.le_single_hour.text()[-3] != "." or self.le_single_hour.text()[-3] != "." or self.le_3_half.text()[-3] != "." or self.le_3_hour.text()[-3] != "." or self.le_dogs.text()[-3] != "." or self.le_small_animals.text()[-3] != "." or self.le_birds.text()[-3] != "." or self.le_half.text()[-3] != "." or self.le_hour.text()[-3] != ".":
                messages.append("Please make sure you use a decimal place in the correct spot")
        else:
            messages.append("Please don't leave any fields blank")

        return messages

    def SubmitPrices(self):
        validate_messages = self.ValidateFields()
        if len(validate_messages) == 0:
            are_you_sure = ConfirmationWindow(self, "Are you sure you wish you change your prices?")
            are_you_sure.show()
            are_you_sure.raise_()
            self.decision = are_you_sure.exec_() #confirmation
            if self.decision == 1: #get prices in pennies
                #strips out all chars but numbers then converts to integer
                record1 = int(re.sub("[£.]", "", self.le_single_hour.text()))
                record2 = int(re.sub("[£.]", "", self.le_single_half.text()))
                record3 = int(re.sub("[£.]", "", self.le_3_hour.text())) * 2
                record4 = int(re.sub("[£.]", "", self.le_3_half.text())) * 2
                record5 = int(re.sub("[£.]", "", self.le_3_hour.text())) * 3
                record6 = int(re.sub("[£.]", "", self.le_3_half.text())) * 3
                record7 = int(re.sub("[£.]", "", self.le_dogs.text()))
                record8 = int(re.sub("[£.]", "", self.le_small_animals.text()))
                record9 = int(re.sub("[£.]", "", self.le_birds.text()))
                record10 = int(re.sub("[£.]", "", self.le_half.text()))
                record11 = int(re.sub("[£.]", "", self.le_hour.text()))
                record12 = int(re.sub("[£.]", "", self.le_half.text())) * 2
                record13 = int(re.sub("[£.]", "", self.le_half.text())) + int(re.sub("[£.]", "", self.le_hour.text()))
                record14 = int(re.sub("[£.]", "", self.le_hour.text())) * 2

                prices = [["Dog Walking - Single 1 Hour", record1], ["Dog Walking - Single Half Hour", record2], ["Dog Walking - 2 For 1 Hour", record3], ["Dog Walking - 2 For Half Hour", record4], ["Dog Walking - 3 For 1 Hour", record5], ["Dog Walking - 3 For Half Hour", record6], ["Animal Boarding - Dog", record7], ["Animal Boarding - Small Animal", record8], ["Animal Boarding - Birds", record9], ["Pet Sitting - Half Hour A Day", record10], ["Pet Sitting - Hour A Day", record11], ["Pet Sitting - Hour A Day (Two Half Hours)", record12], ["Pet Sitting - Hour And Half A Day", record13], ["Pet Sitting - Two Hours A Day", record14]]

                for count in range(1, 15): #update all records in prices table
                    database.EditRecord(self.table_name, prices[count-1], count)
                self.BackToSearch()
        else: #shows validation errors if needed
            validation_dialog = ValidationDialog(self, validate_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_()

    def BackToSearch(self):
        self.close()
        self.came_from.show()
