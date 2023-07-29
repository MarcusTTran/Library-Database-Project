
class TextMenu:


    @staticmethod
    def getMenuUserInput(options):
        isInputValid = False

        while not isInputValid:
            menuSelection = int(input("Enter a selection: "))

            if (menuSelection <= len(options) and menuSelection >= list(options.keys())[0]):
                print(menuSelection)
                return menuSelection

            else:
                print("Please enter a valid selection")