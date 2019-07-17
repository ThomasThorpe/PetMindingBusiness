#Thomas Thorpe
#Pet Service System Database Management Window

from PyQt4.QtGui import *

import sqlite3
from Notification import *
from AreYouSureWindow import *
from RestoreDatabase import *
from datetime import datetime #used to make timestamp
import shutil #used for copying and renameing files.
import os #used for files and directories

class DatabaseWindow(QMainWindow):
    def __init__(self, came_from):
        super(QMainWindow,self).__init__(came_from)
        self.setWindowTitle("Database Backup & Restore Window")
        self.CreateDatabaseWindow()
        self.came_from = came_from #parent
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.database_layout)
        self.setCentralWidget(self.central_widget)

    def CreateDatabaseWindow(self):
        #Create Widgets
        self.backup_button = QPushButton("Backup Database")
        self.restore_button = QPushButton("Restore Database")
        self.back_button = QPushButton("Back To Home")
        self.progress_bar = QProgressBar()
        self.progress_bar.hide() #create progress bar but hide until needed

        #Create Layout
        self.upper_layout = QHBoxLayout()
        self.upper_layout.addWidget(self.backup_button)
        self.upper_layout.addWidget(self.restore_button)
        self.upper_layout.addWidget(self.back_button)

        self.database_layout = QVBoxLayout()
        self.database_layout.addLayout(self.upper_layout)
        self.database_layout.addWidget(self.progress_bar)

        #Connections
        self.back_button.clicked.connect(self.BackToHome)
        self.restore_button.clicked.connect(self.RestoreDatabase)
        self.backup_button.clicked.connect(self.BackupDatabase)

    def RestoreDatabase(self): #restore pervious backup
        are_you_sure = ConfirmationWindow(self, "Are you sure you wish to restore an earlier version of the database? You should make a backup before restoring to be safe.")
        are_you_sure.setModal(True)
        are_you_sure.show()
        are_you_sure.raise_()
        self.decision = are_you_sure.exec_()
        if self.decision == 1:
            if not(os.path.isdir(os.getcwd() + "\DatabaseBackups")): #if there isn't the backups dir
                notification = Notification(self, "No backups have been made")
                notification.setModal(True)
                notification.show()
                notification.raise_()
            else:
                filenames = os.listdir(os.getcwd() + "\DatabaseBackups") #get list of all backups
                select_database = SelectDatabase(self, filenames) #send to restore window
                select_database.show()
                select_database.raise_()
                self.hide()

    def BackupDatabase(self): #create backup of .db file with a timestamp
        are_you_sure = ConfirmationWindow(self, "Are you sure you wish to make a backup of the current database?")
        are_you_sure.setModal(True)
        are_you_sure.show()
        are_you_sure.raise_()
        self.decision = are_you_sure.exec_() #confirmation
        if self.decision == 1:
            self.progress_bar.show() #show progress bar
            self.progress_bar.setRange(0,7) #set max steps for progress bar
            if not(os.path.isdir(os.getcwd() + "\DatabaseBackups")):
                os.makedirs(os.getcwd() + "\DatabaseBackups") #create backup folder if not exists
            self.progress_bar.setValue(1) #update progress bar
            connection = sqlite3.connect("Pet_Service.db")
            self.progress_bar.setValue(2)#update progress bar
            cursor = connection.cursor()
            cursor.execute("begin immediate") #lock database before backup
            self.progress_bar.setValue(3)#every now and then update progress
            shutil.copy(os.getcwd() + "\Pet_Service.db", os.getcwd() + "\DatabaseBackups") #make copy
            self.progress_bar.setValue(4)#update progress bar
            connection.rollback() #unlock database
            self.progress_bar.setValue(5)#update progress bar
            today = datetime.today()
            today = (str(today.strftime("-%d_%m_%Y_%H_%M_%S")))
            self.progress_bar.setValue(6)#update progress bar
            try:
                os.rename(os.getcwd() + "\DatabaseBackups\Pet_Service.db", os.path.join(os.getcwd() + "\DatabaseBackups", "Pet_Service" + today + ".db" )) #rename with timestamp
            except FileExistsError: #if you try to backup database twice within same second then error because file name already exists, this just cancels it
                pass
            self.progress_bar.setValue(7)
            self.progress_bar.hide() #hide progress when no longer needed
            self.progress_bar.setValue(0) #set progress bar back to 0% ready for next time if window not closed between attempts

    def BackToHome(self):
        self.close()
        self.came_from.show()
