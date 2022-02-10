"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 09-02-2022 21:30:00
@Title : solve use case 14
"""

import csv
from collections import OrderedDict
from operator import getitem


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

    def addcontact(self):
        """
        desc: Add object in dictionary
        """
        Contact.contactlist[self.firstname] = {"firstname": self.firstname, "lastname": self.lastname,
                                               "address": self.address, "city": self.city, "state": self.state,
                                               "zipcode": self.zipcode, "phonenumber": self.phonenumber,
                                               "email": self.email}


class EditContact:

    def __init__(self, name):
        self.name = name
        self.editcontact(name)

    def editcontact(self, name):
        """
        desc: Edit existing contact
        :parameter name - assign name:
        """
        if name in Contact.contactlist.keys():
            a = Contact.contactlist[name]
            print(a)
            while True:
                changeoption = int(input("Select where u want to change \n1:firstname\n2:lastname\n3:address\n4:city\n5"
                                         ":state\n6:zipcode\n7:phonenumber\n8:email\n9:exit\n"))
                if changeoption == 1:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["firstname"] = value
                elif changeoption == 2:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["lastname"] = value
                elif changeoption == 3:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["address"] = value
                elif changeoption == 4:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["city"] = value
                elif changeoption == 5:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["state"] = value
                elif changeoption == 6:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["zipcode"] = value
                elif changeoption == 7:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["phonenumber"] = value
                elif changeoption == 8:
                    value = input("Enter new: ")
                    Contact.contactlist[name]["email"] = value
                else:
                    break
        else:
            print("Not exist\n")


class ShowContact:
    def __init__(self, name):
        self.name = name
        self.showdetails(name)

    def showdetails(self, name):
        """
        desc: show particular contact details
        :parameter name - assign name:
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
        :parameter name - assign book name:
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
        """
        desc: search particular contact from book using city name
        :parameter option: assign options to call methods
        :parameter name - assign name:
        """

        if option == 1:
            self.searchbycityname(name)
        elif option == 2:
            self.searchbystatename(name)
        else:
            print("\tChoose Correct Option\n")

    def searchbycityname(self, cityname):
        """
        desc: search particular contact from book using city name
        :parameter cityname: assign city name to search
        """
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['city'] == cityname:
                print("\tContact details is {}\n".format(Contact.contactlist[name]))
            else:
                print("\tNot available\n")

    def searchbystatename(self, statename):
        """
        desc: search particular contact from book using city name
        :parameter statename: assign state name
        """
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['state'] == statename:
                print("\tContact details is {}\n".format(Contact.contactlist[name]))
            else:
                print("\tNot available\n")


class SearchAndCountContact:
    def __init__(self, option, name):
        self.name = name
        self.option = option
        self.options(option, name)

    def options(self, option, name):
        """
        desc: search particular contact from book using city name
        :parameter option: assign options to call methods
        :parameter name - assign name:
        """
        if option == 1:
            self.searchbycityname(name)
        elif option == 2:
            self.searchbystatename(name)
        else:
            print("\tChoose Correct Option\n")

    def searchbycityname(self, cityname):
        """
        desc: count particular contact from book using city name
        :parameter cityname - assign cityname:
        """
        count = 0
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['city'] == cityname:
                count = count + 1
            else:
                print("\tNot available")
        print("\tcount of contacts in contact book is {}\n".format(count))

    def searchbystatename(self, statename):
        """
        desc: count particular contact from book using city name
        :parameter statename: assign state name
        """
        count = 0
        for name in Contact.contactlist.keys():
            if Contact.contactlist[name]['state'] == statename:
                count = count + 1
            else:
                print("\tNot available")
        print("\tcount of contacts in contact book is {}\n".format(count))


class Sort:
    def __init__(self, option):
        self.option = option
        self.options(option)

    def options(self, option):
        """
        desc: search particular contact from book using city name
        :parameter option: assign options to call methods
        """
        if option == 1:
            self.sortbyname()
        elif option == 2:
            self.sortbycity()
        elif option == 3:
            self.sortbystate()
        elif option == 4:
            self.sortbyzip()
        else:
            print("\tChoose Correct Option\n")

    def sortbyname(self):
        """
        desc: sort by name
        """
        list1 = sorted(Contact.contactlist.items())
        print(list1)

    def sortbycity(self):
        """
        desc: sort by city name
        """
        res = OrderedDict(sorted(Contact.contactlist.items(), key=lambda x: getitem(x[1], 'city')))
        print("The sorted dictionary by city name is : " + str(res))

    def sortbystate(self):
        """
        desc: sort by state name
        """
        res = OrderedDict(sorted(Contact.contactlist.items(), key=lambda x: getitem(x[1], 'state')))
        print("The sorted dictionary by state name is : " + str(res))

    def sortbyzip(self):
        """
        desc: sort by zip code
        """
        res = OrderedDict(sorted(Contact.contactlist.items(), key=lambda x: getitem(x[1], 'zip')))
        print("The sorted dictionary by zip code is : " + str(res))


class ReadAndWrite:
    def __init__(self, option):
        self.option = option
        self.options(option)

    def options(self, option):
        """
        desc: search particular contact from book using city name
        :parameter option: assign options to call methods
        """
        if option == 1:
            self.writefile()
        elif option == 2:
            self.readfile()
        else:
            print("\tChoose Correct Option\n")

    def writefile(self):
        """
        desc: Write all details in file
        """
        with open("addresbook.txt", 'w') as file:
            for key, value in Contact.contactlist.items():
                file.write("{} : {}\n".format(key, value))
            print("file write successfully")
        file.close()

    def readfile(self):
        """
        desc: read all details in file
        """
        file = open("addresbook.txt", "r")
        print(file.read())


class ReadAndWriteInCsv:
    def __init__(self, option):
        self.option = option
        self.options(option)

    def options(self, option):
        """
        desc: search particular contact from book using city name
        :parameter option: assign options to call methods
        """
        if option == 1:
            self.writefile()
        elif option == 2:
            self.readfile()
        else:
            print("\tChoose Correct Option\n")

    def writefile(self):
        """
        desc: Write all details in csv file
        """
        field_names = ["firstname", "lastname", "address", "city", "state", "zipcode", "phonenumber", "email"]
        with open("addresbook.csv", 'w') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(Contact.contactlist.values())
            print("file write successfully")
        file.close()

    def readfile(self):
        """
        desc: read all details in csv file
        """
        with open('addresbook.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)
