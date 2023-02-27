# Gabriel Carrillo
# SE 126
# Lab #7

# Variables Declared:
# fName                 list of first names
# lName                 list of last names
# department            list of departments
# position              list of positions
# salary                list of salaries
# average               average salaries for MIS dept
# payRaise              total company 5% raise
# length                length of list

import csv

fName = []
lName = []
department = []
position = []
salary = []

# define swap function, swaps the order of data in list
def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp

# define sort function, sorts each list by the first list in the argument
def sort(list1, list2, list3, list4, list5):
    length = len(list1)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (list1[j] > list1[j + 1]):

                swap(list1, j)
                swap(list2, j)
                swap(list3, j)
                swap(list4, j)
                swap(list5, j)

# define average function, calculates the average salaries of MIS dept
def average(department, salary):
    length = len(department)
    total = 0
    counter = 0
    average = 0
    for i in range (0, length):
        if department[i] == "MIS":
            total += salary[i]
            counter += 1
    average = total / counter
    return average

# define check_raise function, checks the cost of 5% raise for all employees
def check_raise(salary):
    total = 0
    payRaise = 0
    for i in salary:
        total += i
    payRaise = total * .05  
    return payRaise  


#==== MAIN PROGRAM ====

with open (r"C:\Users\g.carrillo\Desktop\Git Repo\SE126_02-Intermediate_Python\Lab7\Lab7.csv") as csvfile:
    file = csv.reader(csvfile)
    # read rows into list
    for row in file:
        fName.append(row[0])
        lName.append(row[1])
        department.append(row[2])
        position.append(row[3])
        salary.append(int(row[4]))

length = len(fName)

# for i in range (0, length):
#     print(fName[i].ljust(12), end= " ")
#     print(lName[i].ljust(10), end= " ")
#     print(department[i].ljust(15), end= " ")
#     print(position[i].ljust(13), end= " ")
#     print(salary[i])

# call sort function, sort by salary from lowest to highest
sort(salary, lName, department, fName, position)

# print ten highest salaries
print('\n\nTen Highest Salaries:')
for i in range(-1, -11, -1):
    print(f"{salary[i]}".ljust(7), end="")
    print(f"{lName[i]}".ljust(10), end="")
    print(f"{department[i]}".ljust(10))


# print ten lowest salaries
print('\n\nTen Lowest Salaries:')
for i in range(0, 10):
    print(f"{salary[i]}".ljust(7), end="")
    print(f"{lName[i]}".ljust(10), end="")
    print(f"{department[i]}".ljust(10))


# call average function, calculate average salary for MIS dept
average = average(department, salary)
print(f"\nAverage salary for MIS Department: ${average: .2f}")

# call check_raise function, calculates 5% raise for all employees
payRaise = check_raise(salary)
print(f"Total cost for 5% raise: ${payRaise: .2f}")

# call sort function, sort by departments
sort(department, lName, fName, position, salary)

# print the first 5 records
print('\n\nFirst 5 sorted by department:')
for i in range (0, 5):
    print(fName[i].ljust(12), end= " ")
    print(lName[i].ljust(10), end= " ")
    print(department[i].ljust(15), end= " ")
    print(position[i].ljust(13), end= " ")
    print(salary[i])

# print the last 5 records
print('\n\nLast 5 sorted by department:')
for i in range (-1, -6, -1):
    print(fName[i].ljust(12), end= " ")
    print(lName[i].ljust(10), end= " ")
    print(department[i].ljust(15), end= " ")
    print(position[i].ljust(13), end= " ")
    print(salary[i])

