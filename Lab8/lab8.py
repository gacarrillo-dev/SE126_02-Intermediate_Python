# Gabriel Carrillo
# SE126
# 3/2/2023
# Lab 8

# Variables Declared



# define the seating chart
seating_chart = [['#' for j in range(30)] for i in range(15)]

# define ticket prices
ROW_PRICES = [200.0, 200.0, 200.0, 200.0, 200.0, 175.0, 175.0, 175.0, 175.0, 175.0, 150.0, 150.0, 150.0, 150.0, 150.0]

# define function to print seating chart
def print_seating_chart():
    row_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234'
    print('    ', end='')
    for i in range(30):
        print(str(i+1).rjust(2), end=' ')
    print()
    for i in range(15):
        print(str(i+1).rjust(2), end='  ')
        for j in range(30):
            print(seating_chart[i][j], end=' ')
        print(row_labels[i*2:i*2+2])

# define function to get the number of available seats
def get_num_available_seats():
    return sum(row.count('#') for row in seating_chart)

# define function to get the number of available seats in each row
def get_num_available_seats_per_row():
    return [row.count('#') for row in seating_chart]

# define function to get the number of seats sold
def get_num_seats_sold():
    return sum(row.count('*') for row in seating_chart)

# define function to get the total ticket sales
def get_total_ticket_sales():
    return sum([ROW_PRICES[i] * row.count('*') for i, row in enumerate(seating_chart)])

# display the seating chart
print_seating_chart()

# loop until user chooses to quit
while True:
    # display options
    print()
    print('Options:')
    print('1. Purchase a ticket')
    print('2. View total ticket sales')
    print('3. View number of seats sold and available seats')
    print('4. Quit')
    choice = input('Enter your choice: ')
    
    if choice == '1':
        # get row and seat numbers from user
        row_num = int(input('Enter row number: '))
        seat_num = int(input('Enter seat number: '))
        
        # check if seat is available
        if seating_chart[row_num-1][seat_num-1] == '#':
            # mark seat as sold
            seating_chart[row_num-1][seat_num-1] = '*'
            
            # calculate ticket price
            ticket_price = ROW_PRICES[row_num-1]
            
            # display ticket price and seating chart
            print('Ticket price: $%.2f' % ticket_price)
            print_seating_chart()
        else:
            print('Seat not available.')
    elif choice == '2':
        # display total ticket sales
        total_sales = get_total_ticket_sales()
        print('Total ticket sales: $%.2f' % total_sales)
    elif choice == '3':
        # display number of seats sold and available seats
        num_sold = get_num_seats_sold()
        num_available = get_num_available_seats()
        print('Number of seats sold: %d' % num_sold)
        print('Number of seats available: %d' % num_available)
        print('Number of seats available per row:', get_num_available_seats_per_row())
    elif choice == '4':
        # quit the program
        break
    else:
        print('Invalid choice.')
