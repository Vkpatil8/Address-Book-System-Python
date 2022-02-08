from address_book_main import Contact, EditContact, ShowContact


def contact():
    Contact()


def editcontact():
    contactname = input("Enter contact name\n")
    EditContact(contactname)


def close():
    pass


def showcontact():
    contactname = input("Enter contact name\n")
    ShowContact(contactname)

class ShowMenu:
    @classmethod
    def show_main_menu(cls, option):
        if option == 1:
            contact()
        elif option == 2:
            editcontact()
        elif option == 3:
            showcontact()
        else:
            close()


if __name__ == '__main__':
    while True:
        option = int(input("1. Create Contact\n2. Edit Contact\n3. Show Details \n4. Exit\n"))
        ShowMenu.show_main_menu(option)
