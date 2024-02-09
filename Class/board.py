'''
Game board Class

- create the board from a file
- hold master level list of whats on the board
- holds locations of spawnable locations
- keep track of cells
- tells the button if its disabled or not
'''
import random
from tkinter import *
from Utilities import settings, utils

class Game_Board:
    SPAWN_LOCATIONS = []
    MASTER_BOARD = []
    MASTER_BTN_BOARD = {}
    DEBUG_SPAWN_LOCATIONS = []
    OBSTACLE_LOCATIONS = []
    MASTER_OBSTACLES = {}
    OBSTACLE_CHECK_LIST =[]
    def __init__(self):
        """All scores are initially 0."""


# Initial board
    def init_board(self, file):
        # file = "GameBoard/TheCave.txt"
        with open(file, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into fields based on whitespace
                fields = line.strip().split()
                Game_Board.MASTER_BOARD.append(fields)
            file.close()
        return Game_Board.MASTER_BOARD

    @staticmethod
    def button_locations():
        rows = len(Game_Board.MASTER_BOARD)
        i = 0
        while i < rows:
            #
            cols = len(Game_Board.MASTER_BOARD[i])
            j = 0
            while j < cols:
                Game_Board.MASTER_BTN_BOARD.update({(i, j) : Game_Board.MASTER_BOARD[i][j]})
                j += 1
            i += 1

# Read the current board
    @staticmethod
    def read_board():
        # for i in Cell.MASTER_BOARD:
        #     print(i)
        rows = len(Game_Board.MASTER_BOARD)
        board = []
        i = 0
        while i < rows:
            #
            board.append([])
            cols = len(Game_Board.MASTER_BOARD[i])
            j = 0
            while j < cols:
                if Game_Board.MASTER_BOARD[i][j] != 'H':
                    board[i].append(' ')
                else:
                    board[i].append(Game_Board.MASTER_BOARD[i][j])
                j += 1
            i += 1
        for i in board:
            # print(' '.join(i))
            print(i)

    @staticmethod
    def obstacle_locations():
        Game_Board.OBSTACLE_LOCATIONS.clear()
        rows = len(Game_Board.MASTER_BOARD)
        i = 0
        while i < rows:
            #
            Game_Board.OBSTACLE_LOCATIONS.append([])
            cols = len(Game_Board.MASTER_BOARD[i])
            j = 0
            while j < cols:
                if (Game_Board.MASTER_BOARD[i][j] == 'W') or (Game_Board.MASTER_BOARD[i][j] == 'P') or (
                        Game_Board.MASTER_BOARD[i][j] == 'H') or (Game_Board.MASTER_BOARD[i][j] == 'T') or (
                        Game_Board.MASTER_BOARD[i][j] == 'M') or (Game_Board.MASTER_BOARD[i][j] == ' '):
                    Game_Board.OBSTACLE_LOCATIONS[i].append(j)
                    if Game_Board.MASTER_BOARD[i][j] != 'W':
                        Game_Board.MASTER_OBSTACLES.update({Game_Board.MASTER_BOARD[i][j]: [i, j]})
                        Game_Board.MASTER_OBSTACLES.update({Game_Board.MASTER_BOARD[i][j]: (i, j)})
                j += 1
            i += 1
        return Game_Board.OBSTACLE_LOCATIONS

    @staticmethod
    def spawn_locations():
        global SPAWN_LOCATIONS
        Game_Board.SPAWN_LOCATIONS.clear()
        rows = len(Game_Board.MASTER_BOARD)
        i = 0
        while i < rows:
            #
            Game_Board.SPAWN_LOCATIONS.append([])
            cols = len(Game_Board.MASTER_BOARD[i])
            j = 0
            while j < cols:
                if (Game_Board.MASTER_BOARD[i][j] == 'E'):
                    Game_Board.SPAWN_LOCATIONS[i].append(j)
                j += 1
            i += 1
        return Game_Board.SPAWN_LOCATIONS

    @staticmethod
    def debug_spawn_locations():
        Game_Board.DEBUG_SPAWN_LOCATIONS.clear()
        rows = len(Game_Board.MASTER_BOARD)

        i = 0
        while i < rows:
            #
            Game_Board.DEBUG_SPAWN_LOCATIONS.append([])
            cols = len(Game_Board.MASTER_BOARD[i])
            j = 0
            while j < cols:
                if (Game_Board.MASTER_BOARD[i][j] == 'E'):
                    Game_Board.DEBUG_SPAWN_LOCATIONS[i].append(' ')
                else:
                    Game_Board.DEBUG_SPAWN_LOCATIONS[i].append(Game_Board.MASTER_BOARD[i][j])
                j += 1
            i += 1
        return Game_Board.DEBUG_SPAWN_LOCATIONS

    @staticmethod
    def spawn_object(object):
        Game_Board.spawn_locations()
        rows = len(Game_Board.SPAWN_LOCATIONS) - 1

        ran_row = random.sample(range(1, rows), 1)[0]
        ran_col = random.choice(Game_Board.SPAWN_LOCATIONS[ran_row])
        # Check to see if location is not within a certain amount of spaces
        Game_Board.MASTER_OBSTACLES.update({object: (ran_row, ran_col)})
        Game_Board.MASTER_BOARD[ran_row][ran_col] = object

        Game_Board.obstacle_locations()
        Game_Board.debug_spawn_locations()
        Game_Board.spawn_locations()
