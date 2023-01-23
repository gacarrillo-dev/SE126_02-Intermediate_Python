# SE126.02
# Gabriel Carrillo
# 01/23/2023
# Lab 3
#
# Variables Declared:
# ===================
#   computers               List of computers, data imported from csv file
#   numComputers            Number of computers processed in the csv file
#   oldComputers            List of computers older than 2 years
#   numDesktops             Number of desktops in the oldComputer list
#   numLaptops              Number of laptops in the oldComputer list
#   laptopCost              Total cost for laptop replacement
#   desktopCost             Total cost for desktop replacement




import csv

computers = []
oldComputers = []
numDesktops = 0
numLaptops = 0
numComputers = 0
laptopCost = 0
desktopCost = 0

# function to update description of type from initals to words
def update_type(computers):
    for data in computers:
        if (data[0] == 'D'):
            data[0] = 'Desktop'
        elif (data[0] == 'L'):
            data[0] = 'Laptop'

# function to update the description of brand from initals to words
def update_brand(computers):
    for data in computers:
        if (data[1] == 'DL'):
            data[1] = 'Dell'
        elif (data[1] == 'GW'):
            data[1] = 'Gateway'

# function to check if row has 1 disk
# if row has 1 disk put a "" placeholder for second disk in the index location 
def update_secondDisk(computers):
    for data in computers:
        if (int(data[5]) == 1):
            data.insert(6, '')

# function to check if computers are more than 2 years old
def get_old_computers(computers):
    for data in computers:
        if (23 - int(data[8])) > 2:
            oldComputers.append(data)          

#============================================================================
# END OF FUNCTIONS


# open csv file and parse the records from the csv file
with open (r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_3\lab3.csv") as csvfile:
    file = csv.reader(csvfile)
    # add each row from file to a list called computers
    for row in file:
       computers.append(row)
       numComputers += 1

# run the update_type function
update_type(computers)

# run the update_brand function
update_brand(computers)

# run the update_secondDisk function
update_secondDisk(computers)

# run the get old computers function
get_old_computers(computers)

# for loop to calculate the cost of replacement
for data in oldComputers:
    if (data[0] == 'Desktop'):
        desktopCost += 2000
        numDesktops += 1
    elif (data[0] == 'Laptop'):
        laptopCost += 1500
        numLaptops += 1

# print the infomation with left-justify to align data correctly
print("Type".ljust(9) + "Brand".ljust(8) + "CPU".ljust(5) + "RAM".ljust(5) + "1st Disk".ljust(10) + "No HDD".ljust(8) + "2nd Disk".ljust(10) + "OS".ljust(4) + "YR")
for data in oldComputers:
    print(f"{data[0]}".ljust(9) + f"{data[1]}".ljust(8) + f"{data[2]}".ljust(5) + f"{data[3]}".ljust(5) +f"{data[4]}".ljust(10) + f"{data[5]}".ljust(8) + f"{data[6]}".ljust(10) + f"{data[7]}".ljust(4) + f"{data[8]}")

print(f"\n{numDesktops} desktops were processed. Total cost for replacement: ${desktopCost}")
print(f"{numLaptops} laptops were processed. Total cost for replacement: ${laptopCost}")
input("\nPress any key to continue ...")