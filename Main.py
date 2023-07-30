from TextUI import *
from DatabaseManager import *

import sqlite3
from sqlite3 import Error






def main():
    print("Application Started")

    print("Attempting connection to database...")
    db_file = "library.db"



    databaseManager = DatabaseManager()
    databaseManager.create_connection(db_file)
    ui = TextUI(databaseManager)
    ui.start()

    print("Exiting Application")


if __name__ == "__main__":
    main()
