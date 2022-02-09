"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 09-02-2022 14:30:00
@Title : solve use case 11
"""


class Contact:
    contactlist = {}

    def __init__(self):
        """
        desc: Add contact details using console
        """
        self.firstname = input("Enter first name: ")
        if self.firstname not in Contact.contactlist.keys():
            self.lastname = input("Enter last name: ")
            self.address = input("Enter address: ")
            self.city = input("Enter city: ")
            self.state = input("Enter state: ")
            self.zipcode = input("Enter zipcode: ")
            self.phonenumber = input("Enter phone number: ")
            self.email = input("Enter email: ")
            self.addcontact()
        else:
            print("Already exist\n")

    def __eq__(self, other):
        if Contact.contactlist[self.firstname] == Contact.contactlist[other.firstname]:
            return False
        return True

    def addcontact(self):
        """
        desc: Add object in dictionary
        """
        Contact.contactlist[self.firstname] = {"1": self.firstname, "2": self.lastname,
                                               "3": self.address, "4": self.city, "5": self.state,
                                               "6": self.zipcode, "7": self.phonenumber,
                                               "8": self.email}


class EditContact:

    def __init__(self, name):
        self.name = name
        self.editcontact(name)

    def editcontact(self, name):
        """
        desc: Edit existing contact
        """
        if name in Contact.contactlist.keys():
            a = Contact.contactlist[name]
            print(a)
            while True:
                changeoption = int(input("Select where u want to change \n1:firstname\n2:lastname\n3:address\n4:city\n5"
                                         ":state\n6:zipcode\n7:phonenumber\n8:email\n9:exit\n"))
                if changeoption == 9:
                    break
                value = input("Enter new: ")
                Contact.contactlist[name]["{}".format(changeoption)] = value
        else:
            print("Not exist\n")


class ShowContact:
    def __init__(self, name):
        self.name = name
        self.showdetails(name)

    def showdetails(self, name):
        """
        desc: show particular contact details
        """
        if name in Contact.contactlist.keys():
            print(Contact.contactlist[name])
        else:
            print("Not exist\n")


class DeleteContact:
    def __init__(self, name):
        self.name = name
        self.deletecontact(name)

    def deletecontact(self, name):
        """
        desc: Delete particular contact from book
        """
        if name in Contact.contactlist.keys():
            del Contact.contactlist[name]
            print("contact details of {} is delete successfully\n".format(name))

        else:
            print("Not exist\n")


class SearchContact:
    def __init__(self, option, name):
        self.name = name
        self.option = option
        self.options(option, name)

    def options(self, option, name):
        if option == 1:
            self.searchbycityname(name)
        elif option == 2:
            self.searchbystatename(name)
        else:
            print("\tChoose Correct Option\n")

    def searchbycityname(self, cityname):
        """
        desc: search particular contact from book using city name
        """
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['4'] == cityname:
                print("\tContact details is {}\n".format(Contact.contactlist[name]))
            else:
                print("\tNot available\n")

    def searchbystatename(self, statename):
        """
        desc: search particular contact from book using city name
        """
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['5'] == statename:
                print("\tContact details is {}\n".format(Contact.contactlist[name]))
            else:
                print("\tNot available\n")


class SearchAndCountContact:
    def __init__(self, option, name):
        self.name = name
        self.option = option
        self.options(option, name)

    def options(self, option, name):
        if option == 1:
            self.searchbycityname(name)
        elif option == 2:
            self.searchbystatename(name)
        else:
            print("\tChoose Correct Option\n")

    def searchbycityname(self, cityname):
        """
        desc: count particular contact from book using city name
        """
        count = 0
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['4'] == cityname:
                count = count + 1
            else:
                print("\tNot available")
        print("\tcount of contacts in contact book is {}\n".format(count))

    def searchbystatename(self, statename):
        """
        desc: count particular contact from book using city name
        """
        count = 0
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['5'] == statename:
                count = count + 1
            else:
                print("\tNot available")
        print("\tcount of contacts in contact book is {}\n".format(count))


class Sort:
    def __init__(self):
        self.sortbyname()

    def sortbyname(self):
        list1 = sorted(Contact.contactlist.items())
        print(list1)
