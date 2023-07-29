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
                self.manager.searchCatalogue()
            elif menuSelection == 2:
                print("Checkout")
            elif menuSelection == 3:
                print("Return")
            elif menuSelection == 4:
                self.manager.donateAnItem()
            elif menuSelection == 5:
                print("Search")
            elif menuSelection == 6:
                print("Register")
            elif menuSelection == 7:
                self.manager.addPersonnel()
            elif menuSelection == 8:
                self.manager.listPersonnelContact()
            elif menuSelection == 9:
                print("Exiting Application...")
                userExit = True
            else:
                print("Invalid option selected")



