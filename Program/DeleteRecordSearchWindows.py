#Thomas Thorpe
#Pet Service System Delete Record Search Windows Function

from PetServiceDatabase import *
from Notification import *
from AreYouSureWindow import *

def DeleteRecord(came_from, current_record_id, table_name):
    are_you_sure = ConfirmationWindow(came_from, "Are you sure you wish to delete this record? This action cannot be undone.")
    are_you_sure.setModal(True)
    are_you_sure.show()
    are_you_sure.raise_()
    decision = are_you_sure.exec_() #confirm deletion window
    if decision == 1:
        if current_record_id != -1 and current_record_id != "There Are No Records To Display":
            database.DeleteRecord(table_name, current_record_id)
            came_from.DisplayAll()
        else: #notify if record not selected
            notification = Notification(came_from, "Please select a record")
            notification.setModal(True)
            notification.show()
            notification.raise_()