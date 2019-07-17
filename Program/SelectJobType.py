#Thomas Thorpe
#Pet Service Select Job Type Window

from PyQt4.QtGui import *

from CreateJobWindow import *

class SelectJobType(QMainWindow):
    def __init__(self, came_from):
        super(QMainWindow,self).__init__(came_from)
        self.setWindowTitle("Select Job Type")
        self.CreateJobTypeWindow()
        self.came_from = came_from

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.job_type_layout)
        self.setCentralWidget(self.central_widget)

    def CreateJobTypeWindow(self):
        #Create Widgets
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

        self.submit_button = QPushButton("Submit")
        self.cancel_button = QPushButton("Cancel")

        #Create Layout
        self.job_type_layout = QVBoxLayout()
        self.bottom_layout = QHBoxLayout()

        self.bottom_layout.addWidget(self.submit_button)
        self.bottom_layout.addWidget(self.cancel_button)

        self.job_type_layout.addWidget(self.select_job_combo)
        self.job_type_layout.addLayout(self.bottom_layout)

        #Connections
        self.cancel_button.clicked.connect(self.BackToJobs)
        self.submit_button.clicked.connect(self.CreateJob)

    def CreateJob(self):
        job_num = self.select_job_combo.currentIndex()
        job_name = self.select_job_combo.currentText()
        create_job_window = CreateJobWindow(self, job_num, job_name)
        create_job_window.show()
        create_job_window.raise_()
        self.hide()

    def BackToJobs(self):
        self.close()
        self.came_from.show()
