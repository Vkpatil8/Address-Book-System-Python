"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 10-02-2022 10:30:00
@Title : solve use case 15
"""

from address_book_main import Contact, EditContact, ShowContact, DeleteContact, SearchContact, SearchAndCountContact, \
    Sort, ReadAndWrite, ReadAndWriteInCsv, ReadAndWriteInJson


class ShowMenu:
    """
        desc: Show mein menu
    """
    while True:
        option = int(input("\n1. Create Contact\n2. Edit Contact\n3. Show Details \n4. Delete\n5. Search Contact by "
                           "city or state\n6. Count Contacts by city or state\n7. Sort\n8. Read & Write File\n9. Read "
                           "& Write Csv File\n10. Read & Write Json File\n11. Exit\n "))
        if option == 1:
            Contact()
        elif option == 2:
            contactname = input("Enter contact name\n")
            EditContact(contactname)
        elif option == 3:
            ShowContact()
        elif option == 4:
            contactname = input("Enter contact name\n")
            DeleteContact(contactname)
        elif option == 5:
            while True:
                searchoption = int(input("\t1: Search by city name\n\t2: Search by state name\n\t3: Exit\n\t"))
                if searchoption == 3:
                    break
                cityname = input("\tEnter name: ")
                SearchContact(searchoption, cityname)
        elif option == 6:
            while True:
                countoption = int(input("\t1: count by city name\n\t2: count by state name\n\t3: Exit\n\t"))
                if countoption == 3:
                    break
                cityname = input("\tEnter name: ")
                SearchAndCountContact(countoption, cityname)
        elif option == 7:
            while True:
                sortoption = int(input("\t1: sort by name\n\t2: sort by city name\n\t3: sort by state name\n\t4: sort "
                                       "by zip code\n\t5. Exit\n\t"))
                if sortoption == 5:
                    break
                Sort(sortoption)

        elif option == 8:
            while True:
                option = int(input("\t1: Write file\n\t2: Read file\n\t3: Exit\n\t"))
                if option == 3:
                    break
                ReadAndWrite(option)
        elif option == 9:
            while True:
                option = int(input("\t1: Write file\n\t2: Read file\n\t3: Exit\n\t"))
                if option == 3:
                    break
                ReadAndWriteInCsv(option)
        elif option == 10:
            while True:
                option = int(input("\t1: Write file\n\t2: Read file\n\t3: Exit\n\t"))
                if option == 3:
                    break
                ReadAndWriteInJson(option)
        elif option == 11:
            break
        else:
            print("Enter correct option")



