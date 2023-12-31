# Library Database
## Introduction
A database that models a real-world library equipped with event rooms, events, library personnel, a varied catalogue of items, and more. Users can log in, search and register for events, search and borrow movies, novels, etc., sign-up as employees, and much more.
The database is coded in SQlite3 version 3.42.0 and the manager program was implemented using Python. </br>


## Entities and Relationships Schema </br>
First and foremost, our database includes a User table that will represent a library member. The User table stores a user’s ID, their name, fines owed, and one of their hobbies or interests. The database also includes an Item table which represents the various borrowable (or soon-to-be borrowable) items in the library. The Item table holds an item’s ID, title, author (or artist/publisher/director depending on the Items’ media type), media type, release date, and an upcomingAddition attribute that marks an item as an upcoming addition to the library’s catalogue. </br>

Our database also includes a Borrows table which stores which items are currently being borrowed by which users as well as each borrowed item’s return date. Our Borrow table has triggers which functions as constraints. One trigger prevents users who owe over $5 in fines from borrowing any books. Another trigger charges users with a fine if they return a book past its due date. The last trigger prevents users from borrowing items that have not yet been added to the catalogue (“coming soon” items). </br>

The personnel table is used to store information on the library’s employees and volunteers. Each library personnel has an ID, name, job role as well as an email address. The database includes a Room table which keeps track of all rooms in the library. This table works in tandem with our Events table which stores information on library events and bookclubs. Each Event will occur in a room listed in the Rooms table. </br>

The Event table holds information such as the event’s ID, name, type (or topic of the event), room number (where the event will be held), and the date and time of the Event. Users can search for and register for events by their name or type. When users decide to register for an event, if they have not already registered yet, it will be added to the Attends table. The Attends table represents which library members will be attending which events by storing the data with a combination of userID, and eventID. If they have registered already, it will return an error. No user can register for an event twice. </br>

Book Club meetings and events are stored in the Events table. Book club meetings have the same information as events such as eventID, eventName (name of the bookclub), eventType(will always be ‘Book Club’ in this case), roomID, and the date and time of meetings. Users can join any book club and once registered, they will be automatically enrolled for every book club meeting for that specific club. Users cannot sign up for the same book club twice. </br>

