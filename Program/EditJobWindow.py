#Thomas Thorpe
#Pet Service Edit Job Window

from PetServiceDatabase import *

import re
import ComboAddNew
import PopulateXCombo
from datetime import datetime
from PyQt4.QtGui import *
from ValidationChecking import *
from CreateCustomerForm import *
from CreatePetForm import *
from ValidationDialog import *
from AreYouSureWindow import *
from Notification import *

class EditJobWindow(QMainWindow):
    def __init__(self, came_from, record_id):
        super(QMainWindow,self).__init__(came_from)
        self.setWindowTitle("Edit Job Window")
        self.came_from = came_from #parent window
        self.table_name = "Jobs"
        self.joining_table_name = "PetsPerJob"
        self.record_id = record_id
        self.CreateEditJobWindow()
        self.PopulateWindow()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.edit_job_layout)
        self.setCentralWidget(self.central_widget)

    def CreateEditJobWindow(self):
        #Create Widgets
        #create labels
        self.lbl_start_date = QLabel("Start Date")
        self.lbl_end_date = QLabel("End Date")
        self.lbl_start_time1 = QLabel("Start Time 1")
        self.lbl_end_time1 = QLabel("End Time 1")
        self.lbl_start_time2 = QLabel("Start Time 2")
        self.lbl_end_time2 = QLabel("End Time 2")
        self.lbl_key = QLabel("Key Locations")
        self.lbl_quote = QLabel("Quote Sent")
        self.lbl_pet1 = QLabel("Pet 1")
        self.lbl_pet2 = QLabel("Pet 2")
        self.lbl_pet3 = QLabel("Pet 3")
        self.lbl_customer = QLabel("Customer")
        self.lbl_job_type = QLabel("Job Type")
        self.lbl_invoice = QLabel("Invoice Sent")
        self.lbl_payment = QLabel("Payment Recieved")
        self.lbl_job_complete = QLabel("Job Complete")

        #create line edits
        self.le_start_date = QLineEdit()
        self.le_end_date = QLineEdit()
        self.le_start_time1 = QLineEdit()
        self.le_end_time1 = QLineEdit()
        self.le_start_time2 = QLineEdit()
        self.le_end_time2 = QLineEdit()
        self.le_key = QLineEdit()
        self.le_key.setMaxLength(30)

        #create combo boxes
        self.select_job_combo = QComboBox(self)
        self.select_job_combo.addItem("Dog Walking - Single 1 Hour")
        self.select_job_combo.addItem("Dog Walking - Single Half Hour")
        self.select_job_combo.addItem("Dog Walking - 2 For 1 Hour")
        self.select_job_combo.addItem("Dog Walking - 2 For Half Hour")
        self.select_job_combo.addItem("Dog Walking - 3 For 1 Hour")
        self.select_job_combo.addItem("Dog Walking - 3 For Half Hour")
        self.select_job_combo.addItem("Animal Boarding - Dog")
        self.select_job_combo.addItem("Animal Boarding - Small Animal")
        self.select_job_combo.addItem("Animal Boarding - Birds")
        self.select_job_combo.addItem("Pet Sitting - Half Hour A Day")
        self.select_job_combo.addItem("Pet Sitting - Hour A Day")
        self.select_job_combo.addItem("Pet Sitting - Hour A Day (Two Half Hours)")
        self.select_job_combo.addItem("Pet Sitting - Hour And Half A Day")
        self.select_job_combo.addItem("Pet Sitting - Two Hours A Day") 

        self.quote_combo = QComboBox(self)
        self.quote_combo.addItem("Yes")
        self.quote_combo.addItem("No") 

        self.customer_combo = QComboBox(self)
        self.PopulateCustomerCombo()

        self.pet1_combo = QComboBox(self)
        self.pet2_combo = QComboBox(self)
        self.pet3_combo = QComboBox(self)
        self.PopulatePetCombos()

        self.invoice_combo = QComboBox(self)
        self.invoice_combo.addItem("Yes")
        self.invoice_combo.addItem("No")

        self.payment_combo = QComboBox(self)
        self.payment_combo.addItem("Yes")
        self.payment_combo.addItem("No")

        self.job_complete_combo = QComboBox(self)
        self.job_complete_combo.addItem("Yes")
        self.job_complete_combo.addItem("No")
        self.job_complete_combo.setEditable(False)

        self.submit_button = QPushButton("Submit Revisions")
        self.cancel_button = QPushButton("Cancel")
        self.check_avalibility_button = QPushButton("Check Availability")

        #Create Layout
        #create grid layout
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.lbl_start_date,0,0)
        self.grid_layout.addWidget(self.lbl_end_date,1,0)
        self.grid_layout.addWidget(self.lbl_start_time1,2,0)
        self.grid_layout.addWidget(self.lbl_end_time1,3,0)
        self.grid_layout.addWidget(self.lbl_start_time2,4,0)
        self.grid_layout.addWidget(self.lbl_end_time2,5,0)
        self.grid_layout.addWidget(self.lbl_key,6,0)
        self.grid_layout.addWidget(self.lbl_customer,7,0)

        self.grid_layout.addWidget(self.le_start_date,0,1)
        self.grid_layout.addWidget(self.le_end_date,1,1)
        self.grid_layout.addWidget(self.le_start_time1,2,1)
        self.grid_layout.addWidget(self.le_end_time1,3,1)
        self.grid_layout.addWidget(self.le_start_time2,4,1)
        self.grid_layout.addWidget(self.le_end_time2,5,1)
        self.grid_layout.addWidget(self.le_key,6,1)
        self.grid_layout.addWidget(self.customer_combo,7,1)
        
        self.grid_layout.addWidget(self.lbl_job_type,0,2)
        self.grid_layout.addWidget(self.lbl_quote,1,2)
        self.grid_layout.addWidget(self.lbl_invoice,2,2)
        self.grid_layout.addWidget(self.lbl_payment,3,2)
        self.grid_layout.addWidget(self.lbl_job_complete,4,2)
        self.grid_layout.addWidget(self.lbl_pet1,5,2)
        self.grid_layout.addWidget(self.lbl_pet2,6,2)
        self.grid_layout.addWidget(self.lbl_pet3,7,2)
        
        self.grid_layout.addWidget(self.select_job_combo,0,3)
        self.grid_layout.addWidget(self.quote_combo,1,3)
        self.grid_layout.addWidget(self.invoice_combo,2,3)
        self.grid_layout.addWidget(self.payment_combo,3,3)
        self.grid_layout.addWidget(self.job_complete_combo,4,3)
        self.grid_layout.addWidget(self.pet1_combo,5,3)
        self.grid_layout.addWidget(self.pet2_combo,6,3)
        self.grid_layout.addWidget(self.pet3_combo,7,3)

        #bottom two buttons
        self.bottom_bar_layout = QHBoxLayout()
        self.bottom_bar_layout.addWidget(self.submit_button)
        self.bottom_bar_layout.addWidget(self.cancel_button)

        #layout
        self.edit_job_layout = QVBoxLayout()
        self.edit_job_layout.addLayout(self.grid_layout)
        self.edit_job_layout.addLayout(self.bottom_bar_layout)
        self.edit_job_layout.addWidget(self.check_avalibility_button)

        #Connections
        self.cancel_button.clicked.connect(self.BackToParent)
        self.submit_button.clicked.connect(self.EditJob)
        self.customer_combo.activated.connect(self.CheckAddCustomer)
        self.pet1_combo.activated.connect(self.CheckAddPet1)
        self.pet2_combo.activated.connect(self.CheckAddPet2)
        self.pet3_combo.activated.connect(self.CheckAddPet3)
        self.check_avalibility_button.clicked.connect(self.CheckAvalibility)

    def BackToParent(self):
        self.close()
        self.came_from.show()
        self.came_from.DisplayAll()

    def PopulateWindow(self):
        sql = """SELECT {0}.JobID, {0}.CustomerID, {0}.StartDate, {0}.EndDate, {0}.HadASessionBefore, {0}.DateOfLastSession, {0}.JobType, {0}.StartTime1, {0}.EndTime1, {0}.StartTime2, {0}.EndTime2, {0}.KeyLocation, {0}.QuoteSent, {0}.InvoiceSent, {0}.PaymentReceived, {0}.JobComplete, {1}.PetID FROM {0}, {1} WHERE {1}.JobID={0}.JobID AND {0}.JobID="{2}" """.format(self.table_name,self.joining_table_name, self.record_id)
        data = database.FetchAllResult(sql)

        #setting line edits
        self.le_start_date.setText(data[0][2])
        self.le_end_date.setText(data[0][3])
        self.le_start_time1.setText(data[0][7])
        self.le_end_time1.setText(data[0][8])
        self.le_start_time2.setText(data[0][9])
        self.le_end_time2.setText(data[0][10])
        self.le_key.setText(data[0][11])

        #setting combos
        index = self.select_job_combo.findText(data[0][6])
        if index >= 0:
            self.select_job_combo.setCurrentIndex(index)

        if data[0][12] == 1:
            self.quote_combo.setCurrentIndex(0)
        elif data[0][12] == 0:
            self.quote_combo.setCurrentIndex(1)

        if data[0][13] == 1:
            self.invoice_combo.setCurrentIndex(0)
        elif data[0][13] == 0:
            self.invoice_combo.setCurrentIndex(1)

        if data[0][14] == 1:
            self.payment_combo.setCurrentIndex(0)
        elif data[0][14] == 0:
            self.payment_combo.setCurrentIndex(1)

        if data[0][15] == 1:
            self.job_complete_combo.setCurrentIndex(0)
        elif data[0][15] == 0:
            self.job_complete_combo.setCurrentIndex(1)

        #setting foriegn combos
        customer_id = data[0][1]
        sql = """SELECT FirstName, LastName FROM Customer WHERE CustomerID={0}""".format(customer_id)

        customer_data = database.FetchOneResult(sql)
        customer_name = "{0} {1}".format(customer_data[0], customer_data[1])

        index = self.customer_combo.findText(customer_name)
        if index >= 0:
            self.customer_combo.setCurrentIndex(index)
        else:
            self.customer_combo.setCurrentIndex(0)

        self.PopulatePetCombos() #populate pet combos with only pets belonging to owner
        pet_id = data[0][16]
        sql = """SELECT PetName FROM Pet WHERE PetID={0}""".format(pet_id)
        pet_data = database.FetchOneResult(sql)
        pet_name = pet_data[0]

        index = self.pet1_combo.findText(pet_name)
        if index >= 0:
            self.pet1_combo.setCurrentIndex(index)
        else:
            self.pet1_combo.setCurrentIndex(0)

        if len(data) >= 2: #if more than 1 pet
            pet_id = data[1][16]
            sql = """SELECT PetName FROM Pet WHERE PetID={0}""".format(pet_id)
            pet_data = database.FetchOneResult(sql)
            pet_name = pet_data[0]

            index = self.pet2_combo.findText(pet_name)
            if index >= 0:
                self.pet2_combo.setCurrentIndex(index)
            else:
                self.pet2_combo.setCurrentIndex(1)  
        else:
            self.pet2_combo.setCurrentIndex(1)

        if len(data) == 3: #if 3 pets
            pet_id = data[2][16]
            sql = """SELECT PetName FROM Pet WHERE PetID={0}""".format(pet_id)
            pet_data = database.FetchOneResult(sql)
            pet_name = pet_data[0]

            index = self.pet3_combo.findText(pet_name)
            if index >= 0:
                self.pet3_combo.setCurrentIndex(index)
            else:
                self.pet3_combo.setCurrentIndex(1)  
        else:
            self.pet3_combo.setCurrentIndex(1)              

    def CheckAvalibility(self):
        start_date = self.le_start_date.text()
        end_date = self.le_end_date.text()
        start_time_1 = self.le_start_time1.text()
        start_time_2 = self.le_start_time2.text()
        end_time_1 = self.le_end_time1.text()
        end_time_2 = self.le_end_time2.text()

        if start_date != "" and end_date != "" and start_time_1 != "" and start_time_2 != "" and end_time_1 != "" and end_time_2 != "":
            messages = []
            check_result = CheckTimeslots(start_time_1, end_time_1, start_time_2, end_time_2, self.select_job_combo.currentText())
            if check_result != -1:
                messages.append(check_result)

            check_result = CheckAvailability(start_date, end_date, start_time_1, end_time_1, True, self.record_id) 
            if check_result != -1:
                messages.append(check_result + " In StartTime1 + EndTime1")
            elif start_time_2 != "N/A" and end_time_2 != "N/A":
                check_result = CheckAvailability(start_date, end_date, start_time_2, end_time_2, True, self.record_id)
                if check_result != -1:
                    messages.append(check_result + " In StartTime2 + EndTime2")

            if len(messages) != 0:
                message = ""
                for each in messages:
                    message = message + each + ";"
            else:
                message = "No Issues with the current time slots"
        else:
            message = "Please fill in all times and dates"

        notification = Notification(self, message)
        notification.setModal(True)
        notification.show()
        notification.raise_()


    def ValidateFields(self):
        start_date = self.le_start_date.text()
        end_date = self.le_end_date.text()
        start_time_1 = self.le_start_time1.text()
        start_time_2 = self.le_start_time2.text()
        end_time_1 = self.le_end_time1.text()
        end_time_2 = self.le_end_time2.text()

        messages = []
        #regex validations
        check_results = CheckJobDatesTimes(start_date, end_date, start_time_1, start_time_2, end_time_1, end_time_2)

        if len(check_results) != 0:
            for each in check_results:
                messages.append(each) #add all messages collected for date and time checking
        elif start_date != "" and end_date != "" and start_time_1 != "" and start_time_2 != "" and end_time_1 != "" and end_time_2 != "":
            check_result = CheckAvailability(start_date, end_date, start_time_1, end_time_1, True, self.record_id)
            if check_result != -1:
                messages.append(check_result + " In StartTime1 + EndTime1")
            elif start_time_2 != "N/A" and end_time_2 != "N/A":
                check_result = CheckAvailability(start_date, end_date, start_time_2, end_time_2, True, self.record_id)
                if check_result != -1:
                    messages.append(check_result + " In StartTime2 + EndTime2")

            check_result = CheckTimeslots(start_time_1, end_time_1, start_time_2, end_time_2, self.select_job_combo.currentText())
            if check_result != -1:
                messages.append(check_result)

        #check foriegn keys are selected (or n/a for some pet combos)
        if str(self.customer_combo.currentText()) == "Add New Customer":
            messages.append("No customer was selected")

        if str(self.pet1_combo.currentText()) == "Add New Pet" or str(self.pet1_combo.currentText()) == "N/A":
            messages.append("You must have selected a pet in pet 1 drop-down")

        if str(self.pet2_combo.currentText()) == "Add New Pet":
            messages.append("Please select a pet or N/A in pet 2 drop-down")

        if str(self.pet3_combo.currentText()) == "Add New Pet":
            messages.append("Please select a pet or N/A in pet 3 drop-down")

        #check no same pet twice
        if str(self.pet1_combo.currentText()) == str(self.pet2_combo.currentText()) and str(self.pet1_combo.currentText()) != "N/A" and str(self.pet1_combo.currentText()) != "Add New Pet":
            messages.append("You cannot select the same pet twice")

        if str(self.pet1_combo.currentText()) == str(self.pet3_combo.currentText()) and str(self.pet1_combo.currentText()) != "N/A" and str(self.pet1_combo.currentText()) != "Add New Pet":
            messages.append("You cannot select the same pet twice") 

        if str(self.pet2_combo.currentText()) == str(self.pet3_combo.currentText()) and str(self.pet2_combo.currentText()) != "N/A" and str(self.pet2_combo.currentText()) != "Add New Pet":
            messages.append("You cannot select the same pet twice")

        #make sure no fields are blank (mostly done above)
        if self.le_key.text() == "":
            messages.append("No key details were entered")

        return messages

    def EditJob(self):
        validation_messages = self.ValidateFields()
        if len(validation_messages) == 0: #make sure no validatin errors
            are_you_sure = ConfirmationWindow(self, "Are you sure you wish to edit this record? This action cannot be undone.")
            are_you_sure.show()
            are_you_sure.raise_()
            self.decision = are_you_sure.exec_() #confirmation
            if self.decision == 1:
                #getting foriegn keys
                customer_name = str(self.customer_combo.currentText())
                customer_name_split = customer_name.split()
                sql = """SELECT CustomerID FROM Customer WHERE FirstName="{0}" AND LastName="{1}" """.format(customer_name_split[0],customer_name_split[1])
                customer_id = database.FetchAllResult(sql)
                customer_id = int(customer_id[0][0])

                #finding if had session before + date of it if exists
                sql = """SELECT StartDate FROM Jobs WHERE CustomerID ={0} """.format(customer_id)
                data = database.FetchAllResult(sql)
                if len(data) == 0:
                    had_session_before = 0
                    date_last_session = "N/A"
                elif len(data) != 0:
                    had_session_before = 1
                    sql = """SELECT StartDate FROM Jobs WHERE CustomerID={0} ORDER BY strftime(StartDate, "%d/%m/%Y") DESC""".format(customer_id)
                    data = database.FetchAllResult(sql)

                    list_of_dates = []
                    for each in data:
                        date_unformat = each[0]
                        day = int(date_unformat[0:2])
                        month = int(date_unformat[-7:-5])
                        year = int(date_unformat[-4:])
                        date = datetime(year,month,day)
                        list_of_dates.append(date)
                    date_last_session = max(list_of_dates).strftime("%d/%m/%Y")

                #getting job type
                job_name = self.select_job_combo.currentText()

                #getting bools values from drop downs
                if self.quote_combo.currentIndex() == 1:
                    quote_sent = 0
                else:
                    quote_sent = 1

                if self.invoice_combo.currentIndex() == 1:
                    invoice_sent = 0
                else:
                    invoice_sent = 1

                if self.payment_combo.currentIndex() == 1:
                    payment_received = 0
                else:
                    payment_received = 1

                if self.job_complete_combo.currentIndex() == 1:
                    job_complete = 0
                else:
                    job_complete = 1

                values = []
                values.append(customer_id)
                values.append(self.le_start_date.text())
                values.append(self.le_end_date.text())
                values.append(had_session_before)
                values.append(date_last_session)
                values.append(job_name)
                values.append(self.le_start_time1.text())
                values.append(self.le_end_time1.text())
                values.append(self.le_start_time2.text())
                values.append(self.le_end_time2.text())
                values.append(self.le_key.text())
                values.append(quote_sent)
                values.append(invoice_sent)
                values.append(payment_received)
                values.append(job_complete)

                database.EditRecord(self.table_name, values, self.record_id)

                #Dealing With PersPerJob Joining table
                database.DeleteJoiningTableRecord(self.record_id)

                if self.pet1_combo.currentIndex() != 0 and self.pet1_combo.currentIndex() != 1:
                    pet_name = str(self.pet1_combo.currentText())
                    sql = """SELECT PetID FROM Pet WHERE CustomerID={0} AND PetName="{1}" """.format(customer_id, pet_name)
                    pet_id = database.FetchOneResult(sql)
                    pet_id = pet_id[0]
                    database.AddJoiningTableRecord(self.record_id, pet_id)
                if self.pet2_combo.currentIndex() != 0 and self.pet2_combo.currentIndex() != 1:
                    pet_name = str(self.pet2_combo.currentText())
                    sql = """SELECT PetID FROM Pet WHERE CustomerID={0} AND PetName="{1}" """.format(customer_id, pet_name)
                    pet_id = database.FetchOneResult(sql)
                    pet_id = pet_id[0]
                    database.AddJoiningTableRecord(self.record_id, pet_id) 
                if self.pet3_combo.currentIndex() != 0 and self.pet3_combo.currentIndex() != 1:
                    pet_name = str(self.pet3_combo.currentText())
                    sql = """SELECT PetID FROM Pet WHERE CustomerID={0} AND PetName="{1}" """.format(customer_id, pet_name)
                    pet_id = database.FetchOneResult(sql)
                    pet_id = pet_id[0]
                    database.AddJoiningTableRecord(self.record_id, pet_id)
                self.BackToParent()
        else:
            validation_dialog = ValidationDialog(self, validation_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_() 

    def CheckAddPet1(self):
        combo_num = 1
        selection_num = self.pet1_combo.currentIndex()
        if selection_num == 0:
            self.AddNewPetCall(selection_num, combo_num)

    def CheckAddPet2(self):
        combo_num = 2
        selection_num = self.pet2_combo.currentIndex()
        if selection_num == 0:
            self.AddNewPetCall(selection_num, combo_num)

    def CheckAddPet3(self):
        combo_num = 3
        selection_num = self.pet3_combo.currentIndex()
        if selection_num == 0:
            self.AddNewPetCall(selection_num, combo_num)

    def AddNewPetCall(self, selection_num, combo_num): #popup pet creation if called from any pet combo
        ComboAddNew.AddNewPet(self, selection_num, combo_num)

    def CheckAddCustomer(self): #popup customer creation if selected from customer combo
        ComboAddNew.CheckAddNewCustomer(self, self.customer_combo.currentIndex())

    def PopulateCustomerCombo(self):
        PopulateXCombo.PopulateCustomerCombo(self)

    def PopulatePetCombos(self):
        customer_name = str(self.customer_combo.currentText())
        customer_name_split = customer_name.split()

        #clear anything in combos before populating as could be repopulating them as selecting different customer
        self.pet1_combo.clear()
        self.pet2_combo.clear()
        self.pet3_combo.clear()

        if len(customer_name_split) != 0  and len(customer_name_split) != 3:
            sql = """SELECT CustomerID FROM Customer WHERE FirstName="{0}" AND LastName="{1}" """.format(customer_name_split[0], customer_name_split[1])
            customer_id = database.FetchAllResult(sql)
            customer_id = int(customer_id[0][0])

            sql = """SELECT PetName FROM Pet WHERE CustomerID ="{0}" """.format(customer_id)
            data = database.FetchAllResult(sql)

            pet_list = ["Add New Pet", "N/A"]
            for count in range(len(data)):
                pet_list.append("{0}".format(data[count][0]))
            self.pet1_combo.addItems(pet_list)
            self.pet2_combo.addItems(pet_list)
            self.pet3_combo.addItems(pet_list)
        else:
            pet_list = ["Add New Pet", "N/A"]
            self.pet1_combo.addItems(pet_list)
            self.pet2_combo.addItems(pet_list)
            self.pet3_combo.addItems(pet_list)
