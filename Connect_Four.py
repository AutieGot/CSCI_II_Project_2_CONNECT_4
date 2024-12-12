# Program Name: Connect Four
# Author:       Austin Allen
# Date:         December 11, 2022
# Purpose:      Connect Four game created from structure of Battleship. A two-player
#               competitive game where the users attempt to create a straight, four long
#               string either horizontally or vertically.

# declare lists
x_axis = []
connect_board = []

# declare variables
first_turn = True
second_turn = True
winner = False

# create x_axis
for x in range(1, 8):
    x_axis.append(str(x))

# create connect_board list
for x in range(6):
    connect_board.append([" "] * 7)

# callable function to print list
def print_board():
    row = "| "
    # prints lists without "" or ,
    print ("  " + "   ".join(x_axis))
    for lst in connect_board:
        print ("+---+---+---+---+---+---+---+")
        print ("|   |   |   |   |   |   |   |")
        for spot in lst:
            row += spot + " | "
        print (row)
        print ("|   |   |   |   |   |   |   |")
        row = "| "
    print ("+---+---+---+---+---+---+---+")

# callable function to receive col input
def column():
    numeric = False
    while not numeric:
        # user can input numbers 1-7 which will be changed to 0-6
        col = int(input("Col: ")) - 1
        # make sure input is within parameters
        if 6 >= col >= 0 and connect_board[0][col] != "X" and connect_board[0][col] != "O":
            numeric = True
        elif col > 6 or col < 0:
            print ("That number was greater than 7 or less than 1.")
            print ("Please enter a number from 1 to 7.")
        else:
            print ("Input Error")
            print ("Please enter a number from 1 to 7.")
    return col

# input for first_player is "X"
def first_player():
    x = 5
    while x >= 0:
        if connect_board[x][col] != "X" and connect_board[x][col] != "O":
            connect_board[x][col] = "X"
            break
        x -= 1

# input for second_player is "O"
def second_player():
    x = 5
    while x >= 0:
        if connect_board[x][col] != "X" and connect_board[x][col] != "O":
            connect_board[x][col] = "O"
            break
        x -= 1

# check for winner negative diagonal
def winner_check_4(winner = False):
    x = 2
    y = 0
    for i in range(3):
        while x >= 0 and y <= 3:
            # reduces time by checking for blank space
            if connect_board == " ":
                y += 1
            # checks for four "X"s in a negative diagonal
            elif connect_board[x][y] == "X" and connect_board[x + 1][y + 1] == "X" and connect_board[x + 2][y + 2] == "X" and connect_board[x + 3][y + 3] == "X":
                print ("Player one wins!")
                winner = True
                break
            # checks for four "O"s in a positive diagonal
            elif connect_board[x][y] == "O" and connect_board[x + 1][y + 1] == "O" and connect_board[x + 2][y + 2] == "O" and connect_board[x + 3][y + 3] == "O":
                print ("Player two wins!")
                winner = True
                break
            else:
                # shifts to the right one
                y += 1
        if winner:
            break
        elif not winner:
            # resets to the left and up one
            x -= 1
            y = 0
    return winner

# check for winner positive diagonal
def winner_check_3(winner = False):
    x = 5
    y = 0
    for i in range(3):
        while x >= 3 >= y:
            # reduces time by checking for blank space
            if connect_board == " ":
                y += 1
            # checks for four "X"s in a positive diagonal
            elif connect_board[x][y] == "X" and connect_board[x - 1][y + 1] == "X" and connect_board[x - 2][y + 2] == "X" and connect_board[x - 3][y + 3] == "X":
                print ("Player one wins!")
                winner = True
                break
            # checks for four "O"s in a positive diagonal
            elif connect_board[x][y] == "O" and connect_board[x - 1][y + 1] == "O" and connect_board[x - 2][y + 2] == "O" and connect_board[x - 3][y + 3] == "O":
                print ("Player two wins!")
                winner = True
                break
            else:
                # shifts to the right one
                y += 1
        if winner:
            break
        elif not winner:
            # resets to the left and up one
            x -= 1
            y = 0
    if not winner:
        winner = winner_check_4(winner)
    return winner

# check for winner vertically
def winner_check_2(winner = False):
    x = 5
    y = 0
    for i in range(3):
        while x >= 3 and y <= 6:
            # reduces time by checking for blank space
            if connect_board == " ":
                y += 1
            # checks for four "X"s in a row vertically
            elif connect_board[x][y] == "X" and connect_board[x - 1][y] == "X" and connect_board[x - 2][y] == "X" and connect_board[x - 3][y] == "X":
                print ("Player one wins!")
                winner = True
                break
            # checks for four "O"s in a row vertically
            elif connect_board[x][y] == "O" and connect_board[x - 1][y] == "O" and connect_board[x - 2][y] == "O" and connect_board[x - 3][y] == "O":
                print ("Player two wins!")
                winner = True
                break
            else:
                # shifts to the right one
                y += 1
        if winner:
            break
        elif not winner:
            # resets to the left and up one
            x -= 1
            y = 0
    if not winner:
        winner = winner_check_3(winner)
    return winner

# check for winner horizontally
def winner_check_1(winner = False):
    x = 5
    y = 0
    for i in range(6):
        while y <= 3 and x >= 0:
            # reduces time by checking for blank space
            if connect_board[x][y] == " ":
                y += 1
            #checks for four "X"s in a row horizontally
            elif connect_board[x][y] == "X" and connect_board[x][y + 1] == "X" and connect_board[x][y + 2] == "X" and connect_board[x][y + 3] == "X":
                print ("Player one wins!")
                winner = True
                break
            # checks for four "O" in a row horizontally
            elif connect_board[x][y] == "O" and connect_board[x][y + 1] == "O" and connect_board[x][y + 2] == "O" and connect_board[x][y + 3] == "O":
                print ("Player two wins!")
                winner = True
                break
            else:
                # shifts to the right one
                y += 1
        if winner:
            break
        elif not winner:
            # resets to the left and up one
            x -= 1
            y = 0
    # unless winner is decided, will call winner_check_2 for vertical
    if not winner:
        winner = winner_check_2(winner)
    return winner

# print blank board
print_board()

# introduction
print ("This is the start of Connect Four!")
print ("We'll start with the first player.")
print ("Enter the number of a column from 1 to 7 to begin.")
col = column()
first_player()
print_board()
print ("Okay, now it is the second player's turn.")
col = column()
second_player()
print_board()

# loops until winner is chosen or all space is taken
for i in range(20):
    if not winner:
        col = column()
        first_player()
        print_board()
        winner = winner_check_1(winner)
    if not winner:
        col = column()
        second_player()
        print_board()
        winner = winner_check_1(winner)
    if winner:
        break
else:
    print ("There is no more space!")
