class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")
    
    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"Contact {index}:")
                print(contact)
                print("--------------------")
    
    def search_contact(self, keyword):
        found = False
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print("No matching contacts found.")
    
    def update_contact(self, name, phone_number):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = phone_number
                print("Contact updated successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")
    
    def delete_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")
    
    def menu(self):
        while True:
            print("\n--- Contact Book Menu ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                new_contact = Contact(name, phone_number, email, address)
                self.add_contact(new_contact)
            
            elif choice == '2':
                self.view_contacts()
            
            elif choice == '3':
                keyword = input("Enter name or phone number to search: ")
                self.search_contact(keyword)
            
            elif choice == '4':
                name = input("Enter name of contact to update: ")
                phone_number = input("Enter new phone number: ")
                self.update_contact(name, phone_number)
            
            elif choice == '5':
                name = input("Enter name of contact to delete: ")
                self.delete_contact(name)
            
            elif choice == '6':
                print("Thank you for using the Contact Book.")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
