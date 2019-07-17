#Thomas Thorpe
#Pet Service System Display Job Details

from PetServiceDatabase import *

from DisplayCustomerDetails import *
from DisplayPetDetails import *
from PyQt4.QtGui import *

class DisplayJobDetails(QDialog):#window to display record, used mainly when double clicking id in table views
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Job Details")
        self.table_name = "Jobs"
        self.joining_table_name = "PetsPerJob"
        self.record_id = record_id
        self.GetJobInformation()
        self.CreateDisplayJobWindow()
        self.setLayout(self.display_job_layout)
        self.exec_()

    def CreateDisplayJobWindow(self):
        #Create Widgets
        #labels
        self.lbl_job_type = QLabel("Job Type")
        self.lbl_start_date = QLabel("Start Date")
        self.lbl_end_date = QLabel("End Date")
        self.lbl_start_time1 = QLabel("Start Time 1")
        self.lbl_end_time1 = QLabel("End Time 1")
        self.lbl_start_time2 = QLabel("Start Time 2")
        self.lbl_end_time2 = QLabel("End Time 2")
        self.lbl_key = QLabel("Key Locations")
        self.lbl_customer = QLabel("Customer - ID")
        self.lbl_pet1 = QLabel("Pet 1 - ID")
        self.lbl_pet2 = QLabel("Pet 2 - ID")
        self.lbl_pet3 = QLabel("Pet 3 - ID")
        self.lbl_quote = QLabel("Quote Sent")
        self.lbl_invoice = QLabel("Invoice Sent")
        self.lbl_payment = QLabel("Payment Recieved")
        self.lbl_job_complete = QLabel("Job Complete")

        #line edits (setting values and uneditable)
        self.le_job_type = QLineEdit()
        self.le_job_type.setEnabled(False)
        self.le_job_type.setText(self.data[0][6])
        self.le_start_date = QLineEdit()
        self.le_start_date.setEnabled(False)
        self.le_start_date.setText(self.data[0][2])
        self.le_end_date = QLineEdit()
        self.le_end_date.setEnabled(False)
        self.le_end_date.setText(self.data[0][3])
        self.le_start_time1 = QLineEdit()
        self.le_start_time1.setEnabled(False)
        self.le_start_time1.setText(self.data[0][7])
        self.le_end_time1 = QLineEdit()
        self.le_end_time1.setEnabled(False)
        self.le_end_time1.setText(self.data[0][8])
        self.le_start_time2 = QLineEdit()
        self.le_start_time2.setEnabled(False)
        self.le_start_time2.setText(self.data[0][9])
        self.le_end_time2 = QLineEdit()
        self.le_end_time2.setEnabled(False)
        self.le_end_time2.setText(self.data[0][10])
        self.le_key = QLineEdit()
        self.le_key.setEnabled(False)
        self.le_key.setText(self.data[0][11])
        self.le_customer = QLineEdit()
        self.le_customer.setEnabled(False)
        self.le_customer.setText(str(self.data[0][1]))
        self.le_pet1 = QLineEdit()
        self.le_pet1.setEnabled(False)
        self.le_pet1.setText(str(self.data[0][16]))
        self.le_pet2 = QLineEdit()
        self.le_pet2.setEnabled(False)
        self.le_pet3 = QLineEdit()
        self.le_pet3.setEnabled(False)
        self.le_quote = QLineEdit()
        self.le_quote.setEnabled(False)
        #setting bool values
        if self.data[0][12] == 0:
            self.le_quote.setText("No")
        elif self.data[0][12] == 1:
            self.le_quote.setText("Yes")
        self.le_invoice = QLineEdit()
        self.le_invoice.setEnabled(False)
        if self.data[0][13] == 0:
            self.le_invoice.setText("No")
        elif self.data[0][1] == 1:
            self.le_invoice.setText("Yes")
        self.le_payment = QLineEdit()
        self.le_payment.setEnabled(False)
        if self.data[0][14] == 0:
            self.le_payment.setText("No")
        elif self.data[0][14] == 1:
            self.le_payment.setText("Yes")
        self.le_job_complete = QLineEdit()
        self.le_job_complete.setEnabled(False)
        if self.data[0][15] == 0:
            self.le_job_complete.setText("No")
        elif self.data[0][15] == 1:
            self.le_job_complete.setText("Yes")

        #check if more than 1 pet
        if len(self.data) == 3:
            self.le_pet2.setText(str(self.data[1][16]))
            self.le_pet3.setText(str(self.data[2][16]))
        elif len(self.data) == 2:
            self.le_pet2.setText(str(self.data[1][16]))
            self.le_pet3.setText("N/A")
        else:
            self.le_pet2.setText("N/A")
            self.le_pet3.setText("N/A")

        #buttons
        self.customer_button = QPushButton("Check Customer Details")
        self.pet1_button = QPushButton("Check Pet 1 Details")
        if self.le_pet2.text() != "N/A": #create more check buttons if there is more than 1 pet
            self.pet2_button = QPushButton("Check Pet 2 Details")
        if self.le_pet3.text() != "N/A":
            self.pet3_button = QPushButton("Check Pet 3 Details")

        #create layout
        self.display_job_layout = QGridLayout()

        self.display_job_layout.addWidget(self.lbl_job_type,0,0)
        self.display_job_layout.addWidget(self.lbl_start_date,1,0)
        self.display_job_layout.addWidget(self.lbl_end_date,2,0)
        self.display_job_layout.addWidget(self.lbl_start_time1,3,0)
        self.display_job_layout.addWidget(self.lbl_end_time1,4,0)
        self.display_job_layout.addWidget(self.lbl_start_time2,5,0)
        self.display_job_layout.addWidget(self.lbl_end_time2,6,0)
        self.display_job_layout.addWidget(self.lbl_key,7,0)

        self.display_job_layout.addWidget(self.le_job_type,0,1)
        self.display_job_layout.addWidget(self.le_start_date,1,1)
        self.display_job_layout.addWidget(self.le_end_date,2,1)
        self.display_job_layout.addWidget(self.le_start_time1,3,1)
        self.display_job_layout.addWidget(self.le_end_time1,4,1)
        self.display_job_layout.addWidget(self.le_start_time2,5,1)
        self.display_job_layout.addWidget(self.le_end_time2,6,1)
        self.display_job_layout.addWidget(self.le_key,7,1)

        self.display_job_layout.addWidget(self.lbl_customer,0,2)
        self.display_job_layout.addWidget(self.lbl_pet1,1,2)
        self.display_job_layout.addWidget(self.lbl_pet2,2,2)
        self.display_job_layout.addWidget(self.lbl_pet3,3,2)
        self.display_job_layout.addWidget(self.lbl_quote,4,2)
        self.display_job_layout.addWidget(self.lbl_invoice,5,2)
        self.display_job_layout.addWidget(self.lbl_payment,6,2)
        self.display_job_layout.addWidget(self.lbl_job_complete,7,2)

        self.display_job_layout.addWidget(self.le_customer,0,3)
        self.display_job_layout.addWidget(self.le_pet1,1,3)
        self.display_job_layout.addWidget(self.le_pet2,2,3)
        self.display_job_layout.addWidget(self.le_pet3,3,3)
        self.display_job_layout.addWidget(self.le_quote,4,3)
        self.display_job_layout.addWidget(self.le_invoice,5,3)
        self.display_job_layout.addWidget(self.le_payment,6,3)
        self.display_job_layout.addWidget(self.le_job_complete,7,3)

        self.display_job_layout.addWidget(self.customer_button,8,0)
        self.display_job_layout.addWidget(self.pet1_button,8,1)
        if self.le_pet2.text() != "N/A": #add extra buttons to layout if needed
            self.display_job_layout.addWidget(self.pet2_button,8,2)
            self.pet2_button.clicked.connect(self.CheckPet2Details)
        if self.le_pet3.text() != "N/A":
            self.display_job_layout.addWidget(self.pet3_button,8,3)
            self.pet3_button.clicked.connect(self.CheckPet3Details)

        #connections
        self.customer_button.clicked.connect(self.CheckCustomerDetails)
        self.pet1_button.clicked.connect(self.CheckPet1Details)

    def CheckCustomerDetails(self):
        display_customer_details = DisplayCustomerDetails(self, int(self.le_customer.text()))
        display_customer_details.show()
        display_customer_details.raise_()

    def CheckPet1Details(self):
        pet_id = int(self.le_pet1.text())
        self.CheckPetDetails(pet_id)

    def CheckPet2Details(self):
        pet_id = int(self.le_pet2.text())
        self.CheckPetDetails(pet_id)

    def CheckPet3Details(self):
        pet_id = int(self.le_pet3.text())
        self.CheckPetDetails(pet_id)

    def CheckPetDetails(self, pet_id):
        display_pet_details = DisplayPetDetails(self, pet_id)
        display_pet_details.show()
        display_pet_details.raise_()

    def GetJobInformation(self):
        sql = """SELECT {0}.JobID, {0}.CustomerID, {0}.StartDate, {0}.EndDate, {0}.HadASessionBefore, {0}.DateOfLastSession, {0}.JobType, {0}.StartTime1, {0}.EndTime1, {0}.StartTime2, {0}.EndTime2, {0}.KeyLocation, {0}.QuoteSent, {0}.InvoiceSent, {0}.PaymentReceived, {0}.JobComplete, {1}.PetID FROM {0}, {1} WHERE {1}.JobID = {0}.JobID AND {0}.JobID="{2}" """.format(self.table_name, self.joining_table_name, self.record_id)
        self.data = database.FetchAllResult(sql)
