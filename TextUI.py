from TextMenu import *
import re

class TextUI:
    connection = None
    manager = None

    userid = None
    username = None

    def __init__(self, manager):
        self.manager = manager







    # Login page to enter userID
    def start(self):


        # repeat ask user for id unless enters 0 to exit
        userExit = False
        while not userExit:
            print("TIP: Try entering some of these userIDs: ")

            rows = self.manager.getUserIDs()
            for row in rows:
                print(row[0], end = "\t")
            print("\n")


            print("Enter user ID for login or press 0 to exit application: ")

            userInput = input("Enter user ID: ")

            if (self.manager.checkUserIDExists(userInput)):
                self.userid = userInput
                self.username = self.manager.getNameFromUserID(self.userid)
                self.mainMenu()
            elif (userInput == '0'):
                userExit = True
            else:
                print("UserID not found")








    # Main Menu after login screen
    def mainMenu(self):

        options = {
            1: "Borrow: Explore Library Catalogue",
            2: "Return: View Checked out items",
            3: "Donate library items",
            4: "Search library events",
            5: "Register for library events",
            6: "Volunteer at X Public Library",
            7: "Get help from a librarian",
            0: "Exit application"
        }

        userExit = False
        while not userExit:
            print("X Public Library Online: Main Menu")

            print("Currently logged in as: ")
            print("\t UserID {}: {}\n".format(self.userid, self.username))


            TextMenu.printOptions(options)
            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.searchCatalogue()
            elif menuSelection == 2:
                self.returnItems()
            elif menuSelection == 3:
                self.donateAnItem()
            elif menuSelection == 4:
                print("Search")
            elif menuSelection == 5:
                print("Register")
            elif menuSelection == 6:
                self.addVolunteer()
            elif menuSelection == 7:
                self.listPersonnel()
            elif menuSelection == 0:
                print("Logging out...")
                userExit = True
            else:
                print("Invalid option selected")





    # User can search and checkout library catalogue
    def searchCatalogue(self):

        options = {
            1: "Search item by title",
            2: "Search item by author",
            3: "Checkout item",
            0: "Exit catalogue"
        }

        rows = self.manager.getCatalogue()
        columnNames = self.manager.getColumnNamesFromTable("Item")

        menuSelection = None

        userExit = False
        while not userExit:

            print("\n\n\n\n\n-Library Catalogue-")
            self.printCatalogue(rows, columnNames)
            TextMenu.printOptions(options)

            # # Allows user to retry entry without reprinting entire catalogue
            # if (menuSelection != 3):
            #     print("\n\n\n\n\n-Library Catalogue-")
            #     self.printCatalogue(rows, columnNames)
            #     TextMenu.printOptions(options)

            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.searchItemByTitle(columnNames)
            elif menuSelection == 2:
                self.searchItemByAuthor(columnNames)
            elif menuSelection == 3:
                self.borrowItem()
            elif menuSelection == 0:
                userExit = True
            else:
                print("Invalid option selected")

        print("")

    # Print all Item rows with columnNames
    def printCatalogue(self, rows, columnNames):

        # Print column Names
        i = 0
        while i < len(columnNames) - 1:
            print("{0:20}".format(columnNames[i].upper()), end='')
            i = i + 1

        # Add extra coming soon column
        print("{0:20}".format("coming soon".upper()), end='')

        # Add extra availability column
        print("{0:20}".format("availability".upper()), end='')
        print('')


        columnLength = len(columnNames)

        # Print all rows in Item table
        i = 0
        for row in rows:
            while i < len(columnNames):
                self.printCatalogueRow(i, row, columnLength)
                i = i + 1
            if (self.manager.checkItemAvailable(row[0])):
                print("Available")
            else:
                print("Unavailable")

            i = 0

        print('\n')

    # Print each row in the catalogue with upcomingAttribute replaced with COMING SOON
    def printCatalogueRow(self, i, row, columnLength):
        columnAttribute = str(row[i])
        shortenedString = columnAttribute[:19]
        if (i == columnLength - 1):
            if (columnAttribute == '1'):
                shortenedString = "COMING SOON"
            else:
                shortenedString = ""
        print("{0:20}".format(shortenedString), end='')


    # Search item by author
    def searchItemByAuthor(self, columnNames):
        author = input("Enter author's name: ")

        options = {
            1: "Checkout item",
            0: "Exit search screen"
        }

        userExit = False

        while not userExit:
            rows = self.manager.getCatalogueByAuthor(author)
            self.printCatalogue(rows, columnNames)

            TextMenu.printOptions(options)
            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.borrowItem()
            elif menuSelection == 0:
                userExit = True
            else:
                print("Invalid option selected")


    def searchItemByTitle(self, columnNames):
        title = input("Enter item's title: ")

        options = {
            1: "Checkout item",
            0: "Exit search screen"
        }

        userExit = False

        while not userExit:
            rows = self.manager.getCatalogueByTitle(title)
            self.printCatalogue(rows, columnNames)

            TextMenu.printOptions(options)
            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.borrowItem()
            elif menuSelection == 0:
                userExit = True
            else:
                print("Invalid option selected")

    # Asks user for itemID to borrow
    def borrowItem(self):

        itemID = input("Enter itemID to borrow: ")

        itemExists = False
        isItemAvailable = False
        if (self.manager.checkItemExists(itemID)):
            itemExists = True

        if (itemExists and self.manager.checkItemAvailable(itemID)):
            isItemAvailable = True
            error = self.manager.borrowItem(self.userid, itemID)
            if error:
                print(error)
            else:
                print("Item borrowed successfully")

        if (not itemExists):
            print("Item with itemID not found")

        if (itemExists and not isItemAvailable):
            print("Item is currently not available")

        input("Press any key to continue: ")
        print("")


    def returnItems(self):

        fines = self.manager.getFines(self.userid)

        print("\nFines due: ${:.2f}".format(fines))
        print("Please payoff any fines at your local branch\n")

        options = {
            1: "Return item",
            0: "Exit screen"
        }

        userExit = False

        while not userExit:
            checkedOutRows = self.manager.getCheckedOutItems(self.userid)

            self.printCheckedoutItems(checkedOutRows, ("itemID", "Title", "Type", "Return by Date"))

            TextMenu.printOptions(options)
            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.returnItem()
            elif menuSelection == 0:
                userExit = True
            else:
                print("Invalid option selected")



    def printCheckedoutItems(self, checkedOutRows, columns):

        columnLength = len(columns)

        # Print column Names
        i = 0
        while i < columnLength:
            print("{0:20}".format(columns[i].upper()), end='')
            i = i + 1
        print("")

        # Print all rows in Item table
        i = 0
        for row in checkedOutRows:
            while i < columnLength:
                columnAttribute = str(row[i])
                shortenedString = columnAttribute[:19]
                print("{0:20}".format(shortenedString), end='')
                i = i + 1
            i = 0
            print("")

        print('\n')


    def returnItem(self):

        userExit = False

        while not userExit:
            menuSelection = input("Enter the itemID of the Item you wish to return or press 0 to exit: ")


            try:
                menuSelection = int(menuSelection)
                if menuSelection == 0:
                    userExit = True
                else:
                    if (self.manager.checkItemExists(menuSelection)):
                        self.manager.returnItem(self.userid, menuSelection)
                        print("Item returned successfully")

                    else:
                        print("Item not found")

            except ValueError:
                print("Invalid option selected")





    def donateAnItem(self):

        print("\n\n\n\n\n-Donation Menu-")

        print("Press 0 to exit from Donation Menu at anytime: ")

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
            insertInformation = [title, author, type, releaseDate]
            self.manager.donateAnItem(insertInformation)

            print("\nItem successfully donated")
            print("Please bring your item to the local library for dropoff")

            input("Press any key to continue: ")

        else:
            print("Donation Cancelled\n")



    def addVolunteer(self):

        print("\n\n\n\n\n-Apply to become a Volunteer-")

        print("To become a volunteer please fill in the following submission form: ")


        name = self.manager.getNameFromUserID(self.userid)

        print("You are volunteering as: {}".format(name))

        userExit = False
        while not userExit:
            userInput = input("Please enter your email address or press 0 to cancel form: ")
            #userInput = re.compile(userInput)

            if (userInput == "0"):
                print("Volunteer Form Cancelled\n")
                userExit = True
            elif (bool(re.search("\.com", userInput)) and bool(re.search('@', userInput))):
                print("Thank you for volunteer. You've been added to our personnel list.")
                volunteerInformation = (name, userInput)
                self.manager.addVolunteer(volunteerInformation)
                userExit = True
                print("We will contact you shortly")
                input("Press any key to continue: ")

            else:
                print("Email address not of valid form")




    def listPersonnel(self):

        print("\n\n\n\n\nTo request help from a librarian please email one of the following: \n")


        rows = self.manager.getPersonnelContactInfo()
        columnNames = self.manager.getColumnNamesFromTable("Personnel")

        print("-Personnel Information-")

        # print columns
        i = 0
        while i < len(columnNames) - 1:
            print("{0:20}".format(columnNames[i + 1]), end='')
            i = i + 1
        print('')

        i = 0
        for row in rows:
            while i < len(columnNames) - 1:
                columnAttribute = str(row[i])
                shortenedString = columnAttribute[:19]
                print("{0:20}".format(shortenedString), end='')
                i = i + 1
            print('')
            i = 0
        print('\n')

        input("Press any key to exit: ")
