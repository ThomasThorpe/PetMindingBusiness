#Thomas Thorpe
#Pet Service System Display Pet Details

from PetServiceDatabase import *

from DisplayCustomerDetails import *
from PyQt4.QtGui import *

class DisplayPetDetails(QDialog):#window to display record, used mainly when double clicking id in table views
    def __init__(self, came_from, record_id):
        super(QDialog,self).__init__(came_from)
        self.setWindowTitle("Pet Details")
        self.record_id = record_id
        self.GetPetInformation()
        self.CreateDisplayPetWindow()
        self.setLayout(self.display_pet_layout)
        self.exec_()

    def CreateDisplayPetWindow(self):
        #create widgets
        #labels
        self.lbl_name = QLabel("Name")
        self.lbl_species = QLabel("Species")
        self.lbl_breed = QLabel("Breed")
        self.lbl_colours = QLabel("Colours")
        self.lbl_dob = QLabel("Date of Birth")
        self.lbl_food_name = QLabel("Food Name")
        self.lbl_food_frequency = QLabel("Food Frequency")
        self.lbl_lead = QLabel("On Lead?")
        self.lbl_spayed = QLabel("Spayed?")
        self.lbl_behaviour = QLabel("Behaviour")
        self.lbl_commands = QLabel("Commands")
        self.lbl_food_location = QLabel("Food Location")
        self.lbl_owner = QLabel("Owner/Customer ID")
        self.lbl_cleaning = QLabel("Cleaning Requirements")
        self.lbl_night = QLabel("Night Requirements")
        self.lbl_other = QLabel("Other Information")

        #line edis (Seting values and uneditable)
        self.le_name = QLineEdit()
        self.le_name.setEnabled(False)
        self.le_name.setText(self.data[0][2])
        self.le_species = QLineEdit()
        self.le_species.setEnabled(False)
        self.le_species.setText(self.data[0][3])
        self.le_breed = QLineEdit()
        self.le_breed.setEnabled(False)
        self.le_breed.setText(self.data[0][4])
        self.le_colours = QLineEdit()
        self.le_colours.setEnabled(False)
        self.le_colours.setText(self.data[0][5])
        self.le_dob = QLineEdit()
        self.le_dob.setEnabled(False)
        self.le_dob.setText(self.data[0][6])
        self.le_food_name = QLineEdit()
        self.le_food_name.setEnabled(False)
        self.le_food_name.setText(self.data[0][10])
        self.le_food_frequency = QLineEdit()
        self.le_food_frequency.setEnabled(False)
        self.le_food_frequency.setText(self.data[0][12])
        self.le_lead = QLineEdit()
        self.le_lead.setEnabled(False)
        #setting bool values
        if self.data[0][16] == 0:
            self.le_lead.setText("No")
        elif self.data[0][16] == 1:
            self.le_lead.setText("Yes")
        self.le_spayed = QLineEdit()
        self.le_spayed.setEnabled(False)
        if self.data[0][7] == 0:
            self.le_spayed.setText("No")
        elif self.data[0][7] == 1:
            self.le_spayed.setText("Yes")
        self.le_customer_id = QLineEdit()
        self.le_customer_id.setEnabled(False)
        self.le_customer_id.setText(str(self.data[0][1])) #set customer id

        #text edits
        self.tx_behaviour = QTextEdit(self)
        self.tx_behaviour.setMaximumHeight(60)
        self.tx_behaviour.setReadOnly(True)
        self.tx_behaviour.insertPlainText(self.data[0][8])
        self.tx_commands = QTextEdit(self)
        self.tx_commands.setMaximumHeight(60)
        self.tx_commands.setReadOnly(True)
        self.tx_commands.insertPlainText(self.data[0][9])
        self.tx_food_location = QTextEdit(self)
        self.tx_food_location.setMaximumHeight(60)
        self.tx_food_location.setReadOnly(True)
        self.tx_food_location.insertPlainText(self.data[0][11])
        self.tx_cleaning = QTextEdit(self)
        self.tx_cleaning.setMaximumHeight(60)
        self.tx_cleaning.setReadOnly(True)
        self.tx_cleaning.insertPlainText(self.data[0][14])
        self.tx_night = QTextEdit(self)
        self.tx_night.setMaximumHeight(60)
        self.tx_night.setReadOnly(True)
        self.tx_night.insertPlainText(self.data[0][13])
        self.tx_other = QTextEdit(self)
        self.tx_other.setMaximumHeight(60)
        self.tx_other.setReadOnly(True)
        self.tx_other.insertPlainText(self.data[0][15])

        self.customer_button = QPushButton("Check Owner Details")

        #create layout
        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.lbl_name)
        self.vbox1.addWidget(self.lbl_species)
        self.vbox1.addWidget(self.lbl_breed)
        self.vbox1.addWidget(self.lbl_colours)
        self.vbox1.addWidget(self.lbl_dob)
        self.vbox1.addWidget(self.lbl_food_name)
        self.vbox1.addWidget(self.lbl_food_frequency)
        self.vbox1.addWidget(self.lbl_lead)
        self.vbox1.addWidget(self.lbl_spayed)
        self.vbox1.addWidget(self.lbl_owner)

        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.le_name)
        self.vbox2.addWidget(self.le_species)
        self.vbox2.addWidget(self.le_breed)
        self.vbox2.addWidget(self.le_colours)
        self.vbox2.addWidget(self.le_dob)
        self.vbox2.addWidget(self.le_food_name)
        self.vbox2.addWidget(self.le_food_frequency)
        self.vbox2.addWidget(self.le_lead)
        self.vbox2.addWidget(self.le_spayed)
        self.vbox2.addWidget(self.le_customer_id)

        self.gridbox3 = QGridLayout()
        self.gridbox3.addWidget(self.lbl_behaviour,0,0)
        self.gridbox3.addWidget(self.lbl_commands,1,0)
        self.gridbox3.addWidget(self.lbl_food_location,2,0)
        self.gridbox3.addWidget(self.tx_behaviour,0,1)
        self.gridbox3.addWidget(self.tx_commands,1,1)
        self.gridbox3.addWidget(self.tx_food_location,2,1)
        self.gridbox3.addWidget(self.customer_button,3,1)

        self.gridbox4 = QGridLayout()
        self.gridbox4.addWidget(self.lbl_cleaning,0,0)
        self.gridbox4.addWidget(self.lbl_night,1,0)
        self.gridbox4.addWidget(self.lbl_other,2,0)
        self.gridbox4.addWidget(self.tx_cleaning,0,1)
        self.gridbox4.addWidget(self.tx_night,1,1)
        self.gridbox4.addWidget(self.tx_other,2,1)

        self.display_pet_layout = QHBoxLayout()
        self.display_pet_layout.addLayout(self.vbox1)
        self.display_pet_layout.addLayout(self.vbox2)
        self.display_pet_layout.addLayout(self.gridbox3)
        self.display_pet_layout.addLayout(self.gridbox4)

        #connections
        self.customer_button.clicked.connect(self.CheckOwnerDetails)

    def CheckOwnerDetails(self):
        display_owner_details = DisplayCustomerDetails(self, int(self.le_customer_id.text()))
        display_owner_details.show()
        display_owner_details.raise_()

    def GetPetInformation(self):
        sql = """SELECT * FROM Pet WHERE PetID={0}""".format(self.record_id)
        self.data = database.FetchAllResult(sql)
