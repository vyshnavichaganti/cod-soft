def display_menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone to search: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if search_term in name.lower() or search_term in info['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave field blank to keep current value.")
        phone = input(f"Enter new phone (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
        address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        print(f"Contact '{name}' updated.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
