#Thomas Thorpe
#Pet Service System Display Vet Details

from PetServiceDatabase import *

from PyQt4.QtGui import *

class DisplayVetDetails(QDialog): #window to display record, used mainly when double clicking id in table views
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Vet Details")
        self.record_id = record_id
        self.GetVetInformation()
        self.CreateDisplayVetWindow()
        self.setLayout(self.display_vet_layout)
        self.exec_()

    def CreateDisplayVetWindow(self):
        #create widgets
        #labels
        self.lbl_first_name = QLabel("First Name")
        self.lbl_last_name = QLabel("Last Name")
        self.lbl_addr1 = QLabel("Address Line 1")
        self.lbl_addr2 = QLabel("Address Line 2")
        self.lbl_addr3 = QLabel("Address Line 3")
        self.lbl_addr4 = QLabel("Address Line 4")
        self.lbl_postcode = QLabel("Post Code")
        self.lbl_phone = QLabel("Phone Number")

        #line edits (setting values and uneditable)
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
        self.le_phone = QLineEdit()
        self.le_phone.setEnabled(False)
        self.le_phone.setText(self.data[0][8])

        #create layout
        self.display_vet_layout = QGridLayout()

        self.display_vet_layout.addWidget(self.lbl_first_name,0,0)
        self.display_vet_layout.addWidget(self.lbl_last_name,1,0)
        self.display_vet_layout.addWidget(self.lbl_addr1,2,0)
        self.display_vet_layout.addWidget(self.lbl_addr2,3,0)
        self.display_vet_layout.addWidget(self.lbl_addr3,4,0)
        self.display_vet_layout.addWidget(self.lbl_addr4,5,0)
        self.display_vet_layout.addWidget(self.lbl_postcode,6,0)
        self.display_vet_layout.addWidget(self.lbl_phone,7,0)

        self.display_vet_layout.addWidget(self.le_first_name,0,1)
        self.display_vet_layout.addWidget(self.le_last_name,1,1)
        self.display_vet_layout.addWidget(self.le_addr1,2,1)
        self.display_vet_layout.addWidget(self.le_addr2,3,1)
        self.display_vet_layout.addWidget(self.le_addr3,4,1)
        self.display_vet_layout.addWidget(self.le_addr4,5,1)
        self.display_vet_layout.addWidget(self.le_postcode,6,1)
        self.display_vet_layout.addWidget(self.le_phone,7,1)

    def GetVetInformation(self):
        sql = """SELECT * FROM Vet WHERE VetID={0}""".format(self.record_id)
        self.data = database.FetchAllResult(sql)
