# Library Application

from circle import *

import sqlite3
from sqlite3 import Error




def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
            print("Database failed to connect")
        
        return conn
    
    

        
        
def searchCatalogue(connection):

        
        searchAll = '''SELECT * FROM Item'''

        cursor = connection.cursor()

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
                1 : "Search item by title", 
                2 : "Search item by author", 
                3 : "Search item by type", 
                4 : "Exit catalogue"
                }

            for i in options: 
                print("{}. {}".format(i, options[i]))
            
            menuSelection = getMenuUserInput(options)
            
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
            


# Serves as insert row?
def donateAnItem(connection):
    
        print("\n\n\n\n\n-Donation Menu-")
    
        sql = '''INSERT INTO Item(itemID, name, releaseDate, availability, upcomingAddition)
                VALUES((SELECT MAX(itemID) + 1 FROM Item),?,?,0,1)'''
    
        name = input("Enter the name of the item you wish to donate: ")
        releaseDate = input("Enter the release date of the item you wish to donate (YYYY-MM-DD): ")
        
        cursor = connection.cursor()
        
        
        insertInformation = (name, releaseDate)
        

        
        cursor.execute(sql, insertInformation)
        
        connection.commit()
        
        return cursor.lastrowid



def getMenuUserInput(options):
        isInputValid = False
        
        while not isInputValid:
            menuSelection = int(input("Enter a selection: "))
            
            if(menuSelection <= len(options) and menuSelection >= list(options.keys())[0]):
                print(menuSelection)
                isInputValid = True
            else:
                print("Please enter a valid selection")
                
        return menuSelection
        

def mainMenu(connection):
        
        userExit = False
        
        while not userExit:
            print("X Public Library Online: Main Menu")
            
            options = {
                1 : "Search Library Catalogue", 
                2 : "Checkout library items", 
                3 : "Return borrowed items", 
                4 : "Donate library items", 
                5 : "Search library events", 
                6 : "Register for library events", 
                7 : "Volunteer at XPL", 
                8 : "Ask for help from a librarian",
                9   : "Exit application"
                }

            for i in options: 
                print("{}. {}".format(i, options[i]))
            
            
            
            menuSelection = getMenuUserInput(options)

                

            
            if menuSelection == 1:
                searchCatalogue(connection)
            elif menuSelection == 2:
                print("Checkout")
            elif menuSelection == 3:
                print("Return")
            elif menuSelection == 4:
                donateAnItem(connection)
            elif menuSelection == 5:
                print("Search")
            elif menuSelection == 6:
                print("Register")
            elif menuSelection == 7:
                print("Volunteer")
            elif menuSelection == 8:
                print("Help")
            elif menuSelection == 9:
                print("Exiting Application...")
                userExit = True
            else:
                print("Invalid option selected")
            
            
            
        
        
        
        




def main():
        print("Application Started")
        
            
            
        print("Attempting connection to database...")
        db_file = "library.db"
        

        connection = create_connection(r"library.db")

            
        circle1 = CircleObj("red")
        print(circle1.getColour())
        print(circle1.getSize())
        circle1.setSize(69)
        print(circle1.getSize())


        
        print("\n\n\n\n\nWelcome to X Public Library Online")   
        
        mainMenu(connection)
        
        print("Thank you for using X Public Library Online")
        
        
        
if __name__ == "__main__":
    main()



