#Thomas Thorpe
#Pet Service Select Database Restore

from PyQt4.QtGui import *

from Notification import *
import sqlite3
import os #used for files and directorys
import shutil #used for copying

class SelectDatabase(QDialog):
    def __init__(self, came_from, databases):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Select A Database To Restore")
        self.came_from = came_from
        self.CreateSelectDatabaseWindow(databases)
        self.setLayout(self.select_database_layout)

    def CreateSelectDatabaseWindow(self, databases):
        #create widgets
        self.lbl_format = QLabel("The format of the files is as follows:")
        self.lbl_example = QLabel("Pet_Service-Day_Month_Year_Hours_Minutes_Seconds.db")
        self.database_combo = QComboBox(self)
        self.database_combo.addItems(databases)
        self.confirm_button = QPushButton("Confirm Selection")

        #create layout
        self.select_database_layout = QVBoxLayout()
        self.select_database_layout.addWidget(self.lbl_format)
        self.select_database_layout.addWidget(self.lbl_example)
        self.select_database_layout.addWidget(self.database_combo)
        self.select_database_layout.addWidget(self.confirm_button)

        #connections
        self.confirm_button.clicked.connect(self.ConfirmChoice)

    def ConfirmChoice(self):
        self.choice = self.database_combo.currentText()

        connection = sqlite3.connect("Pet_Service.db")
        connection.commit()
        connection.close() #close the database while swapping in old copy

        shutil.copyfile(os.path.join(os.getcwd() + "\DatabaseBackups", self.choice), os.getcwd() + "\Pet_Service.db") #replace .db file that is used with backup (no need to rename)
        notification = Notification(self, "Restore Complete") #tell user restore has been completed
        notification.show()
        notification.raise_()

        self.came_from.show()
        self.close()
