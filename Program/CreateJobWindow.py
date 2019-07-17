#Thomas Thorpe
#Pet Service Create Job Window

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
from Notification import *

class CreateJobWindow(QMainWindow):
    def __init__(self, came_from, job_num, job_name):
        super(QMainWindow,self).__init__(came_from)
        self.setWindowTitle("Create Job Window")
        self.job_num = job_num        #passed from select job window before
        self.job_name = job_name      #passed from select job window before
        self.CreateNewJobWindow()
        self.came_from = came_from #parent
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.create_job_layout)
        self.setCentralWidget(self.central_widget)

    def CreateNewJobWindow(self):
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

        #create line edits
        self.le_start_date = QLineEdit()
        self.le_start_date.setPlaceholderText("DD/MM/YYYY")
        self.le_end_date = QLineEdit()
        self.le_end_date.setPlaceholderText("DD/MM/YYYY")
        self.le_start_time1 = QLineEdit()
        self.le_start_time1.setPlaceholderText("00:00")
        self.le_end_time1 = QLineEdit()
        self.le_end_time1.setPlaceholderText("23:59")

        self.le_start_time2 = QLineEdit()
        if self.job_num == 11 or self.job_num == 13: #checking if there is two sessiosn to decide defualt value
            self.le_start_time2.setPlaceholderText("00:00")
        else:
            self.le_start_time2.setText("N/A")

        self.le_end_time2 = QLineEdit()
        if self.job_num == 11 or self.job_num == 13: #checking if there is two sessiosn to decide defualt value
            self.le_end_time2.setPlaceholderText("23:59")
        else:
            self.le_end_time2.setText("N/A")

        self.le_key = QLineEdit()
        self.le_key.setMaxLength(30)

        #create combo boxes
        self.quote_combo = QComboBox(self)
        self.quote_combo.addItem("Yes")
        self.quote_combo.addItem("No")
        self.quote_combo.setCurrentIndex(1) #sets default to No

        self.customer_combo = QComboBox(self)
        self.PopulateCustomerCombo()

        self.pet1_combo = QComboBox(self)
        self.pet2_combo = QComboBox(self)
        self.pet3_combo = QComboBox(self)
        self.PopulatePetCombos()

        #buttons
        self.add_button = QPushButton("Submit New Job Details")
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

        self.grid_layout.addWidget(self.le_start_date,0,1)
        self.grid_layout.addWidget(self.le_end_date,1,1)
        self.grid_layout.addWidget(self.le_start_time1,2,1)
        self.grid_layout.addWidget(self.le_end_time1,3,1)
        self.grid_layout.addWidget(self.le_start_time2,4,1)
        self.grid_layout.addWidget(self.le_end_time2,5,1)

        self.grid_layout.addWidget(self.lbl_key,0,2)
        self.grid_layout.addWidget(self.lbl_quote,1,2)
        self.grid_layout.addWidget(self.lbl_customer,2,2)
        self.grid_layout.addWidget(self.lbl_pet1,3,2)
        self.grid_layout.addWidget(self.lbl_pet2,4,2)
        self.grid_layout.addWidget(self.lbl_pet3,5,2)

        self.grid_layout.addWidget(self.le_key,0,3)
        self.grid_layout.addWidget(self.quote_combo,1,3)
        self.grid_layout.addWidget(self.customer_combo,2,3)
        self.grid_layout.addWidget(self.pet1_combo,3,3)
        self.grid_layout.addWidget(self.pet2_combo,4,3)
        self.grid_layout.addWidget(self.pet3_combo,5,3)

        #bottom two buttons
        self.bottom_bar_layout = QHBoxLayout()
        self.bottom_bar_layout.addWidget(self.add_button)
        self.bottom_bar_layout.addWidget(self.cancel_button)

        #layout
        self.create_job_layout = QVBoxLayout()
        self.create_job_layout.addLayout(self.grid_layout)
        self.create_job_layout.addLayout(self.bottom_bar_layout)
        self.create_job_layout.addWidget(self.check_avalibility_button)

        #Connections
        self.cancel_button.clicked.connect(self.BackToJobs)
        self.add_button.clicked.connect(self.AddJob)
        self.customer_combo.activated.connect(self.CheckAddCustomer)
        self.pet1_combo.activated.connect(self.CheckAddPet1)
        self.pet2_combo.activated.connect(self.CheckAddPet2)
        self.pet3_combo.activated.connect(self.CheckAddPet3)
        self.check_avalibility_button.clicked.connect(self.CheckAvalibility)

    def CheckAddPet1(self):
        combo_num = 1
        selection_num = self.pet1_combo.currentIndex()
        if selection_num == 0: #make sure add new was picked
            self.AddNewPetCall(selection_num, combo_num)

    def CheckAddPet2(self):
        combo_num = 2
        selection_num = self.pet2_combo.currentIndex()
        if selection_num == 0: #make sure add new was picked
            self.AddNewPetCall(selection_num, combo_num)

    def CheckAddPet3(self):
        combo_num = 3
        selection_num = self.pet3_combo.currentIndex()
        if selection_num == 0: #make sure add new was picked
            self.AddNewPetCall(selection_num, combo_num)

    def AddNewPetCall(self, selection_num, combo_num): #add new pet window if called from any combo
        ComboAddNew.AddNewPet(self, selection_num, combo_num)

    def CheckAddCustomer(self): #check if new customer selected from dropdown
        ComboAddNew.CheckAddNewCustomer(self, self.customer_combo.currentIndex())

    def BackToJobs(self): #goes back to window needed once closed
        self.close()
        self.came_from.BackToJobs()

    def CheckAvalibility(self):
        start_date = self.le_start_date.text()
        end_date = self.le_end_date.text()
        start_time_1 = self.le_start_time1.text()
        start_time_2 = self.le_start_time2.text()
        end_time_1 = self.le_end_time1.text()
        end_time_2 = self.le_end_time2.text()

        if start_date != "" and end_date != "" and start_time_1 != "" and start_time_2 != "" and end_time_1 != "" and end_time_2 != "":
            messages = []
            check_result = CheckTimeslots(start_time_1, end_time_1, start_time_2, end_time_2, self.job_name)
            if check_result != -1:
                messages.append(check_result)

            check_result = CheckAvailability(start_date, end_date, start_time_1, end_time_1, False,0) 
            if check_result != -1:
                messages.append(check_result + " In StartTime1 + EndTime1")
            elif start_time_2 != "N/A" and end_time_2 != "N/A":
                check_result = CheckAvailability(start_date, end_date, start_time_2, end_time_2, False,0)
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
            check_result = CheckAvailability(start_date, end_date, start_time_1, end_time_1, False,0)
            if check_result != -1:
                messages.append(check_result + " In StartTime1 + EndTime1")
            elif start_time_2 != "N/A" and end_time_2 != "N/A":
                check_result = CheckAvailability(start_date, end_date, start_time_2, end_time_2, False,0)
                if check_result != -1:
                    messages.append(check_result + " In StartTime2 + EndTime2")

            check_result = CheckTimeslots(start_time_1, end_time_1, start_time_2, end_time_2, self.job_name)
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

    def AddJob(self):
        validation_messages = self.ValidateFields()
        if len(validation_messages) == 0:
            #getting foriegn key IDs
            customer_name = str(self.customer_combo.currentText())
            customer_name_split = customer_name.split()
            sql = """SELECT CustomerID FROM Customer WHERE FirstName="{0}" AND LastName="{1}" """.format(customer_name_split[0],customer_name_split[1])
            customer_id = database.FetchAllResult(sql)
            customer_id = int(customer_id[0][0]) #get foriegn key id of customer

            #finding if had session before + date of it if exists
            sql = """SELECT StartDate FROM Jobs WHERE CustomerID ={0} """.format(customer_id)
            data = database.FetchAllResult(sql)
            if len(data) == 0:
                had_session_before = 0
                date_last_session = "N/A" #if no session before
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
                    date = datetime(year,month,day) #convert to datetime object
                    list_of_dates.append(date)
                date_last_session = max(list_of_dates).strftime("%d/%m/%Y") #gets last session

            #setting some default bools when creating job
            invoice_sent = 0
            payment_received = 0
            job_complete = 0

            #get bool values from drop-downs
            if self.quote_combo.currentIndex() == 1:
                quote_sent = 0
            else:
                quote_sent = 1

            #list of values to insert
            values = []
            values.append(customer_id)
            values.append(self.le_start_date.text())
            values.append(self.le_end_date.text())
            values.append(had_session_before)
            values.append(date_last_session)
            values.append(self.job_name)
            values.append(self.le_start_time1.text())
            values.append(self.le_end_time1.text())
            values.append(self.le_start_time2.text())
            values.append(self.le_end_time2.text())
            values.append(self.le_key.text())
            values.append(quote_sent)
            values.append(invoice_sent)
            values.append(payment_received)
            values.append(job_complete)

            database.AddRecord("Jobs", values)

            #Add To PetsPerJob joining table
            sql = """SELECT JobID FROM Jobs WHERE CustomerID={0} AND StartDate="{1}" AND EndDate="{2}" AND JobType="{3}" AND StartTime1="{4}" """.format(customer_id, values[1], values[2], self.job_name, values[6])
            job_id = database.FetchOneResult(sql)
            job_id = int(job_id[0]) #get job id

            if self.pet1_combo.currentIndex() != 0 and self.pet1_combo.currentIndex() != 1:
                pet_name = str(self.pet1_combo.currentText())
                sql = """SELECT PetID FROM Pet WHERE CustomerID={0} AND PetName="{1}" """.format(customer_id, pet_name)
                pet_id = database.FetchOneResult(sql)
                pet_id = pet_id[0]
                database.AddJoiningTableRecord(job_id, pet_id)
            if self.pet2_combo.currentIndex() != 0 and self.pet2_combo.currentIndex() != 1:
                pet_name = str(self.pet2_combo.currentText())
                sql = """SELECT PetID FROM Pet WHERE CustomerID={0} AND PetName="{1}" """.format(customer_id, pet_name)
                pet_id = database.FetchOneResult(sql)
                pet_id = pet_id[0]
                database.AddJoiningTableRecord(job_id, pet_id) 
            if self.pet3_combo.currentIndex() != 0 and self.pet3_combo.currentIndex() != 1:
                pet_name = str(self.pet3_combo.currentText())
                sql = """SELECT PetID FROM Pet WHERE CustomerID={0} AND PetName="{1}" """.format(customer_id, pet_name)
                pet_id = database.FetchOneResult(sql)
                pet_id = pet_id[0]
                database.AddJoiningTableRecord(job_id, pet_id)
            self.BackToJobs()
        else:
            validation_dialog = ValidationDialog(self, validation_messages)
            validation_dialog.setModal(True)
            validation_dialog.show()
            validation_dialog.raise_()

    def PopulateCustomerCombo(self):
        PopulateXCombo.PopulateCustomerCombo(self)

    def PopulatePetCombos(self):
        customer_name = str(self.customer_combo.currentText())
        customer_name_split = customer_name.split()

        if len(customer_name_split) != 0  and len(customer_name_split) != 3:
            sql = """SELECT CustomerID FROM Customer WHERE FirstName="{0}" AND LastName="{1}" """.format(customer_name_split[0], customer_name_split[1])
            customer_id = database.FetchAllResult(sql)
            customer_id = int(customer_id[0][0])

            sql = """SELECT PetName FROM Pet WHERE CustomerID ="{0}" """.format(customer_id)
            data = database.FetchAllResult(sql)

            pet_list = ["Add New Pet", "N/A"]
            if len(data) != 0:
                for count in range(len(data)):
                    pet_list.append("{0}".format(data[count][0]))
                self.pet1_combo.setCurrentIndex(2)
                if self.job_num == 2 or self.job_num == 3: #setting default values according to job
                    self.pet2_combo.setCurrentIndex(2)
                    self.pet3_combo.setCurrentIndex(1)
                elif self.job_num == 4 or self.job_num == 5: #settin default values according to job
                    self.pet2_combo.setCurrentIndex(2)
                    self.pet3_combo.setCurrentIndex(2)
            self.pet1_combo.addItems(pet_list)
            self.pet2_combo.addItems(pet_list)
            self.pet3_combo.addItems(pet_list)
            self.pet1_combo.setCurrentIndex(0)
            self.pet2_combo.setCurrentIndex(0)
            self.pet3_combo.setCurrentIndex(0)
        else:
            pet_list = ["Add New Pet", "N/A"]
            self.pet1_combo.addItems(pet_list)
            self.pet2_combo.addItems(pet_list)
            self.pet3_combo.addItems(pet_list)
            self.pet1_combo.setCurrentIndex(1)
            self.pet2_combo.setCurrentIndex(1)
            self.pet3_combo.setCurrentIndex(1)

