from TextMenu import *

class TextUI:
    connection = None
    manager = None

    userid = None
    username = None

    def __init__(self, manager):
        self.manager = manager








    def start(self):

        rows = self.manager.getUserIDs()

        while True:
            print("Try entering some of these ids: ")
            for row in rows:
                print(row[0], end = " ")
            print("\n")


            validUserID = False
            print("Enter user id for login or press 0 to exit: ")
            userID = input("Enter user id: ")

            if (userID == '0'):
                break

            for row in rows:
                if (userID == str(row[0])):
                    self.userid = int(row[0])
                    self.username = self.manager.getNameFromUserID(self.userid)
                    validUserID = True

            if (validUserID):
                print("")
                self.mainMenu()
            else:
                print("User ID not found\n")







    def mainMenu(self):


        userExit = False
        while not userExit:
            print("X Public Library Online: Main Menu")

            print("Currently logged in as: ")
            print("\t User {}: {}\n".format(self.userid, self.username))

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


    def printCatalogue(self, rows, columnNames):
        i = 0
        while i < len(columnNames):
            print("{0:20}".format(columnNames[i]), end='')
            i = i + 1
        print("{0:20}".format("Availability"), end='')
        print('')

        i = 0
        for row in rows:
            while i < len(columnNames):
                columnAttribute = str(row[i])
                shortenedString = columnAttribute[:19]
                print("{0:20}".format(shortenedString), end='')
                i = i + 1
            if (self.manager.checkItemAvailable(row[0])):
                print("1", end='')
            else:
                print("0", end='')

            print('')
            i = 0
        print('\n')


    # User can search and checkout library catalogue
    def searchCatalogue(self):

        rows = self.manager.getAllCatalogue()
        columnNames = self.manager.getColumnNamesFromTable("Item")

        userExit = False

        options = {
            1: "Search item by title",
            2: "Search item by author",
            3: "Checkout item",
            0: "Exit catalogue"
        }

        menuSelection = None
        while not userExit:

            # Avoids reprinting of entire catalogue if checkout option (3) was pressed
            # Allows user to retry entry without having to reprint entire catalogue
            if (menuSelection != 3):
                print("\n\n\n\n\n-Library Catalogue-")
                self.printCatalogue(rows, columnNames)
                TextMenu.printOptions(options)
                avoidReprint = True


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


    def searchItemByAuthor(self, columnNames):
        author = input("Enter author's name: ")

        rows = self.manager.getCatalogueByAuthor(author)
        self.printCatalogue(rows, columnNames)

        options = {
            1: "Checkout item",
            0: "Exit screen"
        }




        userExit = False

        while not userExit:
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

        rows = self.manager.getCatalogueByTitle(title)
        self.printCatalogue(rows, columnNames)

        options = {
            1: "Checkout item",
            0: "Exit screen"
        }

        userExit = False

        while not userExit:
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
            self.manager.borrowItem(self.userid, itemID)
            print("Item borrowed successfully")

        if (not itemExists):
            print("Item not found")

        if (itemExists and not isItemAvailable):
            print("Item is currently not available")


    def returnItems(self):


        checkedOutRows = self.manager.getCheckedOutItems(self.userid)

        self.printCatalogue(checkedOutRows, ("ItemID", "Title"))

        input("Press any key to continue: ")

        # Add fines
        # Remove available attribute, add return date to borrows table




    def donateAnItem(self):

        print("\n\n\n\n\n-Donation Menu-")

        print("Press 0 to exit from Donation Menu at anytime: ")

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

            insertInformation = (title, author, type, releaseDate)

            self.manager.donateAnItem(insertInformation)


        else:
            print("Donation Cancelled\n")



    def addVolunteer(self):

        print("\n\n\n\n\n-Apply to become a Volunteer-")

        print("To become a volunteer please fill in the following submission form: ")
        print("Press 0 to exit volunteer screen at anytime")

        name = None
        emailAddress = None

        isInput0 = False
        while not isInput0:
            name = input("Enter your full name: ")
            if (name == "0"):
                isInput0 = True
                break
            elif (name != ""):
                break
            else:
                print("Please enter your name")

        while not isInput0:
            emailAddress = input("Please enter your email address: ")
            if (emailAddress == "0"):
                isInput0 = True
                break
            elif (emailAddress != ""):
                break
            else:
                print("Please an email address")

        if (not isInput0):
            print("You've been added to our personnel list")
            volunteerInformation = (name, emailAddress)

            self.manager.addVolunteer(volunteerInformation)


        else:
            print("Volunteer Form Cancelled\n")


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
