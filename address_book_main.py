"""
@Author: Vishal Patil
@Date: 08-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 08-02-2022 11:20:00
@Title : solve use case 1
"""

print("welcome in Address Book")


class Contact:

    def __init__(self, firstname, lastnames, address, city, state, zipcode, phonenumber, email):
        self.firstname = firstname
        self.lastnames = lastnames
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phonenumber = phonenumber
        self.email = email


if __name__ == '__main__':
    Contact("vishal", "Patil", "Limb", "Limb", "Maharashtra", "416312", "8329235763", "Vk@gmail.com")
