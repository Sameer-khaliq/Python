# === Contact Book ===
# 1. Add contact
# 2. View all contacts
# 3. Search contact
# 4. Update contact
# 5. Delete contact
# 6. Exit
class StudentNotFoundError(Exception):
    pass
    # contacts dictionary of dictionaries
contacts = {
    "Sameer": {"phone": "03001234567", "email": "sameer@email.com"},
    "Ali": {"phone": "03009876543", "email": "ali@email.com"}
}

# File save karna:
def save_contacts(contacts, filepath="contacts.txt"):
    with open(filepath, 'w') as file:
        for name,info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")



    

# File load karna:
def load_contacts(filepath="contacts.txt"):
    # tumhara code

    contacts = {}
    try:
        with open(filepath,'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    name,phone,email = line.split(',')
                    contacts[name] = {'phone' : phone, 'email': email}
    except FileNotFoundError:
        print("File not found")
    return contacts

# Add contact:
def add_contact(contacts, name, phone, email):
    name = input("Enter name: ")
    if not name:
        print("name cannot be empty!!")
        return
    
    if name in contacts:
        print("Contact already exists!!")
        return
    phone = input("Enter phone no. : ")
    email = input("Enter the email: ")
    contacts[name] = {'phone':phone, 'email': email}
    save_contacts('contacts.txt')
    print(f"{name} added successfully as new contact")


# Search:
def search_contact(contacts, name):
    name = input("Enter name to search in contacts: ")
    if not name:
        print("Name cannot be empty!!")
        return
    if name in contacts:
        print("Contact found")
        print(f"{name},{name['phone']},{name['email']}")


# Delete:
def delete_contact(contacts, name):
    name = input("Enter name to delete: ")
    try:
        if name in contacts:
            del contacts[name]
            save_contacts('contacts.txt')
            print("Contact deleted successfully")
        else:
            raise StudentNotFoundError
    except(StudentNotFoundError):
        print("No person of this name")
    # StudentNotFoundError jaisi custom exception use karo
    # tumhara code

def update_contact(contacts):
    name = input("enter name to update: ")
    if not name:
        print("Name cannot be empty !!")
        return
    if name not in contacts:
        print("Name not in the contacts!!")
    current_phone = contacts['name']['phone']
    current_email = contacts['name']['phone']
    
    new_phone = input("Enter new phone no.[{current_phone}] : ").strip()
    new_email = input("Enter new email:[{current_email}] ").strip()
    
    if new_phone:
        contacts['name']['phone'] = new_phone
    if new_email:
        contacts['name']['email'] = new_email

    save_contacts('contacts.txt')
    print("Contacts updated successfully!!")


def view_all_contacts(contacts,filepath = 'contacts.txt'):
    if not contacts:
        print("Contact list is empty!!")
    else:
        with open(filepath, 'r') as file:
            for name,info in contacts.items():
                contact_list = file.read()
                print(contact_list)
view_all_contacts(contacts,'contacts.txt')
