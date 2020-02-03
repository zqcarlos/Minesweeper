# TODO: Takes a board and attempts to solve the board. 
# Return a boolean indicating if the board was successfully solved.
from board import Board
import random
from datetime import datetime

def solve(board) -> bool:
    random.seed(datetime.now())
    while True:
        res, err = board.drop(random.randint(0, board.n-1), random.randint(0, board.n-1))
        if res == 'M' or res == 'END':
            return res == 'END'

