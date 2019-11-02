import numpy as np

def check_move(row,col,board):
    if board[row,col] == 0:
        return True
    else:
        return False

def apply_move(game_board):
    print('game_board : ', game_board)
    board_1 = game_board [0:2 , 3:5]
    board_2 = game_board [3:5 , 3:5]
    board_3 = game_board [3:5 , 0:2]
    board_4 = game_board [0:2 , 0:2]
    
    movesAreValid = False

    while (not movesAreValid):
        print('Are you stupid ?')
        row = int(input ("row coordinate:"))
        col = int(input("column coordinate:"))
        rot = int(input("input rotation:"))
        turn = int(input("Player:"))
        movesAreValid = check_move(row,col,game_board)

    game_board[row,col] = turn
    if rot == 1:
        np.rot90(board_1,3)
    elif rot == 2:
        np.rot90(board_1)
    elif rot == 3:
        np.rot90(board_2,3)
    elif rot == 4:
        np.rot90(board_2)
    elif rot == 5:
        np.rot90(board_3,3)
    elif rot == 6:
        np.rot90(board_3)
    elif rot == 7:
        np.rot90(board_4,3)
    elif rot == 8:
        np.rot90(board_4)
    return game_board # returns updated gameboard

def check_horrizontal(game_board): # function to check for horrizontal winnings only later we will have check veritical is the rows
    if game_board[0] == game_board[1] == game_board[2] == game_board[3] == game_board[4] and game_board[4] != 0:
        return True
    elif game_board[1] == game_board[2] == game_board[3] == game_board[4] == game_board[5] and game_board[4] != 0:
        return True
    else:
        return False

def check_veritcal(game_board):
    if (game_board[0,0] == game_board[1,0] == game_board[2,0] == game_board[3,0] == game_board[4,0] and game_board[4,0] != 0):
        return True # first vertical column
    elif (game_board[1,0] == game_board[2,0] == game_board[3,0] == game_board[4,0] == game_board[5,0] and game_board[4,0] != 0):
        return True # first vertical column
    elif (game_board[0,1] == game_board[1,1] == game_board[2,1] == game_board[3,1] == game_board[4,1] and game_board[4,1] != 0):
        return True # second vertical column
    elif (game_board[1,1] == game_board[2,1] == game_board[3,1] == game_board[4,1] == game_board[5,1] and game_board[4,0] != 0):
        return True # second vertical column
    elif (game_board[0,2] == game_board[1,2] == game_board[2,2] == game_board[3,2] == game_board[4,2] and game_board[4,2] != 0):
        return True # third vertical column
    elif (game_board[1,2] == game_board[2,2] == game_board[3,2] == game_board[4,2] == game_board[5,2] and game_board[4,0] != 0):
        return True # third vertical column
    elif (game_board[0,3] == game_board[1,3] == game_board[2,3] == game_board[3,3] == game_board[4,3] and game_board[4,0] != 0):
        return True # fourth vertical column
    elif (game_board[1,3] == game_board[2,3] == game_board[3,3] == game_board[4,3] == game_board[5,3] and game_board[4,0] != 0):
        return True # fourth vertical column
    elif (game_board[0,4] == game_board[1,4] == game_board[2,4] == game_board[3,4] == game_board[4,4] and game_board[4,0] != 0):
        return True # fifth vertical column
    elif (game_board[1,4] == game_board[2,4] == game_board[3,4] == game_board[4,4] == game_board[5,4] and game_board[4,0] != 0):
        return True # fifth vertical column
    elif (game_board[0,5] == game_board[1,5] == game_board[2,5] == game_board[3,5] == game_board[4,5] and game_board[4,0] != 0):
        return True # first vertical column
    elif (game_board[1,5] == game_board[2,5] == game_board[3,5] == game_board[4,5] == game_board[5,5] and game_board[4,5] != 0):
        return True # first vertical column

def check_diagonal(game_board):
    if (game_board[0,0] == game_board[1,1] == game_board[2,2] == game_board[3,3] == game_board[4,4] and game_board[4,4] != 0):
        return True # middle diagonal
    elif (game_board[1,1] == game_board[2,2] == game_board[3,3] == game_board[4,4] == game_board[5,5] and game_board[4,4] != 0):
        return True # middle diagonal
    elif (game_board[0,5] == game_board[1,4] == game_board[2,3] == game_board[3,2] == game_board[4,1] and game_board[4,1] != 0):
        return True # right to left diagonal can you check the above statement 
    elif (game_board[1,5] == game_board[2,4] == game_board[3,3] == game_board[4,2] == game_board[5,0] and game_board[5,0] != 0):
        return True # right to left diagonal
    elif (game_board[1,0] == game_board[2,1] == game_board[3,2] == game_board[4,3] == game_board[5,4] and game_board[5,4] != 0):
        return True # left to right bottom diagonal
    elif (game_board[0,1] == game_board[1,2] == game_board[2,3] == game_board[3,4] == game_board[4,5] and game_board[4,5] != 0):
        return True 
    elif (game_board[1,5] == game_board[2,4] == game_board[3,3] == game_board[4,2] == game_board[5,1] and game_board[5,1] != 0):
        return True 
    elif (game_board[0,4] == game_board[1,3] == game_board[2,2] == game_board[3,1] == game_board[4,0] and game_board[4,0] != 0):
        return True 

def check_victory(game_board):
    winByVeritcal = check_veritcal(game_board)
    winByDiagonal = check_diagonal(game_board)
    winByHorizontal = False
    for i in range(len(game_board)): 
        for j in range(len(game_board[i])):
            if (not winByHorizontal):
                winByHorizontal = check_horrizontal(game_board[i]) # pass in individual rows to check horrizontal funtion
    if winByHorizontal:
        return True
    elif winByVeritcal:
        return True
    elif winByDiagonal:
        return True
    else:
        return False