from TextMenu import *

class TextUI:
    connection = None
    manager = None

    def __init__(self, manager):
        self.manager = manager






    def start(self):
        userExit = False

        while not userExit:
            print("X Public Library Online: Main Menu")

            options = {
                1: "Search Library Catalogue",
                2: "Checkout library items",
                3: "Return borrowed items",
                4: "Donate library items",
                5: "Search library events",
                6: "Register for library events",
                7: "Volunteer at XPL",
                8: "Ask for help from a librarian",
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
                self.addPersonnel()
            elif menuSelection == 8:
                self.listPersonnel()
            elif menuSelection == 9:
                print("Exiting Application...")
                userExit = True
            else:
                print("Invalid option selected")




    def searchCatalogue(self):

        rows = self.manager.getAllCatalogue()
        columnNames = self.manager.getColumnNamesFromTable("Item")

        userExit = False

        while not userExit:
            print("\n\n\n\n\n-Library Catalogue-")

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



    def addPersonnel(self):

        print("\n\n\n\n\n-Become a Volunteer-")

        print("To become a volunteer please fill in the following prompts: ")


        print("Press 0 to exit volunteer screen at anytime")

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

            self.manager.addPersonnel(volunteerInformation)


        else:
            print("Volunteer Form Cancelled\n")


    def listPersonnel(self):

        print("\n\n\n\n\nTo request help from a librarian please email one of the following: \n")


        rows = self.manager.getPersonnelContactInfo()

        columnNames = self.manager.getColumnNamesFromTable("Personnel")

        userExit = False

        while not userExit:
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

            print("1: Exit Personnel Information")

            menuSelection = int(input("Enter a selection: "))

            if menuSelection == 1:
                userExit = True
            else:
                print("Invalid option selected")