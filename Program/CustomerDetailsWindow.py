#Thomas Thorpe
#Pet Service Customer Details Window

from PyQt4.QtGui import *

from CreateCustomerForm import *
from SearchCustomerDetailsWindow import *
from CreateEmergencyContactForm import *
from SearchEmergencyContactsWindow import *
from CreateVetForm import *
from SearchVetDetailsWindow import *
from CreatePetForm import *
from SearchPetDetailsWindow import *

class CustomerDetailsWindow(QMainWindow):
    def __init__(self, came_from):
        super(QMainWindow,self).__init__(came_from)
        self.setWindowTitle("Customer Details Window")
        self.CreateCustomerDetailsWindow()
        self.came_from = came_from #parent window
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.customer_details_layout)
        self.setCentralWidget(self.central_widget)

    def CreateCustomerDetailsWindow(self):
        #Create Widgets
        #buttons
        self.new_customer_button = QPushButton("Create New Customer")
        self.search_customers_button = QPushButton("Customer Details")
        self.new_emergency_button = QPushButton("Create New Emergency Contact")
        self.search_emergency_button = QPushButton("Emergency Contact Details")

        self.new_vet_button = QPushButton("Create New Vet Details")
        self.search_vets_button = QPushButton("Vet Details")
        self.new_pet_button = QPushButton("Create New Pet Details")
        self.search_pets_button = QPushButton("Pet Details")

        self.back_button = QPushButton("Back To Home")

        #Create Layout
        self.top_half_layout = QGridLayout()
        self.customer_details_layout = QVBoxLayout()

        self.top_half_layout.addWidget(self.new_customer_button,0,0)
        self.top_half_layout.addWidget(self.search_customers_button,1,0)
        self.top_half_layout.addWidget(self.new_emergency_button,2,0)
        self.top_half_layout.addWidget(self.search_emergency_button,3,0)
        self.top_half_layout.addWidget(self.new_vet_button,0,1)
        self.top_half_layout.addWidget(self.search_vets_button,1,1)
        self.top_half_layout.addWidget(self.new_pet_button,2,1)
        self.top_half_layout.addWidget(self.search_pets_button,3,1)

        self.customer_details_layout.addLayout(self.top_half_layout)
        self.customer_details_layout.addWidget(self.back_button)

        #Connections
        self.back_button.clicked.connect(self.BackToHome)
        self.new_customer_button.clicked.connect(self.OpenNewCustomer)
        self.new_emergency_button.clicked.connect(self.OpenEmergencyContact)
        self.new_vet_button.clicked.connect(self.OpenNewVet)
        self.new_pet_button.clicked.connect(self.OpenNewPet)
        self.search_customers_button.clicked.connect(self.OpenSearchCustomers)
        self.search_emergency_button.clicked.connect(self.OpenSearchEmergency)
        self.search_pets_button.clicked.connect(self.OpenSearchPet)
        self.search_vets_button.clicked.connect(self.OpenSearchVet)

#all buttons to different windows
    def OpenSearchVet(self):
        new_search_vets_window = SearchVetDetailsWindow(self)
        new_search_vets_window.show()
        new_search_vets_window.raise_()
        self.hide()

    def OpenSearchPet(self):
        new_search_pets_window = SearchPetDetailsWindow(self)
        new_search_pets_window.show()
        new_search_pets_window.raise_()
        self.hide()

    def OpenSearchEmergency(self):
        new_search_emergency_window = SearchEmergencyContactsWindow(self)
        new_search_emergency_window.show()
        new_search_emergency_window.raise_()
        self.hide()

    def OpenSearchCustomers(self):
        new_search_customer_window = SearchCustomersWindow(self)
        new_search_customer_window.show()
        new_search_customer_window.raise_()
        self.hide()

    def OpenNewPet(self):
        new_pet_window = CreatePetWindow(self)
        new_pet_window.show()
        new_pet_window.raise_()

    def OpenNewVet(self):
        new_vet_window = CreateVetWindow(self)
        new_vet_window.show()
        new_vet_window.raise_()

    def OpenEmergencyContact(self):
        new_emergency_contact_window = CreateEmergencyContactWindow(self)
        new_emergency_contact_window.show()
        new_emergency_contact_window.raise_()

    def OpenNewCustomer(self):
        new_customer_window = CreateCustomerWindow(self)
        new_customer_window.show()
        new_customer_window.raise_()

    def BackToHome(self):
        self.close()
        self.came_from.show()
