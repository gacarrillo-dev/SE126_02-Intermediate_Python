# Gabriel Carrillo
# SE 126.02
# LAB 6A
# 2/18/2023
#
# Variables Declared
# 
# firstName                 list of first names
# lastName                  list of last names
# phoneNumber               list of phone numbers
# email                     list of email addresses
# department                list of department names
# position                  list of position names

import csv

firstName = []
lastName = []
phoneNumber = []
email = []
department = []
position = []

#==== FUNCTIONS ====

# define function to get the last name from user
def get_name():
    name = input("Enter name to search: ")
    return name

# define function to do a binary search of last name list
def binary_search(searchName):
    min = 0
    max = len(lastName) - 1

    guess = int((min + max)/2)

    while(searchName != lastName[guess] and min <= max):
        if (searchName < lastName[guess]):
            max = guess -1
        else:
            min = guess + 1

        guess = int((min + max)/2)

    if (searchName == lastName[guess]):
        print("Name is found.")
        print(firstName[guess], end=" ")
        print(lastName[guess], end=" ")
        print(phoneNumber[guess], end=" ")
        print(email[guess], end=" ")
        print(department[guess], end=" ")
        print(position[guess])

    else:
	    print("Name is not found.")


#==== MAIN PROGRAM ====
with open (r'C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_6a\Lab6a-2.csv') as csvfile:
    employee_file = csv.reader(csvfile)

    # store employee data into lists
    for row in employee_file:
        firstName.append(row[0])
        lastName.append(row[1])
        phoneNumber.append(row[2])
        email.append(row[3])
        department.append(row[4])
        position.append(row[5])

searchName = get_name()
binary_search(searchName)
