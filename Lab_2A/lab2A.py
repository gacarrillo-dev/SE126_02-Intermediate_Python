"""
SE126.02
Gabriel Carrillo
01/21/2023
Lab 2A

Variables Declared:
    overageRooms        List of rooms that have an excess of attendees
    numOverRooms        Number of rooms that have an overage
    numRecords          Number of records processed from the csv file
    room                Room name from csv file
    capacity            Number of capacity from csv file
    attendees           Number of attendees from csv file
    overage             Calculated overage of attendees from each room
"""

import csv

overageRooms = []
numOverRooms = 0
numRecords = 0

# function to calculate overage of attendees from each room
def calc_overage(overageRooms):
    for room in overageRooms:
        overage = int(room[2]) - int(room[1])
        room.append(overage)

# open csv file and parse the records from the csv file
with open (r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_2A\lab2a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        room = row[0]
        capacity = int(row[1])
        attendees = int(row[2])

        # if the attendees is greater than capacity add room to the Overage Room list
        if (attendees > capacity):
            overageRooms.append(row)
            numOverRooms += 1
    
        numRecords += 1

# run the calculate overage function
calc_overage(overageRooms)
     
# print the infomation with left-justify to align data correctly
print("Room".ljust(20) + "Capacity".ljust(15) + "Attendees".ljust(15) + "Overage")
for rooms in overageRooms:
    print(f"{rooms[0]}".ljust(20) + f"{rooms[1]}".ljust(15) + f"{rooms[2]}".ljust(15) + f"{rooms[3]}")


print(f"\nProcessed {numRecords} records.")
print(f"There are {numOverRooms} rooms over the limit.")
input("\nPress any key to continue ...")
