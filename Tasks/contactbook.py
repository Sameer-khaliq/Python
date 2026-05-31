# Custom Exception for deletion as requested
class StudentNotFoundError(Exception):
    pass

#_______FILE OPERATIONS___________

def save_contacts(contacts, filepath="contacts.txt"):
    with open(filepath, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

def load_contacts(filepath="contacts.txt"):
    contacts = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Check for empty lines
                    name, phone, email = line.split(",")
                    contacts[name] = {"phone": phone, "email": email}
    except FileNotFoundError:
        pass    # File exist nahi karti — empty dict return hogi
    return contacts


#_______CONTACT OPERATIONS___________

# 1. Add contact
def add_contact(contacts):
    name = input('Enter name: ').strip()
    if not name:
        print("Name cannot be empty!")
        return

    # Duplicate names check
    if name in contacts:
        print("Contact already exists! Use update option to change details.")
        return

    phone = input('Enter phone number: ').strip()
    email = input('Enter email: ').strip()

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

# 2. View all contacts
def view_all_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return
    
    print("\n--- ALL CONTACTS ---")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")

# 3. Search contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nFound -> Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")

# 4. Update contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact does not exist.")
        return
    
    print(f"Updating details for {name} (Leave blank to keep current value):")
    current_phone = contacts[name]['phone']
    current_email = contacts[name]['email']
    
    new_phone = input(f"Enter new phone [{current_phone}]: ").strip()
    new_email = input(f"Enter new email [{current_email}]: ").strip()
    
    # Agar user blank choray toh purana data hi rahe
    if new_phone:
        contacts[name]['phone'] = new_phone
    if new_email:
        contacts[name]['email'] = new_email
        
    save_contacts(contacts)
    print("Contact updated successfully.")

# 5. Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    try:
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact deleted successfully.")
        else:
            raise StudentNotFoundError
    except StudentNotFoundError:
        print("Error: Contact not found. Delete operation failed.")




def main():
    # Program start par file se data load karega
    contacts = load_contacts()
    
    while True:
        print("\n=== Contact Book ===")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_all_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()