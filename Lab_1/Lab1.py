"""
SE126.02
Gabriel Carrillo
01/11/2023
Lab 1

Variables Declared:
capacity            the capacity of the room
attendees           number of people attending the conference
roomCapacity        the capacity of the room
roomAttendees       number of people attending the conference
overage             overage of attendees
vacant              number of space available for conference
answer              yes or no answer from user to check more rooms
checkAnswer         answer of user set to lowercase

"""

# define function to get capactity of the room
def capacity():
    capacity = int(input("What is the capacity of the room? "))
    return capacity

# define function to get the number of attendees
def attendees():
    attendees = int(input("How many people want to attend the event? "))
    return attendees

# define function to determine if conference can be held or not
# then calculate availability or overage
def register(capacity, attendees):
    if attendees > capacity:
        overage = attendees - capacity
        print(f"The conference cannot be held due to fire regulations. Please remove {overage} people.")
    else:
        vacant = capacity - attendees
        print(f"The conference can be held. {vacant} more people can attend.")

# define function to determine if user wants to check more rooms
def more_rooms():
    while True:
        answer = input("Do you want to check anymore rooms (y/n)? ")
        checkAnswer = answer.lower()
        if checkAnswer == 'y':
            break
        elif checkAnswer == 'n':
            exit()

# define fucntion to run the program
def run():
    while True:
        roomCapacity = capacity()
        roomAttendees = attendees()
        register(roomCapacity, roomAttendees)
        more_rooms()

# if program is run and not imported
if __name__ == "__main__":
    run()
