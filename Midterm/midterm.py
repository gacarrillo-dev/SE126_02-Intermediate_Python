# SE126.02
# Gabriel Carrillo
# 02/07/2023
# MidTerm
#
# Variables Declared:
# ===================
# playerName            list of player names
# playerRace            list of player races
# playerChar            list of player character names  
# numHits               list of player hits
# greaterThan           number of hits greater than 40
# total                 total sum of hits
# average               average number of hits
# length                length of list


import csv

playerName = []
playerRace = []
playerChar = []
numHits = []

#=== FUNCTIONS ====

# function to search hits greater than 40
def greater_than():
    greaterThan = 0
    for hit in numHits:
       if hit > 40:
           greaterThan += 1
    return greaterThan

# function to calculate average of hits
def calc_average():
    total = 0
    average = 0
    for hit in numHits:
        total += hit
    average = total / len(numHits)
    return average

#==== MAIN PROGRAM ======

# open csv file and parse the records from the csv file
with open (r"C:\Users\g.carrillo\Desktop\Git Repo\SE126_02-Intermediate_Python\Midterm\Midterm.csv") as csvfile:
    file = csv.reader(csvfile)
    # add each row from file to a each list of records
    for row in file:
        playerName.append(row[0])
        playerRace.append(row[1])
        playerChar.append(row[2])
        numHits.append(int(row[3]))

# print header 
print("Player".ljust(10) + "Race".ljust(12) + "Character".ljust(11) + "Hits")

length = len(playerName)        

# print each player's information
for row in range(0, length):
    print(f"{playerName[row]}".ljust(9), end=" ")
    print(f"{playerRace[row]}".ljust(11), end=" ")
    print(f"{playerChar[row]}".ljust(11), end=" ")
    print(numHits[row], end = "\n")

# print hits greather than 40
print(f"\nNumber of players with 40 or more hits: {greater_than()}")

# print average of hits with 2 decimal places
print(f"The average number of hits: {calc_average(): .2f}")

input("\nPress any key to continue . . .")
        