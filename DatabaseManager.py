import sqlite3
from sqlite3 import Error

from TextMenu import *


class DatabaseManager:
    connection = None

    def create_connection(self, db_file):
        connection = None
        try:
            connection = sqlite3.connect(db_file)
        except Error as e:
            print(e)
            print("Database failed to connect")

        self.connection = connection

    def getAllCatalogue(self):

        searchAll = '''SELECT * FROM Item'''

        cursor = self.connection.cursor()

        cursor.execute(searchAll)
        rows = cursor.fetchall()

        return rows


    def getCatalogueByAuthor(self, author):

        searchByAuthor = '''SELECT * FROM Item WHERE author = ? COLLATE NOCASE'''

        cursor = self.connection.cursor()

        print(author)

        cursor.execute(searchByAuthor, (author,))

        return cursor.fetchall()



    def getCatalogueByTitle(self, title):

        searchByTitle = '''SELECT * FROM Item WHERE name = ? COLLATE NOCASE'''

        cursor = self.connection.cursor()

        print(title)

        cursor.execute(searchByTitle, (title,))

        return cursor.fetchall()



    def getNumberOfRowsFromTable(self, table):
        sqlNumberColumns = '''SELECT COUNT(*) FROM pragma_table_info(?)'''

        cursor = self.connection.cursor()

        cursor.execute(sqlNumberColumns, table)

        return cursor.fetchall()


    def getColumnNamesFromTable(self, tableName):

        #sqlTables = '''.tables'''
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        rows = cursor.fetchall()

        tableExists = False
        for row in rows:
            if (row[0] == tableName):
                tableExists = True

        if (tableExists):
            sqlBlankSearch = 'SELECT * FROM {}'.format(tableName)

            cursor = self.connection.cursor()

            cursor.execute(sqlBlankSearch)

            columnNames = [description[0] for description in cursor.description]

            return columnNames

        else:
            return None



    def donateAnItem(self, insertInformation):

        sqlDonateItem = '''INSERT INTO Item(itemID, name, author, type, releaseDate, available, upcomingAddition)
                        VALUES((SELECT IFNULL(MAX(itemID) + 1, 0) FROM Item),?,?,?,?,0,1)'''

        cursor = self.connection.cursor()

        cursor.execute(sqlDonateItem, insertInformation)

        self.connection.commit()

        return cursor.lastrowid






    def addPersonnel(self, volunteerInformation):

        sqlVolunteerInsert = '''INSERT INTO Personnel(employeeID, role, name, emailAddress)
                VALUES((SELECT IFNULL(MAX(employeeID) + 1, 0) FROM Personnel), "Volunteer",?,?)'''

        cursor = self.connection.cursor()

        cursor.execute(sqlVolunteerInsert, volunteerInformation)

        self.connection.commit()

        return cursor.lastrowid




    def getPersonnelContactInfo(self):
        sqlListPersonnelContact = '''SELECT role, name, emailAddress FROM Personnel'''

        cursor = self.connection.cursor()

        cursor.execute(sqlListPersonnelContact)
        rows = cursor.fetchall()

        return rows