import sqlite3
from sqlite3 import Error


class DatabaseManager:
    connection = None

    def create_connection(self, db_file):
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            print("Database connected\n")
        except Error as e:
            print(e)
            print("Database failed to connect")

        self.connection = connection



    def close_connection(self):
        self.connection.close()
        print("\nDatabase connection closed")


    def checkUserIDExists(self, userID):
        rows = self.getUserIDs()

        validUserID = False
        for row in rows:
            if (userID == str(row[0])):
                self.userid = int(row[0])
                validUserID = True

        if (validUserID):
            return True
        else:
            return False


    def getCatalogue(self):

        searchAll = '''SELECT * FROM Item'''

        cursor = self.connection.cursor()

        cursor.execute(searchAll)
        rows = cursor.fetchall()

        return rows


    def getCatalogueByAuthor(self, author):

        searchByAuthor = '''SELECT * FROM Item WHERE author LIKE ? COLLATE NOCASE'''

        cursor = self.connection.cursor()

        author = author + '%'
        cursor.execute(searchByAuthor, (author,))

        return cursor.fetchall()



    def getCatalogueByTitle(self, title):

        searchByTitle = '''SELECT * FROM Item WHERE title LIKE ? COLLATE NOCASE'''

        cursor = self.connection.cursor()

        title = title + '%'
        cursor.execute(searchByTitle, (title,))

        return cursor.fetchall()



    def getNumberOfRowsFromTable(self, table):
        sqlNumberColumns = '''SELECT COUNT(*) FROM pragma_table_info(?)'''

        cursor = self.connection.cursor()

        cursor.execute(sqlNumberColumns, table)

        return cursor.fetchall()


    def getColumnNamesFromTable(self, tableName):

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



    def getUserIDs(self):
        sqlUserId = '''SELECT * from User'''

        cursor = self.connection.cursor()

        cursor.execute(sqlUserId)
        rows = cursor.fetchall()

        return rows


    def getNameFromUserID(self, userID):
        sqlUserName = '''SELECT name from User where userID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlUserName, (userID,))
        rows = cursor.fetchall()[0]

        return rows[0]


    def donateAnItem(self, insertInformation):

        sqlDonateItem = '''INSERT INTO Item(itemID, title, author, type, releaseDate, upcomingAddition)
                        VALUES((SELECT IFNULL(MAX(itemID) + 1, 0) FROM Item),?,?,?,?,1)'''

        cursor = self.connection.cursor()

        cursor.execute(sqlDonateItem, insertInformation)

        self.connection.commit()

        return cursor.lastrowid


    # Insert new row into Borrow table with specified userID and itemID
    def borrowItem(self, userID, itemID):
        sqlBorrowInsert = '''INSERT INTO Borrows(itemID, userID) VALUES (?, ?)'''

        insertInformation = (itemID, userID)

        cursor = self.connection.cursor()

        try:
            cursor.execute(sqlBorrowInsert, insertInformation)
            self.connection.commit()
            return None

        except sqlite3.IntegrityError as e:
            return e









    def getFines(self, userID):
        sqlFinesQuery = '''SELECT finesDue FROM User WHERE userID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlFinesQuery, (userID, ))

        fines = cursor.fetchone()

        return fines[0]


    def returnItem(self, userID, itemID):
        sqlReturnBorrow = '''DELETE FROM Borrows WHERE Borrows.userID = ? and Borrows.itemID = ? '''

        cursor = self.connection.cursor()

        cursor.execute(sqlReturnBorrow, (userID, itemID))

        self.connection.commit()

        return cursor.lastrowid


    # Returns False if itemID found in Borrows table or upcomingAttribute of tuple with matching itemID in Item table
    # is set to 1; returns True otherwise
    def checkItemAvailable(self, itemID):
        #Check itemID not found in Borrows table
        sqlBorrowQuery = '''SELECT itemID FROM Borrows WHERE itemID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlBorrowQuery, (itemID, ))

        borrowRows = cursor.fetchall()

        #Check itemID upcomingAddition attribute set to True
        sqlBorrowQuery = '''SELECT upcomingAddition FROM Item WHERE itemID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlBorrowQuery, (itemID, ))

        itemRows = cursor.fetchall()[0]

        upcomingAddition = False
        if (itemRows[0] == 1):
            upcomingAddition = True

        #if not borrowRows and not upcomingAddition:
        if not borrowRows:
            return True
        else:
            return False


    def checkItemUpcomingAddition(self, itemID):
        sqlBorrowQuery = '''SELECT upcomingAddition FROM Item WHERE itemID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlBorrowQuery, (itemID, ))

        rows = cursor.fetchone()[0]

        upcomingAddition = False
        if (rows == 1):
            upcomingAddition = True

        if not upcomingAddition:
            return True
        else:
            return False


    # Returns True if itemID found in Item table; False if not
    def checkItemExists(self, itemID):
        sqlItemQuery = '''SELECT itemID FROM Item WHERE itemID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlItemQuery, (itemID, ))

        itemRows = cursor.fetchall()

        if itemRows:
            return True
        else:
            return False


    def addVolunteer(self, volunteerInformation):

        sqlVolunteerInsert = '''INSERT INTO Personnel(employeeID, role, name, emailAddress)
                VALUES((SELECT IFNULL(MAX(employeeID) + 1, 0) FROM Personnel), "Volunteer",?,?)'''

        cursor = self.connection.cursor()

        cursor.execute(sqlVolunteerInsert, volunteerInformation)

        self.connection.commit()

        return cursor.lastrowid



    def getCheckedOutItems(self, userID):
        sqlBorrowQuery = '''SELECT Item.itemID, Item.title, Item.type, Borrows.returnDate FROM Borrows NATURAL JOIN ITEM WHERE userID = ?'''

        cursor = self.connection.cursor()

        cursor.execute(sqlBorrowQuery, (userID, ))

        rows = cursor.fetchall()

        return rows


    def getPersonnelContactInfo(self):
        sqlListPersonnelContact = '''SELECT role, name, emailAddress FROM Personnel'''

        cursor = self.connection.cursor()

        cursor.execute(sqlListPersonnelContact)
        rows = cursor.fetchall()

        return rows


    def searchForEvent(self, searchKey):
        sqlSearchAllEvents = '''SELECT eventID, eventName, datetime(event) FROM Event'''
        sqlSearchEventsWithSubstring = '''SELECT eventID, eventName, datetime(event) FROM event WHERE eventName LIKE :search'''
        cursor = self.connection.cursor()

        if (searchKey == ""):
            cursor.execute(sqlSearchAllEvents)
        else:
            cursor.execute(sqlSearchEventsWithSubstring, {"search": "%" + searchKey + "%"})

        eventsLst = cursor.fetchall()
        return eventsLst


