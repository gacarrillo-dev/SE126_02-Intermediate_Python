# SE126.02
# Gabriel Carrillo
# 02/01/2023
# Lab 4b
#
# Variables Declared:
# ===================
# seats                 list of seats
# seatRow               user selected row 
# seatCol               user selected column
# answer                user answer to select more seats



import os

# === GLOBAL VARIABLES ====

seats = [
    [1, 'A', 'B', 'C', 'D'], 
    [2, 'A', 'B', 'C', 'D'],
    [3, 'A', 'B', 'C', 'D'],
    [4, 'A', 'B', 'C', 'D'],
    [5, 'A', 'B', 'C', 'D'],
    [6, 'A', 'B', 'C', 'D'],
    [7, 'A', 'B', 'C', 'D']
]
seatRow = 0
seatCol = 0
answer = 'y'


#======= FUNCTIONS ========

# clear screen
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac or linux
    else:
        os.system('clear')

# function to grab row from user
def get_seat_row():
    while True:
        seatRow = (int(input("Please enter seat row: ")) - 1)
        if seatRow < 0 or seatRow >= len(seats):
            print("Selection is out of range. Please try again.")
        else:
            break
    return seatRow

# function to grab column from user
def get_seat_col():
    while True:
        seatCol = input("Please enter seat letter: ")
        if seatCol.upper() == 'A':
            seatCol = int(1)
            break
        elif seatCol.upper() == 'B':
            seatCol = int(2)
            break
        elif seatCol.upper() == 'C':
            seatCol = int(3)
            break
        elif seatCol.upper() == 'D':
            seatCol = int(4)
            break
        else:
            print("Incorred letter entered. Try again.")
    return seatCol

# function to ask user for select more seats or end program
def more_seats():
    while True:
        answer = input("Would you like to select more seats? (y/n): ")
        if answer == 'y' or answer == 'n':
            break
        else:
            print("Invalid letter. Please try again")
    return answer

# fucntion to update the seats
def assign_seats(seatRow, seatCol):
    if seats[seatRow][seatCol] == 'X':
        print("\nSeat is already taken!")
    else:
        print("Updating seats ...")
        seats[seatRow][seatCol] = 'X'


# create function to print out seats
def print_seats(seats):
    for r in seats:
        for c in r:
            print(c, end = " ".ljust(3))
        print()     
    print('\n')     

#======== END OF FUNCTIONS ========



#==== MAIN PROGRAM =====

while True:
    clear()
    print_seats(seats)

    seatRow = get_seat_row()
    seatCol = get_seat_col()

    assign_seats(seatRow, seatCol)

    print("\nSeats have been update see below ... \n")
    print_seats(seats)

    answer = more_seats()
    if answer == 'n':
        print("Exiting...")
        break
    


