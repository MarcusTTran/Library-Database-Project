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
            print("Enter user id for login or press 9 to exit: ")
            userID = input("Enter user id: ")

            if (userID == '9'):
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
                1: "Search Library Catalogue",
                2: "Checkout library items",
                3: "Return borrowed items",
                4: "Donate library items",
                5: "Search library events",
                6: "Register for library events",
                7: "Volunteer at X Public Library",
                8: "Get help from a librarian",
                9: "Exit application"
            }

            for i in options:
                print("{}. {}".format(i, options[i]))

            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.searchCatalogue()
            elif menuSelection == 2:
                print("Checkout")
            elif menuSelection == 3:
                print("Return")
            elif menuSelection == 4:
                self.donateAnItem()
            elif menuSelection == 5:
                print("Search")
            elif menuSelection == 6:
                print("Register")
            elif menuSelection == 7:
                self.addVolunteer()
            elif menuSelection == 8:
                self.listPersonnel()
            elif menuSelection == 9:
                print("Logging out...")
                userExit = True
            else:
                print("Invalid option selected")


    def printCatalogue(self, rows, columnNames):
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



    def searchCatalogue(self):

        rows = self.manager.getAllCatalogue()
        columnNames = self.manager.getColumnNamesFromTable("Item")

        userExit = False

        while not userExit:
            print("\n\n\n\n\n-Library Catalogue-")

            # print columns and items
            self.printCatalogue(rows, columnNames)


            options = {
                1: "Search item by title",
                2: "Search item by author",
                3: "Exit catalogue"
            }

            for i in options:
                print("{}. {}".format(i, options[i]))

            menuSelection = TextMenu.getMenuUserInput(options)

            if menuSelection == 1:
                self.searchItemByTitle(columnNames)
            elif menuSelection == 2:
                self.searchItemByAuthor(columnNames)
            elif menuSelection == 3:
                userExit = True
            else:
                print("Invalid option selected")


    def searchItemByAuthor(self, columnNames):
        author = input("Enter author's name: ")

        rows = self.manager.getCatalogueByAuthor(author)
        self.printCatalogue(rows, columnNames)

        input("Press any key to exit: ")





    def searchItemByTitle(self, columnNames):
        title = input("Enter item's title: ")

        rows = self.manager.getCatalogueByTitle(title)
        self.printCatalogue(rows, columnNames)

        input("Press any key to exit: ")




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

    def searchLibEvents(self):
        tableName = "Event"
        userExit = False
        rows = self.manager.listTable(tableName)
        columnNames = self.manager.getColumnNamesFromTable(tableName)

        while not userExit:
            # print all events
            print("\n\n\n\n\n-Events Catalogue- \n")
            self.printCatalogue(rows, columnNames)

            options = {
                1: "Search event by name",
                2: "Search event by type",
                3: "Exit catalogue"
            }

            for i in options:
                print("{}. {}".format(i, options[i]))

            eventMenuSelection = TextMenu.getMenuUserInput(options)
            if eventMenuSelection == 1:
                eventType = "name"
                self.searchEventHandler(eventType, columnNames)
            elif eventMenuSelection == 2:
                eventType = "type"
                self.searchEventHandler(eventType, columnNames)
            elif eventMenuSelection == 3:
                userExit = True
            else:
                print("Invalid option selected")


    def searchEventHandler(self, eventType, columnNames):
        if eventType.lower() == "type":
            eventSearchKey = input("Please enter an event name:")
        else:
            eventSearchKey = input("Please enter an event type:")

        rows = self.manager.searchForEvent(eventSearchKey, eventType)
        self.printCatalogue(rows, columnNames)
        input("Press any key to exit: ")