#Thomas Thorpe
#Pet Service Jobs Window

from PyQt4.QtGui import *

from SelectJobType import *
from SearchJobsWindow import *

class JobsWindow(QMainWindow):
    def __init__(self, came_from):
        super(QMainWindow,self).__init__(came_from)
        self.setWindowTitle("Jobs Window")
        self.CreateJobsWindow()
        self.came_from = came_from #parent window
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.jobs_layout)
        self.setCentralWidget(self.central_widget)

    def CreateJobsWindow(self):
        #Create Widgets
        self.new_job_button = QPushButton("Create New Jobs")
        self.search_button = QPushButton("Job Details")
        self.current_jobs_button = QPushButton("Check Current Jobs")
        self.back_button = QPushButton("Back To Home")

        #Create Layout
        self.jobs_layout = QVBoxLayout()
        self.jobs_layout.addWidget(self.new_job_button)
        self.jobs_layout.addWidget(self.search_button)
        self.jobs_layout.addWidget(self.current_jobs_button)
        self.jobs_layout.addWidget(self.back_button)

        #Connections
        self.back_button.clicked.connect(self.BackToHome)
        self.new_job_button.clicked.connect(self.CreateJob)
        self.search_button.clicked.connect(self.SearchWindowDefault)
        self.current_jobs_button.clicked.connect(self.SearchWindowCurrent)

    def BackToHome(self):
        self.close()
        self.came_from.show()

    def SearchWindowDefault(self):
        self.OpenSearchWindow(1) #passed value to show all by default

    def SearchWindowCurrent(self):
        self.OpenSearchWindow(0) #passes value to display oustanding by default

    def OpenSearchWindow(self, display_current):
        search_jobs = SearchJobsWindow(self, display_current)
        search_jobs.show()
        search_jobs.raise_()
        self.hide()

    def CreateJob(self):
        select_job = SelectJobType(self)
        select_job.show()
        select_job.raise_()
        self.hide()
        
