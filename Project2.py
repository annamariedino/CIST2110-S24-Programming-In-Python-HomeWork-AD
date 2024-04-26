# Project 2
# Name: Anna-Marie DiNofrio
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the Contacts. MAKE YOUR LIFE EASIER AND ENABLE WORDWRAP! VIEW -> WORD WRAP.
#
# The program will have the following features:
# 1. Add contact
# 2. View Contacts
# 3. Delete contact
# 4. Save Contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
from calendar import c
import csv
import datetime as dt
from math import e
from time import strftime
import sys
import tabulate


contact_dict = {}

def import_csv(file):
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            birthday = dt.datetime.strptime(row[3], '%m/%d/%Y').date()
            contact_dict[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
    print("Contacts imported successfully")

#CONTACTS [row[0]] = {'Phone': row[1], 'Email': row[2s], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
  # remove header
# this is an example to import the contacts.csv. Either have the add_contact function call the import_csv function or make the contacts variable GLOBAL



def add_contact(name, phone, email, birthday):
            # contact here is the dictionary of contacts -> Need to implement the function to import_csv first
            """This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
            Args:
                name (str): The name of the contact
                phone (str): The phone number of the contact
                email (str): The email address of the contact
                birthday (int): The birthday of the contact
            Returns:
                bool: True if the contact was added and False if the contact was not added
            """
            # insert import_csv function here. Returned value is a dictionary
            # contact = import_csv(contacts.csv)
            if name in contact_dict:
                print("Contact already exists")
                return False
            else:
                bday = dt.datetime(int(birthday.split("/")[2]), int(birthday.split("/")[0]), int(birthday.split("/")[1]))
                contact_dict[name] = [phone, email, bday]
                return True

# def save_contacts_to_csv(contacts):
#     with open('contacts_new.csv', 'x', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Name", "Phone", "Email", "Birthday"])
#         for name, info in contacts.items():
#             writer.writerow([name, info['Phone'], info['Email'], info['Birthday'].strftime('%m/%d/%Y')])
# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("Welcome to the Contact List Program")

def menu():
    while True:
        try:
            print("1. Add contact")
            print("2. View contacts")
            print("3. Delete contact")
            print("4. Save contacts to csv file")
            print("5. Next Birthday")
            print("0. Quit")
            menu_option = input("Please select an option: ")
            return int(menu_option) 
        except ValueError:
            print("Please enter a number")

   
# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above.
# The program will run until the user selects option 0 to quit.
# The program will be implemented in a file called Project2.py.
# The program will use the following functions:


# add_contact() -> add a contact to a dictionary

# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts.
# The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday.
# The function will take one parameter, the name of the csv file.
# The function will display an error message if the file does not exist.
# The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.



# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]


# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries.
# You can unpack the dictionary into a list of dictionaries.
# Like in Lab 11 and then use the tabulate library to display the contacts in a table format.
# This is optional and not required. You can use string formatting to display the contacts in a table format.
def view_Contacts():
    table = []
    for name, info in contact_dict.items():
        print(name, info)
    # for name, info in contact_dict.items():
    #     table.append({'Name': name, 'Phone': info[0], 'Email': info[1], 'Birthday': str(info[2])})
    # print(tabulate(table, headers='keys'))
    # print(table)

    
# delete_contact(id) - This function will delete a contact from the dictionary.
# The function will take one parameter, the name of the contact to delete.
# The function will return True if the contact was deleted and False if the contact was not deleted.
# The function will display an error message if the contact does not exist.
def delete_contact(name):
    if name in contact_dict:
        del contact_dict[name]
        return True
    else:
        print("Contact does not exist")
        return False
    
# next_birthday() - This function will disp1lay the next birthday. The function will take no parameters.
# The function will return nothing. The function will display a message if there are no Contacts in the dictionary.
# The function will display a message if there are no birthdays in the next 30 days.
# The function will display the next birthday and name if there is a birthday in the next 30 days.
# Use string formatting to display the next birthday.
# The birthdays should be sorted in consecutive order.
# The birthday dates should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue.
# 1: you could replace all the years with the current year.
# 2: you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.
def next_birthday():
    today = dt.datetime.today()
    next_birthday = None
    for name, info in contact_dict.items():
        contact_birthday = info['Birthday'].replace(year=today.year)
        # print(next_birthday)
        if contact_birthday >= today:
            # print(next_birthday)
            # print(contact_birthday, next_birthday['Birthday'])
            if next_birthday is None or contact_birthday < next_birthday['Birthday']:
                # print(f"Next birthday is {name} on {info['Birthday'].strftime('%m/%d/%Y')}")
                next_birthday = {'Name': name, 'Birthday': info['Birthday']}
    if next_birthday is None:
        print("No birthdays in the next 30 days")
    else:
        print(f"Next birthday is {next_birthday['Name']} on {next_birthday['Birthday'].strftime('%m/%d/%Y')}")
# save_csv() - This function will save the Contacts to the csv file.
# Prompt the user to enter a filename to save the Contacts to.
# If the file exists, overwrite the file. If the file does not exist, create the file.
# The function will return True if the Contacts were saved and False if the Contacts were not saved.
def save_csv():
    filename = input('Enter a filename')
    with open(f"{filename}.csv", 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Birthday"])
        for name, info in contact_dict.items():
            writer.writerow([name, info[0], info[1], str(info[2])])
        return True
   
# The main function will be used to run the program.
# The main function will use a while loop to display the menu and get the user's choice.
# The main function will call the appropriate function based on the user's choice.
# The main function will also call the save_csv function to save the Contacts to the csv file before the program ends.


def main():
    """Add Code here to call the functions and run the program""" 
    import_csv('contacts.csv')
    while True:
        menu_option = menu()
        if menu_option == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            birthday = input("Enter birthday (mm/dd/yyyy): ")
            add_contact(name, phone, email, birthday)
        elif menu_option == 2:
            view_Contacts()
        elif menu_option == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif menu_option == 4:
            save_csv()
        elif menu_option == 5:
            next_birthday()
        elif menu_option == 0:
            break
        else:
            print("Invalid option. Please try again.")
   
   
    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?
# for name in Contacts:
#     if name.lower.startswith("a"):
#         print(name)
#     # How many emails are yahoo emails?
# for email in Contacts:
#     if email.endswith("yahoo.com"):
#         print(email)
#     # How many .org emails are there?
# for email in Contacts:
#     if email.endswith(".org"):
#         print(email)
#     # How many Contacts have a birthday in January?
# for birthday in Contacts:
#     if birthday.month == 1:
#         print(birthday)
   
# Final Note: You will want to utilize code from other labs, homeworks, and projects. The Bank Account Program will be a good resource for the menu and main function. Use try except statements when possible.


if __name__ == "__main__":
    main()
