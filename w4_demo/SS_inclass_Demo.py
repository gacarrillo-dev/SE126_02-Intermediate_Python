import csv

fName = []
lName = []
age = []

with open(r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\w4_demo\example.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        fName.append(row[0])
        lName.append(row[1])
        age.append(row[2])
     
#====== Sequential Search Using a for loop ==============
flag = -1
lookUp = input("Eneter person's last name: ")
for i in range(0, len(age)):
    if (lookUp.lower() == lName[i].lower()):
        flag = i
        print(flag, "  ", i)

if (flag == -1):
    print("Record not found!!!")
else:
    print(fName[flag], " ", lName[flag], age[flag])



#====== Sequential Search Using a while loop ==============

i = 0
lookUp = input("Eneter person's last name: ")

while (i < len(lName) and lookUp.lower() != lName[i].lower()):
    i = i + 1

if(i >= len(lName)):
    print("Record not found!!!")
else:
    print(fName[i], " ", lName[i], age[i])

