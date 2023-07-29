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

    def searchCatalogue(self):

        searchAll = '''SELECT * FROM Item'''

        cursor = self.connection.cursor()

        cursor.execute(searchAll)
        rows = cursor.fetchall()

        columnNames = [description[0] for description in cursor.description]

        userExit = False

        while not userExit:
            print("\n\n\n\n\n-Library Catalogue-")

            row = rows[0]

            # print columns
            i = 0
            while i < len(columnNames):
                print("{0:20}".format(columnNames[i]), end='')
                i = i + 1
            print('')

            i = 0
            for row in rows:
                while i < len(columnNames):
                    columnAttribute = str(row[i])
                    shortenedString = columnAttribute[:19]
                    print("{0:20}".format(shortenedString), end='')
                    i = i + 1
                print('')
                i = 0
            print('\n')

            options = {
                1: "Search item by title",
                2: "Search item by author",
                3: "Search item by type",
                4: "Exit catalogue"
            }

            for i in options:
                print("{}. {}".format(i, options[i]))

            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                print("Browse")
            elif menuSelection == 2:
                print("Checkout")
            elif menuSelection == 3:
                print("Return")
            elif menuSelection == 4:
                userExit = True
            else:
                print("Invalid option selected")




    def donateAnItem(self):

        print("\n\n\n\n\n-Donation Menu-")

        sqlDonateItem = '''INSERT INTO Item(itemID, name, author, type, releaseDate, available, upcomingAddition)
                VALUES((SELECT IFNULL(MAX(itemID) + 1, 0) FROM Item),?,?,?,?,0,1)'''

        title = None
        author = None
        type = None
        releaseDate = None

        isInput0 = False
        while True:
            title = str(input("Enter the title of the item you wish to donate: "))
            if (title == "0"):
                isInput0 = True
                break
            elif (title != ""):
                break
            else:
                print("Please enter the items title")

        while not isInput0:
            author = str(input("Please enter the author/director/publisher of the item: "))
            if (author == "0"):
                isInput0 = True
                break
            elif (author != ""):
                break
            else:
                print("Please enter a author")

        while not isInput0:
            type = str(input("Please enter the item's media form (Book/CD/DVD/Journal/etc) : "))
            if (type == "0"):
                isInput0 = True
                break
            elif (type != ""):
                break
            else:
                print("Please enter the item's type")

        while not isInput0:
            releaseDate = str(input("Enter the release date of the item you wish to donate (YYYY-MM-DD): "))
            if (releaseDate == "0"):
                isInput0 = True
                break
            elif (releaseDate != ""):
                break
            else:
                print("Please enter a release date")

        if (not isInput0):
            print("Item successfully donated")
            isEnteringInfo = False

            cursor = self.connection.cursor()

            insertInformation = (title, author, type, releaseDate)

            cursor.execute(sqlDonateItem, insertInformation)

            self.connection.commit()

            return cursor.lastrowid


        print("Donation Cancelled\n")









    def addPersonnel(self):

        print("\n\n\n\n\n-Become a Volunteer-")

        sqlVolunteerInsert = '''INSERT INTO Personnel(employeeID, role, name, emailAddress)
                VALUES((SELECT IFNULL(MAX(employeeID) + 1, 0) FROM Personnel), "Volunteer",?,?)'''

        print("To become a volunteer please fill in the following prompts: ")

        isEnteringInfo = True
        while isEnteringInfo:
            print("Press 0 to exit volunteer screen")

            isNameValid = False
            isEmailValid = False
            isInput0 = False
            while not isInput0 and isNameValid:
                name = input("Enter your full name: ")
                if (name == "0"):
                    isInput0 = True
                    break
                elif (name != ""):
                    isNameValid = True
                else:
                    print("Please enter a valid name")

            while not isInput0 and isEmailValid:
                emailAddress = input("Please enter your email address: ")
                if (emailAddress == "0"):
                    break
                elif (emailAddress != ""):
                    isEmailValid = True
                else:
                    print("Please enter a valid email address")

            if (not isInput0):
                print("Item successfully donated")
                isEnteringInfo = False

                cursor = self.connection.cursor()

                insertInformation = (name, emailAddress)

                cursor.execute(sqlVolunteerInsert, insertInformation)

                self.connection.commit()

                return cursor.lastrowid

            else:
                isEnteringInfo = False
                print("Volunteer Form Cancelled\n")




    def listPersonnelContact(self):
        print("\n\n\n\n\nTo request help from a librarian please email one of the following: \n")

        sqlListPersonnelContact = '''SELECT role, name, emailAddress FROM Personnel'''

        cursor = self.connection.cursor()

        cursor.execute(sqlListPersonnelContact)
        rows = cursor.fetchall()

        columnNames = [description[0] for description in cursor.description]

        userExit = False

        while not userExit:
            print("-Personnel Information-")

            row = rows[0]

            # print columns
            i = 0
            while i < len(columnNames):
                print("{0:20}".format(columnNames[i]), end='')
                i = i + 1
            print('')

            i = 0
            for row in rows:
                while i < len(columnNames):
                    columnAttribute = str(row[i])
                    shortenedString = columnAttribute[:19]
                    print("{0:20}".format(shortenedString), end='')
                    i = i + 1
                print('')
                i = 0
            print('\n')

            print("1: Exit Personnel Information")

            menuSelection = int(input("Enter a selection: "))

            if menuSelection == 1:
                userExit = True
            else:
                print("Invalid option selected")