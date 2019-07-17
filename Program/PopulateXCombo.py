#Thomas Thorpe
#Pet Service System PopulateXCombo

from PetServiceDatabase import *

def PopulateVetCombo(came_from):
    sql = """SELECT VetFirstName, VetLastName FROM Vet"""
    data = database.FetchAllResult(sql)

    vet_list = ["Add New Vet"]
    for count in range(len(data)):
        vet_list.append("{0} {1}".format(data[count][0], data[count][1]))
    came_from.vet_combo.addItems(vet_list)

def PopulateEmergencyCombo(came_from):
    sql = """SELECT EmFirstName, EmLastName FROM Emergency"""
    data = database.FetchAllResult(sql)

    emergency_list = ["Add New Emergency Contact"]
    for count in range(len(data)):
        emergency_list.append("{0} {1}".format(data[count][0], data[count][1]))
    came_from.emergency_combo.addItems(emergency_list)

def PopulateCustomerCombo(came_from):
    sql = """SELECT FirstName, LastName FROM Customer"""
    data = database.FetchAllResult(sql)

    customer_list = ["Add New Customer"]
    if len(data) != 0:
        for count in range(len(data)):
            customer_list.append("{0} {1}".format(data[count][0], data[count][1]))
        came_from.customer_combo.addItems(customer_list)
        came_from.customer_combo.setCurrentIndex(1) #set default to first customer not "add new x"
    else:
        came_from.customer_combo.addItems(customer_list)
        came_from.customer_combo.setCurrentIndex(0)