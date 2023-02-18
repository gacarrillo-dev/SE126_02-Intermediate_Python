# Gabriel Carrillo
# SE 126.02
# 02/17/2023
# Lab 5b
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
changed = 0

#==== FUNCTIONS =====

# search for email addresses in the MIS department
def search_email():
    length = len(department)
    for pos in range(0, length):
        if (department[pos] == "MIS"):
            print (email[pos])
    

# change TLD from MIS department email addresses
def change_email():
    global changed
    length = len(department)
    for pos in range(0, length):
        if (department[pos] == "MIS"):
            email[pos] = email[pos].replace(".com", ".net")
            changed += 1
            

#==== MAIN PROGRAM =====

# open and read file
with open(r'C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_5b\Lab5B.csv') as csvfile:
    employee_file = csv.reader(csvfile)

    # add each data into list
    for row in employee_file:
        firstName.append(row[0])
        lastName.append(row[1])
        phoneNumber.append(row[2])
        email.append(row[3])
        department.append(row[4])
        position.append(row[5])


print("Emails from the MIS department:")
search_email()
change_email()
print ('\nEmails TLD changed:')
search_email()
print(f"\nNumber of emails changed: {changed}")
input("Press any key to continue ...")
    



