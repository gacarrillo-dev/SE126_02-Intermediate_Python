"""
SE126.02
Gabriel Carrillo
01/21/2023
Lab 2A

Variables Declared:
    computers               List of computers, data imported from csv file
    numComputers            Number of computers processed in the csv file


"""


import csv

computers = []
numComputers = 0

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
# if row has 1 disk put a "" placeholder for second disk in index 
def update_secondDisk(computers):
    for data in computers:
        if (int(data[5]) == 1):
            data.insert(6, '')



# open csv file and parse the records from the csv file
with open (r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_2B\lab2b.csv") as csvfile:
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



# print the infomation with left-justify to align data correctly
print("Type".ljust(9) + "Brand".ljust(8) + "CPU".ljust(5) + "RAM".ljust(5) + "1st Disk".ljust(10) + "No HDD".ljust(8) + "2nd Disk".ljust(10) + "OS".ljust(4) + "YR")
for data in computers:
    print(f"{data[0]}".ljust(9) + f"{data[1]}".ljust(8) + f"{data[2]}".ljust(5) + f"{data[3]}".ljust(5) +f"{data[4]}".ljust(10) + f"{data[5]}".ljust(8) + f"{data[6]}".ljust(10) + f"{data[7]}".ljust(4) + f"{data[8]}")

print(f"\n{numComputers} computers were processed from the csv file.")
input("Press any key to exit ...")