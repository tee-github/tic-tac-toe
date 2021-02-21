#tic tac toe game 

import os

def board_display():
    print(board[0][0] + " |",board[0][1] + " |",board[0][2])
    print("—— ——— ——")
    print(board[1][0] + " |",board[1][1] + " |",board[1][2])
    print("—— ——— ——")
    print(board[2][0] + " |",board[2][1] + " |",board[2][2])

def get_player_turn():
    global turn
    global position_row
    global position_col
    turn_end = False
    while turn_end == False:
        position_row = int(input("Choose a position for the row: "))
        position_row = int(position_row) - 1
    
        position_col = int(input("Choose a position for the column: "))
        print("\n")
        position_col = int(position_col) - 1

        if int(position_row) <= 2 and int(position_row) >= 0 and int(position_col) <= 2 and int(position_col) >= 0 and board[position_row][position_col] != " " :
            print("That move has already been made!")
        elif int(position_row) <= 2 and int(position_row) >= 0 and int(position_col) <= 2 and int(position_col) >= 0:
            board[position_row][position_col] = symbols[turn]
            board_display() 
            turn_end = True
        
        else:
            print("\nPlease enter a valid number.\n")

def check_winner():
    # row check
    global winner
    count = 1 
    if board[position_row][(position_col + 1) % 3] == symbols[turn]: 
        count = count + 1

    if board[position_row][(position_col + 2) % 3] == symbols[turn]:
        count = count + 1

    if count == 3:
        winner = True 

    # column check
    count = 1 
    if board[(position_row + 1) % 3][position_col] == symbols[turn]: 
        count = count + 1

    if board[(position_row + 2) % 3][position_col] == symbols[turn]:
        count = count + 1

    if count == 3:
        winner = True    

    # diagonal check 1
    if position_row == position_col:
        count = 1
        if board[(position_row + 1) % 3][(position_col + 1) % 3] == symbols[turn]:
            count = count + 1
        if board[(position_row + 2) % 3][(position_col + 2) % 3] == symbols[turn]:
            count = count + 1

        if count == 3:
            winner = True

    # diag check 2
    if position_row + position_col == 2:
        count = 1
        if board[(position_row - 1) % 3][(position_col + 1) % 3] == symbols[turn]:
            count = count + 1
        if board[(position_row - 2) % 3][(position_col + 2) % 3] == symbols[turn]:
            count = count + 1
        if count == 3:
            winner = True

turn = 0
round = 1
position_row = 0
position_col = 0
symbols = ["X","O"]
winner = False

board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to Tic Tac Toe! \n")
name1 = input("What is your name Player1?: \n") 
name2 = input("What is your name Player2?: \n") 
names = [name1,name2]

print('\n')
board_display()

# main game loop
while winner == False and round <= 9:
    print('\n')
    print(names[turn], " it is your turn to play")
    get_player_turn()
    check_winner()
    turn = (turn + 1) %2 # symbol changes when players swap turns, from X to O
    round = round + 1

if winner == True:
    print("\n\nCongratulations", names[(turn + 1) %2], "you have won!")
if winner == False and round == 10: 
    print("\n\nWe have a draw!")