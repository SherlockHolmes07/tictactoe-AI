"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
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
    
    for i in range(len(board)):
        if board[i][1] == board[i][0] and board[i][1] == board[i][2]:
            return board[i][1]
    
    for i in range(len(board[1])):
        if board[1][i] == board[0][i] and board[1][i] == board[2][i]:
            return board[1][i]

    if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
        return board[1][1]

    if board[1][1] == board[2][0] and board[1][1] == board[0][2]:
        return board[1][1]

    return None  


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for list in board:
        for cell in list:
            if cell == None:
                return False
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    curr_player = player(board)
    all_actions = actions(board)
    
    if curr_player == X:

        lar_value = -9999
        ans = tuple()

        for action in all_actions:
            val = Minimize(result(board,action), lar_value)

            if val > lar_value:
                ans = action
                lar_value = val
        return ans

    else:
        small_value = 9999 
        ans = tuple()
        for action in all_actions:
            val = Maximize(result(board,action), small_value)
            if val < small_value:
                small_value = val
                ans = action
        return ans



def Maximize(board, val):

    if terminal(board):
        return utility(board)
    
    value = -9999

    for action in actions(board):
        value = max(value,Minimize(result(board,action), value))
        if value >= val:
            return value

    return value


def Minimize(board, val):

    if terminal(board):
        return utility(board)
    
    value = 9999

    for action in actions(board):
        value = min(value,Maximize(result(board,action), value))
        if  value <= val:
            return value

    return value
