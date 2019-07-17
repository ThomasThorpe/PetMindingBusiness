#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Thomas Thorpe
#Pet Service Search Jobs Window

from PyQt4.QtGui import *
import os
import shutil #used for moving quotes/invoices to their respective folder
import GetSummaryInformation #used when creating quotes/invoices
from datetime import datetime
from PricesWindow import *
from Notification import *
from AreYouSureWindow import *
from EditJobWindow import *
from DisplayPetDetails import *
from DisplayCustomerDetails import *
from DisplayJobDetails import *
from DeleteRecordSearchWindows import *
from JobsForToday import *

class SearchJobsWindow(QMainWindow):
    def __init__(self, came_from, display_current):
        super(QMainWindow,self).__init__(came_from)
        self.table_name = "Jobs"
        self.joining_table_name = "PetsPerJob"
        self.setWindowTitle("Search Job Details")
        self.came_from = came_from #parent window
        self.CreateSearchWindow() #creates the window

        if display_current == 0: #checks if diaplaying all or outstanding to start with
            self.CurrentJobs()
        else:
            self.DisplayAll()

        self.current_record_id = -1 #rogue value to show no record selected
        self.resize(925,200) #size
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.search_jobs_layout)
        self.setCentralWidget(self.central_widget)

    def CreateSearchWindow(self):
        #create widgets
        self.lbl_search = QLabel("Search By:")
        ##combo box for searching created and populated
        self.attribute_combo = QComboBox(self)
        self.PopulateAttributeCombo()
        #line edits and buttons created
        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText("Enter Search Here")
        self.search_button = QPushButton("Search")
        self.show_all_button = QPushButton("Show All")
        self.current_jobs_button = QPushButton("Show Outstanding Jobs")
        self.outstanding_jobs_button = QPushButton("Show Jobs For Today")
        self.table_viewer = QTableView()
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        self.back_button = QPushButton("Back")
        self.quote_button = QPushButton("Create Quote")
        self.invoice_button = QPushButton("Create Invoice")
        self.prices_button = QPushButton("Prices Information")

        #create layout
        self.search_jobs_layout = QVBoxLayout()
        self.top_third = QHBoxLayout()
        self.bottom_third = QHBoxLayout()

        #top layer of widgets
        self.top_third.addWidget(self.lbl_search)
        self.top_third.addWidget(self.attribute_combo)
        self.top_third.addWidget(self.le_search)
        self.top_third.addWidget(self.search_button)
        self.top_third.addWidget(self.show_all_button)
        self.top_third.addWidget(self.current_jobs_button)
        self.top_third.addWidget(self.outstanding_jobs_button)

        #bottom layer of widgets
        self.bottom_third.addWidget(self.edit_button)
        self.bottom_third.addWidget(self.delete_button)
        self.bottom_third.addWidget(self.quote_button)
        self.bottom_third.addWidget(self.invoice_button)
        self.bottom_third.addWidget(self.prices_button)
        self.bottom_third.addWidget(self.back_button)

        self.search_jobs_layout.addLayout(self.top_third)
        self.search_jobs_layout.addWidget(self.table_viewer) #this widget is whole middle layer
        self.search_jobs_layout.addLayout(self.bottom_third)

        #connections
        self.back_button.clicked.connect(self.BackToJobs)
        self.search_button.clicked.connect(self.GetSearchInformation)
        self.show_all_button.clicked.connect(self.DisplayAll)
        self.current_jobs_button.clicked.connect(self.CurrentJobs)
        self.outstanding_jobs_button.clicked.connect(self.TodayJobs)
        self.edit_button.clicked.connect(self.EditRecord) #will pass selected ID or similar
        self.delete_button.clicked.connect(self.DeleteRecord) #will pass selected ID or similar
        self.quote_button.clicked.connect(self.CreateQuote)
        self.invoice_button.clicked.connect(self.CreateInvoice)
        self.prices_button.clicked.connect(self.OpenPricesWindow)
        self.table_viewer.clicked.connect(self.CellWasClicked)
        self.table_viewer.doubleClicked.connect(self.CellWasDoubleClicked)

    def CellWasClicked(self, index): #gets record id(first column data) from selected row
        y = index.row()
        self.current_record_id = self.table_viewer.model().index(y, 0).data()

    def CellWasDoubleClicked(self, index):
        y = index.row()
        x = index.column()
        if x == 0: #checks if job id was double clicked
            job_id = self.table_viewer.model().index(y,x).data()
            display_job = DisplayJobDetails(self, job_id)
        elif x == 1: #checks if customer id was double clicked
            customer_id = self.table_viewer.model().index(y, x).data()
            display_customer = DisplayCustomerDetails(self, customer_id)
        elif x == 2 or x == 3 or x == 4: #checks if pet id was double clicked
            pet_id = self.table_viewer.model().index(y, x).data()
            if pet_id != "N/A": #make sure it was an ID and not a filler "N/A"
                display_pet = DisplayPetDetails(self, pet_id)

    def PopulateTableView(self, raw_data):
        sql = "PRAGMA table_info({0})".format(self.table_name)
        meta_data_full = database.FetchAllResult(sql) #meta_data of table, including attribute names
        meta_data = []
        for count in range(len(meta_data_full)): #get column headers
            meta_data.append(meta_data_full[count][1])

        meta_data.insert(2, "Pet 1") #insert extra headers for joining table data
        meta_data.insert(3, "Pet 2")
        meta_data.insert(4, "Pet 3")

        real_data = []
        count = 0
        while count < len(raw_data): #creating lists formatted with N/A when only 1/2 pets ect
            temp_record = list(raw_data[count])
            temp_record.insert(2, temp_record.pop())

            try:
                if raw_data[count][0] == raw_data[count + 1][0]:
                    temp_record.insert(3, raw_data[count + 1][0])

                    try:
                        if raw_data[count][0] == raw_data[count + 2][0]:
                            temp_record.insert(4, raw_data[count + 2][0])
                            count = count + 3
                        else:
                            temp_record.insert(4, "N/A")
                            count = count + 2
                    except IndexError:
                        temp_record.insert(4, "N/A")
                        count = len(raw_data)                       
                else:
                    temp_record.insert(3, "N/A")
                    temp_record.insert(4, "N/A")
                    count = count + 1
            except IndexError:
                temp_record.insert(3, "N/A")
                temp_record.insert(4, "N/A")
                count = len(raw_data)
            real_data.append(temp_record)

        for each in real_data: #changing bool values to "yes" or "no"
            if each[7] == 1:
                each[7] = "Yes"
            elif each[7] == 0:
                each[7] = "No"

            if each[15] == 1:
                each[15] = "Yes"
            elif each[15] == 0:
                each[15] = "No"

            if each[16] == 1:
                each[16] = "Yes"
            elif each[16] == 0:
                each[16] = "No"

            if each[17] == 1:
                each[17] = "Yes"
            elif each[17] == 0:
                each[17] = "No"

            if each[18] == 1:
                each[18] = "Yes"
            elif each[18] == 0:
                each[18] = "No"

        #populate table with formatted data model
        self.model = QStandardItemModel()
        if len(raw_data) == 0:
            self.model.setItem(0,0,QStandardItem("There Are No Records To Display"))
            self.model.setHorizontalHeaderItem(0,QStandardItem("N/A"))
        else:
            for row in range(len(real_data)):
                for column in range(len(real_data[0])):
                    item = QStandardItem("{0}".format(real_data[row][column]))
                    self.model.setItem(row, column, item)
                    header = QStandardItem(meta_data[column])
                    self.model.setHorizontalHeaderItem(column, header)
        self.table_viewer.verticalHeader().hide()
        self.table_viewer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_viewer.setModel(self.model)

    def CreateQuote(self):
        if not(os.path.isdir(os.getcwd() + "\Quotes")):
            os.makedirs(os.getcwd() + "\Quotes") #create backup folder if not exists

        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            today = datetime.today()
            today = str(today.strftime("%d/%m/%Y")) #get date

            customer_details, summary_number, summary_word, start_date, end_date, total_cost = GetSummaryInformation.CreateSummary(self.current_record_id)

            summary = "{0} {1} from {2} to {3} has a total cost of £{4:.2f}".format(summary_number, summary_word, start_date, end_date, total_cost) #create summary

            sql = """SELECT JobType FROM "Jobs" WHERE JobID={0}""".format(self.current_record_id)
            job_type = database.FetchOneResult(sql) #get job type
            job_type = job_type[0]

            sql = """SELECT Price FROM "Prices" WHERE JobName ="{0}" """.format(job_type)

            price = database.FetchOneResult(sql)
            price = price[0] #get price
            price = price / 100 #convert to pounds.pennies

            file_name = "QuoteJobID" + str(self.current_record_id) + ".txt"

            with open(file_name, mode = "w", encoding = "utf-8") as my_file:
                my_file.write("Dodpets \n21 Fallow Drive, Eaton Socon, St. Neots \n01480 395910 \ndodpets@gmail.com \nwww.dodpets.co.uk\n\n") #write banner
                my_file.write("Price List & Quote For Services \t Date: {0}\n\n".format(today)) #write date
                my_file.write("- Pricing - \n\t {0} \t £{1:.2f}\n\n".format(job_type, price)) #write job tpye and price for one
                my_file.write("- Quote For Services - \n Customer: \n\t") #header
                my_file.write("{0} {1} \n\t".format(customer_details[0], customer_details[1])) #print customer name
                my_file.write("{0} \n\t{1} \n\t{2} \n\t{3} \n\t{4}\n\n".format(customer_details[2],customer_details[3],customer_details[4],customer_details[5],customer_details[6])) #write customer address details
                my_file.write("Summary:\n\t") #header
                my_file.write("{0}\n\n".format(summary)) #write summary
                my_file.write("Breakdown:\n\t") #header
                my_file.write("{0} x {1} \t £{2:.2f}\n\t".format(summary_number, job_type, total_cost)) #breakdown
                my_file.write("Total Cost: {0:.2f}\n\n".format(total_cost)) #total cost
                my_file.write("Thank You\n\nCheques payable to \"Dodpets\"\n\nBank Transfer Directions-\nBarclays Bank St Neots\nAc Name: Dodpets\nAc No: 23145336\nSort Code: 20-74-81") #payment details
                my_file.close()

                try:
                    shutil.move(file_name, os.getcwd() + "\Quotes") #move to folder
                except Exception: #if exists overwrite
                    shutil.move(file_name, os.path.join(os.getcwd() + "\Quotes", file_name))

            notification = Notification(self, "Quote Created In Quotes Folder")
            notification.show()
            notification.raise_()

        else: #noify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()

    def CreateInvoice(self):
        if not(os.path.isdir(os.getcwd() + "\Invoices")):
            os.makedirs(os.getcwd() + "\Invoices") #create backup folder if not exists

        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            today = datetime.today()
            today = str(today.strftime("%d/%m/%Y")) #get date

            customer_details, summary_number, summary_word, start_date, end_date, total_cost = GetSummaryInformation.CreateSummary(self.current_record_id)

            summary = ("{0} {1} from {2} to {3} has a total cost of £{4:.2f}".format(summary_number, summary_word, start_date, end_date, total_cost)) #create summary

            sql = """SELECT JobType FROM "Jobs" WHERE JobID={0}""".format(self.current_record_id)
            job_type = database.FetchOneResult(sql) #get job type
            job_type = job_type[0]

            sql = """SELECT Price FROM "Prices" WHERE JobName ="{0}" """.format(job_type)

            price = database.FetchOneResult(sql)
            price = price[0] #get price
            price = price / 100 #convert to pound.pennies

            file_name = "InvoiceJobID" + str(self.current_record_id) + ".txt"

            with open(file_name, mode = "w", encoding = "utf-8") as my_file:
                my_file.write("Dodpets \n21 Fallow Drive, Eaton Socon, St. Neots \n01480 395910 \ndodpets@gmail.com \nwww.dodpets.co.uk\n\n") #write banner
                my_file.write("Invoice For Services \t Date: {0}\n\n".format(today)) #write date
                my_file.write("- Pricing - \n\t {0} \t £{1:.2f}\n\n".format(job_type, price)) #write job tpye and price for one
                my_file.write("- Services Provided - \n Customer: \n\t") #header
                my_file.write("{0} {1} \n\t".format(customer_details[0], customer_details[1])) #print customer name
                my_file.write("{0} \n\t{1} \n\t{2} \n\t{3} \n\t{4}\n\n".format(customer_details[2],customer_details[3],customer_details[4],customer_details[5],customer_details[6])) #write customer address details
                my_file.write("Summary:\n\t") #header
                my_file.write("{0}\n\n".format(summary)) #write summary
                my_file.write("Breakdown:\n\t") #header
                my_file.write("{0} x {1} \t £{2:.2f}\n\t".format(summary_number, job_type, total_cost)) #breakdown
                my_file.write("Total Cost: {0:.2f}\n\n".format(total_cost)) #total cost
                my_file.write("Thank You\n\nCheques payable to \"Dodpets\"\n\nBank Transfer Directions-\nBarclays Bank St Neots\nAc Name: Dodpets\nAc No: 23145336\nSort Code: 20-74-81") #payment details
                my_file.close()

                try:
                    shutil.move(file_name, os.getcwd() + "\Invoices") #move to folder
                except Exception: #if exists overwrite
                    shutil.move(file_name, os.path.join(os.getcwd() + "\Invoices", file_name))

            notification = Notification(self, "Invoice Created In Invoices Folder")
            notification.show()
            notification.raise_()

        else: #noify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()

    def DeleteRecord(self):
        DeleteRecord(self, self.current_record_id, self.table_name)

    def EditRecord(self):
        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            self.hide()
            new_edit_job_window = EditJobWindow(self, self.current_record_id)
            new_edit_job_window.show()
            new_edit_job_window.raise_()
        else: #noify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()

    def OpenPricesWindow(self):
        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            prices_window = PricesWindow(self, self.current_record_id)
            prices_window.show()
            prices_window.raise_()
            self.hide()
        else: #noify if no record for example data selected
            notification = Notification(self, "Please select a record for example data")
            notification.show()
            notification.raise_()

    def TodayJobs(self): #filters jobs to go to for today
        sql = """SELECT {0}.JobID, {0}.CustomerID, {0}.StartDate, {0}.EndDate, {0}.HadASessionBefore, {0}.DateOfLastSession, {0}.JobType, {0}.StartTime1, {0}.EndTime1, {0}.StartTime2, {0}.EndTime2, {0}.KeyLocation, {0}.QuoteSent, {0}.InvoiceSent, {0}.PaymentReceived, {0}.JobComplete, {1}.PetID FROM {0}, {1} WHERE {1}.JobID = {0}.JobID AND JobComplete = 0""".format(self.table_name, self.joining_table_name)
        unfiltered_data = database.FetchAllResult(sql)
        GetJobsForToday(self, unfiltered_data)

    def DisplayAll(self):
        sql = """SELECT {0}.JobID, {0}.CustomerID, {0}.StartDate, {0}.EndDate, {0}.HadASessionBefore, {0}.DateOfLastSession, {0}.JobType, {0}.StartTime1, {0}.EndTime1, {0}.StartTime2, {0}.EndTime2, {0}.KeyLocation, {0}.QuoteSent, {0}.InvoiceSent, {0}.PaymentReceived, {0}.JobComplete, {1}.PetID FROM {0}, {1} WHERE {1}.JobID = {0}.JobID""".format(self.table_name, self.joining_table_name)
        data = database.FetchAllResult(sql)

        self.PopulateTableView(data)

    def CurrentJobs(self): #call search function with required parameters
        self.attribute_selected = "JobComplete"
        self.search_text = 0
        self.SearchTable(self.attribute_selected, self.search_text)

    def GetSearchInformation(self): #gets search info then pass to search function
        self.attribute_selected = str(self.attribute_combo.currentText())
        self.search_text = self.le_search.text()
        self.SearchTable(self.attribute_selected, self.search_text)

    def SearchTable(self, attribute, search_text):
        if attribute == "HadASessionBefore" or attribute == "QuoteSent" or attribute == "InvoiceSent" or attribute =="PaymentReceived" or attribute =="JobComplete":
            if search_text == "Yes" or search_text == "yes": #change search to bool value if needed
                search_text = 1
            elif search_text == "No" or search_text == "no":
                search_text = 0

        if attribute != "PetID": #special search for pets as uses joining table
            sql = """SELECT {0}.JobID, {0}.CustomerID, {0}.StartDate, {0}.EndDate, {0}.HadASessionBefore, {0}.DateOfLastSession, {0}.JobType, {0}.StartTime1, {0}.EndTime1, {0}.StartTime2, {0}.EndTime2, {0}.KeyLocation, {0}.QuoteSent, {0}.InvoiceSent, {0}.PaymentReceived, {0}.JobComplete, {1}.PetID FROM {0}, {1} WHERE {1}.JobID={0}.JobID AND {0}.{2}="{3}" """.format(self.table_name, self.joining_table_name, attribute, search_text)
            data = database.FetchAllResult(sql)
        else: #normal search
            sql = """SELECT {0}.JobID, {0}.CustomerID, {0}.StartDate, {0}.EndDate, {0}.HadASessionBefore, {0}.DateOfLastSession, {0}.JobType, {0}.StartTime1, {0}.EndTime1, {0}.StartTime2, {0}.EndTime2, {0}.KeyLocation, {0}.QuoteSent, {0}.InvoiceSent, {0}.PaymentReceived, {0}.JobComplete, {1}.PetID FROM {0}, {1} WHERE {1}.JobID={0}.JobID AND {1}.{2}="{3}" """.format(self.table_name, self.joining_table_name, attribute, search_text)
            data = database.FetchAllResult(sql)            

        self.PopulateTableView(data)

    def BackToJobs(self):
        self.close()
        self.came_from.show()

    def PopulateAttributeCombo(self): #get headers that can be searched
        sql = "PRAGMA table_info({0})".format(self.table_name)
        data = database.FetchAllResult(sql)

        attribute_list = []
        for count in range(len(data)):
            attribute_list.append("{0}".format(data[count][1]))

        attribute_list.insert(2, "PetID")
        self.attribute_combo.addItems(attribute_list)
