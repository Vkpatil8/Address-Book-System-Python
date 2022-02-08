"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 08-02-2022 11:40:00
@Title : solve use case 2
"""

print("welcome in Address Book")


class Contact:
    contactlist = {}

    def __init__(self):
        """
        desc: Add contact details using console
        """
        self.firstname = input("Enter first name: ")
        self.lastname = input("Enter last name: ")
        self.address = input("Enter address: ")
        self.city = input("Enter city: ")
        self.state = input("Enter state: ")
        self.zipcode = input("Enter zipcode: ")
        self.phonenumber = input("Enter phone number: ")
        self.email = input("Enter email: ")
        self.addcontact()

    def addcontact(self):
        Contact.contactlist[self.firstname] = {"1": self.firstname, "2": self.lastname,
                                               "3": self.address, "4": self.city, "5": self.state,
                                               "6": self.zipcode, "7": self.phonenumber,
                                               "8": self.email}


class EditContact:

    def __init__(self, name):
        self.name = name
        self.editcontact(name)

    def editcontact(self, name):
        a = Contact.contactlist[name]
        print(a)
        while True:
            changeoption = int(input("Select where u want to change \n1:firstname\n2:lastname\n3:address\n4:city\n5"
                                     ":state\n6:zipcode\n7:phonenumber\n8:email\n9:exit\n"))
            if changeoption == 9:
                break
            value = input("Enter new: ")
            Contact.contactlist[name]["{}".format(changeoption)] = value


class ShowContact:
    def __init__(self, name):
        self.name = name
        self.showdetails(name)

    def showdetails(self, name):
        print(Contact.contactlist[name])
