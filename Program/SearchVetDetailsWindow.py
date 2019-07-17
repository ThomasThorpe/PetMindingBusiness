#Thomas Thorpe
#Pet Service Search Vet Details Window

from SearchWindow import *
from EditVetForm import *
from DisplayVetDetails import *

class SearchVetDetailsWindow(SearchWindow): #takes template search window
    def __init__(self, came_from):
        super(SearchWindow,self).__init__(came_from)
        self.table_name = "Vet"
        self.DisplayAll()
        self.PopulateAttributeCombo()
        self.setWindowTitle("Search Vet Details Window")

    def CellWasDoubleClicked(self, index): #checks if double clicked vet id to display
        y = index.row()
        x = index.column()
        if x == 0:
            vet_id = self.table_viewer.model().index(y, x).data()
            display_vet = DisplayVetDetails(self, vet_id)

    def EditRecord(self):
        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            new_edit_vet_window = EditVetWindow(self, self.current_record_id)
            new_edit_vet_window.show()
            new_edit_vet_window.raise_()
            self.DisplayAll()
        else: #noify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()
