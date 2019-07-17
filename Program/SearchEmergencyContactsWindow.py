#Thomas Thorpe
#Pet Service Search Emergency Contacts Window

from SearchWindow import *
from EditEmergencyContactForm import *
from DisplayEmergencyContact import *

class SearchEmergencyContactsWindow(SearchWindow): #takes template search window
    def __init__(self, came_from):
        super(SearchWindow,self).__init__(came_from)
        self.table_name = "Emergency"
        self.DisplayAll()
        self.PopulateAttributeCombo()
        self.setWindowTitle("Search Emergency Contacts Window")

    def CellWasDoubleClicked(self, index): #check when double clicked cell
        y = index.row()
        x = index.column()
        if x == 0: #if emergency id double clicked info window displayed
            emergency_id = self.table_viewer.model().index(y, x).data()
            display_emergency = DisplayEmergencyContact(self, emergency_id)

    def EditRecord(self):
        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            new_edit_emergency_contact_window = EditEmergencyContactForm(self, self.current_record_id)
            new_edit_emergency_contact_window.show()
            new_edit_emergency_contact_window.raise_()
            self.DisplayAll()
        else: #notify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()
