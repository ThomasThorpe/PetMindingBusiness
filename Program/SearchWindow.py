#Thomas Thorpe
#Pet Service Search Window Template

from PetServiceDatabase import *
from Notification import *
from PyQt4.QtGui import *
from DeleteRecordSearchWindows import *
from AreYouSureWindow import *

class SearchWindow(QMainWindow): #generalised search window
    def __init__(self,came_from):
        super(QMainWindow,self).__init__(came_from)
        self.came_from = came_from
        self.table_name = "Table Name Here"
        self.setWindowTitle("Search \" Table Name \" Details") #set title to whatever table is used from child window
        self.current_record_id = -1
        self.CreateSearchWindow()
        self.resize(925,200)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.search_layout)
        self.setCentralWidget(self.central_widget)

    def CreateSearchWindow(self):
        #create widgets
        self.lbl_search = QLabel("Search By:")

        self.attribute_combo = QComboBox(self)

        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText("Enter Search Here")
        self.search_button = QPushButton("Search")
        self.show_all_button = QPushButton("Show All")

        self.table_viewer = QTableView()

        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        self.back_button = QPushButton("Back")

        #create layout
        self.search_layout = QVBoxLayout()
        self.top_third = QHBoxLayout()
        self.bottom_third = QHBoxLayout()

        self.top_third.addWidget(self.lbl_search)
        self.top_third.addWidget(self.attribute_combo)
        self.top_third.addWidget(self.le_search)
        self.top_third.addWidget(self.search_button)
        self.top_third.addWidget(self.show_all_button)

        self.bottom_third.addWidget(self.edit_button)
        self.bottom_third.addWidget(self.delete_button)
        self.bottom_third.addWidget(self.back_button)

        self.search_layout.addLayout(self.top_third)
        self.search_layout.addWidget(self.table_viewer)
        self.search_layout.addLayout(self.bottom_third)

        #connections
        self.back_button.clicked.connect(self.BackToParent)
        self.search_button.clicked.connect(self.GetSearchInformation)
        self.show_all_button.clicked.connect(self.DisplayAll)
        self.edit_button.clicked.connect(self.EditRecord) #will pass selected ID or similar
        self.delete_button.clicked.connect(self.DeleteRecord) #will pass selected ID or similar
        self.table_viewer.clicked.connect(self.CellWasClicked)
        self.table_viewer.doubleClicked.connect(self.CellWasDoubleClicked)

    def CellWasClicked(self, index): #gets record id of current row
        y = index.row()
        self.current_record_id = self.table_viewer.model().index(y, 0).data()

    def PopulateTableView(self, data): #in cases with bool values will be polymorphismed
        sql = "PRAGMA table_info({0})".format(self.table_name)
        meta_data = database.FetchAllResult(sql) #get headers for table view

        self.model = QStandardItemModel()
        if len(data) == 0:
            self.model.setItem(0,0,QStandardItem("There Are No Records To Display"))
            self.model.setHorizontalHeaderItem(0,QStandardItem("N/A"))
        else:
            for row in range(len(data)):
                for column in range(len(data[0])):
                    item = QStandardItem("{0}".format(data[row][column]))
                    self.model.setItem(row, column, item)
                    header = QStandardItem(meta_data[column][1])
                    self.model.setHorizontalHeaderItem(column, header)
        self.table_viewer.verticalHeader().hide()
        self.table_viewer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_viewer.setModel(self.model)

    def EditRecord(self): #Will be polymorphismed
        pass

    def DeleteRecord(self):
        DeleteRecord(self, self.current_record_id, self.table_name)

    def BackToParent(self):
        self.close()
        self.came_from.show()

    def DisplayAll(self):
        sql = """SELECT * FROM {0}""".format(self.table_name)
        data = database.FetchAllResult(sql)
        self.PopulateTableView(data)

    def GetSearchInformation(self): #gets attribue and seach text to use
        self.attribute_selected = str(self.attribute_combo.currentText())
        self.search_text = self.le_search.text()
        self.SearchTable(self.attribute_selected, self.search_text)

    def SearchTable(self, attribute, search_text):
        if attribute == "PermissionForVet" or attribute == "PictureUsagePromo" or attribute == "Spayed" or attribute == "OnLead": #if searching bool values then make sure works
            if search_text == "Yes" or search_text == "yes": #for searching bool values
                search_text = 1
            elif search_text == "No" or search_text == "no":
                search_text = 0

        sql = """SELECT * FROM {0} WHERE {1}="{2}" """.format(self.table_name, attribute, search_text)
        data = database.FetchAllResult(sql)
        self.PopulateTableView(data)

    def PopulateAttributeCombo(self): #populates combo box with table headers
        sql = "PRAGMA table_info({0})".format(self.table_name)
        data = database.FetchAllResult(sql)

        attribute_list = []
        for count in range(len(data)):
            attribute_list.append("{0}".format(data[count][1]))
        self.attribute_combo.addItems(attribute_list)
