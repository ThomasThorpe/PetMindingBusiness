#Thomas Thorpe
#Pet Service System Outstanding Jobs

from PetServiceDatabase import *

from PyQt4.QtGui import *
from DisplayCustomerDetails import *
from DisplayJobDetails import *
from JobsForToday import *
from datetime import datetime

class OutstandingJobs(QDialog):
    def __init__(self, came_from):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Outstanding Jobs")
        self.came_from = came_from
        self.CreateOustandingJobsWindow()
        self.GetOutstandingJobsData()
        self.setFixedSize(925, 200) #set window size to be wide enough for all attributes by default
        self.setLayout(self.outstanding_jobs_layout)
        self.exec_()

    def CreateOustandingJobsWindow(self):
        #create widgets
        self.table_viewer = QTableView()
        self.ok_button = QPushButton("Okay")

        #create layout
        self.outstanding_jobs_layout = QVBoxLayout()
        self.outstanding_jobs_layout.addWidget(self.table_viewer)
        self.outstanding_jobs_layout.addWidget(self.ok_button)

        #connections
        self.ok_button.clicked.connect(self.CloseWindow)
        self.table_viewer.doubleClicked.connect(self.CellWasDoubleClicked)

    def PopulateTableView(self, data):
        meta_data = ["JobID", "CustomerID", "Start Date", "End Date", "Start Time 1", "End Time 1", "Start Time 2", "End Time 2", "Key Location"] #attributes needed to display for quick reminder only

        self.model = QStandardItemModel()
        if len(data) == 0: #if no data
            self.model.setItem(0,0,QStandardItem("There are no jobs for today"))
            self.model.setHorizontalHeaderItem(0,QStandardItem("N/A"))
        else: #loop through data to add correctly
            for row in range(len(data)):
                for column in range(len(data[0])):
                    item = QStandardItem("{0}".format(data[row][column]))
                    self.model.setItem(row, column, item)
                    header = QStandardItem(meta_data[column])
                    self.model.setHorizontalHeaderItem(column, header)
        self.table_viewer.verticalHeader().hide()
        self.table_viewer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_viewer.setModel(self.model)

    def CellWasDoubleClicked(self, index):
        y = index.row()
        x = index.column()
        if x == 0: #check if job id double clicked
            job_id = self.table_viewer.model().index(y,x).data()
            display_job = DisplayJobDetails(self, job_id)
        elif x == 1: #check if customer id double clicked
            customer_id = self.table_viewer.model().index(y, x).data()
            display_customer = DisplayCustomerDetails(self, customer_id)

    def GetOutstandingJobsData(self): #Collects data that wants to be displayed and filters to any jobs to go o today
        sql = """SELECT JobID, CustomerID, StartDate, EndDate, StartTime1, EndTime1, StartTime2, EndTime2, KeyLocation FROM Jobs WHERE JobComplete = 0"""
        unfiltered_data = database.FetchAllResult(sql)
        GetJobsForToday(self, unfiltered_data)

    def CloseWindow(self):
        self.close()
        self.came_from.show()
