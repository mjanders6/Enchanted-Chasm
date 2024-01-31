'''
Game board Class
'''

class game_board():

    def __init__(self, col, board):
        """All scores are initially 0."""
        self.col = col
        self.board = []
# Initial board
    def init_board(self):
        j = 0
        while j < self.col:
            if (j == 0) or (j == self.col - 1):
                self.board.append('W')
            else:
                self.board.append('E')
            j += 1
        return self.board

# Spawn Walls

# Spawn game pieces

