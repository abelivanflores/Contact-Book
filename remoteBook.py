import mysql.connector
from mysql.connector import Error

#for my environment, we are using mysql 8.0.21 and an environment using Python 3.6.12 (64-bit)

#To provide background info on the Database I created, the database will automatically generate a unique contact_id that is assigned to each contact as well as create a time and date stamp as to when the contact was created
#The contacts table is split into the following columns: contact_id, last_name, first_name, contact_details, date_created 
#The program gives access for users to execute basic CRUD actions in the contact book

#the code below will automatically log us in to our database when the program is ran, in a professional environment hard coding credentials are not recommended as they pose a security risk 
#instead, we would import the following through a text file in a secure folder on our computer

db = mysql.connector.connect(
    host=" ",
    user=" ",
    passwd=" "
)
mycursor=db.cursor()


#the following code creates a function that will display our program's main menu, this will be looped to allow our user's to make multiple commands before they quit
def print_menu():
    print ("MAIN MENU")
    print ("****************")       
    print ("a. Add Contact")
    print ("d. Delete Contact")
    print ("u. Update Contact")
    print ("b. Display Contact by Alphabetical Order")
    print ("c. Display Contact by Creation Date")
    print ("o. Display All Contacts")
    print ("q. Exit Program")
    print ("****************\n")

#we set x to 1 as it will be the basis of our while loop    
x = 1  

#while loop will be needed for the main menu code below
while x == 1:          ## While loop which will keep going until x = 2
    print('\n')
    print_menu()    ## Displays menu
    userInput = input('What would you like to do?\n')
    if userInput == 'a':
        #if the user selects a) to create a contact we will ask for the new contact's full name and phone number followed by the execution of a command to interact with out database and commiting the changes
        user_last = input("What is their last name?: \n")
        user_first = input("What is their first name?: \n")
        user_details = input("What is their phone number?: \n")
        mycursor.execute("insert into contactos.contactInfo (last_name,first_name,contactDetails) VALUES (%s,%s,%s)",(user_last,user_first,user_details))
        db.commit()
        print('You Created A Contact\n')
    elif userInput == 'd':
        #if the user selects d) to delete a contact we will ask for the contact's associated contact ID number which can be seen when displaying our list of contacts followed by the execution of a command to interact with out database and commiting the changes
         user_delete = input("What is the id number associated with the contact name?: \n")      
         mycursor.execute("DELETE FROM contactos.contactInfo WHERE contact_id =%s;",(user_delete,))
         #code above was figured out on 02/18/21 7:50pm
         db.commit()                       
         print('You Deleted A Contact\n')  
    elif userInput == 'u':
        #if the user selects u) to update a contact we will ask for the contact's associated contact ID number to specify which contact will be updated followed by the execution of a command to interact with out database and commiting the changes
        #I decided to make this function only update their phone number as logically speaking people typically do not need to change their contact's first and last name 
         user_update = input("What is the contact id number associated with the contact name?: \n")      
         update_details = input("What is their new phone number?: \n")
         mycursor.execute("Update contactos.contactInfo SET contactDetails=%s WHERE contact_id =%s",(update_details,user_update))
         #code above was figured out on 02/18/21 7:33pm
         db.commit()
         print('You Updated A Contact\n') 
    elif userInput == 'b':
        #if the user selects b) then we will display our contacts in alphabetical order by first name
        print('Contacts Sorted By Alphabetical Order\n')
        mycursor.execute("Select * FROM contactos.contactInfo ORDER BY first_name ASC") 
        for y in mycursor:
         print ('\n')   
         print(y)               
    elif userInput == 'c':
        #if the user selects c) then we will display our contacts by date of creation, that being said our database organizes our contacts by creation date by default considering a unique contact_id number is generated everytime a contact is created
        print('Contacts Sorted By Date Of Creation\n')
        mycursor.execute("Select * FROM contactos.contactInfo ORDER BY createDate ASC") 
        for z in mycursor:
         print ('\n')   
         print(z)  
    elif userInput == 'o':
        #if the user selects b) then we will display all our contacts, by default they will be sorted by contact_id number in ascending order
        print('All Contacts Presented\n') #code added 02/18/21 5:15pm
        mycursor.execute("Select * FROM contactos.contactInfo") 
        for p in mycursor:
         print ('\n')   
         print(p)     
    elif userInput == 'q':
        #this command will quit our program by breaking our while loop and making x = 2, also will print a statement to communicate the termination of the program
        print('Exit Complete, GoodBye!\n')
        x = 2
        exit




