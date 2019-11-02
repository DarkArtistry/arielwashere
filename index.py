import numpy as np;
from moves import apply_move, check_victory;

def menu():
    game_board = np.zeros ((6,6)) # setup initial board
    game_over = check_victory(game_board) # check if board is not completed
    print('game_over : ', game_over)
    apply_move(game_board)
    while (not game_over):
        print(' not game over : ', not game_over)
        game_board = apply_move(game_board) # set game_board to the updated gameboard
        game_over = check_victory(game_board) # updates board completion
    
    print('final game_board :', game_board)
menu()