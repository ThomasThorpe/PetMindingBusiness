#Thomas Thorpe
#Pet Service System Display Customer/Owner

from PetServiceDatabase import *

from DisplayVetDetails import *
from DisplayEmergencyContact import *
from PyQt4.QtGui import *

class DisplayCustomerDetails(QDialog):#window to display record, used mainly when double clicking id in table views
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Customer Details")
        self.record_id = record_id
        self.GetCustomerInformation()
        self.CreateDisplayCustomerWindow()
        self.setLayout(self.display_customer_layout)
        self.exec_()

    def CreateDisplayCustomerWindow(self):
        #create widgets
        #labels
        self.lbl_first_name = QLabel("First Name")
        self.lbl_last_name = QLabel("Last Name")
        self.lbl_addr1 = QLabel("Address Line 1")
        self.lbl_addr2 = QLabel("Address Line 2")
        self.lbl_addr3 = QLabel("Address Line 3")
        self.lbl_addr4 = QLabel("Address Line 4")
        self.lbl_vet = QLabel("Vet Contact ID")
        self.lbl_postcode = QLabel("Post Code")
        self.lbl_mobile = QLabel("Mobile Number")
        self.lbl_home = QLabel("Home Number")
        self.lbl_email_addr = QLabel("Email Address")
        self.lbl_permission_vet = QLabel("Permission For Vet")
        self.lbl_picture_usuage = QLabel("Permission For Picture Usuage")
        self.lbl_emergency = QLabel("Emergency Contact ID")

        #line edits (setting values and making uneditable)
        self.le_first_name = QLineEdit()
        self.le_first_name.setEnabled(False)
        self.le_first_name.setText(self.data[0][3])
        self.le_last_name = QLineEdit()
        self.le_last_name.setEnabled(False)
        self.le_last_name.setText(self.data[0][4])
        self.le_addr1 = QLineEdit()
        self.le_addr1.setEnabled(False)
        self.le_addr1.setText(self.data[0][5])
        self.le_addr2 = QLineEdit()
        self.le_addr2.setEnabled(False)
        self.le_addr2.setText(self.data[0][6])
        self.le_addr3 = QLineEdit()
        self.le_addr3.setEnabled(False)
        self.le_addr3.setText(self.data[0][7])
        self.le_addr4 = QLineEdit()
        self.le_addr4.setEnabled(False)
        self.le_addr4.setText(self.data[0][8])
        self.le_postcode = QLineEdit()
        self.le_postcode.setEnabled(False)
        self.le_postcode.setText(self.data[0][9])
        self.le_mobile = QLineEdit()
        self.le_mobile.setEnabled(False)
        self.le_mobile.setText(self.data[0][10])
        self.le_home = QLineEdit()
        self.le_home.setEnabled(False)
        self.le_home.setText(self.data[0][11])
        self.le_email_addr = QLineEdit()
        self.le_email_addr.setEnabled(False)
        self.le_email_addr.setText(self.data[0][12])
        self.le_vet = QLineEdit()
        self.le_vet.setEnabled(False)
        self.le_vet.setText(str(self.data[0][2]))
        self.le_emergency = QLineEdit()
        self.le_emergency.setEnabled(False)
        self.le_emergency.setText(str(self.data[0][1]))
        self.le_permission_vet = QLineEdit()
        self.le_permission_vet.setEnabled(False)
        #setting bool values
        if self.data[0][13] == 0:
            self.le_permission_vet.setText("No")
        elif self.data[0][13] == 1:
            self.le_permission_vet.setText("Yes")
        self.le_picture_usuage = QLineEdit()
        self.le_picture_usuage.setEnabled(False)
        if self.data[0][14] == 0:
            self.le_picture_usuage.setText("No")
        elif self.data[0][14] == 1:
            self.le_picture_usuage.setText("Yes")

        #buttons
        self.emergency_button = QPushButton("Check Emergency Contact Details")
        self.vet_button = QPushButton("Check Vet Details")

        #create layout
        self.display_customer_layout = QGridLayout()

        self.display_customer_layout.addWidget(self.lbl_first_name,0,0)
        self.display_customer_layout.addWidget(self.lbl_last_name,1,0)
        self.display_customer_layout.addWidget(self.lbl_addr1,2,0)
        self.display_customer_layout.addWidget(self.lbl_addr2,3,0)
        self.display_customer_layout.addWidget(self.lbl_addr3,4,0)
        self.display_customer_layout.addWidget(self.lbl_addr4,5,0)
        self.display_customer_layout.addWidget(self.lbl_postcode,6,0)
        self.display_customer_layout.addWidget(self.lbl_mobile,7,0)
        self.display_customer_layout.addWidget(self.lbl_home,8,0)
        self.display_customer_layout.addWidget(self.lbl_email_addr,9,0)
        self.display_customer_layout.addWidget(self.lbl_permission_vet,10,0)
        self.display_customer_layout.addWidget(self.lbl_picture_usuage,11,0)
        self.display_customer_layout.addWidget(self.lbl_emergency,12,0)
        self.display_customer_layout.addWidget(self.lbl_vet,13,0)
        self.display_customer_layout.addWidget(self.emergency_button,14,0)

        self.display_customer_layout.addWidget(self.le_first_name,0,1)
        self.display_customer_layout.addWidget(self.le_last_name,1,1)
        self.display_customer_layout.addWidget(self.le_addr1,2,1)
        self.display_customer_layout.addWidget(self.le_addr2,3,1)
        self.display_customer_layout.addWidget(self.le_addr3,4,1)
        self.display_customer_layout.addWidget(self.le_addr4,5,1)
        self.display_customer_layout.addWidget(self.le_postcode,6,1)
        self.display_customer_layout.addWidget(self.le_mobile,7,1)
        self.display_customer_layout.addWidget(self.le_home,8,1)
        self.display_customer_layout.addWidget(self.le_email_addr,9,1)
        self.display_customer_layout.addWidget(self.le_permission_vet,10,1)
        self.display_customer_layout.addWidget(self.le_picture_usuage,11,1)
        self.display_customer_layout.addWidget(self.le_emergency,12,1)
        self.display_customer_layout.addWidget(self.le_vet,13,1)
        self.display_customer_layout.addWidget(self.vet_button,14,1)

        #connections
        self.emergency_button.clicked.connect(self.CheckEmergencyContact)
        self.vet_button.clicked.connect(self.CheckVetDetails)

    def CheckEmergencyContact(self):
        display_emergency_contact = DisplayEmergencyContact(self, int(self.le_emergency.text()))
        display_emergency_contact.show()
        display_emergency_contact.raise_()

    def CheckVetDetails(self):
        display_vet_details = DisplayVetDetails(self, int(self.le_vet.text()))
        display_vet_details.show()
        display_vet_details.raise_()

    def GetCustomerInformation(self):
        sql = """SELECT * FROM Customer WHERE CustomerID={0}""".format(self.record_id)
        self.data = database.FetchAllResult(sql)
