import numpy as np
game_board = np.zeros ((6,6))

board_1 = game_board [0:2 , 3:5]
board_2 = game_board [3:5 , 3:5]
board_3 = game_board [3:5 , 0:2]
board_4 = game_board [0:2 , 0:2]

def display_board(board):
    pass
#4    
def check_victory(board,turn,rot):
    if board[turn,rot] ==
    for r in range(0,6):
        for c in range(0,6):
            while 0 <= col <= 5:
                if board[row,col] == turn:
                    count = 1
                        if board[row,col + 1] == turn:
                            count += 1
                            if
                            turn == 1
                            
                            turn == 2
def check_victory(board,turn,rot):
    check_victory1(board,turn,rot)
    check_victory2(board,turn,rot)
    check_victory3(board,turn,rot)
    check_victory4(board,turn,rot)
    check_victory5(board,turn,rot)
    check_victory6
    check_victory7
    check_victory8
    check_victory9
    check_victory10
    
   
                
         elif:
                while 0 <= row <= 5:
                    if board[row,col] == turn:
                        count = 1
                            if board[row + 1,col] == turn:
                                count += 1
                                else : break
                                
            elif:
                while 0 <= row <= 5 and 0<= col <= 5:
                    if board[row,col] == turn
                        count = 1
                            if board[row + 1, col + 1] == turn:
                                count += 1
            elif:
                if board[row + 1,col - 1] == turn:
                    count += 1
                                        
                # diagonal topleft to rightbottom
            elif # diagonal topright to leftbottom
    return 
#2  
def apply_move(board,turn,row,col,rot):
    menu()
    while True:
        board = (input ("Board:"))
        row = int(input ("row coordinate:"))
        col = int(input("column coordinate:"))
        rot = int(input("input rotation:"))
        turn = int(input("Player:"))
        game_board[row,col] = turn
        
        return game_board

    rot = int(input("input rotation:"))
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
                                else: continue
        

    
    

a=np.zeros ((6,6))
b=0
c=0
d=99
e=1
print(apply_move(a,b,c,d,e))

    return board
    
#3   
def check_move(board,row,col):
    if board[row,col] ==0:
        return True
    else:
        return False

def computer_move(board,turn,level):
    return (0,0,0)

#1 
def menu():
    while True:
        row = int(input ("row coordinate:"))
        if row < 0 and row > 5:
             print("ERROR! Input 0<=row<=5")
             continue
        else:
        col = int(input("column coordinate:"))
        if col < 0 and col > 5:
             print("ERROR! Input 0<=column<=5")
             continue
        else:
        rot = int(input("input rotation index:"))
        if rot < 1 and rot > 8
             print("ERROR! Input 0< rotation index < 9")
             continue
        else:    
        turn = int(input("Player Position 1 or 2:"))
        if turn != 1 and != 2:
            print ("ERROR! Input either 1 or 2 ")
            continue
        break
    
rot = int(input("input rotation:"))
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
                                else: continue
        


def apply_move (board, row, col, rot, turn):
    while True:
        board = (input ("Board:"))
        row = int(input ("row coordinate:"))
        col = int(input("column coordinate:"))
        rot = int(input("input rotation:"))
        turn = int(input("Player:"))
        game_board[row,col] = turn
        
        return game_board
       

    

a=np.zeros ((6,6))
b=0
c=0
d=99
e=1
print(apply_move(a,b,c,d,e))
