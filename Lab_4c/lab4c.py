# SE126.02
# Gabriel Carrillo
# 02/10/2023
# Lab 4c
#
# Variables Declared:
# ===================
# firstName                 list of first names
# lastName                  list of last names
# phoneNumber               list of phone numbers
# email                     list of email addresses
# department                list of departments 
# position                  list of positions
# index                     index of the searched name
# numEmployees              number of employees in the company

import csv

firstName = []
lastName = []
phoneNumber = []
email = []
department = []
position = []
index = -1
numEmployees = 0

#===== FUNCTIONS =======

# function to get the search name from user
def get_name():
    name = input("Enter name to search: ")
    return name

# function to search the list of Last Names
def search_lastName(name):
    length = len(lastName)
   

#==== MAIN PROGRAM ======

# open csv file and parse the records from the csv file
with open (r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_4c\Lab4c.csv") as csvfile:
    file = csv.reader(csvfile)

    # add each row from file to a each list of records
    for row in file:
        firstName.append(row[0])
        lastName.append(row[1])
        phoneNumber.append(row[2])
        email.append(row[3])
        department.append(row[4])
        position.append(row[5])
        numEmployees += 1
        

# length of the list
length = len(lastName)

# print("First".ljust(12) + "Last".ljust(11) + "Phone".ljust(14) + "Email".ljust(28) + "Department".ljust(16) + "Position")
# # print results
# for row in range(0, length):
#     print(f"{firstName[row]}".ljust(12) + f"{lastName[row]}".ljust(11) + f"{phoneNumber[row]}".ljust(14) + f"{email[row]}".ljust(28) + f"{department[row]}".ljust(16) + f"{position[row]}")

# print('\n')


print(f"There are {numEmployees} employees working for the company.\n")
searchName = get_name()

# Sequential search for the last name
for pos in range(0, length):
    if (searchName == lastName[pos]):
        index = pos
        break

# if not found        
if index == -1:
    print('\nName not found!')

# else name found
# print employee information    
else:
    print("\nName found, see information below.\n")
    print(f"{firstName[index]}".ljust(12) + f"{lastName[index]}".ljust(11) + f"{phoneNumber[index]}".ljust(14) + f"{email[index]}".ljust(28) + f"{department[index]}".ljust(16) + f"{position[index]}")

