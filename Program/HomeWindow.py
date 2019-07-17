#Thomas Thorpe
#Pet Service System Main Program

import sys

from PetServiceDatabase import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from OutstandingJobs import *
from JobsWindow import *
from CustomerDetailsWindow import *
from DatabaseWindow import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setWindowTitle("Home Window")
        self.setWindowIcon(QIcon("Logo.png")) #company logo
        self.CreateHomeWindow()
        self.OutstandJobsPopup() #popup jobs for today for reminder when opened
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.home_layout)
        self.setCentralWidget(self.central_widget)
    
    def CreateHomeWindow(self):
        #Create Widgets for home window
        self.jobs_button = QPushButton("Jobs & Bookings")
        self.customer_details_button = QPushButton("Customer Details")
        self.database_button = QPushButton("Database Backup + Restore")
        self.quit_button = QPushButton("Quit")

        #Create Layout for widgets
        self.home_layout = QHBoxLayout()
        self.home_layout.addWidget(self.jobs_button)
        self.home_layout.addWidget(self.customer_details_button)
        self.home_layout.addWidget(self.database_button)
        self.home_layout.addWidget(self.quit_button)

        #Connections
        self.jobs_button.clicked.connect(self.OpenJobsWindow)
        self.customer_details_button.clicked.connect(self.OpenCustomerDetailsWindow)
        self.database_button.clicked.connect(self.OpenDatabaseWindow)
        self.quit_button.clicked.connect(self.QuitProgram)

    def OutstandJobsPopup(self):
        outstanding_jobs = OutstandingJobs(self)
        outstanding_jobs.show()
        outstanding_jobs.raise_()

    def OpenJobsWindow(self):
        jobs_window = JobsWindow(self)
        jobs_window.show()
        jobs_window.raise_()
        self.hide()

    def OpenCustomerDetailsWindow(self):
        customer_details_window = CustomerDetailsWindow(self)
        customer_details_window.show()
        customer_details_window.raise_()
        self.hide()

    def OpenDatabaseWindow(self):
        database_window = DatabaseWindow(self)
        database_window.show()
        database_window.raise_()
        self.hide()

    def QuitProgram(self): #exits program
        sys.exit()

if __name__ == "__main__":
    database.InitialiseTables()
    pet_service_system = QApplication(sys.argv)
    home_window = MainWindow()
    home_window.show()
    home_window.raise_()
    pet_service_system.exec_()
