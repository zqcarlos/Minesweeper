import random

class Board:
    def __init__(self, n, num_mines):
        self.n = n
        self.num_mines = num_mines

        # Board config
        self._COVERED_CHAR  = u'\u25A0'
        self._MINE_CHAR     = 'M'

        # Initiate board and mines set
        self.__board = None
        self.__mines = None
        self.__remain_cnt = None
        self.refresh()
    
    def refresh(self):
        # Generate a random board 
        self.__board = [[self._COVERED_CHAR for i in range(self.n)] for j in range(self.n)]

        # Generate mines set
        self.__mines = {}
        valid_mine_cnt = 0
        while valid_mine_cnt < self.num_mines:
            coor = random.randint(0, self.n**2-1)
            if coor not in self.__mines:
                self.__mines[coor] = True
                valid_mine_cnt += 1

        # Refresh the number of remained uncovered cells
        self.__remain_cnt = self.n ** 2 - self.num_mines

    # TODO: Write interface
    def drop(self, i, j):
        if self._detect_outbound(i, j):
            return None, 'Error: out of range (0, {})'.format(self.n)

        if self.__board[i][j] != self._COVERED_CHAR:
            return None, 'Error: attempt to flip an uncovered cell'

        # Flip a mine cell
        if i * self.n + j in self.__mines:
            self.__board[i][j] = self._MINE_CHAR
            return self._MINE_CHAR, None

        # Flip an empty cell
        # Calculate the number of adjacent mines 
        offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), 
            (1, 0), (-1, 1), (0, 1), (1, 1)]
        mines_cnt = 0
        for offset in offsets:
            new_i, new_j = i + offset[0], j + offset[1]
            if not self._detect_outbound(new_i, new_j) and new_i * self.n + new_j in self.__mines:
                mines_cnt += 1
        self.__board[i][j] = str(mines_cnt)
        self.__remain_cnt -= 1

        if self.__remain_cnt == 0:
            return 'END', None
        else:
            return str(mines_cnt), None

    def show(self):
        print('\n'.join([' '.join(row) for row in self.__board]))
        
    def _detect_outbound(self, i, j):
        return i < 0 or i > self.n or j < 0 or j > self.n





