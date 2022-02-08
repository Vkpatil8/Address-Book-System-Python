"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 08-02-2022 22:00:00
@Title : solve use case 6
"""

print("welcome in Address Book")


class Contact:
    contactlist = {}

    def __init__(self):
        """
        desc: Add contact details using console
        """
        self.firstname = input("Enter first name: ")
        if self.firstname in Contact.contactlist.keys():
            self.lastname = input("Enter last name: ")
            self.address = input("Enter address: ")
            self.city = input("Enter city: ")
            self.state = input("Enter state: ")
            self.zipcode = input("Enter zipcode: ")
            self.phonenumber = input("Enter phone number: ")
            self.email = input("Enter email: ")
            self.addcontact()
        else:
            print("Already exist")

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
            print("Not exist")


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
            print("Not exist")



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
            print("contact details of {} is delete successfully".format(name))

        else:
            print("Not exist")

