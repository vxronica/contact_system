import re

#dictionary to store contacts
contacts = {}

#function to add contacts
def add_contact():

    unique_identifier = input("Enter unique identifier (phone number or email address): ")

    #check to see if email is correctly formatted
    if not (re.match(r"^(?:\+1)?\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$", unique_identifier) or re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", unique_identifier)):
        print("Invalid identifier format. Please try again.")
        return
    
    if unique_identifier in contacts:
        print("A contact with this identifier already exists in the system.")
        return
    
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    #check to verifity phone number format
    if not re.match(r"^(?:\+1)?\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$", phone):
        print("Invalid phone number format. Please try again.")
        return
    
    email = input("Enter email address: ")
    #check email format
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        print("Invalid email address format. Please try again.")
        return
    
    address = input("Enter address: ")
    notes = input("Enter additional notes: ")

    #new entry with unique identifier as key
    contacts[unique_identifier] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address,
        'Notes': notes
    }
    print("Contact added successfully to the sytem.")
    
#function to edit contacts
def edit_contact():
    unique_identifier = input("Enter unique identifier(phone number/email) of the contact to edit: ")
    if unique_identifier not in contacts:
        print("Contact not found.")
        return
    
    name = input(f"Enter name ({contacts[unique_identifier]['Name']})(Leave empty if you would like to make no changes): ")
    phone = input(f"Enter phone number ({contacts[unique_identifier]['Phone']})(Leave empty if you would like to make no changes): ")

    #check phone number format
    if phone and not re.match(r"^(?:\+1)?\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$", phone):
        print("Invalid phone number format. Please try again")
        return
    
    email = input(f"Enter email address ({contacts[unique_identifier]['Email']}): ")
    #check email format
    if email and not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        print("Invalid email address format. Please try again")
        return
    
    address = input(f"Enter address ({contacts[unique_identifier]['Address']})(Leave empty if you would like to make no changes): ")
    notes = input(f"Enter additional notes ({contacts[unique_identifier]['Notes']})(Leave empty if you would like to make no changes): ")

    #updates contacts dictironary w new values. old values are kept if no values are added
    contacts[unique_identifier] = {
        'Name': name if name else contacts[unique_identifier]['Name'],
        'Phone': phone if phone else contacts[unique_identifier]['Phone'],
        'Email': email if email else contacts[unique_identifier]['Email'],
        'Address': address if address else contacts[unique_identifier]['Address'],
        'Notes': notes if notes else contacts[unique_identifier]['Notes']
    }
    print("Contact updated successfully.")

#function to delete contacts
def delete_contact():
    unique_identifier = input("Enter unique identifier(phone number or email) of the contact to delete: ")
    if unique_identifier in contacts:
        del contacts[unique_identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

#function to seach for contacts
def search_contact():
    unique_identifier = input("Enter unique identifier(phone number or email) of the contact to search: ")
    if unique_identifier in contacts:
        for key, value in contacts[unique_identifier].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

#function to display all contacts
def display_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    
    for unique_identifier, details in contacts.items():
        print(f"Contact's Unique Identifier: {unique_identifier}")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("-") #separates contacts

#function to export contacts
def export_contacts():
    file_name = input("Enter the name of the file where you would like to export contacts: ")
    try:
        with open(file_name, 'w') as file:
            for identifier, details in contacts.items():
                file.write(f"{identifier}\n")
                for key, value in details.items():
                    file.write(f"{key}: {value}\n")
                file.write("-\n")
        print("Contacts exported successfully.")
    except IOError as e:
        print(f"An error occurred: {e}")

#function to import contacts
def import_contacts():
    file_name = input("Enter the name of time file where you would like to import contacts from: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read().strip().split("-")
            for contact in content:
                lines = contact.strip().split("\n")
                if not lines:
                    continue
                identifier = lines[0]
                details = {}
                for line in lines[1:]:
                    #split at : for example format Name: John 
                    if ": " in line:
                        key, value = line.split(": ", 1)
                        details[key] = value
                if identifier:
                    contacts[identifier] = details
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Contact Management System!")
    while True:
        print("""
        Menu:
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export contacts to a text file
        7. Import contacts from a text file
        8. Quit`
        """)
        choice = input("Please enter your choice (1-8): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
if __name__ == "__main__":
    main()

