#Thomas Thorpe
#Pet Service System Notification

from PyQt4.QtGui import *

class Notification(QDialog): #general window used to display messages like a print statement in cmd
    def __init__(self, came_from, message):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Notification")
        self.CreateNotificationWindow(message)
        self.setLayout(self.notification_layout)
        self.exec_()

    def CreateNotificationWindow(self, message):
        #create widgets
        self.message = QLabel(message) #message passed from pervious window
        self.ok_button = QPushButton("Ok")

        #create layout
        self.notification_layout = QVBoxLayout()
        self.notification_layout.addWidget(self.message)
        self.notification_layout.addWidget(self.ok_button)

        #connections
        self.ok_button.clicked.connect(self.BackToParent)

    def BackToParent(self):
        self.close()
