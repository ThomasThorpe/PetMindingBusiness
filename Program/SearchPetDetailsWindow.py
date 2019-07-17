#Thomas Thorpe
#Pet Service Search Pet Details Window

from SearchWindow import *
from EditPetForm import *
from DisplayCustomerDetails import *
from DisplayPetDetails import *

class SearchPetDetailsWindow(SearchWindow): #takes template search window
    def __init__(self, came_from):
        super(SearchWindow,self).__init__(came_from)
        self.table_name = "Pet"
        self.DisplayAll()
        self.PopulateAttributeCombo()
        self.setWindowTitle("Search Pet Details Window")

    def CellWasDoubleClicked(self, index): #check if ID was double clicked to display info window
        y = index.row()
        x = index.column()
        if x == 0: #check if pet id was double clicked
            pet_id = self.table_viewer.model().index(y, x).data()
            display_pet = DisplayPetDetails(self, pet_id)
        elif x == 1: #check if customer id was double clicked
            customer_id = self.table_viewer.model().index(y, x).data()
            display_customer = DisplayCustomerDetails(self, customer_id)

    def PopulateTableView(self, raw_data):
        sql = "PRAGMA table_info({0})".format(self.table_name)
        meta_data = database.FetchAllResult(sql)

        real_data = []
        count = 0
        while count < len(raw_data):
            temp_record = list(raw_data[count])
            if temp_record[7] == 1: #setting bool values to "yes" and "no"
                temp_record[7] = "Yes"
            elif temp_record[7] == 0:
                temp_record[7] = "No"

            if temp_record[16] == 1:
                temp_record[16] = "Yes"
            elif temp_record[16] == 0:
                temp_record[16] = "No"
            real_data.append(temp_record)
            count = count + 1

        self.model = QStandardItemModel()
        if len(raw_data) == 0:
            self.model.setItem(0,0,QStandardItem("There Are No Records To Display"))
            self.model.setHorizontalHeaderItem(0,QStandardItem("N/A"))
        else:
            for row in range(len(real_data)):
                for column in range(len(real_data[0])):
                    item = QStandardItem("{0}".format(real_data[row][column]))
                    self.model.setItem(row, column, item)
                    header = QStandardItem(meta_data[column][1])
                    self.model.setHorizontalHeaderItem(column, header)
        self.table_viewer.verticalHeader().hide()
        self.table_viewer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_viewer.setModel(self.model)

    def EditRecord(self):
        if self.current_record_id != -1 and self.current_record_id != "There Are No Records To Display":
            new_edit_pet_window = EditPetForm(self, self.current_record_id)
            new_edit_pet_window.show()
            new_edit_pet_window.raise_()
            self.DisplayAll()
        else: #noify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()
