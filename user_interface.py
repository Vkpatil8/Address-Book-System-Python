"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 09-02-2022 14:30:00
@Title : solve use case 11
"""
from address_book_main import Contact, EditContact, ShowContact, DeleteContact, SearchContact, SearchAndCountContact, \
    Sort


class ShowMenu:
    """
        desc: Show mein menu
    """
    while True:
        option = int(input("\n1. Create Contact\n2. Edit Contact\n3. Show Details \n4. Delete\n5. Search Contact by "
                           "city or state\n6. Count Contacts by city or state\n7. Sort by name\n8. Exit\n"))
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
        elif option == 5:
            searchoption = int(input("\t1: Search by city name\n\t2: Search by state name\n\t"))
            cityname = input("\tEnter name: ")
            SearchContact(searchoption, cityname)
        elif option == 6:
            searchoption = int(input("\t1: count by city name\n\t2: count by state name\n\t"))
            cityname = input("\tEnter name: ")
            SearchAndCountContact(searchoption, cityname)
        elif option == 7:
            Sort()
        else:
            break



