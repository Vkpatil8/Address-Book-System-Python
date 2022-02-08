"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 08-02-2022 22:00:00
@Title : solve use case 5
"""

from address_book_main import Contact, EditContact, ShowContact, DeleteContact


class ShowMenu:
    """
        desc: Show mein menu
    """
    while True:
        option = int(input("1. Create Contact\n2. Edit Contact\n3. Show Details \n4. Delete\n5. Exit\n"))
        if option == 1:
            Contact()
        elif option == 2:
            contactname = input("Enter contact name\n")
            EditContact(contactname)
        elif option == 3:
            contactname = input("Enter contact name\n")
            ShowContact(contactname)
        elif option == 4:
            contactname = input("Enter contact name\n")
            DeleteContact(contactname)
        else:
            break


if __name__ == '__main__':
    ShowMenu()
