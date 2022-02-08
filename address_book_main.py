"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 08-02-2022 11:40:00
@Title : solve use case 2
"""

print("welcome in Address Book")


class Contact:

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


if __name__ == '__main__':
    Contact()
