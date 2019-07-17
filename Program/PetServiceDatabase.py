#Thomas Thorpe
#Pet Service Database Class

import sqlite3
from datetime import date, datetime

class PetServiceDatabase():
    def __init__(self):
        self.db_name = "Pet_Service.db"

    def ExecuteSQLParams(self, sql, params): #execute sql with values, often for adding + edotting
        with sqlite3.connect(self.db_name) as db:
            db.execute("PRAGMA foriegn_keys = ON")
            cursor = db.cursor()
            cursor.execute(sql, params)
            db.commit()

    def ExecuteSQL(self, sql): #execute sql without values, ofeten deleting
        with sqlite3.connect(self.db_name) as db:
            db.execute("PRAGMA foreign_keys = ON")
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()

    def FetchOneResult(self, sql): 
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    def FetchAllResult(self, sql):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def InitialiseTables(self): #create tables if no database exists
        sql = """create table if not exists Vet
                (VetID integer NOT NULL,
                VetFirstName text,
                VetLastName text,
                VetAddr1 text,
                VetAddr2 text,
                VetAddr3 text,
                VetAddr4 text,
                VetPostCode text,
                VetPhoneNum text,
                primary key(VetID))"""
        self.ExecuteSQL(sql)

        sql = """create table if not exists Emergency
                (EmergencyID integer NOT NULL,
                EmFirstName text,
                EmLastName text,
                EmAddr1 text,
                EmAddr2 text,
                EmAddr3 text,
                EmAddr4 text,
                EmPostCode text,
                EmMoblieNum text,
                EmHomeNum text,
                EmEmailAddr text,
                primary key(EmergencyID))"""
        self.ExecuteSQL(sql)

        sql = """create table if not exists Customer
                (CustomerID integer NOT NULL,
                EmergencyID integer,
                VetID integer,
                FirstName text,
                LastName text,
                Addr1 text,
                Addr2 text,
                Addr3 text,
                Addr4 text,
                PostCode text,
                MobileNum text,
                HomeNum text,
                EmailAddr text,
                PermissionForVet integer,
                PictureUsagePromo integer,
                primary key(CustomerID),
                foreign key(EmergencyID) references Emergency(EmergencyID) ON DELETE SET NULL,
                foreign key(VetID) references Vet(VetID) ON DELETE SET NULL)"""
        self.ExecuteSQL(sql)

        sql = """create table if not exists Pet
                (PetID integer NOT NULL,
                CustomerID integer,
                PetName text,
                PetSpecies text,
                Breed text,
                Colours text,
                DoB text,
                Spayed integer,
                Behaviour text,
                Commands text,
                FoodName text,
                FoodLocation text,
                FoodFrequency text,
                NightRequirements text,
                CleaningRequirements text,
                OtherInformation text,
                OnLead integer,
                primary key(PetID),
                foreign key(CustomerID) references Customer(CustomerID) ON DELETE CASCADE)"""
        self.ExecuteSQL(sql)

        sql = """create table if not exists Jobs
                (JobID integer NOT NULL,
                CustomerID integer,
                StartDate DATE,
                EndDate DATE,
                HadASessionBefore integer,
                DateOfLastSession text,
                JobType text,
                StartTime1 text,
                EndTime1 text,
                StartTime2 text,
                EndTime2 text,
                KeyLocation text,
                QuoteSent integer,
                InvoiceSent integer,
                PaymentReceived integer,
                JobComplete integer,
                primary key(JobID),
                foreign key(CustomerID) references Customer(CustomerId) ON DELETE CASCADE)"""
        self.ExecuteSQL(sql)

        #joining table
        sql = """create table if not exists PetsPerJob
                (JobID integer NOT NULL,
                PetID integer NOT NULL,
                foreign key(JobID) references Jobs(JobID) ON DELETE CASCADE,
                foreign key(PetID) references Pet(PetID) ON DELETE CASCADE,
                primary key(JobID, PetID))"""
        self.ExecuteSQL(sql)

        #create prices table with default prices given by client (pennies)
        sql = """SELECT name FROM sqlite_master WHERE type="table" AND name="Prices" """
        data = self.FetchOneResult(sql)
        if data == None:
            sql = """create table if not exists Prices
                    (JobNumber integer NOT NULL,
                    JobName text,
                    Price integer,
                    primary key(JobNumber))"""
            self.ExecuteSQL(sql)

            record1 = ["Dog Walking - Single 1 Hour", 1000]
            self.AddRecord("Prices", record1)
            record2 = ["Dog Walking - Single Half Hour", 600]
            self.AddRecord("Prices", record2)
            record3 = ["Dog Walking - 2 For 1 Hour", 1600]
            self.AddRecord("Prices", record3)
            record4 = ["Dog Walking - 2 For Half Hour", 1000]
            self.AddRecord("Prices", record4)
            record5 = ["Dog Walking - 3 For 1 Hour", 2400]
            self.AddRecord("Prices", record5)
            record6 = ["Dog Walking - 3 For Half Hour", 1500]
            self.AddRecord("Prices", record6)
            record7 = ["Animal Boarding - Dog", 1200]
            self.AddRecord("Prices", record7)
            record8 = ["Animal Boarding - Small Animal", 500]
            self.AddRecord("Prices", record8)
            record9 = ["Animal Boarding - Birds", 500]
            self.AddRecord("Prices", record9)
            record10 = ["Pet Sitting - Half Hour A Day", 550]
            self.AddRecord("Prices", record10)
            record11 = ["Pet Sitting - Hour A Day", 700]
            self.AddRecord("Prices", record11)
            record12 = ["Pet Sitting - Hour A Day (Two Half Hours)", 1100]
            self.AddRecord("Prices", record12)
            record13 = ["Pet Sitting - Hour And Half A Day", 1250]
            self.AddRecord("Prices", record13)
            record14 = ["Pet Sitting - Two Hours A Day", 1400]
            self.AddRecord("Prices", record14)

    def GetPrimaryID(self, table_name): #gets attribute name for primary key based on table name
        if table_name == "Vet":
            primary_key = "VetID"
        elif table_name == "Emergency":
            primary_key = "EmergencyID"
        elif table_name == "Customer":
            primary_key = "CustomerID"
        elif table_name == "Pet":
            primary_key = "PetID"
        elif table_name == "Jobs":
            primary_key = "JobID"
        elif table_name == "Prices":
            primary_key = "JobNumber"
        else:
            return "NULL"
        return primary_key

    def EditRecord(self, table_name, values, record_id):
        sql = "PRAGMA table_info({0})".format(table_name)
        data = self.FetchAllResult(sql)
        attribute_list_without_id = []
        for count in range(len(data) - 1): #get list of attributes in order without id as handled automatically
            attribute_list_without_id.append("{0}".format(data[count + 1][1]))
        primary_key = self.GetPrimaryID(table_name) #get attronite name for primary key

        count = 0
        sql = """UPDATE {0} SET """.format(table_name) #formatting sql to edit record  with values
        while count < len(values):
            if count != (len(values) - 1):
                sql = sql + """{0} = ?,""".format(attribute_list_without_id[count])
            else:
                sql = sql + """{0} = ? WHERE {1} = {2}""".format(attribute_list_without_id[count], primary_key, record_id)
            count += 1
        
        self.ExecuteSQLParams(sql, values)

    def DeleteRecord(self, table_name, id_delete): #delete selected record from selected table
        primary_id = self.GetPrimaryID(table_name) #get attribute name for primary key
        sql = """DELETE FROM {0} WHERE {1} = {2}""".format(table_name, primary_id, id_delete)
        self.ExecuteSQL(sql)

    def AddRecord(self, table_name, values): #formatting sql to add record to x table with values given
        count = 0
        sql = """INSERT INTO {0} VALUES(NULL,""".format(table_name)
        while count < len(values):
            if count != (len(values) - 1):
                sql = sql + """?,"""
            else:
                sql = sql + """?)"""
            count += 1

        self.ExecuteSQLParams(sql, values)

    def AddJoiningTableRecord(self, job_id, pet_id):
        sql = """INSERT INTO PetsPerJob VALUES ({0}, {1})""".format(job_id, pet_id)

        self.ExecuteSQL(sql)

    def DeleteJoiningTableRecord(self, job_id):
        sql = """DELETE FROM PetsPerJob WHERE JobID={0}""".format(job_id)

        self.ExecuteSQL(sql)

database = PetServiceDatabase() #golbal database var used to execute sql
