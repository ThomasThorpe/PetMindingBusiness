#Thomas Thorpe
#Pet Service Search Customer Details Window

from SearchWindow import *
from EditCustomerForm import *
from DisplayCustomerDetails import *
from DisplayVetDetails import *
from DisplayEmergencyContact import *

class SearchCustomersWindow(SearchWindow): #takes template search window
    def __init__(self, came_from):
        super(SearchWindow,self).__init__(came_from)
        self.table_name = "Customer"
        self.DisplayAll()
        self.PopulateAttributeCombo()
        self.setWindowTitle("Search Customer Details Window")

    def CellWasDoubleClicked(self, index): #check when double clicked
        y = index.row()
        x = index.column()
        if x == 0: #check if customer id double clicked
            customer_id = self.table_viewer.model().index(y, x).data()
            display_customer = DisplayCustomerDetails(self, customer_id)
        elif x == 1: #check if emergency id double clicked
            emergency_id = self.table_viewer.model().index(y, x).data()
            display_emergency = DisplayEmergencyContact(self, emergency_id)
        elif x == 2: #check if vet id double clicked
            vet_id = self.table_viewer.model().index(y, x).data()
            display_vet = DisplayVetDetails(self, vet_id)

    def PopulateTableView(self, raw_data):
        sql = "PRAGMA table_info({0})".format(self.table_name)
        meta_data = database.FetchAllResult(sql)

        real_data = []
        count = 0
        while count < len(raw_data):
            temp_record = list(raw_data[count])
            if temp_record[13] == 1: #change bool values to "yes" "no"
                temp_record[13] = "Yes"
            elif temp_record[13] == 0:
                temp_record[13] = "No"

            if temp_record[14] == 1:
                temp_record[14] = "Yes"
            elif temp_record[14] == 0:
                temp_record[14] = "No"
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
            new_edit_customer_window = EditCustomerWindow(self, self.current_record_id)
            new_edit_customer_window.show()
            new_edit_customer_window.raise_()
            self.DisplayAll()
        else: #notify if no record selected
            notification = Notification(self, "Please select a record")
            notification.show()
            notification.raise_()
