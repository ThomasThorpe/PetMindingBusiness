#Thomas Thorpe
#Pet Service System Display Emergency Contact

from PetServiceDatabase import *

from PyQt4.QtGui import *

class DisplayEmergencyContact(QDialog):#window to display record, used mainly when double clicking id in table views
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Emergency Contact Details")
        self.record_id = record_id
        self.GetEmergencyContactInformation()
        self.CreateDisplayEmergencyContact()
        self.setLayout(self.display_emergency_contact)
        self.exec_()

    def CreateDisplayEmergencyContact(self):
        #create widget
        #labels
        self.lbl_first_name = QLabel("First Name")
        self.lbl_last_name = QLabel("Last Name")
        self.lbl_addr1 = QLabel("Address Line 1")
        self.lbl_addr2 = QLabel("Address Line 2")
        self.lbl_addr3 = QLabel("Address Line 3")
        self.lbl_addr4 = QLabel("Address Line 4")
        self.lbl_postcode = QLabel("Post Code")
        self.lbl_mobile = QLabel("Mobile Number")
        self.lbl_home = QLabel("Home Number")
        self.lbl_email_addr = QLabel("Email Address")

        #line edits (set values and set uneditable)
        self.le_first_name = QLineEdit()
        self.le_first_name.setEnabled(False)
        self.le_first_name.setText(self.data[0][1])
        self.le_last_name = QLineEdit()
        self.le_last_name.setEnabled(False)
        self.le_last_name.setText(self.data[0][2])
        self.le_addr1 = QLineEdit()
        self.le_addr1.setEnabled(False)
        self.le_addr1.setText(self.data[0][3])
        self.le_addr2 = QLineEdit()
        self.le_addr2.setEnabled(False)
        self.le_addr2.setText(self.data[0][4])
        self.le_addr3 = QLineEdit()
        self.le_addr3.setEnabled(False)
        self.le_addr3.setText(self.data[0][5])
        self.le_addr4 = QLineEdit()
        self.le_addr4.setEnabled(False)
        self.le_addr4.setText(self.data[0][6])
        self.le_postcode = QLineEdit()
        self.le_postcode.setEnabled(False)
        self.le_postcode.setText(self.data[0][7])
        self.le_mobile = QLineEdit()
        self.le_mobile.setEnabled(False)
        self.le_mobile.setText(self.data[0][8])
        self.le_home = QLineEdit()
        self.le_home.setEnabled(False)
        self.le_home.setText(self.data[0][9])
        self.le_email_addr = QLineEdit()
        self.le_email_addr.setEnabled(False)
        self.le_email_addr.setText(self.data[0][10])

        #create layout
        self.display_emergency_contact = QGridLayout()

        self.display_emergency_contact.addWidget(self.lbl_first_name,0,0)
        self.display_emergency_contact.addWidget(self.lbl_last_name,1,0)
        self.display_emergency_contact.addWidget(self.lbl_addr1,2,0)
        self.display_emergency_contact.addWidget(self.lbl_addr2,3,0)
        self.display_emergency_contact.addWidget(self.lbl_addr3,4,0)
        self.display_emergency_contact.addWidget(self.lbl_addr4,5,0)
        self.display_emergency_contact.addWidget(self.lbl_postcode,6,0)
        self.display_emergency_contact.addWidget(self.lbl_mobile,7,0)
        self.display_emergency_contact.addWidget(self.lbl_home,8,0)
        self.display_emergency_contact.addWidget(self.lbl_email_addr,9,0)

        self.display_emergency_contact.addWidget(self.le_first_name,0,1)
        self.display_emergency_contact.addWidget(self.le_last_name,1,1)
        self.display_emergency_contact.addWidget(self.le_addr1,2,1)
        self.display_emergency_contact.addWidget(self.le_addr2,3,1)
        self.display_emergency_contact.addWidget(self.le_addr3,4,1)
        self.display_emergency_contact.addWidget(self.le_addr4,5,1)
        self.display_emergency_contact.addWidget(self.le_postcode,6,1)
        self.display_emergency_contact.addWidget(self.le_mobile,7,1)
        self.display_emergency_contact.addWidget(self.le_home,8,1)
        self.display_emergency_contact.addWidget(self.le_email_addr,9,1)

    def GetEmergencyContactInformation(self):
        sql = """SELECT * FROM Emergency WHERE EmergencyID={0}""".format(self.record_id)
        self.data = database.FetchAllResult(sql)
