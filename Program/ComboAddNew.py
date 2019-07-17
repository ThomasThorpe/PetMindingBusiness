#Thomas Thorpe
#Pet Service System CheckAddNewX

from CreateEmergencyContactForm import *
from CreateVetForm import *
from CreateCustomerForm import *
from CreatePetForm import *

#module used by various windows when checking if the user clicked "add new X" from combo boxes which contain foriegn keys

def CheckAddNewEmergencyContact(came_from, selection_num):
    if selection_num == 0:  #was clicked
        create_emergency_contact_form = CreateEmergencyContactWindow(came_from)
        create_emergency_contact_form.show()
        create_emergency_contact_form.raise_()
    came_from.emergency_combo.clear()
    came_from.PopulateEmergencyCombo()
    came_from.emergency_combo.setCurrentIndex(selection_num)

def CheckAddNewVet(came_from, selection_num):
    if selection_num == 0: #was clicked
        create_vet_form = CreateVetWindow(came_from)
        create_vet_form.show()
        create_vet_form.raise_()
    came_from.vet_combo.clear()
    came_from.PopulateVetCombo()
    came_from.vet_combo.setCurrentIndex(selection_num)

def CheckAddNewCustomer(came_from, selection_num):
    if selection_num == 0: #was clicked
        create_customer_form = CreateCustomerWindow(came_from)
        create_customer_form.show()
        create_customer_form.raise_()
    came_from.customer_combo.clear()
    came_from.PopulateCustomerCombo()
    came_from.customer_combo.setCurrentIndex(selection_num)
    came_from.pet1_combo.clear()
    came_from.pet2_combo.clear()
    came_from.pet3_combo.clear()
    came_from.PopulatePetCombos()

def CheckAddNewOwner(came_from, selection_num):
    if selection_num == 0: #was clicked
        create_customer_form = CreateCustomerWindow(came_from)
        create_customer_form.show()
        create_customer_form.raise_()
    came_from.customer_combo.clear()
    came_from.PopulateCustomerCombo()
    came_from.customer_combo.setCurrentIndex(selection_num)

def AddNewPet(came_from, selection_num, combo_num):
    create_new_pet = CreatePetWindow(came_from)
    create_new_pet.show()
    create_new_pet.raise_()
    came_from.pet1_combo.clear()
    came_from.pet2_combo.clear()
    came_from.pet3_combo.clear()
    came_from.PopulatePetCombos()
    if combo_num == 1:
        came_from.pet1_combo.setCurrentIndex(selection_num)
    elif combo_num == 2:
        came_from.pet2_combo.setCurrentIndex(selection_num)
    else:
        came_from.pet3_combo.setCurrentIndex(selection_num)