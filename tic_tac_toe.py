#Lets first start by defining the board as a list of lists
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

#Next, lets define a function to print the board
def print_board():
    print("  0  1  2")
    print("0 "+board[0][0]+ " | "+board[0][1]+ " | "+board[0][2])
    print(" ---+---+---")
    print("1 "+board[1][0]+ " | "+board[1][1]+ " | "+board[1][2])
    print(" ---+---+---")
    print("2 "+board[2][0]+ " | "+board[2][1]+ " | "+board[2][2])


#Next, define a function to check if a player has won
def check_win(player):
    #check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        
    #check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    #check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board [1][1] == player and board[2][0] == player:
        return True

    #no win
    return False


#Define a function to check if the board is full 
def check_full():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


#Define the players
players = ["X","O"]
current_player = 0


#Define / setup the main game loop
while True:
    print_board()

    #get the current players move
    move = input("Player "+players[current_player]+", enter your move (row column): ")
    move = move.split()
    row = int(move[0])
    col = int(move[1])

    #Check if the move is valid
    if board[row][col] != " ":
        print("Invalid move.")
        continue

    #make the move
    board[row][col] = players[current_player]

    #Check if the current player has won
    if check_win(players[current_player]):
        print("Player "+players[current_player]+" wins!")
        break
    
    #Check to see if the board is full
    if check_full():
        print("Tie Game!")
        break

    #Switch to other player
    current_player = (current_player+1) %2

