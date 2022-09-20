"""
Tic Tac Toe Player
"""

import math
from re import S
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
   # if terminal(board):
   #     return EMPTY
    x = 0
    o = 0
    for list in board:
        for cell in list:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1
    if x == o:
        return X
    return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = set()
   # if terminal(board):
   #     return s 

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                s.add((i,j))

    return s 
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError("Invalid Cordination")
    elif board[action[0]][action[1]] == X or board[action[0]][action[1]] == O or board[action[0]][action[1]] != EMPTY:
        raise ValueError("Cell is already occupaid.")
    
    move = player(board)
    res_board = copy.deepcopy(board)
    res_board[action[0]][action[1]] = move
    return res_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
